from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# VULN #1: hardcoded secret (intentional)
app.config['SECRET_KEY'] = 'hardcoded_secret_12345'

# VULN #2: reflected input without sanitization (XSS risk)
@app.route("/greet")
def greet():
    name = request.args.get("name", "")
    # intentionally unsafe return for exercise (reflected XSS)
    return f"<h1>Hello {name}</h1>"

@app.route("/")
def home():
    return "Vulnerable Flask app running"

if __name__ == "__main__":
    # debug=True intentionally insecure for the exercise
    app.run(host="0.0.0.0", port=5000, debug=True)
