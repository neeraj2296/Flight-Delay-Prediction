# import io
import csv
import json
import util
import datetime
import numpy as np
import pandas as pd
from sklearn import preprocessing
from flask_cors import cross_origin
from tensorflow.keras.models import load_model
from tensorflow.keras.models import model_from_json
from werkzeug.utils import secure_filename, redirect
from flask import Flask, render_template, request, jsonify, redirect, send_file

model = load_model("./artifacts/delay.h5")

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

@app.route('/transform', methods=["POST"])
def batch_view():
    if request.method == 'POST':

        AL = util.get_Airlines()
        OA = util.get_Origin()
        DA = util.get_Dest()

        if 'file' not in request.files:
            print('File Not Uploaded')
            return render_template('multi.html')
        f = request.files['file']
        if f.filename == '':
            print('No File')
            return render_template('multi.html')
        else:
            filename = secure_filename(f.filename)
            f.save(filename)
            print('File uploaded successfully')

        input_df = pd.read_csv(f.filename)
        result_df = input_df.copy()
        al = input_df["AIRLINE"].to_list()
        oa = input_df["ORIGIN_AIRPORT"].to_list()
        da = input_df["DESTINATION_AIRPORT"].to_list()

        input_df['MONTH'] = input_df["MONTH"]#1
        input_df['DAY'] = input_df["DAY"]#2
        input_df['DAY_OF_WEEK'] = input_df["DAY_OF_WEEK"]#3

        for x in range(len(al)):
            try:
                input_df['AIRLINE'][x] = AL.index(al[x])#4
            except ValueError:
                input_df['AIRLINE'][x] = len(AL)+1

        for x in range(len(oa)):
            try:
                input_df['ORIGIN_AIRPORT'][x] = OA.index(oa[x])#5
            except ValueError:
                input_df['ORIGIN_AIRPORT'][x] = len(OA)+1

        for x in range(len(da)):
            try:
                input_df['DESTINATION_AIRPORT'][x] = DA.index(da[x])#6
            except ValueError:
                input_df['DESTINATION_AIRPORT'][x] = len(DA)+1

        input_df['SCHEDULED_DEPARTURE'] = input_df["SCHEDULED_DEPARTURE"]#7
        input_df['SCHEDULED_TIME'] = input_df["SCHEDULED_TIME"]#8
        input_df['ARRIVAL_DELAY'] = input_df["ARRIVAL_DELAY"]#9

        input = preprocessing.scale(input_df)
        input = np.array([input])
        input_predict = np.array(model.predict(input))
        input_predict = np.squeeze(input_predict)
        print(input_predict.shape)
        print(input_predict)
        result_df['Result'] = input_predict
        result_df['Result_Description'] = result_df['Result']

        result_df.to_csv('prediction.csv')

        return redirect('/downloadfile/' + 'prediction.csv')

    return render_template('multi.html')

@app.route('/downloadfile/<filename>', methods =['GET'])
def download_file(filename):
    return render_template('Download.html', value = filename)

@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = filename
    return send_file(file_path, as_attachment=True, attachment_filename='')

@app.route('/multi', methods = ['GET','POST'])
def batch():
    return render_template('multi.html')

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        print("Getting Flight detail's Flies")
        AL = util.get_Airlines()
        OA = util.get_Origin()
        DA = util.get_Dest()

        SD = request.form["SCHEDULED_DEPARTURE"]#1
        ST = request.form["SCHEDULED_TIME"]#2
        date = request.form["DATE"]#3
        AIRLINE = str(request.form["AIRLINE"])#4
        ORIGIN = str(request.form["ORIGIN_AIRPORT"])#5
        DEST = str(request.form["DESTINATION_AIRPORT"])#6
    
        SDepart = int(SD[:2]+SD[3:5])
        print(SDepart)
        
        STime = int(ST[:2]+ST[3:5])
        print(STime)
        
        
        year,month,day = (int(x) for x in date.split('-'))
        dow = datetime.date(year, month, day).weekday()
        print(day, month, dow)
        print("Inputiing")

        x = np.zeros(len(util.get_columns()))
        x[0] = month
        x[1] = day
        x[2] = dow
        x[3] = AL.index(AIRLINE)
        x[4] = OA.index(ORIGIN)
        x[5] = DA.index(DEST)
        x[6] = SDepart
        x[7] = STime
        x[8] = float(request.form["ARRIVAL_DELAY"])#7
        print(x)

        x = preprocessing.scale(x)
        x = np.array([x])
        prd = model.predict([x], verbose=0)
        prd = np.reshape(prd,(1,))
        output= round(prd[0],2)
        # response = jsonify({
        #     "predictions" : round(output.item(),2)
        # })
        # response.headers.add('Access-Control-Allow-Origin','*')
        if int(output)>0:
            return render_template('single.html', prediction_text="Flight's probable departure will be {} minutes after the schedule".format(round(output.item(),2)))
        elif int(output)<0:
            return render_template('single.html', prediction_text="Flight's probable departure will be {} minutes before the schedule.".format(round(-output.item(),2)))
        elif int(output)==0:
            return render_template('single.html', prediction_text="Flight will be departing on time.")
    # return response

    return render_template('single.html')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/single')
def single():
    return render_template('single.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__": 
    app.run(debug=True)
