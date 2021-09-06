from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaseDefinitionDto")


@attr.s(auto_attribs=True)
class CaseDefinitionDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    key: Union[Unset, None, str] = UNSET
    category: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, int] = UNSET
    resource: Union[Unset, None, str] = UNSET
    deployment_id: Union[Unset, None, str] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    history_time_to_live: Union[Unset, None, int] = UNSET
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
        history_time_to_live = self.history_time_to_live

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
        if history_time_to_live is not UNSET:
            field_dict["historyTimeToLive"] = history_time_to_live

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

        history_time_to_live = d.pop("historyTimeToLive", UNSET)

        case_definition_dto = cls(
            id=id,
            key=key,
            category=category,
            name=name,
            version=version,
            resource=resource,
            deployment_id=deployment_id,
            tenant_id=tenant_id,
            history_time_to_live=history_time_to_live,
        )

        case_definition_dto.additional_properties = d
        return case_definition_dto

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
