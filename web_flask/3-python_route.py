#!/usr/bin/python3
<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:

"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Adding a specific route /hbnb"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text=None):
    """Dynamic inputed text: replace _ for space and show text"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is_cool'):
    """Dynamic inputed text: replace _ for space and show text"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    return ("Hello HBNB")

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def dsiplay_text(text):
    return ("C is %s" % text)

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_text_default(text="is cool"):
    return ('Python %s' % text.replace('_', ' '))


if __name__  == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> 20222ba05ffb64fd4dc0d5bf49800b20d555745d
