#!/bin/python
# -*- coding: utf-8 -*- 
import os
import json

from flask import Flask, jsonify

execution_path = os.getcwd()
models_dir = os.path.join(execution_path, "models")

app = Flask(__name__)

# argument parsing
# Estos fueron los argumentos acordados al 2018-11-21 en mail de Seba Santos
"""
{
                "cluster": ["DW1001", "DW1005", "DW1006", "DW1007"],
                "simulacion": {
                               "x": -60.7439430569999,
                               "y": -32.7657464119999 }
}
"""
mock_content = {'cluster': [{'id': "DW1001",
                             'pct_afectacion': '.10'},
                             {'id': "DW1005",
                             'pct_afectacion': '.05'},
                             {'id':"DW1006",
                             'pct_afectacion':'0.03'},
                             {'id':"DW1007",
                             'pct_afectacion':'0.1'}],
                'cluster_length': 4,
                'simulacion': {'volumen_mes':'200'
                              }
                }

json_response = {}
json_response['result'] = mock_content

@app.route('/')
def im_alive():
    return jsonify({ "message": "I'm alive!"}) 

@app.route('/eesSim', methods= ['GET', 'POST'])
def ees_sim_v1():
    return jsonify(json_response)

if __name__ == '__main__':
    app.run(debug=True)