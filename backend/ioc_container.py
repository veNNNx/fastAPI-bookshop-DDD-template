from dependency_injector import containers, providers

from backend.books.service import BooksService


class ApplicationContainer(containers.DeclarativeContainer):
    books_service = providers.Factory(BooksService)
