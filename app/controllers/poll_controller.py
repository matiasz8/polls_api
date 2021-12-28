from fastapi import APIRouter, status

from app.models.poll import PollListModel, PollModel
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


@router.delete("/deleteAll",
               name="delete_polls",
               status_code=status.HTTP_202_ACCEPTED,
               description="Delete all polls"
               )
async def delete_polls() -> str:
    """delete all polls from database."""
    service_poll.delete_polls()
    return "All polls have been deleted."
