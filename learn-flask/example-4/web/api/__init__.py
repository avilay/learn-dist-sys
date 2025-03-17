"""
To run this example from the learn-flask directory -
cd ~/projects/bitbucket/learn/learn-dist-sys/learn-flask
flask --app example4/web.api run

Then browse to http://127.0.0.1:5000/one or http://127.0.0.1:5000/two
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    from . import app_one, app_two

    app.register_blueprint(app_one.one)
    app.register_blueprint(app_two.two)
    return app
