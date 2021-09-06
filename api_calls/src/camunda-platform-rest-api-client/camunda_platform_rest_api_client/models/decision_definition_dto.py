from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DecisionDefinitionDto")


@attr.s(auto_attribs=True)
class DecisionDefinitionDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    key: Union[Unset, None, str] = UNSET
    category: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, int] = UNSET
    resource: Union[Unset, None, str] = UNSET
    deployment_id: Union[Unset, None, str] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    decision_requirements_definition_id: Union[Unset, None, str] = UNSET
    decision_requirements_definition_key: Union[Unset, None, str] = UNSET
    history_time_to_live: Union[Unset, None, int] = UNSET
    version_tag: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key = self.key
        category = self.category
        name = self.name
        version = self.version
        resource = self.resource
        deployment_id = self.deployment_id
        tenant_id = self.tenant_id
        decision_requirements_definition_id = self.decision_requirements_definition_id
        decision_requirements_definition_key = self.decision_requirements_definition_key
        history_time_to_live = self.history_time_to_live
        version_tag = self.version_tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if category is not UNSET:
            field_dict["category"] = category
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if resource is not UNSET:
            field_dict["resource"] = resource
        if deployment_id is not UNSET:
            field_dict["deploymentId"] = deployment_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if decision_requirements_definition_id is not UNSET:
            field_dict["decisionRequirementsDefinitionId"] = decision_requirements_definition_id
        if decision_requirements_definition_key is not UNSET:
            field_dict["decisionRequirementsDefinitionKey"] = decision_requirements_definition_key
        if history_time_to_live is not UNSET:
            field_dict["historyTimeToLive"] = history_time_to_live
        if version_tag is not UNSET:
            field_dict["versionTag"] = version_tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        category = d.pop("category", UNSET)

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        resource = d.pop("resource", UNSET)

        deployment_id = d.pop("deploymentId", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        decision_requirements_definition_id = d.pop("decisionRequirementsDefinitionId", UNSET)

        decision_requirements_definition_key = d.pop("decisionRequirementsDefinitionKey", UNSET)

        history_time_to_live = d.pop("historyTimeToLive", UNSET)

        version_tag = d.pop("versionTag", UNSET)

        decision_definition_dto = cls(
            id=id,
            key=key,
            category=category,
            name=name,
            version=version,
            resource=resource,
            deployment_id=deployment_id,
            tenant_id=tenant_id,
            decision_requirements_definition_id=decision_requirements_definition_id,
            decision_requirements_definition_key=decision_requirements_definition_key,
            history_time_to_live=history_time_to_live,
            version_tag=version_tag,
        )

        decision_definition_dto.additional_properties = d
        return decision_definition_dto

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
