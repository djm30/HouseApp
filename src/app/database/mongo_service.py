import os
from pymongo import MongoClient


class MongoService:
    def __init__(self):
        self.mongo_connection = MongoClient(host='app_db', port=27017)

    def get_from_collection(self, collection_name, db, query={}):
        mongo_collection = self.mongo_connection[db][collection_name]
        mongo_data = mongo_collection.find(query)
        return list(mongo_data)

    def insert_into_collection(self, collection_name, db, data):
        mongo_collection = self.mongo_connection[db][collection_name]
        mongo_collection.insert_one(data)

    def update_into_collection(self, collection_name, db, query, field, value):        
        mongo_collection = self.mongo_connection[db][collection_name]
        mongo_collection.find_one_and_update(
            {
                "_id" : mongo_collection.find(query).get("_id")
            },
            {
                "$set": {field: value}
            },
            upsert=True
        )
