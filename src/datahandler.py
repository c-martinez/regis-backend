from pymongo import MongoClient

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
        layerCursor = self.collection.find(filter=FIND_ALL, projection=IGNORE_MONGO_ID)
        return [layer for layer in layerCursor]

    def saveLayer(self, layer):
        self.collection.insert_one(layer)
