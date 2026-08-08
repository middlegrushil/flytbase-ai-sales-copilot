import json

from utils.gemini_client import ask_gemini
from utils.storage import load_json


def generate_crm_summary():

    print("=" * 80)
    print("📝 CRM Summary Agent")
    print("=" * 80)

    lead = load_json("input/lead.json")
    research = load_json("output/research.json")
    qualification = load_json("output/qualification.json")
    recommendation = load_json("output/recommendation.json")
    strategy = load_json("output/strategy.json")

    system_prompt = """
You are a Senior Enterprise Account Executive.

Generate a CRM-ready summary.

Return MARKDOWN ONLY.

Structure:

# Opportunity Summary

## Customer

## Industry

## Business Need

## Qualification

## Recommended Solution

## Key Stakeholders

## Risks

## Next Meeting Objective

## Next Action

Maximum 400 words.
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

Strategy

{json.dumps(strategy, indent=2)}
"""

    crm = ask_gemini(
        system_prompt,
        user_prompt,
    )

    with open(
        "output/crm_summary.md",
        "w",
        encoding="utf-8",
    ) as f:

        f.write(crm)

    print("✅ CRM Summary Generated")

    return crm