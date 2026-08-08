import json
import os


def load_json(path):

    if not os.path.exists(path):
        return {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def load_markdown(path):

    if not os.path.exists(path):
        return ""

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def load_outputs():

    return {

        "qualification":
        load_json("output/qualification.json"),

        "research":
        load_json("output/research.json"),

        "strategy":
        load_json("output/strategy.json"),

        "recommendation":
        load_json("output/recommendation.json"),

        "case_study":
        load_json("output/case_study.json"),

        "objections":
        load_json("output/objections.json"),

        "risk_analysis":
        load_json("output/risk_analysis.json"),

        "stakeholders":
        load_json("output/stakeholders.json"),

        "next_action":
        load_json("output/next_action.json"),

        "meeting_prep":
        load_markdown("output/meeting_prep.md"),

        "followup_email":
        load_markdown("output/email.md"),

        "discovery_questions":
        load_markdown("output/discovery_questions.md"),

        "crm_summary":
        load_markdown("output/crm_summary.md"),

        "sales_brief":
        load_markdown("output/sales_brief.md"),

        "partner_recommendation":
        load_markdown("output/partner_recommendation.md"),
    }