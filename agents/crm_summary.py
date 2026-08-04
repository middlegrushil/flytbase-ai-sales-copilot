import json

from utils.gemini_client import ask_gemini


def generate_crm_summary():

    with open("input/lead.json") as f:
        lead = json.load(f)

    with open("output/strategy.json") as f:
        strategy = json.load(f)

    system_prompt = """
Generate a concise CRM summary.

Return Markdown.

Sections:

Account

Opportunity

Pain Points

Current Stage

Recommended Next Step

Notes
"""

    user_prompt = f"""
Lead

{json.dumps(lead, indent=2)}

Strategy

{json.dumps(strategy, indent=2)}
"""

    response = ask_gemini(system_prompt, user_prompt)

    with open("output/crm_summary.md", "w") as f:
        f.write(response)

    print("CRM summary generated!")