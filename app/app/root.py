from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from backend.common import EntityNotFoundException
from backend.ioc_container import ApplicationContainer

from .books.router import router as router_books

application = ApplicationContainer()
application.init_resources()
application.wire(packages=["app"])
app = FastAPI()
app.state.container = application
app.include_router(router_books)


@app.exception_handler(EntityNotFoundException)
async def entity_not_found_exception(request: Request, exc: EntityNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": exc.message[0]},
    )
