import streamlit as st
import os


def download_file(label, file_path):
    """
    Creates a download button for a file.
    """

    if not os.path.exists(file_path):
        return

    with open(file_path, "rb") as f:

        st.download_button(
            label=label,
            data=f.read(),
            file_name=os.path.basename(file_path),
            use_container_width=True
        )


def show_download_buttons():
    """
    Displays all download buttons.
    """

    st.header("📥 Export Reports")

    col1, col2, col3 = st.columns(3)

    with col1:

        download_file(
            "📄 Sales Brief",
            "output/sales_brief.md"
        )

        download_file(
            "📅 Meeting Prep",
            "output/meeting_prep.md"
        )

    with col2:

        download_file(
            "📧 Follow-up Email",
            "output/followup_email.md"
        )

        download_file(
            "📝 CRM Summary",
            "output/crm_summary.md"
        )

    with col3:

        download_file(
            "❓ Discovery Questions",
            "output/discovery_questions.md"
        )

        download_file(
            "🎯 Strategy",
            "output/strategy.json"
        )