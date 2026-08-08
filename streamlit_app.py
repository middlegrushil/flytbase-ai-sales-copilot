import streamlit as st
from components.metrics import show_metrics

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="FlytBase Enterprise Sales Intelligence Platform",
    page_icon="🚁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# LOAD CSS
# ==========================================================

try:

    with open("styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )

except Exception:

    pass

# ==========================================================
# COMPONENTS
# ==========================================================

from components.hero import show_hero
from components.sidebar import show_sidebar
from components.executive_dashboard import (
    show_executive_dashboard,
)
from components.company_snapshot import (
    show_company_snapshot,
)
from components.tabs import show_tabs
from components.download_buttons import (
    show_download_buttons,
)

# ==========================================================
# UI PIPELINE
# ==========================================================

from ui.upload import upload_lead
from ui.pipeline import run_pipeline
from ui.loader import load_outputs

# ==========================================================
# SIDEBAR
# ==========================================================

show_sidebar()

# ==========================================================
# HERO
# ==========================================================

show_hero()

# ==========================================================
# PAGE INTRO
# ==========================================================

st.markdown(
"""
### Enterprise AI Decision Support

This platform assists **FlytBase Solutions Engineers**
by automating enterprise lead qualification,
company intelligence gathering,
solution recommendation,
case study matching,
meeting preparation,
and executive sales documentation.

The platform follows a modular AI workflow where
each specialized agent contributes structured
business intelligence to support sales decisions.
"""
)

st.divider()

# ==========================================================
# LEAD INPUT
# ==========================================================

uploaded = upload_lead()

# ==========================================================
# MAIN
# ==========================================================

# ==========================================================
# MAIN APPLICATION
# ==========================================================

if uploaded:

    st.divider()

    analyze = st.button(
        "🚀 Analyze Enterprise Lead",
        type="primary",
        use_container_width=True,
    )

    if analyze:

        with st.spinner(
            "Running Enterprise Sales Intelligence Pipeline..."
        ):

            run_pipeline()

        outputs = load_outputs()

        qualification = outputs["qualification"]
        research = outputs["research"]
        strategy = outputs["strategy"]
        recommendation = outputs["recommendation"]
        case_study = outputs["case_study"]
        objections = outputs["objections"]
        risks = outputs["risk_analysis"]
        stakeholders = outputs["stakeholders"]
        next_action = outputs["next_action"]
        meeting = (
    outputs.get("meeting_prep")
    or ""
)
        email = (
    outputs.get("followup_email")
    or outputs.get("email")
    or ""
)
        discovery = (
    outputs.get("discovery_questions")
    or ""
)
        crm = (
    outputs.get("crm_summary")
    or ""
)
        report = (
    outputs.get("sales_brief")
    or ""
)
        partner = (
    outputs.get("partner_recommendation")
    or ""
)

        st.success(
            "Enterprise opportunity successfully analyzed."
        )

        # =====================================================
        # EXECUTIVE DASHBOARD
        # =====================================================

        show_executive_dashboard(
            qualification=qualification,
            research=research,
            recommendation=recommendation,
            next_action=next_action,
        )
        show_metrics(
    qualification=qualification,
    research=research,
    stakeholders=stakeholders,
)

        st.divider()

        # =====================================================
        # COMPANY INTELLIGENCE
        # =====================================================

        show_company_snapshot(
    research=research,
    recommendation=recommendation,
    case_study=case_study,
    qualification=qualification,
    stakeholders=stakeholders,
)

        st.divider()

        # =====================================================
        # AI ANALYSIS
        # =====================================================

        st.header("🧠 Enterprise AI Analysis")

        st.caption(
            """
Each section below represents a specialized AI agent
within the FlytBase Enterprise Sales Intelligence workflow.
The agents work together to transform an inbound lead
into an executive-ready sales opportunity.
"""
        )

        show_tabs(
            qualification=qualification,
            research=research,
            strategy=strategy,
            recommendation=recommendation,
            partner=partner,
            meeting=meeting,
            email=email,
            discovery=discovery,
            objections=objections,
            risks=risks,
            stakeholders=stakeholders,
            crm=crm,
            report=report,
        )

        st.divider()

        # =====================================================
        # DOWNLOADS
        # =====================================================

        st.header("📥 Export Sales Assets")

        st.caption(
            "Download AI-generated artifacts for CRM, meetings and customer engagement."
        )

        

        show_download_buttons()

else:

    st.divider()

    st.markdown(
        """
# 🚁 FlytBase Enterprise Sales Intelligence Platform

Transform enterprise inbound leads into actionable sales opportunities using an explainable multi-agent AI workflow.

---

## What this platform does

Instead of manually researching every customer, the platform automatically performs:

✅ Lead Qualification

✅ Company Intelligence

✅ Solution Recommendation

✅ Customer Case Study Matching

✅ Partner Recommendation

✅ Meeting Preparation

✅ Discovery Question Generation

✅ Objection Handling

✅ Risk Assessment

✅ Stakeholder Mapping

✅ CRM Summary Generation

✅ Executive Sales Brief Creation

---

## Why this matters

Enterprise pre-sales activities often require several hours of manual work across multiple tools.

This platform standardizes the entire workflow into a modular AI pipeline that produces consistent, explainable and executive-ready outputs within minutes.

Upload a Lead JSON file and click **Analyze Enterprise Lead** to begin.
"""
    )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.caption("🚁 FlytBase Enterprise Sales Intelligence Platform")

with col2:
    st.caption("Built with Gemini • Tavily • Firecrawl • Streamlit")

with col3:
    st.caption("Multi-Agent AI Architecture")

st.caption(
"""
Designed as an explainable AI decision-support platform for enterprise
lead qualification, solution engineering and sales enablement.

Each AI agent performs a specialized business task and contributes
structured intelligence to a modular enterprise workflow.
"""
)

# ==========================================================
# ARCHITECTURE
# ==========================================================

with st.expander("🏗 System Architecture", expanded=False):

    st.markdown(
"""
## Enterprise Workflow

Lead Upload

⬇️

Company Intelligence

⬇️

Lead Qualification

⬇️

Solution Strategy

⬇️

Recommendation Engine

⬇️

Case Study Matching

⬇️

Partner Recommendation

⬇️

Meeting Preparation

⬇️

Risk Assessment

⬇️

CRM Summary

⬇️

Executive Sales Brief

---

## Why a Multi-Agent Workflow?

Each AI agent is responsible for one specialized enterprise sales task.

This modular architecture improves:

- Explainability
- Maintainability
- Scalability
- Reusability
- Decision transparency

Rather than relying on a single large prompt, the workflow breaks the sales process into structured business decisions, making recommendations easier to validate and extend.
"""
    )

# ==========================================================
# ABOUT
# ==========================================================

with st.expander("ℹ️ About This Project"):

    st.markdown(
        """
## FlytBase AI Sales Copilot

### Workflow

1. FlytBase Knowledge Base (Firecrawl)

2. Similar Case Study Matching

3. Lead Qualification

4. Company Research (Tavily)

5. Sales Strategy

6. Solution Recommendation

7. Meeting Preparation

8. Follow-up Email

9. Discovery Questions

10. Objection Handling

11. Risk Analysis

12. Stakeholder Mapping

13. CRM Summary

14. Executive Sales Brief

---

### Tech Stack

- Python
- Streamlit
- OpenRouter
- Firecrawl
- Tavily Search
- Multi-Agent AI Pipeline

---

Each AI agent performs one specific enterprise sales task and
passes structured outputs to downstream agents.
"""
    )