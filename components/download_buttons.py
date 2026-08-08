import os
import streamlit as st


def download_file(label, file_path):

    if not os.path.exists(file_path):
        return

    with open(file_path, "rb") as f:

        st.download_button(
            label=label,
            data=f.read(),
            file_name=os.path.basename(file_path),
            use_container_width=True,
        )


def show_download_buttons():

    # =====================================================

    st.subheader("📦 Export Sales Assets")

    col1, col2, col3 = st.columns(3)

    with col1:

        download_file(
            "📧 Customer Email",
            "output/email.md",
        )

        download_file(
            "📅 Meeting Preparation",
            "output/meeting_prep.md",
        )

    with col2:

        download_file(
            "🤝 Partner Recommendation",
            "output/partner_recommendation.md",
        )

        download_file(
            "🛡 Objection Handling",
            "output/objections.json",
        )

    with col3:

        download_file(
            "❓ Discovery Questions",
            "output/discovery_questions.md",
        )

        download_file(
            "⚠ Risk Analysis",
            "output/risk_analysis.json",
        )

    st.divider()

    # =====================================================

    st.subheader("📄 Export Reports")

    col1, col2, col3 = st.columns(3)

    with col1:

        download_file(
            "📄 Executive Sales Brief",
            "output/sales_brief.md",
        )

        download_file(
            "📝 CRM Summary",
            "output/crm_summary.md",
        )

    with col2:

        download_file(
            "🎯 Enterprise Strategy",
            "output/strategy.json",
        )

        download_file(
            "🚁 Solution Recommendation",
            "output/recommendation.json",
        )

    with col3:

        download_file(
            "👥 Stakeholder Map",
            "output/stakeholders.json",
        )

        download_file(
            "➡ Next Action",
            "output/next_action.json",
        )