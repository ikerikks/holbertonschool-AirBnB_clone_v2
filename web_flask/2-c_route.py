#!/usr/bin/python3
""" starts a web app """

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_index():
    """ diplays text """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ diplays text """
    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    """ displays text """
    new_text = ""
    for i in text:
        if i == '_':
            i = ' '
        new_text += i
    return f"C {new_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
