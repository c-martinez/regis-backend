from flask import Response
from flask_restplus import Namespace, Resource

ns = Namespace('dav', description='Proxy for webdav')

@ns.route('/')
class WebDavProxy(Resource):
    def get(self):
        '''Get files from webdav'''
        return Response("TBD")

    def post(self):
        '''Add new layer'''
        return Response("TBD")
