from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from backend.common import Base, database, engine
from backend.ioc_container import ApplicationContainer

from .books.exception_handlers import add_book_exception_handlers
from .books.router import router as router_books

application = ApplicationContainer()
application.init_resources()
application.wire(packages=["api"])


@asynccontextmanager
async def lifespan(_fast_api_app: FastAPI) -> AsyncIterator[None]:
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(
    version="0.0.1",
    title="WebAPI",
    lifespan=lifespan,
)
app.state.container = application

Base.metadata.create_all(engine)


# routers
app.include_router(router_books)

# exception handlers
add_book_exception_handlers(app)
