from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello, World!"

@app.route("/usuarios",  methods=["GET"])
def usuarios():
    return jsonify([
        {"id": 1, "nome": "João"},
        {"id": 2, "nome": "Maria"},
        {"id": 3, "nome": "José"}
    ])



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)