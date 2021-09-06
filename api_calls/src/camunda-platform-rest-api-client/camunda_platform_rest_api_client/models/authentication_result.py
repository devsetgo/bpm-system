from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationResult")


@attr.s(auto_attribs=True)
class AuthenticationResult:
    """ """

    authenticated_user: Union[Unset, None, str] = UNSET
    is_authenticated: Union[Unset, None, bool] = UNSET
    tenants: Union[Unset, None, List[str]] = UNSET
    groups: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authenticated_user = self.authenticated_user
        is_authenticated = self.is_authenticated
        tenants: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tenants, Unset):
            if self.tenants is None:
                tenants = None
            else:
                tenants = self.tenants

        groups: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.groups, Unset):
            if self.groups is None:
                groups = None
            else:
                groups = self.groups

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authenticated_user is not UNSET:
            field_dict["authenticatedUser"] = authenticated_user
        if is_authenticated is not UNSET:
            field_dict["isAuthenticated"] = is_authenticated
        if tenants is not UNSET:
            field_dict["tenants"] = tenants
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authenticated_user = d.pop("authenticatedUser", UNSET)

        is_authenticated = d.pop("isAuthenticated", UNSET)

        tenants = cast(List[str], d.pop("tenants", UNSET))

        groups = cast(List[str], d.pop("groups", UNSET))

        authentication_result = cls(
            authenticated_user=authenticated_user,
            is_authenticated=is_authenticated,
            tenants=tenants,
            groups=groups,
        )

        authentication_result.additional_properties = d
        return authentication_result

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
