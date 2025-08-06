from assertpy import assert_that
from fastapi import status

from .steps import Steps


class TestBook:
    def test_get_all_books(self, steps: Steps) -> None:
        response = steps.get_all()
        assert_that(response.status_code).is_equal_to(status.HTTP_200_OK)

        assert_that(response.json()).is_empty()

    def test_get_book_by_id(self, steps: Steps) -> None:
        response_create = steps.create_book()
        id = response_create.json()["id"]
        response = steps.get_by_id(id)

        data = response.json()
        assert_that(response.status_code).is_equal_to(status.HTTP_200_OK)
        assert_that(data["id"]).is_equal_to(1)
        assert_that(data["author"]).is_equal_to("author")
        assert_that(data["title"]).is_equal_to("title")

    def test_get_book_by_id_fails_on_invalid_id(self, steps: Steps) -> None:
        book_id = 99
        response = steps.get_by_id(book_id)

        assert_that(response.status_code).is_equal_to(status.HTTP_404_NOT_FOUND)
        assert_that(response.json()["message"]).is_equal_to(
            f"No book with id={book_id} exists in the store!"
        )

    def test_create_one_book(self, steps: Steps) -> None:
        author = "John"
        title = "Penguin"

        response = steps.create_book(author=author, title=title)

        data = response.json()
        assert_that(response.status_code).is_equal_to(status.HTTP_201_CREATED)
        assert_that(data["id"]).is_equal_to(1)
        assert_that(data["author"]).is_equal_to(author)
        assert_that(data["title"]).is_equal_to(title)

    def test_delete_book_by_id(self, steps: Steps) -> None:
        response_create = steps.create_book()
        id = response_create.json()["id"]
        response = steps.delete_by_id(id)

        assert_that(response.status_code).is_equal_to(status.HTTP_204_NO_CONTENT)

    def test_delete_book_by_id_fails_on_invalid_id(self, steps: Steps) -> None:
        book_id = 99
        response = steps.delete_by_id(book_id)

        assert_that(response.status_code).is_equal_to(status.HTTP_404_NOT_FOUND)
        assert_that(response.json()["message"]).is_equal_to(
            f"No book with id={book_id} exists in the store!"
        )
