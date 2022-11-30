#!/usr/bin/python3
""" starts a web app with flask framework"""

from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_index():
    """ diplays text on a define route
    Args:
        none
    Returns:
        text
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ diplays text on a define route
    Args:
        none
    Returns:
        text
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ displays text on a define route
    Args:
        text: string
    Returns:
        text
    """
    return "C " + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """ displays text on a define route """
    print(text)
    return "Python " + text.replace("_", " ")


@app.route("/python/", strict_slashes=False)
def python(text="is cool"):
    """ displays text on a define route
    Args:
        text: string
    Returns:
        text
    """
    print(text)
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """ displays text on a define route
    Args:
        n: integer
    Returns:
        text
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def is_number_template(n):
    """ displays an html page on a define route
    Args:
        n: integer
    Returns:
        html template
    """
    return render_template("5-number.html")


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ displays an html page on a define route
    Args:
        n: integer
    Returns:
        html template
    """
    return render_template("6-number_odd_or_even.html", num=n) 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
