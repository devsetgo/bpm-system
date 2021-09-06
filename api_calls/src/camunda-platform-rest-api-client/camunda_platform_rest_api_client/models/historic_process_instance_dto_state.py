from enum import Enum


class HistoricProcessInstanceDtoState(str, Enum):
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    COMPLETED = "COMPLETED"
    EXTERNALLY_TERMINATED = "EXTERNALLY_TERMINATED"
    INTERNALLY_TERMINATED = "INTERNALLY_TERMINATED"

    def __str__(self) -> str:
        return str(self.value)
