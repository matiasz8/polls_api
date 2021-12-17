from app.services.mongo_service import MongoAPI as client

from app.models.poll import PollListModel, PollModel, AnswerModel


class PollRepository:
    polls_collection = "polls"
    answers_collection = "answers"

    def all_polls(self) -> PollListModel:
        polls = client(self.polls_collection).read()
        answers = client(self.answers_collection).read()
        for poll in polls:
            for answer in answers:
                if answer['poll_id'] == poll['_id']:
                    poll['answers'] = answer
        return polls

    def create_poll(self, data: PollModel) -> str:
        return client(self.polls_collection).write(data.dict())

    def create_answer(self, data: AnswerModel) -> str:
        return client(self.answers_collection).write(data.dict())
