import json

from utils.gemini_client import ask_gemini


def identify_stakeholders():

    with open("input/lead.json") as f:
        lead = json.load(f)

    with open("output/qualification.json") as f:
        qualification = json.load(f)

    system_prompt = """
You are an Enterprise Account Executive.

Identify:

- Champion
- Economic Buyer
- Technical Buyer
- Procurement
- Executive Sponsor

Return JSON only.
"""

    user_prompt = f"""
Lead

{json.dumps(lead, indent=2)}

Qualification

{json.dumps(qualification, indent=2)}
"""

    response = ask_gemini(system_prompt, user_prompt)

    with open("output/stakeholders.json", "w") as f:
        f.write(response)

    print("Stakeholder mapping completed!")