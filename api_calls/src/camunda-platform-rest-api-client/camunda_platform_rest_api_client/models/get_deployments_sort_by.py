from enum import Enum


class GetDeploymentsSortBy(str, Enum):
    ID = "id"
    NAME = "name"
    DEPLOYMENTTIME = "deploymentTime"
    TENANTID = "tenantId"

    def __str__(self) -> str:
        return str(self.value)
