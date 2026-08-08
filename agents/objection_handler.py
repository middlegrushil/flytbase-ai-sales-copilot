import json

from utils.gemini_client import ask_gemini
from utils.parser import extract_json
from utils.storage import load_json, save_json


def handle_objections():

    print("=" * 80)
    print("🛡️ Objection Handling Agent")
    print("=" * 80)

    research = load_json("output/research.json")
    recommendation = load_json("output/recommendation.json")
    strategy = load_json("output/strategy.json")

    system_prompt = """
You are a Senior Enterprise Solutions Engineer at FlytBase.

Predict the most likely customer objections.

For each objection provide:

- objection
- why_customer_might_raise_it
- recommended_response
- supporting_evidence
- confidence

Return ONLY valid JSON.

{
  "objections":[
    {
      "objection":"",
      "why_customer_might_raise_it":"",
      "recommended_response":"",
      "supporting_evidence":"",
      "confidence":"High | Medium | Low"
    }
  ]
}
"""

    user_prompt = f"""
Research

{json.dumps(research, indent=2)}

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

    objections = extract_json(response)

    save_json(
        "output/objections.json",
        objections,
    )

    print("✅ Objection Analysis Completed")

    return objections