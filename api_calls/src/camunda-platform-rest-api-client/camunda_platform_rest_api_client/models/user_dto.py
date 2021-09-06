from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_credentials_dto import UserCredentialsDto
from ..models.user_profile_dto import UserProfileDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDto")


@attr.s(auto_attribs=True)
class UserDto:
    """ """

    profile: Union[Unset, UserProfileDto] = UNSET
    credentials: Union[Unset, UserCredentialsDto] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile is not UNSET:
            field_dict["profile"] = profile
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, UserProfileDto]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = UserProfileDto.from_dict(_profile)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, UserCredentialsDto]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = UserCredentialsDto.from_dict(_credentials)

        user_dto = cls(
            profile=profile,
            credentials=credentials,
        )

        user_dto.additional_properties = d
        return user_dto

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
