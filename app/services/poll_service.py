import logging

from pydantic import ValidationError

logger = logging.getLogger(__name__)


class PollService:
    """Service who handle Poll data."""

    @classmethod
    def add_poll(cls, payload: dict) -> str:
        """Save poll on db."""
        ...
