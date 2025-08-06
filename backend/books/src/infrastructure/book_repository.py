from attrs import define
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from backend.common import Base, Tables

from ..domain.book import Book
from .exceptions import BookNotFoundException


class BookModel(Base):
    __tablename__ = Tables.BOOKS_TABLE

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    title = Column(String, index=True)
    author = Column(String)


# mypy: disable-error-code=arg-type


@define
class BookTable:
    _session: sessionmaker

    def create_and_save(self, book: Book) -> Book:
        book_model = BookModel(
            title=book.title,
            author=book.author,
        )
        with self._session() as db:
            db.add(book_model)
            db.commit()
            db.refresh(book_model)

        return Book(
            id=book_model.id,
            title=book_model.title,
            author=book_model.author,
        )

    def get_by_id(self, book_id: int) -> Book:
        with self._session() as db:
            book_model = db.query(BookModel).filter(BookModel.id == book_id).first()
            if not book_model:
                raise BookNotFoundException(book_id)

            return Book(
                id=book_model.id,
                title=book_model.title,
                author=book_model.author,
            )

    def get_all(self) -> list[Book]:
        with self._session() as db:
            book_models = db.query(BookModel).all()
            return [
                Book(
                    id=book_model.id,
                    title=book_model.title,
                    author=book_model.author,
                )
                for book_model in book_models
            ]

    def delete_by_id(self, id: int) -> None:
        with self._session() as db:
            book_model = db.query(BookModel).filter(BookModel.id == id).first()

            if not book_model:
                raise BookNotFoundException(id)

            db.delete(book_model)
            db.commit()
