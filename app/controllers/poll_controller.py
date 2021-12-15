from fastapi import APIRouter, status, Depends

from app.models.poll import PollModel
from app.services.poll_service import PollService as service_poll


router = APIRouter()


@router.get("",
            name="Poll API",
            status_code=status.HTTP_200_OK,
            description="Api who provide an easily way to handle Polls"
            )
async def post_poll(card: PollModel = Depends()):
    """Handle polls."""
    ...
