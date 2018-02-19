from flask import Response
from flask_restplus import Namespace, Resource

ns = Namespace('dynamic', description='Definition for dynamic layer')

@ns.route('/')
class WebDavProxy(Resource):
    def get(self):
        '''Get files from webdav'''
        return Response("TBD")
