from enum import Enum


class GetProcessDefinitionsSortBy(str, Enum):
    CATEGORY = "category"
    KEY = "key"
    ID = "id"
    NAME = "name"
    VERSION = "version"
    DEPLOYMENTID = "deploymentId"
    DEPLOYTIME = "deployTime"
    TENANTID = "tenantId "
    VERSIONTAG = "versionTag"

    def __str__(self) -> str:
        return str(self.value)
