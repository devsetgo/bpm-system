from enum import Enum


class GetHistoricProcessInstancesSortBy(str, Enum):
    INSTANCEID = "instanceId"
    DEFINITIONID = "definitionId"
    DEFINITIONKEY = "definitionKey"
    DEFINITIONNAME = "definitionName"
    DEFINITIONVERSION = "definitionVersion"
    BUSINESSKEY = "businessKey"
    STARTTIME = "startTime"
    ENDTIME = "endTime"
    DURATION = "duration"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
