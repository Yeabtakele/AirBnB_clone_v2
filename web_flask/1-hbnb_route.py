#!/usr/bin/python3
"""a script that print two things"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """ print “Hello HBNB!”"""

    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ print in route hbnb"""

    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
