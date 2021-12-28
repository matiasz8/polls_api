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


@router.delete("/deleteAll",
               name="delete_answers",
               status_code=status.HTTP_202_ACCEPTED,
               description="Delete all answers"
               )
async def delete_answers() -> str:
    """delete all answers from database."""
    service_answer.delete_answers()
    return "All answers have been deleted."


@router.delete("/deleteOne",
               name="delete_answer",
               status_code=status.HTTP_202_ACCEPTED,
               description="Delete answer by id"
               )
async def delete_answer(answer_id: str) -> str:
    """delete answer by ID."""
    service_answer.delete_answer_by_id(answer_id)
    return f"Answers {answer_id} have been deleted."
