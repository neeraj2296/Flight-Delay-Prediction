from flask import Flask, render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import util


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Airlines')
def get_Airlines():
    response = jsonify({
        'AIRLINES': util.get_Airlines()
    })

    return response

@app.route('/origin_airport')
def get_Origin():
    response = jsonify({
        'ORIGINI_AIRPORTS': util.get_Origin()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/Destination_airport')
def get_Dest():
    response = jsonify({
        'DESTINATION_AIRPORTS': util.get_Dest()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_delay', methods=['POST'])
def predict_delay():
    MONTH = int(request.form["MONTH"])
    DAY = int(request.form["DAY"])
    DAY_OF_WEEK = int(request.form["DAY_OF_WEEK"])
    AIRLINES = request.form["AIRLINES"]
    ORIGIN_AIRPORT = request.form["ORIGIN_AIRPORT"]
    DESTINATION_AIRPORT = request.form["DESTINATION_AIRPORT"]
    SCHEDULED_TIME = float(request.form["SCHEDULED_TIME"])
    SCHEDULED_DEPARTURE = float(request.form["SCHEDULED_DEPARTURE"])
    ARRIVAL_DELAY = int(request.form["ARRIVAL_DELAY"])

    response = jsonify({
        'Predicted Delay': str(util.get_delay(MONTH,DAY,DAY_OF_WEEK, AIRLINES ,ORIGIN_AIRPORT, DESTINATION_AIRPORT, SCHEDULED_TIME, SCHEDULED_DEPARTURE, ARRIVAL_DELAY))
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__": 
    app.run(debug=True)