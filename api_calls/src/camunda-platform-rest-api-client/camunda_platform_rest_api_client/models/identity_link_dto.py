from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityLinkDto")


@attr.s(auto_attribs=True)
class IdentityLinkDto:
    """ """

    type: Optional[str]
    user_id: Union[Unset, None, str] = UNSET
    group_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        group_id = self.group_id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId", UNSET)

        group_id = d.pop("groupId", UNSET)

        type = d.pop("type")

        identity_link_dto = cls(
            user_id=user_id,
            group_id=group_id,
            type=type,
        )

        identity_link_dto.additional_properties = d
        return identity_link_dto

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
