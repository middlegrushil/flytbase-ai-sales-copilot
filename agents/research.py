import json

from utils.tavily import search_company
from utils.gemini_client import ask_gemini
from utils.parser import extract_json
from utils.storage import load_json, save_json


def company_research():

    print("=" * 80)
    print("🏢 Company Research Agent")
    print("=" * 80)

    lead = load_json("input/lead.json")

    company = lead.get("company_name", "")

    if not company:
        raise ValueError("company_name missing in lead.json")

    tavily = search_company(company)

    raw_results = tavily.get("results", [])

    search_context = ""

    for i, result in enumerate(raw_results, start=1):

        search_context += f"""
Result {i}

Title:
{result.get('title','')}

URL:
{result.get('url','')}

Content:
{result.get('content','')}
"""

    system_prompt = """
You are FlytBase's Enterprise Research Analyst.

Create structured company intelligence.

Return ONLY valid JSON.

{
  "company_overview":"",
  "industry":"",
  "headquarters":"",
  "employee_estimate":"",
  "business_model":"",
  "recent_news":[
      ""
  ],
  "drone_relevance":"",
  "automation_maturity":"",
  "business_challenges":[
      ""
  ],
  "opportunities":[
      ""
  ],
  "sources":[
      ""
  ]
}
"""

    user_prompt = f"""
Company

{company}

==================================================

Search Results

{search_context}

Return JSON only.
"""

    response = ask_gemini(
        system_prompt,
        user_prompt,
    )

    research = extract_json(response)

    save_json(
        "output/research.json",
        research,
    )

    print("✅ Research Completed")

    return research