from enum import Enum


class SchemaLogQueryDtoSortingItemSortBy(str, Enum):
    TIMESTAMP = "timestamp"

    def __str__(self) -> str:
        return str(self.value)
