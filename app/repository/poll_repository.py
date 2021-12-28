import logging


from app.services.mongo_service import MongoAPI
from app.models.poll import PollListModel, PollModel


logger = logging.getLogger(__name__)


class PollRepository:
    polls_collection = "polls"
    answers_collection = "answers"
    client = MongoAPI()

    def all_polls(self) -> PollListModel:
        polls = self.client.read(cursor=self.polls_collection)
        answers = self.client.read(cursor=self.answers_collection)
        for poll in polls:
            for answer in answers:
                if answer['poll_id'] == poll['_id']:
                    if "answers" not in poll:
                        poll["answers"] = [answer]
                    else:
                        poll["answers"].append(answer)
        return polls

    def create_poll(self, data: PollModel) -> str:
        return self.client.write(cursor=self.polls_collection, new_document=data.dict())

    def delete_polls(self):
        return self.client.delete_all(cursor=self.polls_collection)
