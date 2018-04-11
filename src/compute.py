from flask import jsonify
from flask_restplus import Namespace, Resource, reqparse

from datahandler import LayerDataManager

ns = Namespace("compute", description="Regis compute service", validate=True)

layerManager = LayerDataManager()

parser = reqparse.RequestParser()
# parser.add_argument('id', required=True, location='args')
@ns.route("/execute/")
class LayerAdd(Resource):
    @ns.expect(parser, validate=True)
    def post(self):
        '''Add new layer'''
        args = parser.parse_args()

        # x = args['x']

        response = { "status": "ok" }
        return jsonify(response)
