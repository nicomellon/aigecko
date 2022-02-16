import os
from flask import Flask, flash, render_template, request, redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.getcwd() + "/uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# app homepage
@app.route("/")
def index():
    return render_template("index.html")


# get the image provided by the user and store it
@app.route("/upload_image", methods=["POST"])
def upload_image():
    # check if the post request has the file part
    if "file" not in request.files:
        # flash("No file part")
        return 'invalid file'
        # return redirect("/")

    file = request.files['file']
    
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        # flash('No selected file')
        return redirect("/")
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f'valid file going to {UPLOAD_FOLDER}'
        # return redirect("/")

    return 'invalid file'


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