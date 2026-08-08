import json

from utils.gemini_client import ask_gemini
from utils.storage import load_json


def recommend_partner():

    print("=" * 80)
    print("🤝 Partner Recommendation Agent")
    print("=" * 80)

    lead = load_json("input/lead.json")
    research = load_json("output/research.json")
    recommendation = load_json("output/recommendation.json")
    flytbase = load_json("output/flytbase_context.json")

    partner_library = (
        flytbase.get("partners", {})
        .get("markdown", "")
    )

    system_prompt = """
You are FlytBase's Global Partner Manager.

Recommend the SINGLE best implementation partner.

Reason using:

• Geography
• Industry
• Customer profile
• Technical capability
• Deployment requirements

Return MARKDOWN ONLY.

Use this structure:

# Recommended Partner

## Partner

## Why this partner

## Relevant capabilities

## Expected implementation support

## Risks

## Why other partners were not selected
"""

    user_prompt = f"""
Lead

{json.dumps(lead, indent=2)}

==================================================

Research

{json.dumps(research, indent=2)}

==================================================

Recommendation

{json.dumps(recommendation, indent=2)}

==================================================

FlytBase Partner Library

{partner_library}
"""

    partner = ask_gemini(
        system_prompt,
        user_prompt,
    )

    with open(
        "output/partner_recommendation.md",
        "w",
        encoding="utf-8",
    ) as f:

        f.write(partner)

    print("✅ Partner Recommendation Generated")

    return partner