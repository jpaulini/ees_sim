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
@app.route('/')
def im_alive():
    return jsonify({ "message": "I'm alive!") 

if __name__ == '__main__':
    app.run(debug=True)