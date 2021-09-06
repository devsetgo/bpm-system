from enum import Enum


class GetBatchStatisticsSortBy(str, Enum):
    BATCHID = "batchId"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
