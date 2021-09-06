from enum import Enum


class GetTasksSortBy(str, Enum):
    INSTANCEID = "instanceId"
    CASEINSTANCEID = "caseInstanceId"
    DUEDATE = "dueDate"
    EXECUTIONID = "executionId"
    CASEEXECUTIONID = "caseExecutionId"
    ASSIGNEE = "assignee"
    CREATED = "created"
    DESCRIPTION = "description"
    ID = "id"
    NAME = "name"
    NAMECASEINSENSITIVE = "nameCaseInsensitive"
    PRIORITY = "priority"
    PROCESSVARIABLE = "processVariable"
    EXECUTIONVARIABLE = "executionVariable"
    TASKVARIABLE = "taskVariable"
    CASEEXECUTIONVARIABLE = "caseExecutionVariable"
    CASEINSTANCEVARIABLE = "caseInstanceVariable"

    def __str__(self) -> str:
        return str(self.value)
