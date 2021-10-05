from flask import Flask, jsonify, request
import pandas as pd
import joblib

app = Flask(__name__)


@app.route("/", methods=['GET'])
def working():
    return "Working"


@app.route("/predict", methods=['POST'])
def do_prediction():
    json = request.get_json()
    model = joblib.load('model/regmodel.pkl')
    df = pd.DataFrame(json, index=[0])

    y_predict = model.predict(df)

    result = {"Predicted House Price": y_predict[0]}
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
