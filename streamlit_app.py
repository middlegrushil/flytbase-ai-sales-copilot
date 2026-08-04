import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="FlytBase AI Sales Copilot",
    page_icon="🚁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

try:
    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# ==========================================================
# COMPONENTS
# ==========================================================

from components.hero import show_hero
from components.sidebar import show_sidebar
from components.metric_cards import show_metric_cards
from components.dashboard import show_dashboard
from components.charts import show_charts
from components.tabs import show_tabs
from components.download_buttons import show_download_buttons

# ==========================================================
# UI
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
# UPLOAD
# ==========================================================

uploaded = upload_lead()

# ==========================================================
# MAIN
# ==========================================================

if uploaded:

    st.divider()

    if st.button(
        "🚀 Analyze Lead",
        use_container_width=True,
        type="primary"
    ):

        with st.spinner("Running AI Sales Copilot..."):

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
        meeting = outputs["meeting_prep"]
        email = outputs["followup_email"]
        discovery = outputs["discovery_questions"]
        crm = outputs["crm_summary"]
        report = outputs["sales_brief"]
        partner = outputs["partner_recommendation"]

        st.success("🎉 Analysis Completed Successfully!")

        # ==========================================================
        # EXECUTIVE METRICS
        # ==========================================================

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("AI Agents", "14")

        with c2:
            st.metric("Knowledge Sources", "3")

        with c3:
            st.metric("Case Studies", "✓")

        with c4:
            score = qualification.get("qualification_score", 0)
            st.metric("Qualification", f"{score}/100")

        st.progress(score / 100 if score else 0)

        st.divider()

        # ==========================================================
        # DASHBOARD
        # ==========================================================

        show_metric_cards(
            qualification,
            research
        )

        st.divider()

        show_dashboard(
            qualification,
            research,
            recommendation,
            next_action
        )

        st.divider()

        show_charts(
            qualification
        )

        st.divider()

        # ==========================================================
        # COMPANY SNAPSHOT
        # ==========================================================

        left, right = st.columns([2, 1])

        with left:

            st.subheader("🏢 Company Overview")

            st.info(
                research.get(
                    "company_overview",
                    "No company overview available."
                )
            )

            st.subheader("🚁 Recommended Solution")

            if isinstance(recommendation, dict):

                st.markdown(
                    recommendation.get(
                        "recommendation",
                        str(recommendation)
                    )
                )

            else:

                st.markdown(recommendation)

            st.subheader("📚 Similar FlytBase Case Study")

            if isinstance(case_study, dict):

                st.markdown(
                    case_study.get(
                        "case_study",
                        "No case study found."
                    )
                )

            else:

                st.markdown(case_study)

        with right:

            st.subheader("Quick Stats")

            st.metric(
                "Industry",
                research.get("industry", "Unknown")
            )

            st.metric(
                "Champion",
                qualification.get("champion", "Unknown")
            )

            st.metric(
                "Economic Buyer",
                qualification.get(
                    "economic_buyer",
                    "Unknown"
                )
            )

            if score >= 80:

                st.success("🟢 High Opportunity")

            elif score >= 60:

                st.warning("🟡 Medium Opportunity")

            else:

                st.error("🔴 Low Opportunity")

        st.divider()

        # ==========================================================
        # AGENT OUTPUTS
        # ==========================================================

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
    report=report
)

        st.divider()

        # ==========================================================
        # NEXT ACTION
        # ==========================================================

        st.header("➡️ Recommended Next Action")

        if isinstance(next_action, dict):

            st.success(
                next_action.get(
                    "next_action",
                    "No recommendation."
                )
            )

        else:

            st.success(next_action)

        st.divider()

        # ==========================================================
        # DOWNLOADS
        # ==========================================================

        show_download_buttons()

else:

    st.divider()

    st.info(
        """
### Welcome to FlytBase AI Sales Copilot

Upload a Lead JSON file to begin.

The platform will automatically:

✅ Build FlytBase Knowledge Base

✅ Match Similar Case Study

✅ Qualify Lead

✅ Research Company

✅ Recommend FlytBase Solution

✅ Prepare Meeting Notes

✅ Generate Email

✅ Generate Discovery Questions

✅ Handle Objections

✅ Analyze Risks

✅ Map Stakeholders

✅ Generate CRM Summary

✅ Generate Executive Sales Brief
"""
    )

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    st.caption("🚁 FlytBase AI Sales Copilot")

with col2:

    st.caption("Powered by OpenRouter • Firecrawl • Tavily")

with col3:

    st.caption("Enterprise AI Sales Copilot")

st.caption(
    """
Built as a multi-agent AI workflow for enterprise inbound
lead qualification and solution recommendation.
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