from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from backend.books import Book, BookService
from backend.ioc_container import ApplicationContainer

from .schema import BookBase

router = APIRouter(prefix="/books", tags=["Books"])


@router.post(
    "/",
    response_model=BookBase,
    status_code=status.HTTP_201_CREATED,
    summary="Create a book.",
)
@inject
def create(
    payload: BookBase,
    service: BookService = Depends(
        Provide[ApplicationContainer.books.container.books_service]
    ),
) -> Book:
    book = service.create(author=payload.author, title=payload.title)
    return book
