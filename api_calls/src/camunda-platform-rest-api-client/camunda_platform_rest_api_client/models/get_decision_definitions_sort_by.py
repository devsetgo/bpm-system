from enum import Enum


class GetDecisionDefinitionsSortBy(str, Enum):
    CATEGORY = "category"
    DECISIONREQUIREMENTSDEFINITIONKEY = "decisionRequirementsDefinitionKey"
    KEY = "key"
    ID = "id"
    NAME = "name"
    VERSION = "version"
    DEPLOYMENTID = "deploymentId"
    DEPLOYTIME = "deployTime"
    VERSIONTAG = "versionTag"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
