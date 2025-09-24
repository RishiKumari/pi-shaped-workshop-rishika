# DevSecOps Hands-On: Code Security & Shift-Left Practices (Day 1)


## Assignment Overview
This project demonstrates DevSecOps principles by showcasing how to:
- Build a simple Flask application
- Identify hardcoded secrets using Gitleaks
- Secure the application by removing secrets
- Deploy it inside Docker

---

## Prerequisites
Before starting, ensure you have installed and running these tools:
- Git 
- Docker
- VS Code
  - Python / Node (based on chosen app)
  - Docker
- Gitleaks

---

## Installation
- **Language/Framework**: Python (Flask) or Node.js
- **Containerization**: Docker
- **Secret Scanning**: Gitleaks
- **IDE**: VS Code
- **Version Control**: Git + GitHub

---

## Setup & Run
1. Clone the repository:
   ```bash

   git clone https://github.com/RishiKumari/pi-shaped-workshop-rishika.git

   cd pi-shaped-workshop-rishika/Security_Compliance_workshop-rishika/day1

  2. Build and run the Docker container:
      ```    
      docker build -t flask-app .

      docker run -p 5000:5000 flask-app
  
 3. Open in browser:
   
    ```
    http://localhost:5000     

4. Run Gitleaks scan:
    ```
      docker run --rm -v $(pwd):/path ghcr.io/gitleaks/gitleaks:latest detect --source="/path" -v



 ## Repository Structure
 
      pi-shaped-workshop-rishika/
         └── Security_Compliance_workshop-rishika/
              └── day1/
                  ├── app.py
                  ├── requirements.txt
                  ├── Dockerfile
                  ├── .gitignore
                  ├── README.md
              └── screenshots/
                  ├── gitleaks_before.png
                  ├── gitleaks_after.png
                  ├── browser_before.png
                  └── browser_after.png



---

## Core Concept Questions and their Answers: 

### 1. What is Shift-Left Security and why is it important?
Shift-left security means detecting & fixing vulnerabilities early in the development lifecycle (before production). It reduces cost and prevents major risks.


### 2. How does detecting secrets early prevent vulnerabilities?
It avoids sensitive data leaks into production, preventing breaches and misuse of credentials.


### 3. What strategies can be used instead of hardcoding secrets?

Use environment variables

Secret managers (AWS Secrets Manager, HashiCorp Vault, Azure Key Vault)

.env files (never commit to Git)


### 4. Where can secrets still be exposed?
Secrets can leak in:

Old Git commit history

Logs or error messages

Misconfigured CI/CD pipelines
Prevention: use Git history scanning, secret scanning in CI/CD, and rotation of secrets.

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.