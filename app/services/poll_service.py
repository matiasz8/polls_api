import logging

from pydantic import ValidationError

from app.repository.poll_repository import PollRepository

logger = logging.getLogger(__name__)


class PollService:
    """Service who handle Poll data."""
    poll_repository = PollRepository()

    @classmethod
    def add_poll(cls, pool: dict) -> str:
        """Save poll on db."""
        return cls.poll_repository.create_poll(pool)

    @classmethod
    def get_polls(cls) -> dict:
        return cls.poll_repository.all_polls()

    @classmethod
    def add_answer(cls, poll_id: str, answer: str) -> str:
        """Save answer on db."""
        return cls.poll_repository.create_answer(poll_id, answer)
