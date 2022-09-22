from urllib import request
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
# for please select the file for "upload" button
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
  file = FileField("File", validators=[InputRequired()])
  submit = SubmitField("Upload File")

@app.route("/", methods=["GET","POST"])

@app.route("/upload", methods=["GET","POST"])
def upload():
  form = UploadFileForm()
  if form.validate_on_submit():
    file = form.file.data #first grab the file
    file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # then save the file
    return 'File has been uploaded'
  return render_template("upload.html", form=form)

# @app.route("/greet")
# def greet():
#   return render_template("greet.html", name=request.args.get("name","world"))

if __name__ == "__main__":
  app.run(debug=True)