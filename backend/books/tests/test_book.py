import pytest
from assertpy import assert_that

from ..src.application.book_service import BookService
from ..src.infrastructure.exceptions import BookNotFoundException


class TestBook:
    def test_book_get_all(self, book_service: BookService) -> None:
        books = book_service.get_all()
        assert_that(books).is_empty()

    def test_book_create(self, book_service: BookService) -> None:
        author = "author"
        title = "title"

        book = book_service.create(author=author, title=title)

        assert_that(book.author).is_equal_to(author)
        assert_that(book.title).is_equal_to(title)

    @pytest.mark.usefixtures("create_book")
    def test_get_book_by_id(self, book_service: BookService) -> None:
        book = book_service.get_by_id(id=1)
        assert_that(book.author).is_equal_to("author")
        assert_that(book.title).is_equal_to("title")

    def test_get_book_by_id_fails_on_invalid_id(
        self, book_service: BookService
    ) -> None:
        book_id = 99
        with pytest.raises(BookNotFoundException, match=str(book_id)):
            book_service.get_by_id(book_id)

    @pytest.mark.usefixtures("create_book")
    def test_delete_book_by_id(self, book_service: BookService) -> None:
        book_id = 1
        book_service.delete_by_id(book_id)
        with pytest.raises(BookNotFoundException, match=str(book_id)):
            book_service.delete_by_id(book_id)
