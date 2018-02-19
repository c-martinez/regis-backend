from flask import Flask
from flask_cors import CORS
from flask_restplus import Api

from layers import ns as layers_ns
from dav import ns as dav_ns
from dynamic import ns as dynamic_ns

app = Flask(__name__)
app.debug = True
CORS(app)

appVersion = 'v0.1'

api = Api(app, version=appVersion, title='Regis-backend',
    description='ReGIS layers service backend',
)

api.add_namespace(layers_ns)
api.add_namespace(dav_ns)
api.add_namespace(dynamic_ns)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4201)
