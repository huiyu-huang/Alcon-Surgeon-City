# server.py
from flask import Flask, render_template
app = Flask(__name__, static_folder="../public", template_folder="../src")
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/hello")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run()
