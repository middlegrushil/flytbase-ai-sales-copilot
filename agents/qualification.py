import json

from utils.gemini_client import ask_gemini
from utils.parser import extract_json
from utils.storage import load_json, save_json


def qualify_lead():

    print("=" * 80)
    print("📈 Lead Qualification Agent")
    print("=" * 80)

    lead = load_json("input/lead.json")
    research = load_json("output/research.json")

    system_prompt = """
You are FlytBase's Enterprise Sales Qualification Specialist.

Evaluate the opportunity.

Use BOTH:

1. Lead information
2. Company research

Return ONLY valid JSON.

{
  "qualification_score":0,
  "priority":"High | Medium | Low",
  "industry_fit":"",
  "use_case_fit":"",
  "company_size_fit":"",
  "automation_readiness":"",
  "decision_process":"",
  "budget_signal":"",
  "timeline_signal":"",
  "pain_points":[
      ""
  ],
  "strengths":[
      ""
  ],
  "risks":[
      ""
  ],
  "qualification_summary":"",
  "confidence":"High | Medium | Low"
}
"""

    user_prompt = f"""
Lead

{json.dumps(lead, indent=2)}

==================================================

Research

{json.dumps(research, indent=2)}

Return JSON only.
"""

    response = ask_gemini(
        system_prompt,
        user_prompt,
    )

    qualification = extract_json(response)

    save_json(
        "output/qualification.json",
        qualification,
    )

    print("✅ Qualification Completed")

    return qualification