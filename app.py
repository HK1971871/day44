from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify({"msg": "Hello Flask CI/CD!"})

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})

if __name__ == "__main__":
    # Chạy dev server khi phát triển; production sẽ dùng Gunicorn trong Docker
    app.run(host="0.0.0.0", port=5000, debug=True)