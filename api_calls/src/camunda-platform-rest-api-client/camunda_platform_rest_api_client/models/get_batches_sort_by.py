from enum import Enum


class GetBatchesSortBy(str, Enum):
    BATCHID = "batchId"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
