from genericpath import isfile
from flask import *
from werkzeug.utils import secure_filename
import os
from os import listdir, path
import logging # to print in console log
import glob

UPLOAD_FOLDER = 'static/files'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'docs', 'docx']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

def allowed_files(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload():
  uploaded_files = os.listdir('static/files/')
  # checking if the uploaded files' folder is empty
  files_len = len(uploaded_files)
  # if not empty
  if not files_len:
    files = glob.glob('/static/files/*')
    #clearing all the existing files for a new session
    for f in files:
      os.remove(f)
  return render_template('upload.html')

@app.route('/upload result', methods=['GET', 'POST'])
def upload_result():
  if request.method == 'POST':
    f = request.files['file']
    if allowed_files(f.filename):
      filename = secure_filename(f.filename)

      # checking if that named file already in the folder
      file_exist = path.exists(filename)
      logging.info(file_exist)
      if  file_exist != True:
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # checking if the file uploaded successfully in folder
        file_uploaded = os.path.isfile(f.filename)
        app.logger.warning(file_uploaded)
        if file_uploaded != True:
          message = 'file uploading failed'
          app.logger.error(message)
        else:
          message = 'file uploaded successfully'
          app.logger.info(message)
      else:
        message = 'file already exists'
        app.logger.error(message)

    # getting the names on the uploaded files as a list
    uploaded_files = os.listdir('static/files/')
    return render_template('upload.html', uploaded_files=uploaded_files)


if __name__ == "__main__":
  app.run(debug=True)
