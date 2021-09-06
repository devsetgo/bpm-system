from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.identity_service_group_dto import IdentityServiceGroupDto
from ..models.identity_service_user_dto import IdentityServiceUserDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityServiceGroupInfoDto")


@attr.s(auto_attribs=True)
class IdentityServiceGroupInfoDto:
    """ """

    groups: Union[Unset, None, List[IdentityServiceGroupDto]] = UNSET
    group_users: Union[Unset, None, List[IdentityServiceUserDto]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        groups: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            if self.groups is None:
                groups = None
            else:
                groups = []
                for groups_item_data in self.groups:
                    groups_item = groups_item_data.to_dict()

                    groups.append(groups_item)

        group_users: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.group_users, Unset):
            if self.group_users is None:
                group_users = None
            else:
                group_users = []
                for group_users_item_data in self.group_users:
                    group_users_item = group_users_item_data.to_dict()

                    group_users.append(group_users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if group_users is not UNSET:
            field_dict["groupUsers"] = group_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = IdentityServiceGroupDto.from_dict(groups_item_data)

            groups.append(groups_item)

        group_users = []
        _group_users = d.pop("groupUsers", UNSET)
        for group_users_item_data in _group_users or []:
            group_users_item = IdentityServiceUserDto.from_dict(group_users_item_data)

            group_users.append(group_users_item)

        identity_service_group_info_dto = cls(
            groups=groups,
            group_users=group_users,
        )

        identity_service_group_info_dto.additional_properties = d
        return identity_service_group_info_dto

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
