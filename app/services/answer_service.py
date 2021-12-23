import logging

from app.models.poll import AnswerModel
from app.repository.answer_repository import AnswerRepository

logger = logging.getLogger(__name__)


class AnswerService:
    """Service who handle Answer Poll data."""
    answer_repository = AnswerRepository()

    @classmethod
    def get_answers(cls):
        return cls.answer_repository.all_answers()

    @classmethod
    def add_answer(cls, answer: AnswerModel) -> str:
        """Save answer on db."""
        return cls.answer_repository.create_answer(answer)
