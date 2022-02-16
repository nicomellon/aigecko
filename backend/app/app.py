import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.getcwd() + "/uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
images = ["Image A", "Image B"]

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
        return 'invalid file'

    file = request.files['file']
    
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return 'no selected file'
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # save file to uploads directory
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # add to images dictionary
        images[0] = filename

        return jsonify(uid=0)

    return 'invalid file'


# read a previously stored image and return its height and width
@app.route("/analyse_image")
def analyse_image():
    return '<h1>analyse</h1>'


# list all the images uploaded so far as well as their image ids
@app.route("/list_images")
def list_images():        
    return jsonify(images)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")