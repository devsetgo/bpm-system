from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.missing_authorization_dto import MissingAuthorizationDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorizationExceptionDto")


@attr.s(auto_attribs=True)
class AuthorizationExceptionDto:
    """ """

    type: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    missing_authorizations: Union[Unset, None, List[MissingAuthorizationDto]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        message = self.message
        user_id = self.user_id
        missing_authorizations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.missing_authorizations, Unset):
            if self.missing_authorizations is None:
                missing_authorizations = None
            else:
                missing_authorizations = []
                for missing_authorizations_item_data in self.missing_authorizations:
                    missing_authorizations_item = missing_authorizations_item_data.to_dict()

                    missing_authorizations.append(missing_authorizations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if message is not UNSET:
            field_dict["message"] = message
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if missing_authorizations is not UNSET:
            field_dict["missingAuthorizations"] = missing_authorizations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        message = d.pop("message", UNSET)

        user_id = d.pop("userId", UNSET)

        missing_authorizations = []
        _missing_authorizations = d.pop("missingAuthorizations", UNSET)
        for missing_authorizations_item_data in _missing_authorizations or []:
            missing_authorizations_item = MissingAuthorizationDto.from_dict(missing_authorizations_item_data)

            missing_authorizations.append(missing_authorizations_item)

        authorization_exception_dto = cls(
            type=type,
            message=message,
            user_id=user_id,
            missing_authorizations=missing_authorizations,
        )

        authorization_exception_dto.additional_properties = d
        return authorization_exception_dto

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
