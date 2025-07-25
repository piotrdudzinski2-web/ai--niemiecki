from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'AI Niemiecki Asystent działa!'
