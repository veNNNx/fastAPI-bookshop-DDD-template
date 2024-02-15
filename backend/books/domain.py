from attrs import define

from app.app.books.schema import BookOut
from backend.common import Entity


@define
class Book(Entity):
    title: str
    author: str

    def to_dto(self) -> BookOut:
        return BookOut(uuid=self.uuid, title=self.title, author=self.author)
