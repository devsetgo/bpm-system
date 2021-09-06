from enum import Enum


class GroupQueryDtoSortingItemSortBy(str, Enum):
    ID = "id"
    NAME = "name"
    TYPE = "type"

    def __str__(self) -> str:
        return str(self.value)
