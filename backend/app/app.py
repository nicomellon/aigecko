import os
from flask import Flask, request, jsonify, make_response, send_from_directory
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
        return make_response("no file uploaded", 400) 

    file = request.files["file"]  
    # If the user does not select a file
    if file.filename == "":
        return make_response("no selected file", 400)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return make_response(jsonify(id=filename), 200)
    else:
        return make_response("invalid file name", 400)


# read a previously stored image and return its height and width
@app.route("/analyse_image")
def analyse_image():
    image = request.args.get("image")
    images = os.listdir(app.config["UPLOAD_FOLDER"])     

    if image in images:
        file = Image.open(f'{app.config["UPLOAD_FOLDER"]}/{image}')
        width, height = file.size
        return make_response(jsonify(width=width, height=height))
    else:
        return make_response("Image not found", 404)


# serve images as files
@app.route("/images/<image>")
def get_image(image):
    images = os.listdir(app.config["UPLOAD_FOLDER"])     
    if image in images:
        return send_from_directory(app.config["UPLOAD_FOLDER"], image)
    else:
        return make_response("Image not found", 404)



# list all the images uploaded so far as well as their image ids
@app.route("/list_images")
def list_images():
    images = os.listdir(app.config["UPLOAD_FOLDER"])     
    return make_response(jsonify(images), 200)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")