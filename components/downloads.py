import streamlit as st


def download_section():

    st.subheader("Downloads")

    files = [
        ("Sales Brief", "output/sales_brief.md"),
        ("Meeting Prep", "output/meeting_prep.md"),
        ("Follow-up Email", "output/followup_email.md"),
        ("CRM Summary", "output/crm_summary.md"),
        ("Discovery Questions", "output/discovery_questions.md"),
    ]

    for name, path in files:

        try:

            with open(path) as f:

                st.download_button(

                    label=f"⬇ {name}",

                    data=f.read(),

                    file_name=path.split("/")[-1]

                )

        except:

            pass