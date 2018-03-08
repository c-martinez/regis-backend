from flask import jsonify
from flask_restplus import Namespace, Resource, reqparse
import werkzeug

from datahandler import LayerDataManager
from davhandler import WebDavHandler
from config import globalconfig

ns = Namespace("layers", description="Regis layers service", validate=True)

parser = reqparse.RequestParser()
parser.add_argument("id", help="resource ID", required=True, location='form')
parser.add_argument("type", help="Type of layer", required=True, location='form',
    choices=globalconfig['layerTypes'])
parser.add_argument("name", help="Name of the layer", required=True, location='form')
parser.add_argument("visible", help="Layer visibility", required=True, location='form', type=bool)
parser.add_argument("file", help="Attached file", required=False, location="files", type=werkzeug.datastructures.FileStorage)

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

        layerManager.saveLayer(layer)
        defs = { "status": "ok" }
        return jsonify(defs)
