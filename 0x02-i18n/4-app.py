#!/usr/bin/env python3
"""
Babel instanciation of a flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """
    A config class to define the languages supported or sum
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False


def get_locale():
    """
    Get locale function to fetch supported languages
    """
    locale = request.args.get('locale')

    if locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def hello() -> str:
    """
    Renders the hello world template
    """
    return render_template("4-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
