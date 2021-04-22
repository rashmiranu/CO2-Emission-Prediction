from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder="template")

model = pickle.load(open("decision_tree_regressor.pkl", "rb"))

# home page
@app.route("/")
def home():
    return render_template("home.html")


# co2 emission calculation page
@app.route("/emission")
def emission():
    return render_template("emission.html")


@app.route("/result", methods=['POST'])
def predict():

    if request.method == 'POST':
        engine_size = float(request.form['Engine Size(L)'])
        cylinder = int(request.form['Cylinders'])
        fuel_type = int(request.form['Fuel Type'])
        fuel_consumption = float(request.form['Fuel Consumption Comb (L/100 km)'])

        prediction = model.predict([[engine_size, cylinder, fuel_type, fuel_consumption]])
        prediction = prediction[0]

    return render_template('result.html', prediction_text="Your car emits {} grams/km of carbon dioxide".format(prediction))


if __name__ == "__main__":
    app.run(debug= True)