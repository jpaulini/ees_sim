import os
import json

from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with

execution_path = os.getcwd()
models_dir = os.path.join(execution_path, "models")

app = Flask(__name__)
api = Api(app)

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


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class GetEESCapture(Resource):
    def __init__(self, eeslist = None ):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('simulacion', type = list, location = 'json')
        self.parser.add_argument('cluster', type= list, location = 'json')

    def get(self):
        return jsonify(self.ees_list)
    
    def post(self):
        args = self.parser.parse_args()
        print(args["simulacion"])
        print(args["cluster"])
        return None

# Setup the Api resource routing here
# Route the URL to the resource

api.add_resource(HelloWorld, '/')
api.add_resource(GetEESCapture, '/eesSim')

if __name__ == '__main__':
    app.run(debug=True)