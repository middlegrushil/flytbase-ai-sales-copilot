import json

from utils.gemini_client import ask_gemini
from utils.parser import extract_json
from utils.storage import load_json, save_json


def identify_stakeholders():

    print("=" * 80)
    print("👥 Stakeholder Mapping Agent")
    print("=" * 80)

    lead = load_json("input/lead.json")
    research = load_json("output/research.json")
    qualification = load_json("output/qualification.json")
    recommendation = load_json("output/recommendation.json")

    system_prompt = """
You are FlytBase's Enterprise Account Strategist.

Identify the buying committee.

Infer likely stakeholders.

Return ONLY valid JSON.

{
  "champion":{
      "role":"",
      "responsibility":"",
      "engagement_strategy":""
  },

  "economic_buyer":{
      "role":"",
      "responsibility":"",
      "engagement_strategy":""
  },

  "technical_buyer":{
      "role":"",
      "responsibility":"",
      "engagement_strategy":""
  },

  "operations":{
      "role":"",
      "responsibility":"",
      "engagement_strategy":""
  },

  "procurement":{
      "role":"",
      "responsibility":"",
      "engagement_strategy":""
  },

  "executive_sponsor":{
      "role":"",
      "responsibility":"",
      "engagement_strategy":""
  }
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

Recommendation

{json.dumps(recommendation, indent=2)}

Return JSON only.
"""

    response = ask_gemini(
        system_prompt,
        user_prompt,
    )

    stakeholders = extract_json(response)

    save_json(
        "output/stakeholders.json",
        stakeholders,
    )

    print("✅ Stakeholder Mapping Completed")

    return stakeholders