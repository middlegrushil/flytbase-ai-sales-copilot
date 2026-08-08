import json

from utils.gemini_client import ask_gemini
from utils.storage import load_json


def generate_meeting_prep():

    print("=" * 80)
    print("📅 Meeting Preparation Agent")
    print("=" * 80)

    lead = load_json("input/lead.json")
    research = load_json("output/research.json")
    qualification = load_json("output/qualification.json")
    recommendation = load_json("output/recommendation.json")
    strategy = load_json("output/strategy.json")
    case_study = load_json("output/case_study.json")

    system_prompt = """
You are the Lead Enterprise Solutions Engineer at FlytBase.

Prepare an internal meeting brief.

Include:

- Customer overview
- Business problems
- Qualification summary
- Recommended FlytBase solution
- Relevant customer success story
- Stakeholders to engage
- Discovery priorities
- Technical validation topics
- Demo focus
- Success criteria
- Risks
- Next actions

Return MARKDOWN ONLY.

Use headings and bullet points.

Keep it professional.

Maximum 800 words.
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

==================================================

Case Study

{json.dumps(case_study, indent=2)}
"""

    meeting = ask_gemini(
        system_prompt,
        user_prompt,
    )

    with open(
        "output/meeting_prep.md",
        "w",
        encoding="utf-8",
    ) as f:

        f.write(meeting)

    print("✅ Meeting Preparation Generated")

    return meeting