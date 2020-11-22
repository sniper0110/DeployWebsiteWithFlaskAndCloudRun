from flask import Flask, request, redirect, render_template
from werkzeug.utils import  secure_filename
import os

app = Flask(__name__, static_url_path='/static')


@app.route("/", methods=["GET"])
def index() :
    return render_template("index.html")


@app.route("/generic", methods=["GET"])
def generic() :
    return render_template("generic.html")


@app.route("/elements", methods=["GET"])
def elements() :
    return render_template("elements.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))