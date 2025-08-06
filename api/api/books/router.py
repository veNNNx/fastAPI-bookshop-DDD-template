from typing import Annotated

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
    book_service: Annotated[
        BookService,
        Depends(Provide[ApplicationContainer.books.container.book_service]),
    ],
) -> Book:
    return book_service.create(author=payload.author, title=payload.title)


@router.get(
    "/{book_id}",
    response_model=BookBase,
    status_code=status.HTTP_200_OK,
    summary="Get a book by id.",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Requested book does not exist."},
    },
)
@inject
def get_by_id(
    book_id: int,
    book_service: Annotated[
        BookService,
        Depends(Provide[ApplicationContainer.books.container.book_service]),
    ],
) -> Book:
    return book_service.get_by_id(book_id)


@router.get(
    "/",
    response_model=list[BookBase],
    status_code=status.HTTP_200_OK,
    summary="Get all books.",
)
@inject
def get_all(
    book_service: Annotated[
        BookService,
        Depends(Provide[ApplicationContainer.books.container.book_service]),
    ],
) -> list[Book]:
    return book_service.get_all()


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete the book by id.",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Requested book does not exist."},
    },
)
@inject
def delete_by_id(
    book_id: int,
    book_service: Annotated[
        BookService,
        Depends(Provide[ApplicationContainer.books.container.book_service]),
    ],
) -> None:
    book_service.delete_by_id(book_id)
