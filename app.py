from flask import Flask, request, redirect, render_template, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)

# @app.route('/')
# def home():
# 	return render_template('home.html')

@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'models/final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True)