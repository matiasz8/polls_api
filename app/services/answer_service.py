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

    @classmethod
    def delete_answers(cls):
        """Delete answers on db."""
        return cls.answer_repository.delete_answers()

    @classmethod
    def delete_answer_by_id(cls, answer_id: str):
        """Delete answers on db."""
        return cls.answer_repository.delete_answer_by_id(answer_id)
