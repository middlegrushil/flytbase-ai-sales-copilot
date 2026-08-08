import json

from utils.gemini_client import ask_gemini
from utils.parser import extract_json
from utils.storage import load_json, save_json


def analyze_risks():

    print("=" * 80)
    print("⚠ Risk Analysis Agent")
    print("=" * 80)

    qualification = load_json("output/qualification.json")
    recommendation = load_json("output/recommendation.json")
    strategy = load_json("output/strategy.json")

    system_prompt = """
You are FlytBase's Enterprise Risk Assessment Specialist.

Assess the opportunity.

Identify:

• Technical risks
• Commercial risks
• Deployment risks
• Adoption risks
• Procurement risks

Return ONLY valid JSON.

{
    "overall_risk":"Low | Medium | High",

    "technical_risks":[
        {
            "risk":"",
            "severity":"Low | Medium | High",
            "mitigation":""
        }
    ],

    "commercial_risks":[
        {
            "risk":"",
            "severity":"Low | Medium | High",
            "mitigation":""
        }
    ],

    "deployment_risks":[
        {
            "risk":"",
            "severity":"Low | Medium | High",
            "mitigation":""
        }
    ],

    "recommendation":""
}
"""

    user_prompt = f"""
Qualification

{json.dumps(qualification, indent=2)}

==================================================

Recommendation

{json.dumps(recommendation, indent=2)}

==================================================

Strategy

{json.dumps(strategy, indent=2)}

Return JSON only.
"""

    response = ask_gemini(
        system_prompt,
        user_prompt,
    )

    risks = extract_json(response)

    save_json(
        "output/risk_analysis.json",
        risks,
    )

    print("✅ Risk Analysis Completed")

    return risks