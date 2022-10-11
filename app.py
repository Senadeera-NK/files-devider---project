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
  if  files_len != 0:
    dir_path = 'static/files'
    #clearing all the existing files for a new session
    filelist = glob.glob(os.path.join(dir_path, "*"))
    for f in filelist:
      os.remove(f)
  return render_template('upload.html')


@app.route('/upload result', methods=['GET', 'POST'])
def upload_result():
  if request.method == 'POST':
    files = request.files.getlist('files[]')
    for f in files:
      # checking if the file's extension is allowed
      if not allowed_files(f.filename):
        app.logger.error('not a file with an allowed extension')
      else:
        filename = secure_filename(f.filename)

        #getting the path of current folder
        folder_path = os.path.abspath(os.getcwd())
        # checking if that named file already in the folder
        file_exist = os.path.exists(folder_path+'\\static\\files\\'+filename)

        if  file_exist != True:
          f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

          # checking if the file uploaded successfully in folder
          file_uploaded = os.path.exists(folder_path+'\\static\\files\\'+filename)

          if file_uploaded != True:
            message = 'file uploading failed'
          else:
            message = 'file uploaded successfully'
          app.logger.info(message)
        else:
          message = 'file already exists'
          app.logger.error(message)


    # getting the names on the uploaded files as a list
    uploaded_files = os.listdir('static/files/')
    return render_template('upload.html', uploaded_files=uploaded_files)



# deleting selected files form 'files' folder
@app.route('/ProcessSelectedfile/<string:selectedfile>', methods=['POST'])
def delete_file(selectedfile):
  # loads from the js file
  selectedfile = json.loads(selectedfile)
  file_name = selectedfile

  # deleting the file
  os.remove('static/files/'+file_name)
  return('/')


if __name__ == "__main__":
  app.run(debug=True)
