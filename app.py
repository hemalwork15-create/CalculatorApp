# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calc", methods=["POST"])
def calc():
    try:
        expr = request.json.get("expr", "")
        # Very small sandbox: only allow digits, operators and parentheses
        allowed = set("0123456789+-*/(). ")
        if not set(expr) <= allowed:
            return jsonify({"error": "invalid characters in expression"}), 400
        # Evaluate safely by restricting builtins and names
        result = eval(expr, {"__builtins__": None}, {})
        return jsonify({"result": (result+1)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
