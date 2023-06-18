from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

from flask_sqlalchemy import SQLAlchemy
#from datetime 
#configues the key needed to acess fileField and also sends files to "files folder"
app = Flask(__name__)
app.config['SECRET_KEY'] = "secretKey"
app.config['UPLOAD_FOLDER'] = "static/files"
#database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///your_database.db"
db = SQLAlchemy(app)

#File handling
class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route("/", methods=["GET", "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        # fileNames = os.listdir(app.config['UPLOAD_FOLDER'])
        # fileCollection = []
        # for fileName in fileNames: 
        #     fileCollection.append(fileName)
            
        return render_template("project.html", form = form, message = os.path.filename(app.config['UPLOAD_FOLDER']) + "has been uploaded")

    return render_template("project.html",form=form)    


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()




#process a get / post request
#first task is to get session Data to work 
#Store the session data in Sql Alchemy 

