Day 5: Compliance Frameworks CI/CD Pipeline

## 1. Objective
Design and run a CI/CD pipeline that automatically scans a sample Python Flask application and its infrastructure for:  
- Insecure code practices  
- Vulnerable dependencies  
- Misconfigured infrastructure (Terraform)  
- Container/runtime vulnerabilities  
- Leaked secrets or sensitive data  

Tools integrated:  
- Bandit – Python code analysis (SAST)  
- Semgrep – pattern-based SAST scanning  
- Trivy – dependency & container image scanning  
- Checkov – Infrastructure-as-Code scanning  
- Gitleaks – secret detection  
- OWASP ZAP – DAST / runtime scanning  

---

## 2. Repository Structure

Security_Compliance_workshop-yourname/
│
├── day5/
│ ├── app/
│ │ ├── app.py
│ │ └── requirements.txt
│ ├── infrastructure/
│ │ ├── main.tf
│ │ └── variables.tf # Empty
│ └── Dockerfile
└── README.md


---

## 3. Demo Vulnerabilities Introduced

| Type | File | Description |
|------|------|-------------|
| Hardcoded secret | app/app.py | API_KEY hardcoded (`"SUPERSECRET123"`) |
| Vulnerable dependency | app/requirements.txt | `requests==2.25.0` |
| Publicly accessible resource | infrastructure/main.tf | S3 bucket with `acl = "public-read"` |
| Exposed Flask app | app/app.py | Default port `5000` for ZAP scan |

---

## 4. CI/CD Pipeline Setup (GitHub Actions)

- Workflow file: `.github/workflows/day5-devsecops.yml`  
- Pipeline stages:

| Stage | Tool / Purpose | Artifact |
|-------|----------------|----------|
| Install dependencies | Python pip install | - |
| SAST – Python code | Bandit | `bandit-report.html` |
| SAST – Patterns | Semgrep | `semgrep-report.json` |
| Dependency Scan | Trivy (Python) | `trivy-deps-report.json` |
| IaC Security | Checkov | `checkov-report.json` |
| Docker Image Scan | Trivy | `trivy-docker-report.json` |
| Secrets / PII | Gitleaks | `gitleaks-report.json` |
| DAST | OWASP ZAP | `zap-report.html` |

- All reports are saved in `day5/reports/` and uploaded as **artifacts** in GitHub Actions.

---

## 5. Pipeline Execution

1. Commit & push code to GitHub.
2. Workflow runs automatically.
3. Artifacts can be downloaded from the **Actions → day5-devsecops → Artifacts** section.

---

## 6. Scan Results (Example)

- **Bandit:** Detected hardcoded API key in `app.py`.  
- **Semgrep:** Identified insecure Flask usage patterns.  
- **Trivy (Python):** Flagged `requests==2.25.0` as vulnerable.  
- **Checkov:** S3 bucket public-read flagged.  
- **Gitleaks:** Hardcoded API key detected.  
- **Trivy (Docker):** Vulnerable packages in image.  
- **ZAP:** Exposed Flask endpoint detected potential issues.  


---

## Core Concept Questions

### 1️ How does each tool contribute to security & compliance?

| Tool      | Purpose / Contribution |
|-----------|-----------------------|
| **Bandit** | Static Application Security Testing (SAST) for Python code. Detects insecure coding practices, hardcoded secrets, and potential vulnerabilities in source code. |
| **Semgrep** | Pattern-based SAST scanning. Detects insecure coding patterns, anti-patterns, and custom security rules in code. |
| **Trivy (Python / Docker)** | Scans dependencies and container images for known vulnerabilities (CVEs), misconfigurations, and outdated packages. Ensures software and images comply with security standards. |
| **Checkov** | Infrastructure-as-Code (IaC) scanning. Detects insecure configurations in Terraform, CloudFormation, Kubernetes manifests, etc. Helps map findings to compliance frameworks like CIS, NIST, and GDPR. |
| **Gitleaks** | Secret detection. Finds hardcoded credentials, API keys, tokens, and other sensitive data in code repositories. |
| **OWASP ZAP** | Dynamic Application Security Testing (DAST). Scans running web applications for runtime vulnerabilities such as XSS, SQL injection, or exposed endpoints. |

---

### 2️Pick one critical vulnerability

**Vulnerability:** Hardcoded secret in `app.py`  
- **Exploitation:** An attacker can access the API key to call services or access sensitive resources.  
- **Business Impact:** Unauthorized access to systems, potential data breach, regulatory non-compliance.  
- **Remediation:** Move the secret to an environment variable or use a secure secret management system (e.g., AWS Secrets Manager, HashiCorp Vault).  

Example fix in code:
```python
import os
API_KEY = os.getenv("API_KEY")
```

### 3  How would you prioritize fixes when multiple issues are reported?

Severity – Critical/high-risk issues first (e.g., secrets leakage, public infrastructure).
Compliance Impact – Fix vulnerabilities that violate frameworks or regulations (GDPR, NIST, CIS).
Ease of Remediation – Quick wins or low-effort fixes next.
Low-Risk / Low Impact – Less urgent vulnerabilities can be addressed later.
Example: First fix hardcoded secrets → then insecure public S3 bucket → then outdated dependencies.

### 4 How do Checkov findings map to frameworks like CIS AWS / NIST / GDPR?

Example: Public S3 bucket (acl = "public-read")
CIS AWS Benchmark: 2.1 Ensure S3 buckets are not publicly accessible
NIST SP 800-53: SC-7 (Boundary Protection), AC-3 (Access Enforcement)
GDPR: Article 32 – ensures data is secure and access is controlled
Checkov flags the misconfiguration and provides references to relevant compliance frameworks.

### 5 Why are both ZAP (runtime) and Trivy (image scan) needed?
Tool	Purpose	Gap Covered
Trivy (Image Scan)	Scans container images before deployment for vulnerabilities in OS packages, Python dependencies, or Docker misconfigurations	Prevents vulnerable images from entering production (pre-deployment)
ZAP (Runtime Scan)	Scans live web application for runtime vulnerabilities such as XSS, SQL injection, exposed endpoints	Detects issues introduced during runtime, configuration errors, or unexpected exposure

Summary: Trivy secures the image itself, ZAP secures the running application. Both together provide end-to-end security coverage.

---