from flask import Flask, jsonify, request, render_template, redirect, url_for
import pickle


loaded_model = pickle.load(open('/home/pariasrz/health_tracker/finalized_model.sav', 'rb'))

max_D = [64.9671232876712, 2.00, 200.0, 170.0, 2000.0, 1900.0, 3.0, 3.0, 1.0, 1.0, 1.0]
min_D = [39.1095890410959, 1.0, 120.0, 30.0, 40.0, 40.0, 1.0, 1.0, 0.0, 0.0, 0.0]

app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
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

        answer = loaded_model.predict([normalized_instance])
        prob = loaded_model.predict_proba([normalized_instance])[0][1]*100
        prediction = answer[0]

        if prediction == 1.0:
            text = "The risk of the presence of a cardiovascular disease is " + str('{:.2f}'.format(prob)) + "% which is high."
            return redirect(url_for("example", answer = text))
        if prediction == 0.0:
            text = "The risk of the presence of a cardiovascular disease is " + str('{:.2f}'.format(prob)) + "% which is low."
            return redirect(url_for("example", answer = text))

    else:
        return render_template("heart.html")

def external_url_handler(error, endpoint, values):
    "Looks up an external URL when `url_for` cannot build a URL."
    # This is an example of hooking the build_error_handler.
    # Here, lookup_url is some utility function you've built
    # which looks up the endpoint in some external URL registry.
    url = lookup_url(endpoint, **values)
    if url is None:
        # External lookup did not have a URL.
        # Re-raise the BuildError, in context of original traceback.
        exc_type, exc_value, tb = sys.exc_info()
        if exc_value is error:
            raise (exc_type, exc_value, tb)
        else:
            raise error
    # url_for will use this result, instead of raising BuildError.
    return url

app.url_build_error_handlers.append(external_url_handler)

@app.route("/example.html")
def example():
    return render_template("example.html")

#Define second Route and Content
@app.route("/bmi.html")
def bmi():
    return render_template("bmi.html")

#Define third Route and Content
@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/heart.html")
def heart():
    return render_template("heart.html")
