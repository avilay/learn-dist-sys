"""
To run this app from learn-flask directory -

cd ~/projects/bitbucket/learn/learn-dist-sys/learn-flask
flask --app example-2/web.api.hello run
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Example-2!</p>"
