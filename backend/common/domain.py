from uuid import UUID, uuid4

from attr import define


@define
class Entity:
    uuid: UUID

    @staticmethod
    def new_uuid():
        return uuid4()
