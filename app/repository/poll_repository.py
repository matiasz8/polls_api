import logging

from app.core.config import MONGO_DB
from app.services.mongo_service import MongoAPI
from app.models.poll import PollListModel, PollModel, AnswerModel
from app.exceptions.mongo_exception import MongoException


logger = logging.getLogger(__name__)


class PollRepository:
    polls_collection = "polls"
    answers_collection = "answers"

    def __init__(self):
        try:
            logger.info("Connecting database...")
            self.client = MongoAPI(mongo_db=MONGO_DB)
            logger.info("Connection established with Mongo")
        except KeyError as key_err:
            logger.error(f"key error exception: {key_err}")
            raise MongoException("key error exception.") from key_err
        except ConnectionError as conn_err:
            msg = f"Connection error on Mongo service. Details: {conn_err}"
            logger.error(msg)
            raise MongoException(message=msg) from conn_err

    def all_polls(self) -> PollListModel:
        polls = self.client.read(cursor=self.polls_collection)
        answers = self.client.read(cursor=self.answers_collection)
        for poll in polls:
            for answer in answers:
                if answer['poll_id'] == poll['_id']:
                    poll['answers'] = answer
        return polls

    def create_poll(self, data: PollModel) -> str:
        return self.client.write(cursor=self.polls_collection, new_document=data.dict())

    def create_answer(self, data: AnswerModel) -> str:
        return self.client.write(cursor=self.answers_collection, new_document=data.dict())
