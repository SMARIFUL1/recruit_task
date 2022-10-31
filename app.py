import numpy as np
from flask import Flask, render_template, request , jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def Home():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    year = int(request.form.get('year')) - 2021
    month = int(request.form.get('month'))
    features = [[year, month]]
    prediction = model.predict(features)

    return render_template(
        'index.html',
        prediction_text='prediction is {}'.format(prediction))




if __name__ == "__main__":
    app.run(debug=True)