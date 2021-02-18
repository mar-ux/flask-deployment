# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:44:06 2021

@author: smai212
"""
import numpy as np
import flask
from flask import Flask,request,jsonify,render_template
app=Flask(__name__)
@app.route('/h')
def home_page():
    return render_template('index.html')
@app.route('/salarypredict',methods=['POST'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = marmodel.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run()