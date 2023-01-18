#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


<<<<<<< HEAD
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
=======
if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> 193c16293eb429183fd4142bf80c8793f8a903c3
