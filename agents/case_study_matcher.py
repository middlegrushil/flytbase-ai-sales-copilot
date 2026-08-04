import json
import os

from utils.gemini import ask_gemini


def match_case_study():
    """
    Find the most relevant FlytBase case study
    for the inbound enterprise lead.
    """

    if not os.path.exists("input/lead.json"):
        print("❌ lead.json not found")
        return

    if not os.path.exists("output/flytbase_context.json"):
        print("❌ flytbase_context.json not found")
        return

    with open("input/lead.json", "r") as f:
        lead = json.load(f)

    with open("output/flytbase_context.json", "r") as f:
        flytbase = json.load(f)

    company = lead.get("company_name", "")
    industry = lead.get("industry", "")
    use_case = lead.get("interest", "")
    pain_points = ", ".join(lead.get("pain_points", []))

    case_studies = flytbase.get("case_studies", {})
    markdown = case_studies.get("markdown", "")

    prompt = f"""
You are a FlytBase Enterprise Solutions Engineer.

Customer Company:
{company}

Industry:
{industry}

Customer Interest:
{use_case}

Pain Points:
{pain_points}

Below are FlytBase customer case studies.

{markdown}

Choose the SINGLE most relevant case study.

Return markdown only using this format.

# Matching Customer

# Why it Matches

# Business Outcomes

# How the Sales Team Should Use This Story
"""

    answer = ask_gemini(prompt)

    os.makedirs("output", exist_ok=True)

    with open("output/case_study.json", "w") as f:
        json.dump(
            {
                "case_study": answer
            },
            f,
            indent=4,
        )

    print("✅ Case study generated.")