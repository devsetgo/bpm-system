from enum import Enum


class GetJobsSortBy(str, Enum):
    JOBID = "jobId"
    EXECUTIONID = "executionId"
    PROCESSINSTANCEID = "processInstanceId"
    PROCESSDEFINITIONID = "processDefinitionId"
    PROCESSDEFINITIONKEY = "processDefinitionKey"
    JOBPRIORITY = "jobPriority"
    JOBRETRIES = "jobRetries"
    JOBDUEDATE = "jobDueDate"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
