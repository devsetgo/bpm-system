from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MissingAuthorizationDto")


@attr.s(auto_attribs=True)
class MissingAuthorizationDto:
    """ """

    permission_name: Union[Unset, None, str] = UNSET
    resource_name: Union[Unset, None, str] = UNSET
    resource_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permission_name = self.permission_name
        resource_name = self.resource_name
        resource_id = self.resource_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission_name is not UNSET:
            field_dict["permissionName"] = permission_name
        if resource_name is not UNSET:
            field_dict["resourceName"] = resource_name
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        permission_name = d.pop("permissionName", UNSET)

        resource_name = d.pop("resourceName", UNSET)

        resource_id = d.pop("resourceId", UNSET)

        missing_authorization_dto = cls(
            permission_name=permission_name,
            resource_name=resource_name,
            resource_id=resource_id,
        )

        missing_authorization_dto.additional_properties = d
        return missing_authorization_dto

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
