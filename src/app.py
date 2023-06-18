
from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

#Home Page Route
@app.route("/")
def front():
    return render_template("front.html")

#Route to project page

@app.route("/enterfile")
def enterfile():
    return render_template("project.html")

@app.route("fileProcess", methods = ['POST', 'GET'])
def fileProcess():
    if request.method == 'POST':
        try:
            

app.run()




