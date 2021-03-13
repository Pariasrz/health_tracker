from flask import Flask, render_template

#STATIC_DIR = os.path.abspath('/static')

#Create instance
app = Flask(__name__)

#Route
@app.route("/")
def home():
    return render_template("heart.html")

#2nd Route
@app.route("/bmi.html")
def about():
    return render_template("bmi.html")

app.run()
