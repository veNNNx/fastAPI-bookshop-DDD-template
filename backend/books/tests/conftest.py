import pytest

from backend.ioc_container import ApplicationContainer

from ..src.application.book_service import BookService


@pytest.fixture
def book_service(test_app_container: ApplicationContainer) -> BookService:
    return test_app_container.books().book_service()


@pytest.fixture
def create_book(book_service: BookService):
    book_service.create(author="author", title="title")
