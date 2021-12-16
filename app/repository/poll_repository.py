from app.services.mongo_service import MongoAPI as client


class PollRepository:
    polls_collection = "polls"
    answers_collection = "answers"

    def all_polls(self):
        polls = client(self.polls_collection).read()
        answers = client(self.answers_collection).read()
        for poll in polls:
            for answer in answers:
                if answer['poll_id'] == poll['_id']:
                    poll['answers'] = answer
        return polls

    def create_poll(self, poll):
        return client(self.polls_collection).write({"question": poll})

    def create_answer(self, poll_id, answer):
        data = {"poll_id": poll_id, "answer": answer}
        return client(self.answers_collection).write(data)
