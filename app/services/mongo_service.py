from datetime import datetime

from pymongo import MongoClient
from bson import ObjectId


class MongoAPI:
    def __init__(self, document):
        cursor = client["polls"]
        self.collection = cursor[document]

    def read(self):
        documents = self.collection.find()
        output = [{item: str(data[item]) for item in data} for data in documents]
        return output

    def find_byid(self, id):
        return self.collection.find_one({"_id" : ObjectId(id)})

    def write(self, new_document):
        try:
            new_document["created_date"] = datetime.today()
            result = self.collection.insert_one(new_document)
            return str(result.inserted_id)
        except Exception as ex:
            raise Exception(ex)

    def delete_all(self):
        return self.collection.delete_many({})

    def delete_one(self, id):
        return self.collection.delete_one({"_id": id})


print("connecting database...")
client = MongoClient(host='db')
print("connection established with Mongo")
