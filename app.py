from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
#default page's respond
def index():
  return render_template("index.html")

@app.route("/greet")
def greet():
  return render_template("greet.html", name=request.args.get("name","world"))
