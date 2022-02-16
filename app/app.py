from flask import Flask, render_template, request

app = Flask(__name__)

images = [
    "1", "2"
]


# app homepage
@app.route("/")
def index():
    return render_template("index.html", images=images)


# get the image provided by the user and store it
@app.route("/upload_image", methods=["POST"])
def upload_image():
    name = request.form["name"]

    if name:
        return f"Hi {name}"
    else:
        return "Hi"


# read a previously stored image and return its height and width
@app.route("/analyse_image")
def analyse_image():
    return '<h1>analyse</h1>'


# list all the images uploaded so far as well as their image ids
@app.route("/list_images")
def list_images():
    return '<h1>list images</h1>'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")