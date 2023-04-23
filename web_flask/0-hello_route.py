#!/usr/bin/python3
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


if __name__ == '__main__':
<<<<<<< HEAD
=======
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def Display_hello():
    return ('“Hello HBNB!”')


if __name__ == "__main__":
>>>>>>> 281576492604814996c27ad30d910d5154662e8c
    app.run(host='0.0.0.0', port=5000)
