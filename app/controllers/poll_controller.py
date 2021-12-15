import json
from fastapi import APIRouter, status, Depends

from app.models.poll import PollModel
from app.services.poll_service import PollService as service_poll
from app.repository.mongo_api import MongoAPI


router = APIRouter()


@router.get("/get",
            name="get_polls",
            status_code=status.HTTP_200_OK,
            description="Api who provide an easily way to handle Polls"
            )
async def get_poll():
    """Handle polls."""
    polls = MongoAPI("polls").read()
    answers = MongoAPI("answers").read()
    for poll in polls:
        for answer in answers:
            if answer['poll_id'] == poll['_id']:
                poll['answers'] = answer
    return polls


@router.post("/create",
             name="create_poll",
             status_code=status.HTTP_200_OK,
             description="Api who provide an easily way to handle Polls"
             )
async def post_poll(poll):
    """post polls."""
    return MongoAPI("polls").write({"question": poll})


@router.post("/answer",
             name="create_answer",
             status_code=status.HTTP_200_OK,
             description="Post answers for an especific Poll."
             )
async def post_answer(poll_id, answer):
    """post answers for polls."""
    data = {"poll_id": poll_id, "answer": answer}
    return MongoAPI("answers").write(data)
