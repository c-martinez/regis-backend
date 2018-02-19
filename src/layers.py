
from flask import Response, jsonify
from flask_restplus import Namespace, Resource #, fields

import json

ns = Namespace('layers', description='Regis layers service')

@ns.route('/')
class Layers(Resource):
    def get(self):
        '''List all layers'''
        defsFile = 'layerdefinitions.json'
        defs = json.loads(open(defsFile, 'r').read())
        return jsonify(defs)

@ns.route('/add')
class LayerAdd(Resource):
    def post(self):
        '''Add new layer'''
        return Response("TBD")
