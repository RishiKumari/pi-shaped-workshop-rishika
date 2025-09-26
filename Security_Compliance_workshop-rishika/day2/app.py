from flask import Flask, request

app = Flask(__name__)

# Vulnerable endpoint (SQL Injection + XSS demo)
@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.args.get("username", "")
    password = request.args.get("password", "")
    return f"<h1>Login attempted by {username} with password {password}</h1>"

@app.route("/")
def index():
    return "<h2>Welcome to Vulnerable Flask App - Day 2</h2>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
