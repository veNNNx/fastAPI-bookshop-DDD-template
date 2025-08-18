import re

from attrs import Attribute, define, field

from .exceptions import InvalidTitleException
from .validation_patterns import TITLE_REGEX


@define(kw_only=True)
class Book:
    id: int | None = field(default=None)
    title: str = field()
    author: str

    @classmethod
    @title.validator
    def _title_validation(cls, _attribute: Attribute, value: str) -> None:
        if not re.match(TITLE_REGEX, value):
            raise InvalidTitleException(value)
