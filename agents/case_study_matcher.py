import json

from utils.gemini_client import ask_gemini
from utils.parser import extract_json
from utils.storage import load_json, save_json


def match_case_study():

    print("=" * 80)
    print("📚 Case Study Matching Agent")
    print("=" * 80)

    lead = load_json("input/lead.json")

    research = load_json("output/research.json")

    qualification = load_json("output/qualification.json")

    flytbase = load_json("output/flytbase_context.json")

    case_library = (
        flytbase.get("case_studies", {})
        .get("markdown", "")
    )

    system_prompt = """
You are FlytBase's Enterprise Solutions Engineer.

Identify the SINGLE most relevant FlytBase customer success story.

Reason using:

• Industry
• Operational similarity
• Inspection workflow
• Business challenges
• FlytBase capability
• Expected business outcome

Do NOT invent information.

Return ONLY valid JSON.

{
    "matched_customer":"",
    "similarity_score":0,
    "why_relevant":"",
    "business_similarity":[
        ""
    ],
    "technical_similarity":[
        ""
    ],
    "recommended_sales_story":[
        ""
    ],
    "customer_risk_reduction":"",
    "confidence":"High | Medium | Low"
}
"""

    user_prompt = f"""
Lead

{json.dumps(lead, indent=2)}

==================================================

Research

{json.dumps(research, indent=2)}

==================================================

Qualification

{json.dumps(qualification, indent=2)}

==================================================

FlytBase Case Study Library

{case_library}

Return JSON only.
"""

    response = ask_gemini(
        system_prompt,
        user_prompt,
    )

    case_study = extract_json(response)

    save_json(
        "output/case_study.json",
        case_study,
    )

    print("✅ Case Study Matched")

    return case_study