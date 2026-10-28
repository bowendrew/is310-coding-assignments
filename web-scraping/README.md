
# Minecraft Wiki Web Scraping Project

## Research Question

How do Minecraft biomes differ in the types and number of mobs associated with them?

## Data Source

This project uses the independent Minecraft Wiki (https://minecraft.wiki) to collect information about mobs associated with different Minecraft biomes.

The four biomes selected for comparison are Forest, Badlands, Grove, and Cherry Grove.

## Web Scraping Method

I used Python, Requests, and BeautifulSoup to collect data from the Minecraft Wiki.

My scraper navigates two levels of the website:

1. The main Biome page (https://minecraft.wiki/w/Biome), where it identifies links to four selected biomes.
2. The individual biome pages, where it extracts mob names from the Java Edition spawning tables.

I selected Forest, Badlands, Grove, and Cherry Grove for comparison.

The scraper uses an identifying User-Agent, waits two seconds between requests, checks HTTP status codes, and handles request errors.

The collected data is saved in minecraft_biomes.csv, which contains the biome name, mob name, game edition, and source URL.

## Initial Findings

The Forest and Badlands biomes each had 15 listed mob types, while Grove and Cherry Grove each had 13.

Although some biomes have the same number of mobs, the types of mobs differ between them.

## Robots.txt and Responsible Scraping

Before collecting data, I reviewed the Minecraft Wiki's robots.txt file:
https://minecraft.wiki/robots.txt

The file identifies restricted paths, including /w/File:, /w/User:, /w/Special:, and API endpoints. The biome article pages used in this project were not listed as disallowed for a general user agent.

I limited my scraper to four biome pages, used an identifying User-Agent, waited two seconds between requests, and checked HTTP response codes before processing the pages.

The robots.txt file also directs users to follow the site's content licensing terms:
https://meta.weirdgloop.org/w/Meta:Copyrights

## Research Value and Limitations

This dataset helps compare how different Minecraft environments are represented through the mobs associated with them. The number of distinct mob types listed for each biome serves as a measure of documented mob diversity.

However, the number of listed mobs does not tell us how frequently players encounter them. Some mobs may be much rarer than others, and spawning can depend on additional game conditions.

This project only examines four biomes and focuses on Java Edition spawning tables, thus, the findings cannot represent every Minecraft biome nor the Bedrock Edition of the game.

The scraper also depends on the Minecraft Wiki's HTML structure. Changes to the website could affect how accurately the data is collected.

## Reflection

Web scraping allowed me to turn information from individual Minecraft Wiki articles into a structured dataset that can be compared across biomes. One important lesson was that the HTML structure of a webpage affects how data must be extracted. For example, the mob names were stored inside specific HTML elements rather than ordinary table cells. I also learned that collecting data is different from interpreting it. Although my dataset can show differences in the number and types of mobs listed for each biome, it cannot directly measure how often players encounter those mobs during gameplay.