from enum import Enum


class GetHistoricActivityInstancesSortBy(str, Enum):
    ACTIVITYINSTANCEID = "activityInstanceId"
    INSTANCEID = "instanceId"
    EXECUTIONID = "executionId"
    ACTIVITYID = "activityId"
    ACTIVITYNAME = "activityName"
    ACTIVITYTYPE = "activityType"
    STARTTIME = "startTime"
    ENDTIME = "endTime"
    DURATION = "duration"
    DEFINITIONID = "definitionId"
    OCCURRENCE = "occurrence"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
