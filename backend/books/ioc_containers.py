from dependency_injector import containers, providers
from sqlalchemy.orm import sessionmaker

from .src.application.book_service import BookService
from .src.infrastructure.book_repository import BookTable


class BooksContainer(containers.DeclarativeContainer):
    session_factory = providers.Dependency(instance_of=sessionmaker)
    book_tabel = providers.Factory(BookTable, session=session_factory)
    book_service = providers.Factory(BookService, book_tabels=book_tabel)
