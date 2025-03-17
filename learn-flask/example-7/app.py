"""
Demos how to use flask logger and also customize it. Run it from this directory

cd ~/projects/bitbucket/learn/learn-dist-sys/learn-flask/example-7
flask run
"""

import logging
from flask import Flask

logformat = "[%(asctime)s] [%(name)s:%(levelname)s] [pid %(process)s] %(message)s"
logging.basicConfig(
    format=logformat,
    level=logging.DEBUG,
)


app = Flask(__name__)


@app.route("/")
def hello_world():
    app.logger.error("This is an error log!")
    app.logger.warn("This is a warning log.")
    app.logger.info("This is an info log.")
    app.logger.info("This is a debug log.")
    return "<p>Hello, Example-7!</p>"
