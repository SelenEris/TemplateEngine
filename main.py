from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def text_box():
    text = request.form['text']
    processed_text = text.upper()
    return render_template("Bienvenue.html", message=processed_text)


if __name__ == '__main__':
    app.run()
