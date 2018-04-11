from pymongo import MongoClient
from bson import ObjectId

from config import mongoconfig

# Mongo filters and projections
FIND_ALL = {}
IGNORE_MONGO_ID = {"_id": 0} # Do not return field _id

class LayerDataManager:
    def __init__(self):
        mongo_host = mongoconfig['host']
        mongo_port = mongoconfig['port']
        mongo_user = mongoconfig['user']
        mongo_pass = mongoconfig['pass']
        db_name = mongoconfig['db']
        collection_name = mongoconfig['collection']

        client = MongoClient(host=mongo_host, port=mongo_port, username=mongo_user, password=mongo_pass)
        db = client[db_name]
        self.collection = db[collection_name]

    def getLayers(self):
        '''Returns all existing layers saved on MongoDB.'''
        layerCursor = self.collection.find(filter=FIND_ALL, projection=IGNORE_MONGO_ID)
        return [layer for layer in layerCursor]

    def getLayer(self, id):
        '''Returns layer saved on MongoDB with given ID.'''
        layerCursor = self.collection.find(filter={'id': id}, projection=IGNORE_MONGO_ID)
        layers = [layer for layer in layerCursor]
        assert len(layers)<=1, 'Too many layers with the same ID!'
        return layers[0] if len(layers) == 1 else None

    def saveLayer(self, layer):
        '''Create a new layer on MongoDB. An ID is generated for this layer.
        The newly created layer is returned'''

        if 'center' in layer and layer['center']:
            # Specific for circle layers
            c = layer['center'].split(',')
            layer['center'] = [ float(ci) for ci in c ]

        newId = str(ObjectId())
        layer['id'] = newId
        layer['_id'] = newId
        self.collection.insert_one(layer)
        del layer['_id']
        return layer
