from fastapi import APIRouter

from app.controllers import poll_controller as router_poll
from app.core.config import API_PREFIX

api_router = APIRouter(prefix=API_PREFIX)
api_router.include_router(router_poll.router, tags=["poll"], prefix="/poll")
