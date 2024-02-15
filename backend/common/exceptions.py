class EntityNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name
        self.message = f"Entity {self.name} is not found!"
        super().__init__(self.message)
