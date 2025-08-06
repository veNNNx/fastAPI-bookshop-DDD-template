import logging

from attrs import define, field

from ..domain.book import Book
from ..infrastructure.book_repository import BookTable


@define
class BookService:
    logger: logging.Logger = field(init=False)
    _book_tabels: BookTable

    def __attrs_post_init__(self) -> None:
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )

    def create(self, author: str, title: str) -> Book:
        book = Book(id=None, author=author, title=title)
        self.logger.debug("Adding new book with title: %s", title)

        return self._book_tabels.create_and_save(book)

    def get_by_id(self, id: int) -> Book:
        return self._book_tabels.get_by_id(id)

    def get_all(self) -> list[Book]:
        return self._book_tabels.get_all()

    def delete_by_id(self, id: int) -> None:
        book = self._book_tabels.get_by_id(id)
        self.logger.debug("Delete the book with title: %s", book.title)
        self._book_tabels.delete_by_id(id)
