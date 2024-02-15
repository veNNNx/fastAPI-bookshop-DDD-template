from uuid import UUID

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str


class BookOut(BookBase):
    uuid: UUID
