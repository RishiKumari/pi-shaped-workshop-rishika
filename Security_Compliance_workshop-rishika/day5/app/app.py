from flask import Flask

app = Flask(__name__)

# Demo vulnerability: Hardcoded secret
API_KEY = "SUPERSECRET123"  # Bandit & Gitleaks should detect this

@app.route("/")
def home():
    return "Hello, Day 5 Demo!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
