from enum import Enum


class EventSubscriptionQueryDtoSortingItemSortBy(str, Enum):
    CREATED = "created"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
