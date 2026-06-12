from scanner import ai_report
import streamlit as st  # type: ignore[import]

from scanner.headers import check_headers
from scanner.ssl_checker import check_ssl
from scanner.technology import detect_technology
from scanner.port_scan import scan_ports
from scanner.security_score import calculate_score
from scanner.ai_report import generate_recommendations

st.set_page_config(
    page_title="AI Web Security Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Web Security Assessment Dashboard")

url = st.text_input(
    "Enter Website URL",
    "https://google.com"
)

if st.button("Scan"):

    host = (
        url.replace("https://", "")
           .replace("http://", "")
           .split("/")[0]
    )

    # ==========================
    # SECURITY SCORE
    # ==========================

    headers = check_headers(url)
    st.session_state["headers"] = headers

    score = calculate_score(headers)

    if score >= 90:
        risk_level = "Low"

    elif score >= 70:
        risk_level = "Medium"

    else:
        risk_level = "High"

    st.subheader("📊 Security Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Security Score",
            f"{score}/100"
        )

    with col2:
        st.metric(
            "Risk Level",
            risk_level
        )

    if risk_level == "Low":
        st.success("🟢 Low Risk Website")

    elif risk_level == "Medium":
        st.warning("🟡 Medium Risk Website")

    else:
        st.error("🔴 High Risk Website")

    st.divider()

    # ==========================
    # SECURITY HEADERS
    # ==========================

    st.subheader("🔒 Security Headers")

    for header, info in headers.items():

        if info["status"] == "Present":

            st.success(
                f"{header} : Present"
            )

        else:

            st.error(
                f"{header} : Missing ({info['severity']} Risk)"
            )

    st.divider()

    # ==========================
    # SSL CERTIFICATE
    # ==========================

    st.subheader("📜 SSL Certificate")

    ssl_info = check_ssl(host)
    st.session_state["ssl_info"] = ssl_info

    if "Error" in ssl_info:

        st.error(
            ssl_info["Error"]
        )

    else:

        st.write(
            f"**Expiry Date:** {ssl_info['Expiry Date']}"
        )

        st.write(
            f"**Days Remaining:** {ssl_info['Days Remaining']}"
        )

        st.write(
            f"**Issuer:** {ssl_info['Issuer']}"
        )

    st.divider()

    # ==========================
    # TECHNOLOGY STACK
    # ==========================

    st.subheader("⚙️ Technology Stack")

    with st.spinner("Detecting technologies..."):
        technologies = detect_technology(url)

    st.session_state["technologies"] = technologies

    if "Error" in technologies:

        st.error(
            technologies["Error"][0]
        )

    else:

        for category, values in technologies.items():

            st.markdown(
                f"### {category.replace('-', ' ').title()}"
            )

            for value in values:

                st.success(value)

    st.divider()

    # ==========================
    # PORT SCANNER
    # ==========================

    st.subheader("🌐 Open Ports")

    with st.spinner("Scanning ports..."):
        ports = scan_ports(host)

    st.session_state["ports"] = ports

    if len(ports) == 0:

        st.warning(
            "No common open ports detected."
        )

    else:

        for port in ports:

            st.success(
                f"Port {port['port']} ({port['service']}) is Open"
            )

    st.session_state["scan_completed"] = True


st.divider()

if st.session_state.get("scan_completed"):

    if st.button("🤖  Generate Recommendations"):

        with st.spinner(
            "Generating Recommendations..."
        ):

            ai_report = generate_recommendations(
                st.session_state["headers"],
                st.session_state["ssl_info"],
                st.session_state["technologies"],
                st.session_state["ports"]
            )

            st.session_state["ai_report"] = ai_report

if "ai_report" in st.session_state:

    st.subheader(
        "🤖 AI Security Recommendations"
    )

    st.markdown(
        st.session_state["ai_report"]
    )