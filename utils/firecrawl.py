import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

load_dotenv()

app = FirecrawlApp(
    api_key=os.getenv("FIRECRAWL_API_KEY")
)

# Only crawl pages that directly help sales recommendations
PAGES = {

    "products":
    "https://flytbase.com/products/",

    "solutions":
    "https://flytbase.com/solutions/",

    "case_studies":
    "https://flytbase.com/case-studies/",

    "partners":
    "https://flytbase.com/partners/",

}


def scrape_page(url):

    return app.scrape_url(
        url=url,
        formats=["markdown"]
    )


def scrape_all_pages():

    results = {}

    total = len(PAGES)

    for i, (name, url) in enumerate(PAGES.items(), start=1):

        print(f"[{i}/{total}] Scraping {name}")

        try:

            results[name] = scrape_page(url)

        except Exception as e:

            print(f"Failed: {name}")

            results[name] = None

    return results