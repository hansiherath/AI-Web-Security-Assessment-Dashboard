# 🛡️ AI-Powered Web Security Assessment Dashboard

A cybersecurity assessment platform built with Python and Streamlit that analyzes websites for common security issues, evaluates security posture, and generates AI-powered recommendations.

## 🚀 Live Demo

<p align="center">
  <a href="https://ai-web-security-assessment-dashboard.streamlit.app/">
    🔗 Open AI Web Security Assessment Dashboard
  </a>
</p>

## 📌 Overview

The AI Web Security Assessment Dashboard helps users quickly evaluate the security configuration of a website by performing:

- Security Header Analysis
- SSL Certificate Validation
- Technology Stack Detection
- Open Port Scanning
- Security Score Calculation
- AI-Powered Security Recommendations

The platform provides an easy-to-understand security overview for developers, students, and security enthusiasts.

---

## ✨ Features

### 🔒 Security Header Analysis
Checks important HTTP security headers:

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy

### 📜 SSL Certificate Validation

Displays:

- Certificate Issuer
- Expiry Date
- Remaining Validity Period

### ⚙️ Technology Detection

Identifies technologies used by the target website:

- Web Servers
- CMS Platforms
- Programming Languages
- Frameworks

### 🌐 Open Port Scanning

Scans common ports and identifies exposed services.

### 📊 Security Score

Generates a security score between 0–100 and categorizes risk level:

- Low Risk
- Medium Risk
- High Risk

### 🤖 AI Security Recommendations

Uses Google Gemini AI to:

- Analyze scan results
- Identify risks
- Suggest remediation actions

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### Security Modules

- Requests
- SSL
- Socket Programming
- BuiltWith

### AI

- Google Gemini API

---

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/hansiherath/AI-Web-Security-Assessment-Dashboard.git
```

Move into the project:

```bash
cd AI-Web-Security-Assessment-Dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🔑 Environment Variables

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```


