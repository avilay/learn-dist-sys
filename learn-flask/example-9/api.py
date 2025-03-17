"""
Demo for a REST API. To run
cd ~/projects/bitbucket/learn/learn-dist-sys/learn-flask/
flask --app example-9/api run

And then make a GET request to http://127.0.0.1:5000/me. This will result in a
JSON object with the Content-Type header set to the correct value of
applicaiton/json.
"""

from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.get("/me")
def me():
    return {
        "username": "quantum_random",
        "last_active_at": datetime.now().isoformat(),
        "num_posts": 10,
        "is_admin": False,
    }
