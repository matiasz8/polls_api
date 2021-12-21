
import pytest
from unittest import mock

from app.tests.test_base import BaseController
from app.tests.factories.poll_factory import (
    PollListFactory, AnswerFactory, AnswerResponseFactory, PollFactory)


class TestPollController(BaseController):
    poll_controller = "v1/poll"

    def test_get_polls(self, test_client, mocker):
        polls = PollListFactory.create(_id="asdasdasdasdasdasd")
        mocker.patch(
            "app.repository.poll_repository.PollRepository.all_polls",
            return_value=polls
        )
        response = test_client.get(self.poll_controller + "/get")
        data = response.json()
        assert response.status_code == 201
        assert data["question"] == polls.question
        assert data["created_date"] == polls.created_date.isoformat()
