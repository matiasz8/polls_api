from datetime import datetime
from bson import ObjectId
import factory
from faker import Factory

from app.models.poll import PollListModel, PollModel, AnswerResponseModel, AnswerModel

faker = Factory.create()


def ObjectIdStr():
    return str(ObjectId())


class AnswerFactory(factory.Factory):
    answer = factory.LazyAttribute(lambda x: faker.sentence())
    poll_id: str = factory.LazyAttribute(lambda x: ObjectIdStr())

    class Meta:
        model = AnswerModel


class AnswerResponseFactory(factory.Factory):
    _id: str = factory.LazyAttribute(lambda x: ObjectIdStr())
    created_date = factory.LazyFunction(datetime.today)
    answer = factory.LazyAttribute(lambda x: faker.sentence())
    poll_id: str = factory.LazyAttribute(lambda x: ObjectIdStr())

    class Meta:
        model = AnswerResponseModel


class PollFactory(factory.Factory):
    question = factory.LazyAttribute(lambda x: faker.sentence())

    class Meta:
        model = PollModel


class PollListFactory(factory.Factory):
    _id: str = factory.LazyAttribute(lambda x: ObjectIdStr())
    created_date = factory.LazyFunction(datetime.today)
    question = factory.LazyAttribute(lambda x: faker.sentence())
    answers = AnswerResponseFactory()

    class Meta:
        model = PollListModel
