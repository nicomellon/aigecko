from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload_image")
def upload_image():
    return '<h1>upload</h1>'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")