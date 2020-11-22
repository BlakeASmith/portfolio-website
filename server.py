from flask import Flask, \
        send_from_directory, \
        redirect, \
        url_for, \
        render_template

from pathlib import Path

app = Flask(__name__)


@app.route("/index.html")
@app.route("/")
def index():
    return render_template("index.html", title="fucka you")


@app.route("/<path:path>")
def send_file(path):
    return send_from_directory("static", path)


if __name__ == "__main__":
    app.run()
