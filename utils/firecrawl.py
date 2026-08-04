import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

load_dotenv()

app = FirecrawlApp(
    api_key=os.getenv("FIRECRAWL_API_KEY")
)

PAGES = {

    "home":
    "https://flytbase.com/",

    "case_studies":
    "https://flytbase.com/case-studies/",

    "solutions":
    "https://flytbase.com/solutions/",

    "products":
    "https://flytbase.com/products/",

    "partners":
    "https://flytbase.com/partners/",

    "blog":
    "https://flytbase.com/blog/"
}


def scrape_page(url):

    return app.scrape_url(
        url=url,
        formats=["markdown"]
    )


def scrape_all_pages():

    results = {}

    for name, url in PAGES.items():

        print(f"Scraping {name}...")

        try:

            results[name] = scrape_page(url)

        except Exception as e:

            results[name] = {
                "error": str(e)
            }

    return results