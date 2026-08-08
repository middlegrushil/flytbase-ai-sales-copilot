import json

from utils.gemini_client import ask_gemini
from utils.parser import extract_json
from utils.storage import load_json, save_json


def recommend_solution():

    print("=" * 80)
    print("🚁 Solution Recommendation Agent")
    print("=" * 80)

    lead = load_json("input/lead.json")

    research = load_json("output/research.json")

    qualification = load_json("output/qualification.json")

    case_study = load_json("output/case_study.json")

    flytbase = load_json("output/flytbase_context.json")

    solution_info = (
        flytbase.get("solutions", {})
        .get("markdown", "")
    )

    product_info = (
        flytbase.get("products", {})
        .get("markdown", "")
    )

    system_prompt = """
You are the Lead Enterprise Solutions Engineer at FlytBase.

Your task is to recommend the SINGLE best FlytBase solution.

Reasoning order:

Customer Facts

↓

Business Problems

↓

Operational Challenges

↓

FlytBase Capability Mapping

↓

Recommended Product

↓

Expected Business Outcomes

Never invent information.

Use only supplied evidence.

Return ONLY valid JSON.

{
    "recommended_solution":{
        "product":"",
        "overall_fit_score":0,
        "confidence":"High | Medium | Low"
    },

    "customer_pain_points":[
        {
            "pain":"",
            "evidence":""
        }
    ],

    "solution_mapping":[
        {
            "customer_need":"",
            "flytbase_capability":"",
            "technical_reasoning":"",
            "business_reasoning":""
        }
    ],

    "business_value":[
        {
            "benefit":"",
            "expected_impact":""
        }
    ],

    "implementation_plan":[
        ""
    ],

    "risks":[
        {
            "risk":"",
            "mitigation":""
        }
    ],

    "similar_case_study":{
        "customer":"",
        "similarity":"",
        "why_relevant":""
    },

    "alternative_products":[
        {
            "product":"",
            "why_not_selected":""
        }
    ],

    "executive_summary":""
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

Case Study

{json.dumps(case_study, indent=2)}

==================================================

FlytBase Solutions

{solution_info}

==================================================

FlytBase Products

{product_info}

Return JSON only.
"""

    response = ask_gemini(
        system_prompt,
        user_prompt,
    )

    recommendation = extract_json(response)

    save_json(
        "output/recommendation.json",
        recommendation,
    )

    print("✅ Recommendation Generated")

    return recommendation