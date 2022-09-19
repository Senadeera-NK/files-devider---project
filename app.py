from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["POST"])
def upload():
  return render_template("start page.html")
