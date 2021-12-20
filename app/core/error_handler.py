from fastapi import status, Request, HTTPException
from fastapi.responses import JSONResponse


class HTTPCustomException(HTTPException):
    def __init__(self, status_code: int, msg: str, type_value: str = None):
        super().__init__(
            status_code=status_code,
            detail=self.create_detail(msg, type_value))

    @staticmethod
    def create_detail(msg: str, type_value: str = None):
        return {'detail': [{'msg': msg, 'type': type_value}]}


def exception_handler(_: Request, e: HTTPCustomException):
    return JSONResponse(status_code=e.status_code, content=e.detail)


def fatal_exception_handler(_: Request, e: Exception):
    detail = HTTPCustomException.create_detail(f"Internal Error Server:{e}")
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=detail)
