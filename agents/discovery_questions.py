import json

from utils.gemini_client import ask_gemini
from utils.storage import load_json


def generate_discovery_questions():

    print("=" * 80)
    print("❓ Discovery Questions Agent")
    print("=" * 80)

    research = load_json("output/research.json")
    qualification = load_json("output/qualification.json")
    recommendation = load_json("output/recommendation.json")
    strategy = load_json("output/strategy.json")

    system_prompt = """
You are a Senior Enterprise Solutions Engineer at FlytBase.

Generate enterprise discovery questions.

Group questions under these headings:

## Business

## Operations

## Drone Program

## Technical

## Security

## Deployment

## ROI

## Procurement

## Timeline

## Success Metrics

Return MARKDOWN ONLY.

Use numbered questions.

Maximum 15 questions.
"""

    user_prompt = f"""
Company Research

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

    questions = ask_gemini(
        system_prompt,
        user_prompt,
    )

    with open(
        "output/discovery_questions.md",
        "w",
        encoding="utf-8",
    ) as f:

        f.write(questions)

    print("✅ Discovery Questions Generated")

    return questions