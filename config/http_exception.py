from fastapi import HTTPException


def HttpException(message: any, code: int):
    return HTTPException(detail=message, status_code=code)