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
    key = request.args.get('key')
    value = request.args.get('value')
    query = {
        "key" : key,
        "value" : value
    }
    return render_template("index.html", query=query)
    

@app.route("/api/testing")
def testing():
    return "hello"

@app.route("/api/mongodb")
def mongodb():
    path = "Resources/test.json"

    #Create a new mongodb database with collection named "test"
    test = mongo.db.test

    #Read in the json file and write it into the mongo db
    with open(path, 'r') as dataset1_file:
        data = json.load(dataset1_file)
        for x in data:
            test.insert(x)

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)