from flask import Blueprint

one = Blueprint("app_one", __name__, url_prefix="/one")


@one.route("/")
def hello_world():
    return "<p>This is App ONE!</p>"
