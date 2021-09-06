from enum import Enum


class GetTasksDelegationState(str, Enum):
    PENDING = "PENDING"
    RESOLVED = "RESOLVED"

    def __str__(self) -> str:
        return str(self.value)
