from enum import Enum


class GetExternalTasksSortBy(str, Enum):
    ID = "id"
    LOCKEXPIRATIONTIME = "lockExpirationTime"
    PROCESSINSTANCEID = "processInstanceId"
    PROCESSDEFINITIONID = "processDefinitionId"
    PROCESSDEFINITIONKEY = "processDefinitionKey"
    TASKPRIORITY = "taskPriority"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
