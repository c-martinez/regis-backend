from flask import jsonify
from flask_restplus import Namespace, Resource, reqparse
import werkzeug

import json
import requests
from itertools import chain

from datahandler import LayerDataManager
from davhandler import WebDavHandler
from config import globalconfig

ns = Namespace("layers", description="Regis layers service", validate=True)

parser = reqparse.RequestParser()
parser.add_argument("type", help="Type of layer", required=True, location='form',
    choices=globalconfig['layerTypes'])
parser.add_argument("name", help="Name of the layer", required=True, location='form')
parser.add_argument("active", help="Layer visibility", required=True, location='form', type=bool)
parser.add_argument("file", help="Attached file", required=False, location="files", type=werkzeug.datastructures.FileStorage)

# Additional parameters only present for circular layers
parser.add_argument("center", help="Circular layer center", required=False, location='form')
parser.add_argument("radius", help="Circular layer radius", required=False, location='form', type=float)

layerManager = LayerDataManager()
davHandler = WebDavHandler()

@ns.route("/")
class Layers(Resource):
    def get(self):
        '''List all layers'''
        layers = layerManager.getLayers()
        defs = {
            "name": globalconfig['name'],
            "version": globalconfig['version'],
            "layers": layers
        }
        return jsonify(defs)

@ns.route("/add/")
class LayerAdd(Resource):
    @ns.expect(parser, validate=True)
    def post(self):
        '''Add new layer'''
        args = parser.parse_args()

        myFile = args['file']
        del args['file']
        layer = args

        # if myFile is not None -- upload it to webdav and get a URL for it.
        if myFile:
            layer['url'] = davHandler.uploadFile(myFile)

        savedLayer = layerManager.saveLayer(layer)
        defs = { "status": "ok",
                  "layer": savedLayer }
        return jsonify(defs)

infoParser = reqparse.RequestParser()
infoParser.add_argument('id', required=True, location='args')
@ns.route("/info/")
class LayerInfo(Resource):
    @ns.expect(infoParser)
    def get(self):
        '''List columns for geojson file'''
        args = infoParser.parse_args()

        id = args['id']
        layer = layerManager.getLayer(id)
        if layer:
            if layer['type'] == 'geojson':
                url = layer['url']
                geojson = requests.get(url).json()
                propSet = [ set(feature['properties'].keys()) for feature in geojson['features']]
                properties = list(set(chain.from_iterable(propSet)))
                response = { "status": "ok",
                      "columns": properties }
            else:
                response = { "status": "error",
                         "message": "No information retrievable from this type of layer" }
        else:
            response = { "status": "error",
                     "message": "Layer not found" }
        return jsonify(response)
