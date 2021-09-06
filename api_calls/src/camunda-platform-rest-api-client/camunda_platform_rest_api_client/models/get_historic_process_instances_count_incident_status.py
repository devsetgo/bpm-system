from enum import Enum


class GetHistoricProcessInstancesCountIncidentStatus(str, Enum):
    OPEN = "open"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
