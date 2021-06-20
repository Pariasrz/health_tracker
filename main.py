from flask import Flask, render_template

#STATIC_DIR = os.path.abspath('/static')


#Create instance
app = Flask(__name__)

#information we need to normalize the input of the model
max_D = [64.9671232876712, 2.00, 200.0, 170.0, 2000.0, 1900.0, 3.0, 3.0, 1.0, 1.0, 1.0] 
min_D = [39.1095890410959, 1.0, 120.0, 30.0, 40.0, 40.0, 1.0, 1.0, 0.0, 0.0, 0.0]


#Main Route
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
        
        
        
        instance = [float(age), float(gender), float(height), float(weight), float(ap_h), float(ap_l), float(chol), float(glu), float(smoke), float(al), float(excercise) ]    
        normalized_instance = []
        
        #normalizing the input data of the model
        for i in range(0,11):
            if max_D[i] >= instance[i]:
                x_max = max_D[i]
            else:
                x_max = instance[i]
                
            if min_D[i] <= instance[i]:
                x_min = min_D[i]
            else:
                x_min = instance[i]
                
            normalized_x = (instance[i] - x_min) / (x_max - x_min)
            normalized_instance.append(normalized_x)
        
        #predict the answer using the trained model
        answer = model.predict([normalized_instance])
        prediction = answer[0]
        prob = (model.predict_proba([normalized_instance])[0][1])*100 #the prbability of the presence of a cardiovascular disease
        
        #showing the results
        if prediction == 1.0:
            text = "The risk of the presence of a cardiovascular disease is " + str('{:.2f}'.format(prob)) + "% which is high."
            return redirect(url_for("example", answer = text))
        if prediction == 0.0:
            text = "The risk of the presence of a cardiovascular disease is " + str('{:.2f}'.format(prob)) + "% which is low."
            return redirect(url_for("example", answer = text))
            
    else:
        return render_template("heart.html")

#define other routes
@app.route("/example.html")
def example():
    return render_template("example.html")

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
