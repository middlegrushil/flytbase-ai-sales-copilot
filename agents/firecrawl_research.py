from utils.firecrawl import scrape_all_pages
from utils.gemini_client import ask_gemini
from utils.parser import extract_json
from utils.storage import save_json


def firecrawl_research():

    print("=" * 80)
    print("🚁 FlytBase Knowledge Base")
    print("=" * 80)

    pages = scrape_all_pages()

    combined = ""

    for section, doc in pages.items():

        if doc is None:
            continue

        markdown = ""

        # Firecrawl Document object
        if hasattr(doc, "markdown"):
            markdown = doc.markdown

        # Older SDK compatibility
        elif hasattr(doc, "data"):
            data = doc.data

            if isinstance(data, dict):
                markdown = data.get("markdown", "")

        combined += f"""

==================================================
SECTION
==================================================

{section.upper()}

{markdown}

"""

    system_prompt = """
You are building FlytBase's internal knowledge base.

Read all supplied website content.

Summarize it into four sections.

Return ONLY valid JSON.

{
    "products":{
        "markdown":""
    },
    "solutions":{
        "markdown":""
    },
    "case_studies":{
        "markdown":""
    },
    "partners":{
        "markdown":""
    }
}
"""

    response = ask_gemini(
        system_prompt,
        combined,
    )

    context = extract_json(response)

    save_json(
        "output/flytbase_context.json",
        context,
    )

    print("✅ Knowledge Base Created")

    return context