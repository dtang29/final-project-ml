from flask import Flask, render_template, jsonify, redirect, request
from flask_pymongo import PyMongo
from time import gmtime, strftime
import pandas as pd
import json
import sys
from bson import BSON
from bson import json_util

app = Flask(__name__)
mongo = PyMongo(app)


# create route that renders index.html template
@app.route("/", methods=["GET","POST"])
def echo():
    return render_template("index.html")    

@app.route("/plots")
def plots():
    return render_template("plots.html")

if __name__ == "__main__":
    app.run(debug=True)