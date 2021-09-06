from enum import Enum


class GetTasksCountDelegationState(str, Enum):
    PENDING = "PENDING"
    RESOLVED = "RESOLVED"

    def __str__(self) -> str:
        return str(self.value)
