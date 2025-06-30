import os
import pandas as pd
import pickle
from flask import Blueprint, request, jsonify, render_template
from extensions import cache

with open('model.pkl', 'rb') as obj:
    model = pickle.load(obj)


predict_bp = Blueprint("predict",__name__)



def get_cleaned_data(form_data):
    gestation = float(form_data['gestation'])
    parity = int(form_data['parity'])
    age = float(form_data['age'])
    height = float(form_data['height'])
    weight = float(form_data['weight'])
    smoke = float(form_data['smoke'])

    cleaned_data = {"gestation":[gestation],
                    "parity":[parity],
                    "age":[age],
                    "height":[height],
                    "weight":[weight],
                    "smoke":[smoke]
                    }

    return cleaned_data


EXCPECTED_COLUMNS = ["gestation","parity","age","height","weight","smoke"]



@predict_bp.route('/', methods=['GET'])
def home():
    return render_template("index.html")

# define your endpoint
@predict_bp.route("/predict", methods=['POST'])
@cache.cached(timeout=30, query_string=True)
def get_prediction():
    # Get data from user
    baby_data_form = request.form

    # Clean the form data
    try:
        baby_data_cleaned = get_cleaned_data(baby_data_form)
    except (KeyError, ValueError):
        # Missing fields or invalid type, return 400
        return "Invalid input data", 400 

    # Convert into dataframe
    baby_df = pd.DataFrame(baby_data_cleaned)
    baby_df = baby_df[EXCPECTED_COLUMNS]

    # # Load machine learning trained model
    # with open("model.pkl", 'rb') as obj:
    #     model = pickle.load(obj)

    # Make prediction on user data
    prediction = model.predict(baby_df)
    prediction = round(float(prediction), 2)

    # Return rendered template with prediction
    return render_template("index.html", prediction=prediction)
