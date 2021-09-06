from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_profile_dto import UserProfileDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="PasswordPolicyRequestDto")


@attr.s(auto_attribs=True)
class PasswordPolicyRequestDto:
    """ """

    password: Union[Unset, None, str] = UNSET
    profile: Union[Unset, UserProfileDto] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password
        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if profile is not UNSET:
            field_dict["profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password", UNSET)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, UserProfileDto]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = UserProfileDto.from_dict(_profile)

        password_policy_request_dto = cls(
            password=password,
            profile=profile,
        )

        password_policy_request_dto.additional_properties = d
        return password_policy_request_dto

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
