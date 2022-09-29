from flask import *
from werkzeug.utils import secure_filename
import os

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
  return render_template('upload.html')

@app.route('/', methods=['GET', 'POST'])
def upload_result():
  if request.method == 'POST':
    f = request.files['file']
    if allowed_files(f.filename):
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      result = 'files uploaded successfully !!!'
    else:
      result = 'files failed to upload'

      # -- continue.......
  return render_template('/', result=result)


if __name__ == "__main__":
  app.run(debug=True)
