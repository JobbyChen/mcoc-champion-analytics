import time
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

INPUT = Path("data/raw/champion_urls.csv")
OUTPUT = Path("data/raw/champion_details_sample.csv")
FAILED_OUTPUT = Path("data/raw/failed_champion_urls.csv")

# Start with 20 champions while testing
champion_urls = pd.read_csv(INPUT).head(20)

# Load previously collected champions, if available
if OUTPUT.exists():
    existing_df = pd.read_csv(OUTPUT)
    records = existing_df.to_dict("records")
else:
    records = []

# Track URLs that have already been collected
collected_urls = {champion["source_url"] for champion in records}


if FAILED_OUTPUT.exists():
    failed_requests = pd.read_csv(FAILED_OUTPUT).to_dict("records")
else:
    failed_requests = []

for _, row in champion_urls.iterrows():
    url = row["source_url"]

    if url in collected_urls:
        print(f"Already collected, skipping: {url}")
        continue

    try:
        response = requests.get(
            url, headers={"User-Agent": "MCOCChampionAnalytics/0.1"}, timeout=20
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        name_element = soup.select_one(".cp-title h1")
        class_element = soup.select_one(".cp-sub a.cc")
        tier_element = soup.select_one(".cp-tier")

        champion = {
            "name": name_element.get_text(strip=True) if name_element else None,
            "class": class_element.get_text(strip=True) if class_element else None,
            "tier": (
                tier_element.get_text(" ", strip=True).split()[0]
                if tier_element
                else None
            ),
            "source_url": url,
        }

        if not champion["name"] or not champion["class"]:
            print(f"Missing required data: {url}")
            continue

        records.append(champion)
        collected_urls.add(url)
        print(f"Collected: {champion['name']}")
        # Remove this URl from the failure log if it succeeds
        failed_requests = [
            failure for failure in failed_requests 
            if failure["source_url"] != url
        ]
        if FAILED_OUTPUT.exists():
            pd.DataFrame(
                failed_requests,
                columns=["source_url", "error"]
            ).to_csv(FAILED_OUTPUT, index=False)
        # Save progress after each successfully collected champion
        progress_df = pd.DataFrame(
            records, columns=["name", "class", "tier", "source_url"]
        )

        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        progress_df.to_csv(OUTPUT, index=False)

    
    except requests.RequestException as error:
        print(f"Request failed for {url}: {error}")

        failed_requests.append({
            "source_url": url,
            "error": str(error)
        })

        pd.DataFrame(
            failed_requests,
            columns=["source_url", "error"]
        ).to_csv(FAILED_OUTPUT, index=False)


    finally:
        # Wait after every request, including failed or incomplete pages
        time.sleep(2)


OUTPUT.parent.mkdir(parents=True, exist_ok=True)

df = pd.DataFrame(records, columns=["name", "class", "tier", "source_url"])

df.to_csv(OUTPUT, index=False)

print(f"\nSaved {len(df)} champions to {OUTPUT}")
