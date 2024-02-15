from .steps import Steps


class TestBooksCreate:
    def test_create_book(self, steps: Steps) -> None:
        response = steps.create_book()
        assert response.status_code == 201
