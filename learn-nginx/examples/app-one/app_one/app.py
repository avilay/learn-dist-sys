from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    headers = ""
    for header, value in request.headers:
        headers += f"<p>{header}: {value}</p>"

    html = f"""
<!DOCTYPE html>
<html>
    <body>
        <h1 style='color:blue'>App One</h1>
        {headers}
    </body>
</html>
"""
    return html
