from datetime import datetime

from pydantic import BaseModel, validator, Field
from bson.objectid import ObjectId as BsonObjectId
from typing import Optional


class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError('ObjectId required')
        return str(v)


class AnswerModel(BaseModel):  # type: ignore
    answer: str = Field(..., max_length=100, min_length=3)
    poll_id: str = Field(..., max_length=24, min_length=24)


class AnswerResponseModel(AnswerModel):  # type: ignore
    _id: PydanticObjectId
    created_date: datetime


class PollModel(BaseModel):  # type: ignore
    question: str = Field(..., max_length=100, min_length=3)


class PollListModel(PollModel):  # type: ignore
    _id: PydanticObjectId
    created_date: datetime
    answers: Optional = AnswerResponseModel
