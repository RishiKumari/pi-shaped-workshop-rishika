from flask import Flask
import os

app = Flask(__name__)

# API_KEY = "HARDCODED_SECRET_KEY"

API_KEY = os.getenv("API_KEY")


@app.route("/")
def home():
    return f"Hello, Rishika! Your API_KEY for DevSecOps is {API_KEY}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
