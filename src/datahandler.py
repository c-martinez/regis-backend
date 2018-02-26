from pymongo import MongoClient
from configparser import SafeConfigParser

# Mongo filters and projections
FIND_ALL = {}
IGNORE_MONGO_ID = {"_id": 0} # Do not return field _id

class LayerDataManager:
    def __init__(self):
        config = SafeConfigParser()
        config.read('regis-config.ini')
        mongo_host = config.get('mongo', 'host')
        mongo_port = config.getint('mongo', 'port')
        mongo_user = config.get('mongo', 'username', fallback=None)
        mongo_pass = config.get('mongo', 'password', fallback=None)
        db_name = config.get('mongo', 'database')
        collection_name = config.get('mongo', 'collection')

        print({"host": mongo_host, "port": mongo_port,
            "username": mongo_user, "password": mongo_pass})

        client = MongoClient(host=mongo_host, port=mongo_port, username=mongo_user, password=mongo_pass)
        db = client[db_name]
        self.collection = db[collection_name]

    def getLayers(self):
        layerCursor = self.collection.find(filter=FIND_ALL, projection=IGNORE_MONGO_ID)
        return [layer for layer in layerCursor]

    def saveLayer(self, layer):
        self.collection.insert_one(layer)
