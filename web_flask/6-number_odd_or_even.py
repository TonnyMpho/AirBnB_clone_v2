#!/usr/bin/python3
""" script that starts a Flask web application:
listening on 0.0.0.0, port 5000 Routes /: display “Hello HBNB!”
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home_hbnb():
    """ home route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb route return HBNB"""
    return "HBNB"


@app.route("/c/<text>",  strict_slashes=False)
def c_route(text):
    """ display “C ” followed by the value of the text variable """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """ display “Python ”, followed by the value of the text variable """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    text = "{} is odd".format(n)

    if n % 2 == 0:
        text = "{} is even".format(n)

    return render_template("6-number_odd_or_even.html", text=text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
