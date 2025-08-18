from .validation_patterns import TITLE_REGEX


class InvalidTitleException(Exception):
    def __init__(self, title: str):
        message = f"Book with given {title=} has invalid title!"
        message += rf"Allowed title must match the pattern: '{TITLE_REGEX}'"

        super().__init__(message)
