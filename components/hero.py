import streamlit as st


def show_hero():

    st.markdown(
        """
<div style="
background:linear-gradient(135deg,#081522,#102A43);
padding:42px;
border-radius:24px;
border:1px solid rgba(255,255,255,.08);
margin-bottom:30px;
box-shadow:0 20px 50px rgba(0,0,0,.35);
">

<div style="
display:flex;
justify-content:space-between;
align-items:flex-start;
flex-wrap:wrap;
gap:20px;
">

<div style="max-width:900px;">

<p style="
color:#FF8A3D;
font-size:13px;
font-weight:700;
letter-spacing:2px;
text-transform:uppercase;
margin-bottom:12px;
">

FLYTBASE • ENTERPRISE AI SALES COPILOT

</p>

<h1 style="
font-size:50px;
font-weight:800;
color:white;
margin-bottom:10px;
line-height:1.1;
">

Enterprise Sales Intelligence Platform

</h1>

<p style="
font-size:18px;
color:#C7D5E5;
line-height:1.8;
max-width:900px;
margin-bottom:28px;
">

An explainable multi-agent AI platform that assists FlytBase Solutions Engineers
through the complete enterprise pre-sales workflow—from company research and
opportunity qualification to solution mapping, customer success story matching,
sales strategy generation and executive sales documentation.

</p>

<div style="display:flex;gap:12px;flex-wrap:wrap;">

<div style="
padding:10px 18px;
background:#16314D;
border-radius:999px;
color:white;
font-size:14px;
">

🧠 Explainable AI Decisions

</div>

<div style="
padding:10px 18px;
background:#16314D;
border-radius:999px;
color:white;
font-size:14px;
">

🏢 Company Intelligence

</div>

<div style="
padding:10px 18px;
background:#16314D;
border-radius:999px;
color:white;
font-size:14px;
">

🚁 Solution Engineering

</div>

<div style="
padding:10px 18px;
background:#16314D;
border-radius:999px;
color:white;
font-size:14px;
">

📈 Executive Sales Brief

</div>

</div>

</div>

<div style="
background:#162535;
padding:22px;
border-radius:20px;
min-width:280px;
">

<p style="color:#9FB3C8;font-size:13px;">

Workflow

</p>

<div style="margin-top:12px;color:white;line-height:2;">

✅ Company Intelligence<br>

✅ Opportunity Qualification<br>

✅ Solution Recommendation<br>

✅ Sales Strategy<br>

✅ Similar Customer Match<br>

✅ Executive Sales Brief

</div>

</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )