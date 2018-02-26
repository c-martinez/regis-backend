
from flask import jsonify, request
from flask_restplus import Namespace, Resource, fields

from datahandler import LayerDataManager

ns = Namespace("layers", description="Regis layers service", validate=True)

singleLayerDef = ns.model("SingleLayerDefinition", {
    "id": fields.String(description="resource ID", required=True),
    "type": fields.String(description="Type of layer", required=True),
    "name": fields.String(description="Name of the layer", required=True),
    "visible": fields.Boolean(description="Layer visibility", required=True),
})

layerManager = LayerDataManager()

@ns.route("/")
class Layers(Resource):
    def get(self):
        '''List all layers'''
        layers = layerManager.getLayers()
        defs = {
            "name": "GV-webportal layers",
            "version": "0.1",
            "layers": layers
        }
        return jsonify(defs)


@ns.route("/add/")
class LayerAdd(Resource):
    @ns.expect(singleLayerDef, valudate=True)
    def post(self):
        '''Add new layer'''
        layer = request.get_json()
        layerManager.saveLayer(layer)
        defs = { "status": "ok" }
        return jsonify(defs)
