# Day 3 - Secure Coding & Code Scanning

## Objectives

- Practice secure coding workflows using CI/CD.
- Build a GitLab pipeline integrating Bandit, Semgrep, Gitleaks, and OWASP ZAP.
- Detect insecure coding practices, hardcoded secrets, and runtime vulnerabilities.
- Learn to fix vulnerabilities and validate improvements through pipeline re-runs.
- Document findings and answer key security concept questions.

## Prerequisites

- GitLab account with CI/CD runners configured (docker or shell).
- GitHub account to host the repository.
- Basic knowledge of Python (Flask), Docker, and Git.
- Tools installed locally for validation (optional but recommended):
- Python 3.10+
- pip / virtualenv
- Bandit, Semgrep, Gitleaks
- Docker (for running OWASP ZAP)

## Folder Structure
```
pi-shaped-workshop-rishika/
├─ README.md <-- root README with you   r name
├─ Security_Compliance_workshop-rishika/
│ ├─ day3/
│ │ ├─ app/
│ │ │ ├─ app.py
│ │ │ ├─ vulnerable_module.py
│ │ │ └─ requirements.txt
│ │ ├─ .semgrep.yml
│ │ ├─ gitleaks.toml
│ │ └─ .gitlab-ci.yml
│ └─ artifacts-example/ <-- place to collect pipeline artifacts (optional)
│ ├─ bandit-report.html
│ ├─ semgrep-report.json
│ ├─ gitleaks-report.json
│ └─ zap-report.html
└─ .gitignore
```

### Pipeline Setup & Execution
   - Implemented pipeline using GitHub Actions (alternative to GitLab CI).
   - The workflow runs automatically on each push/PR and generates security scan reports.
    - #### Tools integrated:
   - Bandit → Python code security analysis.
   - Semgrep → Detect insecure coding patterns.
   - Gitleaks → Identify hardcoded secrets.
   - OWASP ZAP → Runtime web app vulnerability scan.

  
### Pipeline Screenshot
- Security_Compliance_workshop-rishika/day3/screenshot/pipeline.png

## Artifacts Generated
- Security_Compliance_workshop-rishika/day3/screenshot/bandit-report.html
- Security_Compliance_workshop-rishika/day3/screenshot/semgrep-report.json
- Security_Compliance_workshop-rishika/day3/screenshot/gitleaks-report.json
- Security_Compliance_workshop-rishika/day3/screenshot/zap-report.html (generated via GitHub Actions).
- Security_Compliance_workshop-rishika/day3/screenshot/zap-report.json (generated via GitHub Actions).


> The ZAP report files are generated automatically via GitHub Actions and can be downloaded from the workflow artifacts.


## Core concept answers


### 1) Difference between SAST, DAST, and secrets scanning
- **SAST (Static Application Security Testing):** Scans source code or binaries for coding patterns and vulnerabilities before running the application. Good at finding insecure code (e.g., eval, SQLi patterns). It runs early in CI.
- **DAST (Dynamic Application Security Testing):** Scans a running application (black-box) to find runtime issues like XSS, authentication flaws, server misconfigurations. It tests application behavior and endpoints.
- **Secrets scanning:** Focuses on detecting credentials, API keys, tokens, and other secrets leaked in code or history (e.g., git commits). Tools like Gitleaks scan repositories to prevent accidental leaks.

All three together provide layered protection: SAST finds insecure code patterns, secrets scanning prevents credential leaks, and DAST finds runtime flaws that static analysis cannot.


### 2) Why storing secrets in code is dangerous? Secure alternative
Secrets in code can be accidentally committed and exposed in public repos or leaked via backups. They are often long-lived and reused across environments.
**Secure alternatives:** Use environment variables, secrets managers (AWS Secrets Manager, HashiCorp Vault), or CI/CD secret stores. Ensure rotation and restricted access.


### 3) How adding these scans helps Shift-Left Security
Integrating scans into CI/CD moves detection earlier in the development lifecycle, so developers catch and fix issues before code reaches production — reducing cost and risk.


### 4) If a scan fails in the pipeline — next steps
- Inspect the report artifact (Bandit/semgrep/gitleaks/ZAP).
- Reproduce locally and triage severity.
- Create a fix (code change, config update, rotate secret) and open a PR with remediation.
- Re-run pipeline to verify the fix and update artifacts.

## Findings (example)
- **Vulnerability 1:** Use of `eval()` (SAST/semgrep)
- Impact: Remote code execution if untrusted input reaches eval.
- Fix: Replace with `ast.literal_eval` or proper parser/validation.
- **Vulnerability 2:** Hardcoded secret in `app.py` (gitleaks)
- Impact: Credential exposure, unauthorized access if leaked.
- Fix: Move secret to environment variable and rotate the exposed value.
