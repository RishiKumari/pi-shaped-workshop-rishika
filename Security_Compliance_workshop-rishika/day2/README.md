# Day 2: OWASP ZAP – Dynamic Application Security Testing (DAST)

## Objective
Demonstrate understanding of **OWASP Top 10 vulnerabilities** using **OWASP ZAP**:

- Perform dynamic application security testing
- Identify common vulnerabilities
- Generate reports automatically

---

## Prerequisites
- Git installed
- Docker installed and running
- Python 3.x installed (for app dependencies)
- VS Code or any editor for code inspection

---


## Folder Structure
```
   Security_Compliance_workshop-rishika/
           └── day2/
               ├── app.py
               ├── requirements.txt
               ├── Dockerfile
               ├── zap.yaml
               ├── zap-report.html
               └── screenshots/
                          ├── zap_scan.png  

   ```
---
## Steps to Run

1. **Clone the repository:**
   ```bash
    git clone https://github.com/RishiKumari/pi-shaped-workshop-rishika.git
    cd Security_Compliance_workshop-rishika/day2

2.  **Run the app container:**
     ```
     docker run -d --name my-app-container -p 5000:5000 my-app
     
3.  **Run OWASP ZAP scan:

      ```
      docker run --rm --network container:my-app-container \
      -v $(pwd)/Security_Compliance_workshop-rishika/day2:/zap/wrk/:rw \
       owasp/zap2docker-stable zap-baseline.py \
        -t http://my-app-container:5000/login \
         -r /zap/wrk/zap-report.html

      ```
4.  Open the generated report:
     ```
        open Security_Compliance_workshop-rishika/day2/zap-report.html
     ```
---
### 6. **GitLab CI/CD Pipeline**
   ```
   ## GitLab Pipeline

   The pipeline automatically:
    - Builds the app Docker image
    - Runs the app container
    - Executes OWASP ZAP scan
    - Saves `zap-report.html` as an artifact
   ```

## Screenshots & Reports
- Include screenshots from the ZAP scan here (optional)
- Link or attach zap-report.html from artifacts

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
