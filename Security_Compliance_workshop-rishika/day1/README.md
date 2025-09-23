# DevSecOps Hands-On: Code Security & Shift-Left Practices (Day 1)

## 👤 Author
Rishika Kumari

---

## 🎯 Objective
Demonstrate understanding of **shift-left security principles** by:
- Scanning code for secrets
- Removing exposed secrets
- Verifying clean codebase
- Deploying a sample application securely in Docker

---

## 📌 Prerequisites
Before starting, ensure you have:
- [Git](https://git-scm.com/downloads) installed
- [Docker](https://docs.docker.com/get-docker/) installed and running
- [VS Code](https://code.visualstudio.com/) with extensions:
  - Python / Node (based on chosen app)
  - Docker
  - Markdown Preview
- [Gitleaks](https://github.com/gitleaks/gitleaks) installed

---

## 🛠 Tools & Setup
- **Language/Framework**: Python (Flask) or Node.js
- **Containerization**: Docker
- **Secret Scanning**: Gitleaks
- **IDE**: VS Code
- **Version Control**: Git + GitHub

---

## 📂 Repository Structure
  pi-shaped-workshop-rishika/
│── README.md # Root-level (contains only my name)
│
└── Security_Compliance_workshop-rishika/
└── day1/
├── app.py / app.js
├── Dockerfile
├── requirements.txt / package.json
├── README.md # This file (Day 1 documentation)
└── .gitignore


---

## 🔽 How to Clone this Repo
```bash
# Clone the repo
git clone https://github.com/<your-username>/pi-shaped-workshop-yourname.git

# Navigate into day1 folder
cd pi-shaped-workshop-yourname/Security_Compliance_workshop-yourname/day1

## 🚀 Process

### 1️⃣ Scan Code for Secrets
- Run the following command to detect secrets:
  ```bash
  gitleaks detect --source .
