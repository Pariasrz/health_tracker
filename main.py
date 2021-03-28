from flask import Flask, render_template

#STATIC_DIR = os.path.abspath('/static')

#Create instance
app = Flask(__name__)

#Route
@app.route("/")
def home():
    return render_template("heart.html")

@app.route("/heart.html")
def heart():
    return render_template("heart.html")

@app.route("/bmi.html")
def about():
    return render_template("bmi.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

app.run()
