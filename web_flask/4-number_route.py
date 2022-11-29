#!/usr/bin/python3
""" starts a web app with multiples scripts """

from flask import Flask, url_for
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_index():
    """ diplays text on a define route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ diplays text on a define route """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ displays text on a define route """
    return "C " + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """ displays text on a define route """
    print(text)
    return "Python " + text.replace("_", " ")


@app.route("/python/", strict_slashes=False)
def python(text="is cool"):
    """ displays text """
    print(text)
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """ displays a text with number on a define route """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
