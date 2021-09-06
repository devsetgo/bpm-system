from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentResourceDto")


@attr.s(auto_attribs=True)
class DeploymentResourceDto:
    """A JSON object corresponding to the `Resource` interface in the engine.
    Its properties are as follows:"""

    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    deployment_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        deployment_id = self.deployment_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if deployment_id is not UNSET:
            field_dict["deploymentId"] = deployment_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        deployment_id = d.pop("deploymentId", UNSET)

        deployment_resource_dto = cls(
            id=id,
            name=name,
            deployment_id=deployment_id,
        )

        deployment_resource_dto.additional_properties = d
        return deployment_resource_dto

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
