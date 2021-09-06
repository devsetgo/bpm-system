from enum import Enum


class GetProcessInstancesSortBy(str, Enum):
    INSTANCEID = "instanceId"
    DEFINITIONKEY = "definitionKey"
    DEFINITIONID = "definitionId"
    TENANTID = "tenantId"
    BUSINESSKEY = "businessKey"

    def __str__(self) -> str:
        return str(self.value)
