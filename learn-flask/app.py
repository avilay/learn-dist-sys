"""
To run this app from the learn-flask directory -

cd ~/projects/bitbucket/learn/learn-dist-sys/learn-flask/
flask run
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, App!</p>"
