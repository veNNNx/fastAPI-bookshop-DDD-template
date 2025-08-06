import logging.config

from dependency_injector import containers, providers

from backend.common import LOGGING_CONFIG, SessionLocal

from .books.ioc_containers import BooksContainer


class ApplicationContainer(containers.DeclarativeContainer):
    __self__ = providers.Self()
    logging = providers.Resource(logging.config.dictConfig, LOGGING_CONFIG)
    session_factory = providers.Singleton(lambda: SessionLocal)
    books = providers.Container(
        BooksContainer,
        session_factory=session_factory,
    )
