from dependency_injector import containers, providers
from sqlalchemy.orm import sessionmaker

from backend.common.postgres import SessionLocal

from .src.application.book_service import BookService
from .src.infrastructure.book_repository import BookTable


def _get_session() -> sessionmaker:
    return SessionLocal


class BooksContainer(containers.DeclarativeContainer):
    book_tabel = providers.Factory(BookTable, session=providers.Callable(_get_session))
    book_service = providers.Factory(BookService, book_tabels=book_tabel)
