from flask import Flask, render_template

#STATIC_DIR = os.path.abspath('/static')


#Create instance
app = Flask(__name__)

#Route
@app.route("/", methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        weight = request.form["weight"]
        height = request.form["height"]
        age = request.form["age"]
        gender = request.form["gender"]
        ap_h = request.form["ap_h"]
        ap_l = request.form["ap_l"]
        chol = request.form["cholestrol"]
        glu = request.form["glucose"]
        smoke = request.form["smoke"]
        al = request.form["alcohol"]
        excercise = request.form["excercise"]
        
        
        
        instance = [[int(age), int(gender), int(height), int(weight), int(ap_h), int(ap_l), int(chol), int(glu), int(smoke), int(al), int(excercise) ]]    
        answer = model.predict([instance])
        prediction = answer[0]
        
        if prediction == 1.0:
            text = "High risk for the presence of a cardiovascular disease"
            return redirect(url_for("example", answer = text))
        if prediction == 0.0:
            text = "Low risk for the presence of a cardiovascular disease"
            return redirect(url_for("example", answer = text))
            
    else:
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
