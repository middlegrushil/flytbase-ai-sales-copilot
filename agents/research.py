import json

from utils.gemini_client import ask_gemini
from utils.tavily import search_company


def research_company():

    with open("input/lead.json") as f:
        lead = json.load(f)

    company = lead["company_name"]

    tavily = search_company(company)

    articles = []

    for result in tavily["results"]:

        articles.append({
            "title": result["title"],
            "url": result["url"],
            "content": result["content"]
        })

    system_prompt = """
You are an Enterprise Account Research Analyst.

Summarize the company research.

Focus on:

- Company overview
- Operations
- Industry
- Recent initiatives
- Drone usage
- Automation initiatives
- Inspection processes
- Digital transformation
- Business opportunities for FlytBase

Return valid JSON only.
"""

    user_prompt = json.dumps(articles, indent=2)

    response = ask_gemini(system_prompt, user_prompt)

    with open("output/research.json", "w") as f:
        f.write(response)

    print("Research completed!")