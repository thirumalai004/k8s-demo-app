import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return f"{os.getenv('GREETING', 'Hello')} from version 2\n"

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)