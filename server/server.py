from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

@app.route("/contacts")
def contacts():
    return "Mes contacts"

app.run(port=3000, debug=True)