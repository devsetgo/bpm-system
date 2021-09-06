from enum import Enum


class GetVariableInstancesSortBy(str, Enum):
    VARIABLENAME = "variableName"
    VARIABLETYPE = "variableType"
    ACTIVITYINSTANCEID = "activityInstanceId"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
