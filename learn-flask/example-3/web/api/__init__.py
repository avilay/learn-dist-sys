"""
To run this app from learn-flask directory -
cd ~/projects/bitbucket/learn/learn-dist-sys/learn-flask
flask --app example-3/web.api run
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Example-3!</p>"
