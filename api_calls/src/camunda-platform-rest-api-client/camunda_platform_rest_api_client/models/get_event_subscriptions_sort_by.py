from enum import Enum


class GetEventSubscriptionsSortBy(str, Enum):
    CREATED = "created"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
