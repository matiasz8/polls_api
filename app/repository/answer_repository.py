import logging

from app.services.mongo_service import MongoAPI
from app.models.poll import AnswerModel


logger = logging.getLogger(__name__)


class AnswerRepository:
    answers_collection = "answers"
    client = MongoAPI()

    def all_answers(self):
        return self.client.read(cursor=self.answers_collection)

    def create_answer(self, data: AnswerModel) -> str:
        return self.client.write(cursor=self.answers_collection, new_document=data.dict())

    def delete_answers(self):
        return self.client.delete_all(cursor=self.answers_collection)

    def delete_answer_by_id(self, answer_id):
        return self.client.delete_one_record(cursor=self.answers_collection, id=answer_id)
