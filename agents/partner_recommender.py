import json
import os

from utils.gemini import ask_gemini


def recommend_partner():
    """
    Recommend the best FlytBase implementation partner
    for the inbound customer.
    """

    if not os.path.exists("input/lead.json"):
        print("❌ lead.json not found")
        return

    if not os.path.exists("output/flytbase_context.json"):
        print("❌ flytbase_context.json not found")
        return

    with open("input/lead.json", "r") as f:
        lead = json.load(f)

    with open("output/flytbase_context.json", "r") as f:
        flytbase = json.load(f)

    partners = flytbase.get("partners", {})
    markdown = partners.get("markdown", "")

    prompt = f"""
You are a FlytBase Partner Manager.

A new enterprise lead has arrived.

Lead Details:

{json.dumps(lead, indent=2)}

Below is FlytBase's partner ecosystem.

{markdown}

Your task:

Recommend the BEST implementation partner for this customer.

Return ONLY markdown.

Use the following format:

# Recommended Partner

Partner Name

# Why this Partner

Explain why it fits this customer.

# Relevant Experience

Mention industries, geography or deployment expertise.

# Deployment Advantages

Explain why this partner can help.

# Suggested Introduction

Write a short paragraph the sales team can use.
"""

    recommendation = ask_gemini(prompt)

    os.makedirs("output", exist_ok=True)

    with open("output/partner_recommendation.md", "w") as f:
        f.write(recommendation)

    print("✅ Partner recommendation generated.")