import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin

# Starting page for discovering biome links
main_url = "https://minecraft.wiki/w/Biome"

# Biomes selected for comparison
biomes = {
    "Forest": "https://minecraft.wiki/w/Forest",
    "Badlands": "https://minecraft.wiki/w/Badlands",
    "Grove": "https://minecraft.wiki/w/Grove",
    "Cherry Grove": "https://minecraft.wiki/w/Cherry_grove"
}

# Identify ourselves when accessing the website
HEADERS = {
    "User-Agent": "is310-course-scraper/1.0 (student project; drewb4@illinois.edu)"
}

# Discover biome links from the main Biome page
target_biomes = {
    "Forest": "/w/Forest",
    "Badlands": "/w/Badlands",
    "Grove": "/w/Grove",
    "Cherry Grove": "/w/Cherry_grove"
}

print("Finding biome links from the main wiki page...")

try:
    main_response = requests.get(
        main_url,
        headers=HEADERS,
        timeout=10
    )

    if main_response.status_code == 200:
        main_soup = BeautifulSoup(main_response.text, "html.parser")
        main_content = main_soup.find(id="mw-content-text")

        discovered_biomes = {}

        if main_content:
            for biome_name, target_path in target_biomes.items():
                link = main_content.find("a", href=target_path)

                if link:
                    discovered_biomes[biome_name] = urljoin(
                        main_url, link["href"]
                    )
                    print(f"Found: {biome_name}")

        biomes = discovered_biomes

    else:
        print("Could not access the main Biome page.")
        biomes = {}

except requests.RequestException as error:
    print(f"Request failed: {error}")
    biomes = {}

def extract_mobs(soup):
    # Find the Mobs heading
    mobs_section = soup.find(id="Mobs")

    if not mobs_section:
        return None

    # Find the Java Edition mob table
    heading_container = mobs_section.parent
    java_table = heading_container.find_next_sibling("table")

    if not java_table:
        return None

    mob_names = []

    for row in java_table.find_all("tr"):
        mob_cell = row.find("th")

        if mob_cell:
            mob_text = mob_cell.find("span", class_="sprite-text")

            if mob_text:
                mob_name = mob_text.get_text(" ", strip=True)

                if mob_name not in mob_names:
                    mob_names.append(mob_name)

    return mob_names

# Collect mobs from all four biomes
all_biome_mobs = {}

for biome_name, biome_url in biomes.items():
    print(f"\nScraping {biome_name}...")

    # Wait between requests to avoid overloading the wiki
    time.sleep(2)

    try:
        response = requests.get(
            biome_url,
            headers=HEADERS,
            timeout=10
        )

        # Check the HTTP status before parsing
        if response.status_code != 200:
            print(f"HTTP error: {response.status_code}")
            continue

        biome_soup = BeautifulSoup(response.text, "html.parser")
        mobs = extract_mobs(biome_soup)

        if mobs is None:
            print("No compatible mob table found.")
            continue

        all_biome_mobs[biome_name] = mobs

        print(f"Total mob types: {len(mobs)}")
        print("Mobs:", ", ".join(mobs))

    except requests.RequestException as error:
        print(f"Request failed: {error}")

# Save the collected biome and mob data to CSV
with open("minecraft_biomes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Column headings
    writer.writerow(["Biome", "Mob", "Edition", "Source URL"])

    # Write one row for each mob in each biome
    for biome_name, mobs in all_biome_mobs.items():
        for mob in mobs:
            writer.writerow([
                biome_name,
                mob,
                "Java",
                biomes[biome_name]
            ])

print("\nData saved to minecraft_biomes.csv")