import logging

from pydantic import ValidationError

from app.models.poll import PollListModel, PollModel, AnswerModel
from app.repository.poll_repository import PollRepository

logger = logging.getLogger(__name__)


class PollService:
    """Service who handle Poll data."""
    poll_repository = PollRepository()

    @classmethod
    def get_polls(cls) -> PollListModel:
        return cls.poll_repository.all_polls()

    @classmethod
    def add_poll(cls, pool: PollModel) -> str:
        """Save poll on db."""
        return cls.poll_repository.create_poll(pool)

    @classmethod
    def add_answer(cls, answer: AnswerModel) -> str:
        """Save answer on db."""
        return cls.poll_repository.create_answer(answer)
