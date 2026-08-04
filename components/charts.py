import streamlit as st


def opportunity_color(score):

    if score >= 80:
        return "green"

    elif score >= 60:
        return "orange"

    return "red"


def show_charts(qualification):
    """
    Displays qualification visualizations.
    """

    st.subheader("📈 Lead Qualification")

    score = qualification.get(
        "qualification_score",
        0
    )

    st.progress(score / 100)

    color = opportunity_color(score)

    if color == "green":

        st.success(
            "High-quality enterprise opportunity."
        )

    elif color == "orange":

        st.warning(
            "Medium opportunity. More discovery recommended."
        )

    else:

        st.error(
            "Low opportunity."
        )

    st.metric(
        "Overall Qualification Score",
        f"{score}/100"
    )

    st.caption(
        "Qualification score generated using the AI Lead Qualification Agent."
    )