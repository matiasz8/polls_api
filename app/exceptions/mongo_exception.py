from fastapi import status

from app.core.error_handler import HTTPCustomException


class MongoException(HTTPCustomException):
    DEFAULT_MESSAGE = "Mongo Exception"

    def __init__(self, message: str = DEFAULT_MESSAGE, **kwargs):
        msg = {'error': f'MongoException: {message}'}
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, msg=msg, **kwargs)
