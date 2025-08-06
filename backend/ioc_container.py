import logging.config

from dependency_injector import containers, providers

from backend.books.ioc_containers import BooksContainer
from backend.common import LOGGING_CONFIG


class ApplicationContainer(containers.DeclarativeContainer):
    __self__ = providers.Self()
    logging = providers.Resource(logging.config.dictConfig, LOGGING_CONFIG)
    books = providers.Container(BooksContainer)
