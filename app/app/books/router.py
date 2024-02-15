from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from backend.books import Book
from backend.books.service import BooksService
from backend.ioc_container import ApplicationContainer

from .schema import BookBase, BookOut

router = APIRouter(prefix="/books", tags=["Books"])


@router.post(
    "/",
    response_model=BookOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create a book.",
)
@inject
def create(
    payload: BookBase,
    service: BooksService = Depends(Provide[ApplicationContainer.books_service]),
) -> Book:
    book = service.create(author=payload.author, title=payload.title)
    return book
