from flask import *
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static/files'
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'docs', 'docx']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

@app.route('/')
def upload():
  return render_template('upload.html')

@app.route('/upload result', methods=['GET', 'POST'])
def upload_result():
  if request.method == 'POST':
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    result = 'files uploaded successfully !!!'
    return render_template('upload result.html', result=result)
  result = "files failed to upload"
  return render_template('upload result.html', result=result)


if __name__ == "__main__":
  app.run(debug=True)