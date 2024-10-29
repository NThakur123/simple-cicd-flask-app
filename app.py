# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is a CI/CD pipeline demo."

app.run(host="0.0.0.0", port=5000)
