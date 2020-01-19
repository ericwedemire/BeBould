#!/usr/bin/env python3

import flask as fl
from werkzeug.utils import secure_filename
import findRocks as fr
import os

app = fl.Flask(__name__)
UPLOAD_FOLDER = os.getcwd() + "/uploads"
ALLOWED_EXTENSIONS = {"jpg", ".png", ".bmp"}
SECURITY_KEY = "sdkfgljkszgdfkzrl"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = SECURITY_KEY

@app.route('/', methods=["GET", "POST"])
def upload_file():
    if fl.request.method == "POST":
        # check if the post request has the file part
        if 'file' not in fl.request.files:
            fl.flash('No file part')
            return fl.redirect(fl.request.url)

        file = fl.request.files['file']

        # if user does not select file, browser also submit an empty part
        # without filename
        if file.filename == '':
            try:
                fl.flash('No selected file')
            except:
                print("nothing submitted")
            return fl.redirect(fl.request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return fl.redirect(fl.url_for('uploaded_file', filename=filename))
    return fl.render_template("picUpload.html")


def allowed_file(filename):
    if "." in filename:
        return filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    return False


if __name__ == "__main__":
    app.run(debug=True)