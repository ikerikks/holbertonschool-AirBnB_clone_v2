#!/usr/bin/python3
""" starts a web app """

from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_index():
    """ diplays text """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ diplays text """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ displays text """
    return "C " + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """ displays text """
    print(text)
    return "Python " + text.replace("_", " ")


@app.route("/python/", strict_slashes=False)
def python(text="is cool"):
    """ displays text """
    print(text)
    return "Python " + text.replace("_", " ")


@app.route("/number/<n>", strict_slashes=False)
def is_number(n):
    """ displays a text with number """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
