import json
import streamlit as st


def render(data):

    if data is None or data == {} or data == "" or data == []:
        st.info("No information available.")
        return

    # -----------------------------------------------------
    # Markdown
    # -----------------------------------------------------

    if isinstance(data, str):

        if data.strip().startswith("#"):
            st.markdown(data)
        else:
            st.write(data)

        return

    # -----------------------------------------------------
    # List
    # -----------------------------------------------------

    if isinstance(data, list):

        for item in data:

            if isinstance(item, dict):

                st.markdown("---")

                for k, v in item.items():

                    st.markdown(
                        f"**{k.replace('_',' ').title()}**"
                    )

                    if isinstance(v, list):

                        for x in v:
                            st.markdown(f"- {x}")

                    elif isinstance(v, dict):

                        st.json(v)

                    else:

                        st.write(v)

            else:

                st.markdown(f"• {item}")

        return

    # -----------------------------------------------------
    # Dictionary
    # -----------------------------------------------------

    if isinstance(data, dict):

        for key, value in data.items():

            title = key.replace("_", " ").title()

            with st.expander(title, expanded=True):

                if isinstance(value, dict):

                    for k, v in value.items():

                        st.markdown(
                            f"**{k.replace('_',' ').title()}**"
                        )

                        if isinstance(v, list):

                            for x in v:
                                st.markdown(f"- {x}")

                        elif isinstance(v, dict):

                            for a, b in v.items():

                                st.markdown(
                                    f"**{a.replace('_',' ').title()}**"
                                )

                                st.write(b)

                        else:

                            st.write(v)

                elif isinstance(value, list):

                    for item in value:

                        if isinstance(item, dict):

                            st.markdown("---")

                            for a, b in item.items():

                                st.markdown(
                                    f"**{a.replace('_',' ').title()}**"
                                )

                                if isinstance(b, list):

                                    for x in b:
                                        st.markdown(f"- {x}")

                                else:

                                    st.write(b)

                        else:

                            st.markdown(f"• {item}")

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

    tabs = st.tabs(
        [
            "📈 Opportunity",
            "🏢 Intelligence",
            "🚁 Solution",
            "🎯 Strategy",
            "🤝 Engagement",
            "📄 Executive Brief",
        ]
    )

    # =====================================================

    with tabs[0]:

        st.subheader("Opportunity Qualification")
        render(qualification)

        st.divider()

        st.subheader("Stakeholder Mapping")
        render(stakeholders)

        st.divider()

        st.subheader("Risk Analysis")
        render(risks)

    # =====================================================

    with tabs[1]:

        st.subheader("Company Intelligence")
        render(research)

        st.divider()

        st.subheader("Recommended Partner")

        if partner:
            st.markdown(partner)
        else:
            st.info("No partner recommendation generated.")

    # =====================================================

    with tabs[2]:

        st.subheader("Recommended FlytBase Solution")
        render(recommendation)

        st.divider()

        st.subheader("Discovery Questions")

        if discovery:
            st.markdown(discovery)
        else:
            st.info("Discovery questions unavailable.")

    # =====================================================

    with tabs[3]:

        st.subheader("Enterprise Sales Strategy")
        render(strategy)

        st.divider()

        st.subheader("Meeting Preparation")

        if meeting:
            st.markdown(meeting)
        else:
            st.info("Meeting preparation unavailable.")

    # =====================================================

    with tabs[4]:

        st.subheader("Customer Follow-up Email")

        if email:
            st.markdown(email)
        else:
            st.info("Email not generated.")

        st.divider()

        st.subheader("Objection Handling")
        render(objections)

    # =====================================================

    with tabs[5]:

        st.subheader("CRM Summary")

        if crm:
            st.markdown(crm)
        else:
            st.info("CRM summary unavailable.")

        st.divider()

        st.subheader("Executive Sales Brief")

        if report:
            st.markdown(report)
        else:
            st.info("Sales brief unavailable.")

        st.success("✅ Ready for Sales Review")