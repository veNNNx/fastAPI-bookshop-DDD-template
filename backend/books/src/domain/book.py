from typing import Optional

from attrs import define


@define
class Book:
    id: Optional[int]
    title: str
    author: str
