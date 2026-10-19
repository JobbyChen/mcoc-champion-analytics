
import csv
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

SITEMAP_URL = "https://mcoc.app/sitemap.xml"
OUTPUT = Path("data/raw/champion_urls.csv")

# Download the sitemap
request = urllib.request.Request(
    SITEMAP_URL,
    headers={"User-Agent": "MCOCChampionAnalytics/0.1"}
)

with urllib.request.urlopen(request, timeout=20) as response:
    xml_data = response.read()

# Parse the XML
root = ET.fromstring(xml_data)
namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

champions = []

for entry in root.findall("sm:url", namespace):
    url = entry.findtext("sm:loc", default="", namespaces=namespace)
    last_modified = entry.findtext(
        "sm:lastmod", default="", namespaces=namespace
    )

    if url.startswith("https://mcoc.app/champions/"):
        slug = url.rsplit("/", 1)[-1]

        if slug:
            champions.append({
                "slug": slug,
                "source_url": url,
                "last_modified": last_modified
            })

# Save discovered champion URLs
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["slug", "source_url", "last_modified"]
    )
    writer.writeheader()
    writer.writerows(champions)

print(f"Discovered {len(champions)} champion URLs")
print(f"Saved to {OUTPUT}")
