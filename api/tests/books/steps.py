from attr import define
from fastapi.testclient import TestClient
from httpx import Response


@define
class Steps:
    _client: TestClient

    def create_book(self, title: str = "title", author: str = "author") -> Response:
        return self._client.post("/books", json={"title": title, "author": author})

    def get_all(self) -> Response:
        return self._client.get("/books")

    def get_by_id(self, id: int) -> Response:
        return self._client.get(f"/books/{id}")

    def delete_by_id(self, id: int) -> Response:
        return self._client.delete(f"/books/{id}")
