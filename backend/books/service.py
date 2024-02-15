from attrs import define

from .domain import Book


@define
class BooksService:
    def create(self, author: str, title: str) -> Book:
        book = Book(uuid=Book.new_uuid(), author=author, title=title)
        return book

    def get_all(self) -> list[Book]:
        book = Book(uuid=Book.new_uuid(), author="author", title="title")
        book_2 = Book(uuid=Book.new_uuid(), author="author2", title="title2")
        return [book, book_2]
