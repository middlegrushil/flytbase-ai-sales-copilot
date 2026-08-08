import json

from utils.gemini_client import ask_gemini
from utils.parser import extract_json
from utils.storage import load_json, save_json


def recommend_next_action():

    print("=" * 80)
    print("➡️ Next Action Agent")
    print("=" * 80)

    qualification = load_json("output/qualification.json")
    recommendation = load_json("output/recommendation.json")
    strategy = load_json("output/strategy.json")
    risks = load_json("output/risk_analysis.json")

    system_prompt = """
You are FlytBase's Enterprise Sales Coach.

Determine the SINGLE best next action.

Consider:

- Qualification
- Risks
- Strategy
- Recommended solution

Return ONLY valid JSON.

{
    "next_action":"",
    "owner":"",
    "priority":"High | Medium | Low",
    "timeline":"",
    "reason":"",
    "expected_outcome":""
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

==================================================

Risk Analysis

{json.dumps(risks, indent=2)}

Return JSON only.
"""

    response = ask_gemini(
        system_prompt,
        user_prompt,
    )

    next_action = extract_json(response)

    save_json(
        "output/next_action.json",
        next_action,
    )

    print("✅ Next Action Generated")

    return next_action