from flask import Flask, request, jsonify, render_template
from routes import predict, user
import pandas as pd
import pickle
from extensions import cache


app = Flask(__name__)

# configure my cache
app.config['CACHE_TYPE'] = 'SimpleCache'


# init cache
cache.init_app(app)

## import your blueprints here and register
app.register_blueprint(user.user_bp) 
app.register_blueprint(predict.predict_bp)


# def get_cleaned_data(form_data):
#     gestation = float(form_data['gestation'])
#     parity = int(form_data['parity'])
#     age = float(form_data['age'])
#     height = float(form_data['height'])
#     weight = float(form_data['weight'])
#     smoke = float(form_data['smoke'])

#     cleaned_data = {"gestation":[gestation],
#                     "parity":[parity],
#                     "age":[age],
#                     "height":[height],
#                     "weight":[weight],
#                     "smoke":[smoke]
#                     }


#     return cleaned_data


# @app.route('/', methods=['GET'])
# def home():
#     return render_template("index.html")


## define your endpoint
# @app.route("/predict", methods = ['POST'])
# def get_prediction():
#     # get data from user
#     baby_data_form = request.form

#     baby_data_cleaned = get_cleaned_data(baby_data_form)

#     # convert into dataframe
#     baby_df = pd.DataFrame(baby_data_cleaned)

#     # load machine leanring trained model 
#     with open("model.pkl", 'rb') as obj:
#         model = pickle.load(obj)

#     # make prediciton on user data
#     prediction = model.predict(baby_df)
#     prediction = round(float(prediction), 2)

#     # return reponse in a json format
#     response = {"Prediction":prediction}

#     return render_template("index.html", prediction=prediction)





if __name__ == '__main__':
    app.run(debug=True)