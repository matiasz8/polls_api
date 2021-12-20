import json
from fastapi import APIRouter, status, Depends

from app.models.poll import PollListModel, PollModel, AnswerModel
from app.services.poll_service import PollService as service_poll


router = APIRouter()


@router.get("/get",
            name="get_polls",
            status_code=status.HTTP_200_OK,
            description="Api who provide an easily way to handle Polls"
            )
async def get_poll() -> PollListModel:
    """Handle polls."""
    return service_poll.get_polls()


@router.post("/create",
             name="create_poll",
             status_code=status.HTTP_200_OK,
             description="Api who provide an easily way to handle Polls"
             )
async def post_poll(question: PollModel) -> str:
    """post polls."""
    return service_poll.add_poll(question)


@router.post("/answer",
             name="create_answer",
             status_code=status.HTTP_200_OK,
             description="Post answers for an especific Poll."
             )
async def post_answer(answer: AnswerModel) -> str:
    """post answers for polls."""
    return service_poll.add_answer(answer)
