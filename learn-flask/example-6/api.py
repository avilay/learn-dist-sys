"""
Demos how flask picks up .env and .flaskenv provided python-dotenv package is
installed. These files need to be in the same directory as the one from which
flask is invoked. Specifying a current working directory will not work.

This will not work because the dot files are not in learn-flask.
cd ~/projects/bitbucket/learn/learn-dist-sys/learn-flask
flask --app example-6/api run

I need to change into example-6 directory.
cd ~/projects/bitbucket/learn/learn-dist-sys/learn-flask/example-6
flask --app api run
"""

import os
from flask import Flask

app = Flask(__name__)
secret_key = os.environ["SECRET_KEY"]
access_key = os.environ["ACCESS_KEY"]

print(f"Access key is {access_key} and secret key is {secret_key}")


@app.route("/")
def hello_world():
    return "<p>Hello, Env Files!</p>"
