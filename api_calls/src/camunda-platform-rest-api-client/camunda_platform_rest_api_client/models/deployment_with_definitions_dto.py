import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.atom_link import AtomLink
from ..models.deployment_with_definitions_dto_deployed_case_definitions import (
    DeploymentWithDefinitionsDtoDeployedCaseDefinitions,
)
from ..models.deployment_with_definitions_dto_deployed_decision_definitions import (
    DeploymentWithDefinitionsDtoDeployedDecisionDefinitions,
)
from ..models.deployment_with_definitions_dto_deployed_decision_requirements_definitions import (
    DeploymentWithDefinitionsDtoDeployedDecisionRequirementsDefinitions,
)
from ..models.deployment_with_definitions_dto_deployed_process_definitions import (
    DeploymentWithDefinitionsDtoDeployedProcessDefinitions,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentWithDefinitionsDto")


@attr.s(auto_attribs=True)
class DeploymentWithDefinitionsDto:
    """ """

    links: Union[Unset, None, List[AtomLink]] = UNSET
    id: Union[Unset, None, str] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    deployment_time: Union[Unset, None, datetime.datetime] = UNSET
    source: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    deployed_process_definitions: Union[Unset, None, DeploymentWithDefinitionsDtoDeployedProcessDefinitions] = UNSET
    deployed_decision_definitions: Union[Unset, None, DeploymentWithDefinitionsDtoDeployedDecisionDefinitions] = UNSET
    deployed_decision_requirements_definitions: Union[
        Unset, None, DeploymentWithDefinitionsDtoDeployedDecisionRequirementsDefinitions
    ] = UNSET
    deployed_case_definitions: Union[Unset, None, DeploymentWithDefinitionsDtoDeployedCaseDefinitions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

        id = self.id
        tenant_id = self.tenant_id
        deployment_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.deployment_time, Unset):
            deployment_time = self.deployment_time.isoformat() if self.deployment_time else None

        source = self.source
        name = self.name
        deployed_process_definitions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.deployed_process_definitions, Unset):
            deployed_process_definitions = (
                self.deployed_process_definitions.to_dict() if self.deployed_process_definitions else None
            )

        deployed_decision_definitions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.deployed_decision_definitions, Unset):
            deployed_decision_definitions = (
                self.deployed_decision_definitions.to_dict() if self.deployed_decision_definitions else None
            )

        deployed_decision_requirements_definitions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.deployed_decision_requirements_definitions, Unset):
            deployed_decision_requirements_definitions = (
                self.deployed_decision_requirements_definitions.to_dict()
                if self.deployed_decision_requirements_definitions
                else None
            )

        deployed_case_definitions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.deployed_case_definitions, Unset):
            deployed_case_definitions = (
                self.deployed_case_definitions.to_dict() if self.deployed_case_definitions else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if id is not UNSET:
            field_dict["id"] = id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if deployment_time is not UNSET:
            field_dict["deploymentTime"] = deployment_time
        if source is not UNSET:
            field_dict["source"] = source
        if name is not UNSET:
            field_dict["name"] = name
        if deployed_process_definitions is not UNSET:
            field_dict["deployedProcessDefinitions"] = deployed_process_definitions
        if deployed_decision_definitions is not UNSET:
            field_dict["deployedDecisionDefinitions"] = deployed_decision_definitions
        if deployed_decision_requirements_definitions is not UNSET:
            field_dict["deployedDecisionRequirementsDefinitions"] = deployed_decision_requirements_definitions
        if deployed_case_definitions is not UNSET:
            field_dict["deployedCaseDefinitions"] = deployed_case_definitions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = AtomLink.from_dict(links_item_data)

            links.append(links_item)

        id = d.pop("id", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        _deployment_time = d.pop("deploymentTime", UNSET)
        deployment_time: Union[Unset, None, datetime.datetime]
        if _deployment_time is None:
            deployment_time = None
        elif isinstance(_deployment_time, Unset):
            deployment_time = UNSET
        else:
            deployment_time = isoparse(_deployment_time)

        source = d.pop("source", UNSET)

        name = d.pop("name", UNSET)

        _deployed_process_definitions = d.pop("deployedProcessDefinitions", UNSET)
        deployed_process_definitions: Union[Unset, None, DeploymentWithDefinitionsDtoDeployedProcessDefinitions]
        if _deployed_process_definitions is None:
            deployed_process_definitions = None
        elif isinstance(_deployed_process_definitions, Unset):
            deployed_process_definitions = UNSET
        else:
            deployed_process_definitions = DeploymentWithDefinitionsDtoDeployedProcessDefinitions.from_dict(
                _deployed_process_definitions
            )

        _deployed_decision_definitions = d.pop("deployedDecisionDefinitions", UNSET)
        deployed_decision_definitions: Union[Unset, None, DeploymentWithDefinitionsDtoDeployedDecisionDefinitions]
        if _deployed_decision_definitions is None:
            deployed_decision_definitions = None
        elif isinstance(_deployed_decision_definitions, Unset):
            deployed_decision_definitions = UNSET
        else:
            deployed_decision_definitions = DeploymentWithDefinitionsDtoDeployedDecisionDefinitions.from_dict(
                _deployed_decision_definitions
            )

        _deployed_decision_requirements_definitions = d.pop("deployedDecisionRequirementsDefinitions", UNSET)
        deployed_decision_requirements_definitions: Union[
            Unset, None, DeploymentWithDefinitionsDtoDeployedDecisionRequirementsDefinitions
        ]
        if _deployed_decision_requirements_definitions is None:
            deployed_decision_requirements_definitions = None
        elif isinstance(_deployed_decision_requirements_definitions, Unset):
            deployed_decision_requirements_definitions = UNSET
        else:
            deployed_decision_requirements_definitions = (
                DeploymentWithDefinitionsDtoDeployedDecisionRequirementsDefinitions.from_dict(
                    _deployed_decision_requirements_definitions
                )
            )

        _deployed_case_definitions = d.pop("deployedCaseDefinitions", UNSET)
        deployed_case_definitions: Union[Unset, None, DeploymentWithDefinitionsDtoDeployedCaseDefinitions]
        if _deployed_case_definitions is None:
            deployed_case_definitions = None
        elif isinstance(_deployed_case_definitions, Unset):
            deployed_case_definitions = UNSET
        else:
            deployed_case_definitions = DeploymentWithDefinitionsDtoDeployedCaseDefinitions.from_dict(
                _deployed_case_definitions
            )

        deployment_with_definitions_dto = cls(
            links=links,
            id=id,
            tenant_id=tenant_id,
            deployment_time=deployment_time,
            source=source,
            name=name,
            deployed_process_definitions=deployed_process_definitions,
            deployed_decision_definitions=deployed_decision_definitions,
            deployed_decision_requirements_definitions=deployed_decision_requirements_definitions,
            deployed_case_definitions=deployed_case_definitions,
        )

        deployment_with_definitions_dto.additional_properties = d
        return deployment_with_definitions_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
