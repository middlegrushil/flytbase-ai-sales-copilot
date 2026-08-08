import json

from utils.gemini_client import ask_gemini
from utils.storage import load_json


def generate_report():

    print("=" * 80)
    print("📄 Executive Sales Brief Agent")
    print("=" * 80)

    lead = load_json("input/lead.json")
    research = load_json("output/research.json")
    qualification = load_json("output/qualification.json")
    recommendation = load_json("output/recommendation.json")
    strategy = load_json("output/strategy.json")
    case_study = load_json("output/case_study.json")
    stakeholders = load_json("output/stakeholders.json")
    objections = load_json("output/objections.json")
    risks = load_json("output/risk_analysis.json")
    next_action = load_json("output/next_action.json")

    system_prompt = """
You are preparing an executive sales brief for FlytBase leadership.

Create a concise executive report.

Return MARKDOWN ONLY.

Structure:

# Executive Sales Brief

## Opportunity Overview

## Customer Summary

## Qualification

## Business Problems

## Recommended FlytBase Solution

## Similar Customer Success Story

## Stakeholders

## Key Risks

## Expected Business Value

## Sales Strategy

## Recommended Next Action

## Executive Recommendation

Maximum 1000 words.
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

==================================================

Stakeholders

{json.dumps(stakeholders, indent=2)}

==================================================

Objections

{json.dumps(objections, indent=2)}

==================================================

Risks

{json.dumps(risks, indent=2)}

==================================================

Next Action

{json.dumps(next_action, indent=2)}
"""

    report = ask_gemini(
        system_prompt,
        user_prompt,
    )

    with open(
        "output/sales_brief.md",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(report)

    print("✅ Executive Sales Brief Generated")

    return report