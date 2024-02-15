from __future__ import annotations

from dependency_injector import containers, providers

from .books import BooksService


class ApplicationContainer(containers.DeclarativeContainer):
    books_service = providers.Factory(BooksService)
