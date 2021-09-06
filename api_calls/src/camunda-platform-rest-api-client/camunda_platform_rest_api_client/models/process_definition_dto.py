from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessDefinitionDto")


@attr.s(auto_attribs=True)
class ProcessDefinitionDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    key: Union[Unset, None, str] = UNSET
    category: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, int] = UNSET
    resource: Union[Unset, None, str] = UNSET
    deployment_id: Union[Unset, None, str] = UNSET
    diagram: Union[Unset, None, str] = UNSET
    suspended: Union[Unset, None, bool] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    version_tag: Union[Unset, None, str] = UNSET
    history_time_to_live: Union[Unset, None, int] = UNSET
    startable_in_tasklist: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key = self.key
        category = self.category
        description = self.description
        name = self.name
        version = self.version
        resource = self.resource
        deployment_id = self.deployment_id
        diagram = self.diagram
        suspended = self.suspended
        tenant_id = self.tenant_id
        version_tag = self.version_tag
        history_time_to_live = self.history_time_to_live
        startable_in_tasklist = self.startable_in_tasklist

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if resource is not UNSET:
            field_dict["resource"] = resource
        if deployment_id is not UNSET:
            field_dict["deploymentId"] = deployment_id
        if diagram is not UNSET:
            field_dict["diagram"] = diagram
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if version_tag is not UNSET:
            field_dict["versionTag"] = version_tag
        if history_time_to_live is not UNSET:
            field_dict["historyTimeToLive"] = history_time_to_live
        if startable_in_tasklist is not UNSET:
            field_dict["startableInTasklist"] = startable_in_tasklist

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        category = d.pop("category", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        resource = d.pop("resource", UNSET)

        deployment_id = d.pop("deploymentId", UNSET)

        diagram = d.pop("diagram", UNSET)

        suspended = d.pop("suspended", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        version_tag = d.pop("versionTag", UNSET)

        history_time_to_live = d.pop("historyTimeToLive", UNSET)

        startable_in_tasklist = d.pop("startableInTasklist", UNSET)

        process_definition_dto = cls(
            id=id,
            key=key,
            category=category,
            description=description,
            name=name,
            version=version,
            resource=resource,
            deployment_id=deployment_id,
            diagram=diagram,
            suspended=suspended,
            tenant_id=tenant_id,
            version_tag=version_tag,
            history_time_to_live=history_time_to_live,
            startable_in_tasklist=startable_in_tasklist,
        )

        process_definition_dto.additional_properties = d
        return process_definition_dto

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
