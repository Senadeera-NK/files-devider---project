from urllib import request
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField

app = Flask(__name__)

@app.route("/")
#default page's respond
def index():
  return render_template("index.html")

@app.route("/upload")
def upload():

  return render_template("uploading.html")

# @app.route("/greet")
# def greet():
#   return render_template("greet.html", name=request.args.get("name","world"))

if __name__ == "__main__":
  app.run(debug=True)