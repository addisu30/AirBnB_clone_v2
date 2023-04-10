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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> 20222ba05ffb64fd4dc0d5bf49800b20d555745d
