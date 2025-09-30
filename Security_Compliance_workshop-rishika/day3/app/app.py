from flask import Flask, request, jsonify
import os
from vulnerable_module import insecure_eval


app = Flask(__name__)
# Intentionally hardcoded secret (vulnerable) - will fix later
app.config['SECRET_KEY'] = 'SUPER_SECRET_KEY_SHOULD_NOT_BE_IN_CODE'


@app.route('/')
def index():return "Hello from vulnerable Flask app!"


@app.route('/compute', methods=['POST'])
def compute():
# insecure usage: evaluating user input (vulnerability)
 data = request.get_json() or {}
 expr = data.get('expr', '2+2')
 result = insecure_eval(expr)
 return jsonify({'expr': expr, 'result': result})


if __name__ == '__main__':
# Use 0.0.0.0 so CI docker containers can reach it
 app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))