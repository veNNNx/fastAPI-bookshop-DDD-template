from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from backend.common import Base, database, engine
from backend.ioc_container import ApplicationContainer

from .books.exception_handlers import add_book_exception_handlers
from .books.router import router as router_books


@asynccontextmanager
async def lifespan(_fast_api_app: FastAPI) -> AsyncIterator[None]:
    await database.connect()
    yield
    await database.disconnect()


def create_app(container: ApplicationContainer) -> FastAPI:
    app = FastAPI(
        version="0.0.1",
        title="WebAPI",
        lifespan=lifespan,
    )
    app.state.container = container

    Base.metadata.create_all(engine)

    app.include_router(router_books)
    add_book_exception_handlers(app)

    return app
