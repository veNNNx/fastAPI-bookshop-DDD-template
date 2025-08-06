from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
