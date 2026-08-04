import json

from utils.gemini_client import ask_gemini


def generate_meeting_prep():

    with open("input/lead.json") as f:
        lead = json.load(f)

    with open("output/qualification.json") as f:
        qualification = json.load(f)

    with open("output/research.json") as f:
        research = json.load(f)

    with open("output/strategy.json") as f:
        strategy = json.load(f)

    with open("output/recommendation.json") as f:
        recommendation = json.load(f)

    system_prompt = """
You are a Senior Solutions Engineer at FlytBase.

Prepare a concise but detailed meeting preparation document for the Account Executive.

Use ONLY the provided information.

Return the response in Markdown.
"""

    user_prompt = f"""
Lead

{json.dumps(lead, indent=2)}

Qualification

{json.dumps(qualification, indent=2)}

Research

{json.dumps(research, indent=2)}

Strategy

{json.dumps(strategy, indent=2)}

Recommendation

{json.dumps(recommendation, indent=2)}

Generate the following sections.

# Meeting Objective

# Customer Overview

# Attendees

# Business Challenges

# Key Talking Points

# Discovery Questions

Generate 10 questions.

# Recommended Demo Flow

Describe a recommended demo sequence.

# Likely Customer Objections

# Success Criteria

How will we know this meeting was successful?

# Immediate Next Steps
"""

    response = ask_gemini(system_prompt, user_prompt)

    with open("output/meeting_prep.md", "w") as f:
        f.write(response)

    print("Meeting prep generated!")