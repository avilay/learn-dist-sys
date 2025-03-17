"""
Demos how to use different config files.

cd ~/projects/bitbucket/learn/learn-dist-sys/learn-flask/example-8
export EXAMPLE8_CONFIG='dev.cfg'
flask --app flask_app run
"""

import logging
from flask import Flask

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, instance_relative_config=True)
app.config.from_envvar("EXAMPLE8_CONFIG")


@app.route("/")
def hello_world():
    app.logger.info(f"Running as {app.config['ENV']} environment.")
    app.logger.info(f"The database can be reached at {app.config['DATABASE_URI']}.")
    return "<p>Hello, Example-8!</p>"
