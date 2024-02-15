from attr import define
from fastapi import Response
from fastapi.testclient import TestClient

from backend.books import BooksService


@define
class Steps:
    books_service: BooksService
    test_app: TestClient

    def create_book(self) -> Response:
        return self.test_app.post("/books/", json={"title": "str", "author": "str"})
