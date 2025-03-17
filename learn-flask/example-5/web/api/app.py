"""
This is a non-demo, i.e., it does not work. It is there to show that flask will
not automatically pick up web.api.app module, even though it is named app. That
only works for a stand-alone python file.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Example-5!</p>"
