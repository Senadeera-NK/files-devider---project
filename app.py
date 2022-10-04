from genericpath import isfile
from flask import *
from werkzeug.utils import secure_filename
import os
from os import listdir, path
import logging # to print in console log

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
    path='static/files/'
    #clearing all the existing files for a new session
    for filename in os.listdir(path):
      file = path+filename
      if os.path.isfile(file):
        app.logger.warning('Deleting file: ', file)
        os.remove(file)
  return render_template('upload.html')

@app.route('/upload result', methods=['GET', 'POST'])
def upload_result():
  if request.method == 'POST':
    f = request.files['file']
    if allowed_files(f.filename):
      filename = secure_filename(f.filename)

      # checking if that named file already in the folder
      file_exist = path.exists(filename)
      if  file_exist != True:
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # checking if the file uploaded successfully in folder
        file_uploaded = path.exists(filename)
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
