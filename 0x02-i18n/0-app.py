#!/usr/bin/env python3
"""
Flask Babel Simple Recall of how a flask app works
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"], strict_slashes=False)
def hello() -> str:
    """
    Simple flask recall of how a flask app runs
    """
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
