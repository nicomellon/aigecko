import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PIL import Image

UPLOAD_FOLDER = os.getcwd() + "/uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# get the image provided by the user and store it
@app.route("/upload_image", methods=["POST"])
def upload_image():
    # check if the post request has the file part
    if "file" not in request.files:
        return "invalid file", 400 

    file = request.files['file']
    
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return "no selected file", 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify(uid=0)

    return 'invalid file'


# read a previously stored image and return its height and width
@app.route("/analyse_image")
def analyse_image():
    image = request.args.get("image")
    images = os.listdir(UPLOAD_FOLDER)     

    if image in images:
        file = Image.open(f"{UPLOAD_FOLDER}/{image}")
        width, height = file.size
        return send_from_directory(app.config['UPLOAD_FOLDER'], image, width=width, height=height)
    else:
        return 'Image not found', 404



# list all the images uploaded so far as well as their image ids
@app.route("/list_images")
def list_images():
    images = os.listdir(UPLOAD_FOLDER)     
    return jsonify(images)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")