#!/usr/bin/python3
"""starts a web app"""

from flask import Flask
from os import getenv
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"

if __name__ == "__main__":
    port = int(getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
