class BookNotFoundException(Exception):
    def __init__(self, id: int):
        message = f"No book with {id=} exists in the store!"

        super().__init__(message)
