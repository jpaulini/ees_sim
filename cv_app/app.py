import os
import json

from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

execution_path = os.getcwd()
models_dir = os.path.join(execution_path, "models")

app = Flask(__name__)
api = Api(app)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# Setup the Api resource routing here
# Route the URL to the resource

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)