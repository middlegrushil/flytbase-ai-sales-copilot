import json

from utils.gemini_client import ask_gemini


def generate_report():

    # -----------------------------
    # Load Files
    # -----------------------------
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

    with open("output/stakeholders.json") as f:
        stakeholders = json.load(f)

    with open("output/objections.json") as f:
        objections = json.load(f)

    with open("output/risk_analysis.json") as f:
        risks = json.load(f)

    with open("output/next_action.json") as f:
        next_action = json.load(f)

    with open("output/meeting_prep.md") as f:
        meeting_prep = f.read()

    with open("output/crm_summary.md") as f:
        crm_summary = f.read()

    with open("output/discovery_questions.md") as f:
        discovery_questions = f.read()

    with open("output/followup_email.md") as f:
        followup_email = f.read()

    # -----------------------------
    # Prompt
    # -----------------------------
    prompt = f"""
You are a Senior Enterprise Sales Consultant at FlytBase.

Prepare a professional INTERNAL SALES BRIEF.

Use ONLY the information provided below.

==================================================
LEAD
==================================================

{json.dumps(lead, indent=2)}

==================================================
QUALIFICATION
==================================================

{json.dumps(qualification, indent=2)}

==================================================
RESEARCH
==================================================

{json.dumps(research, indent=2)}

==================================================
STRATEGY
==================================================

{json.dumps(strategy, indent=2)}

==================================================
RECOMMENDATION
==================================================

{json.dumps(recommendation, indent=2)}

==================================================
STAKEHOLDERS
==================================================

{json.dumps(stakeholders, indent=2)}

==================================================
OBJECTIONS
==================================================

{json.dumps(objections, indent=2)}

==================================================
RISK ANALYSIS
==================================================

{json.dumps(risks, indent=2)}

==================================================
NEXT ACTION
==================================================

{json.dumps(next_action, indent=2)}

==================================================
MEETING PREP
==================================================

{meeting_prep}

==================================================
CRM SUMMARY
==================================================

{crm_summary}

==================================================
DISCOVERY QUESTIONS
==================================================

{discovery_questions}

==================================================
FOLLOW-UP EMAIL
==================================================

{followup_email}

==================================================

Generate a comprehensive sales brief with these sections:

# Executive Summary

# Opportunity Health

# Customer Overview

# MEDDPICC Summary

# Stakeholder Mapping

# Business Challenges

# Recommended FlytBase Solution

# Sales Strategy

# Meeting Preparation

# Discovery Questions

# Customer Objections

# Risk Assessment

# CRM Summary

# Follow-up Plan

# Immediate Next Action

# Executive Takeaway

Return ONLY Markdown.
"""

    report = ask_gemini(
        "You are a Senior Enterprise Sales Consultant.",
        prompt
    )

    with open("output/sales_brief.md", "w") as f:
        f.write(report)

    print("Sales brief generated!")