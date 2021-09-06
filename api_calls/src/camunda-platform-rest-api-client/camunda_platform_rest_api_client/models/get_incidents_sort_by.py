from enum import Enum


class GetIncidentsSortBy(str, Enum):
    INCIDENTID = "incidentId"
    INCIDENTMESSAGE = "incidentMessage"
    INCIDENTTIMESTAMP = "incidentTimestamp"
    INCIDENTTYPE = "incidentType"
    EXECUTIONID = "executionId"
    ACTIVITYID = "activityId"
    PROCESSINSTANCEID = "processInstanceId"
    PROCESSDEFINITIONID = "processDefinitionId"
    CAUSEINCIDENTID = "causeIncidentId"
    ROOTCAUSEINCIDENTID = "rootCauseIncidentId"
    CONFIGURATION = "configuration"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
