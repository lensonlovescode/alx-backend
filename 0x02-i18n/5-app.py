#!/usr/bin/env python3
"""
Babel instanciation of a flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config():
    """
    A config class to define the languages supported or sum
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = 'en'

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False



def get_locale():
    """
    Get locale function to fetch supported languages
    """
    locale = request.args.get("locale")
    if locale:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)

def get_user():
    """
    gets the user to login as
    """
    uuid = request.args.get('login_as')
    if uuid:
        return users.get(uuid)
    return None

@app.before_request
def before_request():
    """
    Gets the logged user if any
    """
    g.user = get_user()


@app.route('/')
def hello() -> str:
    """
    Renders the hello world template
    """
    if g.user:
        return render_template("5-index.html", username=g.user["name"])

    return render_template("5-index.html")

if __name__ == "__main__":
    app.run(debug=True)
