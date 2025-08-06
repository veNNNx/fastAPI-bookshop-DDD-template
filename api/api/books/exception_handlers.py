from fastapi import FastAPI, status

from backend.books import BookNotFoundException

from ..utils import register_exception_handler

EXCEPTION_STATUS_CODES = {
    BookNotFoundException: status.HTTP_404_NOT_FOUND,
}


def add_book_exception_handlers(app: FastAPI) -> None:
    for exc_class, status_code in EXCEPTION_STATUS_CODES.items():
        register_exception_handler(app, exc_class, status_code)
