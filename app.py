from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("start page.html")

if __name__ == "__main__":
  from waitress import serve
  serve(app, host="0.0.0.0", port=8080)

def upload():
  return render_template("uploading.html")
