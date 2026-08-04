import streamlit as st


def render_dictionary(data):
    """
    Nicely render dictionaries, lists and strings.
    """

    if data is None:
        st.info("No data available.")
        return

    if isinstance(data, str):
        st.markdown(data)
        return

    if not isinstance(data, dict):
        st.write(data)
        return

    for key, value in data.items():

        title = key.replace("_", " ").title()

        with st.container(border=True):

            st.markdown(f"### {title}")

            if isinstance(value, list):

                for item in value:
                    st.markdown(f"- {item}")

            elif isinstance(value, dict):

                for k, v in value.items():

                    st.markdown(
                        f"**{k.replace('_',' ').title()}**"
                    )

                    st.write(v)

            else:

                st.write(value)


def show_tabs(
    qualification,
    research,
    strategy,
    recommendation,
    partner,
    meeting,
    email,
    discovery,
    objections,
    risks,
    stakeholders,
    crm,
    report,
):
    """
    Display every AI Agent output.
    """

    (
        tab1,
        tab2,
        tab3,
        tab4,
        tab5,
        tab6,
        tab7,
        tab8,
        tab9,
        tab10,
        tab11,
        tab12,
        tab13,
    ) = st.tabs(
        [
            "📋 Qualification",
            "🔍 Research",
            "🎯 Strategy",
            "🚁 Recommendation",
            "🤝 Partner",
            "📅 Meeting",
            "📧 Email",
            "❓ Discovery",
            "⚠️ Objections",
            "🛡️ Risks",
            "👥 Stakeholders",
            "📝 CRM",
            "📄 Sales Brief",
        ]
    )

    with tab1:

        st.subheader("Lead Qualification")

        render_dictionary(qualification)

    with tab2:

        st.subheader("Company Intelligence")

        render_dictionary(research)

    with tab3:

        st.subheader("Sales Strategy")

        render_dictionary(strategy)

    with tab4:

        st.subheader("Recommended FlytBase Solution")

        render_dictionary(recommendation)

    with tab5:

        st.subheader("Recommended FlytBase Partner")

        st.markdown(partner)

    with tab6:

        st.subheader("Meeting Preparation")

        st.markdown(meeting)

    with tab7:

        st.subheader("Follow-up Email")

        st.markdown(email)

    with tab8:

        st.subheader("Discovery Questions")

        st.markdown(discovery)

    with tab9:

        st.subheader("Objection Handling")

        render_dictionary(objections)

    with tab10:

        st.subheader("Risk Analysis")

        render_dictionary(risks)

    with tab11:

        st.subheader("Stakeholder Mapping")

        render_dictionary(stakeholders)

    with tab12:

        st.subheader("CRM Summary")

        st.markdown(crm)

    with tab13:

        st.subheader("Executive Sales Brief")

        st.markdown(report)