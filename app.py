from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'AI Niemiecki Asystent działa!'
from flask import render_template

@app.route("/audio")
def audio():
    return render_template("audio.html")
