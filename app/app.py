#!/bin/python
# -*- coding: utf-8 -*- 
import os
import json

from flask import Flask, jsonify, request

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
def response_factory(result = None, error = None , message = None):
    d = {}
    d['results'] = {'cluster': [],
                    'cluster_length': 0,
                    'simulacion': {}}
    d['error'] = error
    d['message'] = message
    return d

@app.route('/')
def im_alive():
    return jsonify({ "message": "I'm alive!"}) 

@app.route('/eesSim', methods= ['GET', 'POST'])
def ees_sim_v1():
    lat = None
    long = None

    out = response_factory()
    # if not request.is_json():
    #     out['error'] = 'Error'
    #     out['message'] = 'POST should contain JSON. Set mimetype to \'Application/json\''

    try:
        body_info = request.get_json(force=True)
    except ValueError:
        out['error'] = 'Error'
        out['message'] = 'Error parsing JSON input'

    if 'cluster' in body_info.keys():
        cluster_list = []
        for es in body_info['cluster']:
            cluster_list.append({'id': es})
        out['results']['cluster'] = cluster_list
        out['results']['cluster_length'] = len(cluster_list)

    if 'simulacion' in body_info.keys():
        if 'lat' in body_info['simulacion']:
            lat = body_info['simulacion']['lat']
        if 'long' in body_info['simulacion']:
            long = body_info['simulacion']['long']
        if lat is None or long is None:
            out['results']['simulacion'] = {}
            out['error'] = 'MissingLatLong'
            out['message'] = 'Especificar latitud y longitud en simulacion como \'lat\' y \'long\''

    return jsonify(out)

if __name__ == '__main__':
    app.run(debug=True)