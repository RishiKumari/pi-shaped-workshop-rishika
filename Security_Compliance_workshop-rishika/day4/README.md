# Day 4 — CI/CD-Based DevSecOps Pipeline (Flask)

## Objective
Design a **CI/CD pipeline** that automatically scans a Flask application for:

- Insecure code practices  
- Vulnerable dependencies  
- Runtime vulnerabilities  

**Tools integrated:** Bandit, Semgrep, Trivy, OWASP ZAP  

Pipeline runs via **GitHub Actions** and saves all scan reports as artifacts.  

---

## Prerequisites

- Python 3.12+
- pip
- Docker
- Git
- Bandit (`pip install bandit`)
- Semgrep (`pip install semgrep`)
- Trivy (installed via Docker or native)
- OWASP ZAP (Docker image)


---

## Project Structure
  ```
 pi-shaped-workshop-rishika/
│
├── .github/
│   └── workflows/
│       └── devsecops-day4.yml   ← your Day 4 GitHub Actions file
│
├── Security_Compliance_workshop-rishika/
│   ├── day1/
│   ├── day2/
│   ├── day3/
│   ├── day4/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   ├── .env
│   │   └── README.md
│   └── day5/
│
├── Dockerfile
├── .gitlab-ci.yml
└── README.md

  ```
  
## Vulnerabilities introduced (minimum 2)
1. **Hardcoded secret in app.py**  
   - Impact: Secrets exposed in code can be leaked from repo and abused.  
   - Fix: read secret from `APP_SECRET` env var; rotate any exposed secrets.

2. **Outdated base image (python:3.8-slim-buster)**  
   - Impact: OS packages in that image may have known CVEs (RCE, privilege escalation).  
   - Fix: update to a newer base image (e.g., `python:3.12-slim`) and re-scan; patch/upgrade packages.

---
## Core concept answers (paste as-is)
**Q1: Why run Trivy scans in CI instead of only after deployment?**  
A: Running Trivy in CI detects OS and package CVEs before images are pushed or deployed, preventing vulnerable artifacts from reaching production and enabling earlier, cheaper remediation.

**Q2: Why run security scans (SAST, dependency scanning, DAST) in CI and not only in production?**  
A: Shift-left security: CI scanning gives developers immediate feedback, enforces policy before deployment, reduces remediation cost and time, and prevents production incidents.

**Q3: How do Bandit, Semgrep, Trivy, and OWASP ZAP complement each other? One unique detection each:**  
- **Bandit**: Python-focused static checks (e.g., hardcoded secrets, use of `eval`) — *Bandit detects hardcoded secrets that DAST can't.*  
- **Semgrep**: Custom pattern rules and policy enforcement (e.g., unsafe regex or business-specific checks) — *Semgrep can detect custom policy violations.*  
- **Trivy**: Image and dependency CVEs (OS packages, Python libs) — *Trivy finds CVEs in the Docker base image that static code scanners won't find.*  
- **OWASP ZAP**: Runtime vulnerabilities (reflected XSS, missing security headers) — *ZAP discovers runtime issues like reflected XSS which static analyzers miss.*

**Q4: If Trivy reports HIGH severity in a base image or Bandit flags hardcoded secrets, what should a developer do?**  
A: For Trivy HIGH: update the base image or package to a patched version, rebuild, retest, and redeploy; if immediate upgrade isn't possible, add compensating controls and schedule urgent patching. For Bandit secrets: remove the secret from code, rotate the secret (revoke and replace if necessary), store secrets in a secret manager (GitHub Secrets / Vault), and add checks to prevent re-commit.

---

## Artifacts & Screenshots
Attach or link the artifacts downloaded from the GitHub Actions run:
- `bandit-report.html`
- `semgrep.sarif`
- `trivy-report.json`
- `zap-report.html`



