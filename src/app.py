from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user = request.form["nm"]
        return user + " is their name"  # You should return a response here
    else: 
        print("A GET request was used")
        name = "John Doe"
        return render_template("project.html", name=name)
     
if __name__ == "__main__":
    app.run()




