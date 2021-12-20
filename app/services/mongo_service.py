from datetime import datetime
from bson import ObjectId
from pymongo import MongoClient

from app.core.config import MONGO_HOST
from app.exceptions.mongo_exception import MongoException


class MongoAPI():
    def __init__(self, mongo_db):
        self.client = MongoClient(host=MONGO_HOST)
        self.cursor = self.client[mongo_db]

    def read(self, cursor):
        self.collection = self.cursor[cursor]
        documents = self.collection.find()
        output = [{item: str(data[item]) for item in data} for data in documents]
        return output

    def find_byid(self, cursor, id):
        self.collection = self.cursor[cursor]
        return self.collection.find_one({"_id" : ObjectId(id)})

    def write(self, cursor, new_document):
        self.collection = self.cursor[cursor]
        try:
            new_document["created_date"] = datetime.today()
            result = self.collection.insert_one(new_document)
            return str(result.inserted_id)
        except Exception as ex:
            raise MongoException(message=f"writting error. Details: {ex}")

    def delete_all(self, cursor):
        return self.collection.delete_many({})

    def delete_one(self, cursor, id):
        self.collection = self.cursor[cursor]
        return self.collection.delete_one({"_id": id})
