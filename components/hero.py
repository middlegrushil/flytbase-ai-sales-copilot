import streamlit as st


def show_hero():
    """
    Displays the application hero section.
    """

    st.markdown(
        """
        <div style="
            background:#f8fafc;
            padding:30px;
            border-radius:16px;
            border:1px solid #e5e7eb;
            margin-bottom:25px;
        ">

        <h1 style="margin-bottom:0px;">
        🚁 FlytBase AI Sales Copilot
        </h1>

        <h4 style="color:#6b7280;">
        Enterprise Sales Intelligence Platform
        </h4>

        <p style="font-size:16px; color:#4b5563;">

        Automatically qualify enterprise leads, research companies,
        generate tailored sales strategies, recommend FlytBase
        autonomous drone solutions, prepare meetings,
        draft follow-up emails, analyze risks,
        and generate complete enterprise sales briefs.

        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )