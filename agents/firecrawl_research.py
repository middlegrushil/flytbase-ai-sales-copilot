import json
import os

from utils.firecrawl import scrape_all_pages


def convert_document(doc):
    """
    Convert Firecrawl Document into a JSON-serializable dictionary.
    """

    if doc is None:
        return None

    metadata = {}

    if getattr(doc, "metadata", None):
        metadata = {
            "title": getattr(doc.metadata, "title", ""),
            "url": getattr(doc.metadata, "url", ""),
            "description": getattr(doc.metadata, "description", "")
        }

    return {
        "metadata": metadata,
        "markdown": getattr(doc, "markdown", "")
    }


def firecrawl_research():

    os.makedirs("output", exist_ok=True)

    pages = scrape_all_pages()

    cleaned = {}

    for page_name, document in pages.items():
        cleaned[page_name] = convert_document(document)

    with open("output/flytbase_context.json", "w") as f:
        json.dump(cleaned, f, indent=4)

    print("✅ Firecrawl knowledge base created successfully!")