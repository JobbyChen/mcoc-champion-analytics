
import requests
from bs4 import BeautifulSoup

url = "https://mcoc.app/champions/abomination"
# Download the champion page
response = requests.get(
    url,
    headers={"User-Agent": "MCOCChampionAnalytics/0.1"},
    timeout=20
)
response.raise_for_status()

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find the champion attributes
name_element = soup.select_one(".cp-title h1")
class_element = soup.select_one(".cp-sub a.cc")
tier_element = soup.select_one(".cp-tier")
portrait_element = soup.select_one(".champ-portrait img")

champion = {
    "name": name_element.get_text(strip=True) if name_element else None,
    "class": class_element.get_text(strip=True) if class_element else None,
    "tier": (
        tier_element.get_text(" ", strip=True).split()[0]
        if tier_element else None
    ),
    "portrait_url": (
        requests.compat.urljoin(url, portrait_element["src"])
        if portrait_element and portrait_element.has_attr("src")
        else None
    ),
    "source_url": url
}

print(champion)
