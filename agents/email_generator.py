import json

from utils.gemini_client import ask_gemini
from utils.storage import load_json


def generate_email():

    print("=" * 80)
    print("📧 Follow-up Email Agent")
    print("=" * 80)

    lead = load_json("input/lead.json")
    research = load_json("output/research.json")
    recommendation = load_json("output/recommendation.json")
    strategy = load_json("output/strategy.json")
    case_study = load_json("output/case_study.json")

    system_prompt = """
You are a Senior Enterprise Account Executive at FlytBase.

Write a professional follow-up email.

The email must sound human.

Do NOT sound like AI.

Structure:

Subject

Greeting

Personalized opening

Customer understanding

Business value

Relevant FlytBase customer success story

Suggested next meeting

Professional closing

Return MARKDOWN ONLY.

Maximum 350 words.
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

Strategy

{json.dumps(strategy, indent=2)}

==================================================

Case Study

{json.dumps(case_study, indent=2)}
"""

    email = ask_gemini(
        system_prompt,
        user_prompt,
    )

    with open(
        "output/email.md",
        "w",
        encoding="utf-8",
    ) as f:

        f.write(email)

    print("✅ Follow-up Email Generated")

    return email