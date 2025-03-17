from flask import Blueprint

two = Blueprint("app_two", __name__, url_prefix="/two")


@two.route("/")
def hello_world():
    return "<p>This is App TWO!</p>"
