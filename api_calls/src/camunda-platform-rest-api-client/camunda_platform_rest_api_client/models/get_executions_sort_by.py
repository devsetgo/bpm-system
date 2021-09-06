from enum import Enum


class GetExecutionsSortBy(str, Enum):
    INSTANCEID = "instanceId"
    DEFINITIONKEY = "definitionKey"
    DEFINITIONID = "definitionId"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
