import logging
from datetime import datetime
from bson import ObjectId
from pymongo import MongoClient

from app.core.config import MONGO_HOST, MONGO_DB
from app.exceptions.mongo_exception import MongoException

logger = logging.getLogger(__name__)


class MongoAPI():

    def __init__(self):
        try:
            logger.info("Connecting database...")
            self.client = MongoClient(host=MONGO_HOST)
            self.cursor = self.client[MONGO_DB]
            logger.info("Connection established with Mongo")
        except KeyError as key_err:
            logger.error(f"key error exception: {key_err}")
            raise MongoException("key error exception.") from key_err
        except ConnectionError as conn_err:
            msg = f"Connection error on Mongo service. Details: {conn_err}"
            logger.error(msg)
            raise MongoException(message=msg) from conn_err

    def read(self, cursor):
        self.collection = self.cursor[cursor]
        documents = self.collection.find()
        return [{item: str(data[item]) for item in data} for data in documents]

    def find_by_id(self, cursor, id):
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
        self.collection = self.cursor[cursor]
        return self.collection.delete_many({})

    def delete_one_record(self, cursor, id):
        self.collection = self.cursor[cursor]
        return self.collection.delete_one({"_id": ObjectId(id)})
