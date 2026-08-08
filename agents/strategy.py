import json

from utils.gemini_client import ask_gemini
from utils.parser import extract_json
from utils.storage import load_json, save_json


def create_strategy():

    print("=" * 80)
    print("🎯 Enterprise Sales Strategy Agent")
    print("=" * 80)

    lead = load_json("input/lead.json")

    research = load_json("output/research.json")

    qualification = load_json("output/qualification.json")

    recommendation = load_json("output/recommendation.json")

    case_study = load_json("output/case_study.json")

    system_prompt = """
You are FlytBase's Lead Enterprise Solutions Engineer.

Build the internal sales strategy.

Think like an Enterprise AE + Solutions Engineer.

Reasoning order

Customer

↓

Problems

↓

Business Impact

↓

Technical Fit

↓

Commercial Fit

↓

Discovery Plan

↓

Demo Plan

↓

Meeting Success Criteria

Return ONLY valid JSON.

{
    "pursue_opportunity":true,

    "priority":"High | Medium | Low",

    "meeting_objective":"",

    "why_pursue":[
        {
            "reason":"",
            "evidence":""
        }
    ],

    "technical_validation":[
        {
            "question":"",
            "why_it_matters":""
        }
    ],

    "commercial_validation":[
        {
            "question":"",
            "why_it_matters":""
        }
    ],

    "recommended_demo":[
        {
            "feature":"",
            "business_reasoning":""
        }
    ],

    "recommended_stakeholders":[
        {
            "role":"",
            "reason":""
        }
    ],

    "technical_risks":[
        {
            "risk":"",
            "mitigation":""
        }
    ],

    "commercial_risks":[
        {
            "risk":"",
            "mitigation":""
        }
    ],

    "success_criteria":[
        ""
    ],

    "next_best_actions":[
        ""
    ],

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

Recommendation

{json.dumps(recommendation, indent=2)}

==================================================

Case Study

{json.dumps(case_study, indent=2)}

Return JSON only.
"""

    response = ask_gemini(
        system_prompt,
        user_prompt,
    )

    strategy = extract_json(response)

    save_json(
        "output/strategy.json",
        strategy,
    )

    print("✅ Strategy Generated")

    return strategy