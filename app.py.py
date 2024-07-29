from flask import Flask
app = Flask(__name__)

@app.route("/home")
def hello():
    return "party tiem!"

@app.route("/")
def hello():
    return "Hello, World!"