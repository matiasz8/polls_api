from fastapi import APIRouter, status

from app.models.poll import AnswerModel
from app.services.answer_service import AnswerService as service_answer


router = APIRouter()


@router.get("",
            name="get_answers",
            status_code=status.HTTP_200_OK,
            description="Get all answers."
            )
async def get_answer():
    """get all answers from polls."""
    return service_answer.get_answers()


@router.post("/create",
             name="create_answer",
             status_code=status.HTTP_200_OK,
             description="Post answers for an especific Poll."
             )
async def post_answer(answer: AnswerModel) -> str:
    """post answers for polls."""
    return service_answer.add_answer(answer)
