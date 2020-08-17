from flask import Flask, render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import util
import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model
from sklearn import preprocessing
model = load_model("./artifacts/delay_01.h5")

app = Flask(__name__)
@app.route("/airline")
def get_Airlines():
    response = jsonify({
        'AIRLINE': util.get_Airlines()
    })

    return response
    
@app.route("/origin")
def get_Origin():
    response = jsonify({
        'ORIGIN': util.get_Origin()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
    
@app.route("/destination")
def get_Dest():
    response = jsonify({
        'DESTIN': util.get_Dest()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        print("Getting Json Flies")
        AL = util.get_Airlines()
        OA = util.get_Origin()
        DA = util.get_Dest()
        print("Inputiing")
        x = np.zeros(len(util.get_columns()))
        print(x)
        x[0] = int(request.form["MONTH"])
        print(x)
        x[1] = int(request.form["DAY"])
        x[2] = int(request.form["DAY_OF_WEEK"])
        AIRLINE = str(request.form["AIRLINE"])
        ORIGIN = str(request.form["ORIGIN_AIRPORT"])
        DEST = str(request.form["DESTINATION_AIRPORT"])
        x[3] = AL.index(AIRLINE)
        x[4] = OA.index(ORIGIN)
        x[5] = DA.index(DEST)
        x[6] = float(request.form["SCHEDULED_DEPARTURE"])
        x[7] = float(request.form["SCHEDULED_TIME"])
        x[8] = float(request.form["ARRIVAL_DELAY"])
        
        x = preprocessing.scale(x)
        x = np.array([x])
        prd = model.predict([x], verbose=0)
        prd = np.reshape(prd,(1,))
        output=np.round(prd[0],2)

        response = jsonify({
            "predictions" : str(output)
        })
    return response
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/single')
def single():
    return render_template('single.html')

@app.route('/multi', methods = ["GET", "POST"])
def multi():
    return render_template('multi.html')

if __name__ == "__main__": 
    app.run(debug=True)