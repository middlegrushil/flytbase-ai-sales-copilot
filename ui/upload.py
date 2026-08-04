import os
import streamlit as st


def upload_lead():
    """
    Uploads a lead JSON file and saves it to input/lead.json.
    """

    st.header("📂 Upload Lead")

    uploaded_file = st.file_uploader(
        "Upload Lead JSON",
        type=["json"],
        help="Upload the inbound lead JSON file."
    )

    if uploaded_file is None:
        st.info("Please upload a lead JSON file to begin.")
        return False

    os.makedirs("input", exist_ok=True)

    with open("input/lead.json", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Lead uploaded successfully!")

    st.json(
        {
            "Filename": uploaded_file.name,
            "Size (KB)": round(uploaded_file.size / 1024, 2),
        }
    )

    return True