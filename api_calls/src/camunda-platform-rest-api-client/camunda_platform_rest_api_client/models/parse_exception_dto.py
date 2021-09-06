from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.parse_exception_dto_details import ParseExceptionDtoDetails
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParseExceptionDto")


@attr.s(auto_attribs=True)
class ParseExceptionDto:
    """ """

    type: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    details: Union[Unset, None, ParseExceptionDtoDetails] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        message = self.message
        details: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict() if self.details else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if message is not UNSET:
            field_dict["message"] = message
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        message = d.pop("message", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, None, ParseExceptionDtoDetails]
        if _details is None:
            details = None
        elif isinstance(_details, Unset):
            details = UNSET
        else:
            details = ParseExceptionDtoDetails.from_dict(_details)

        parse_exception_dto = cls(
            type=type,
            message=message,
            details=details,
        )

        parse_exception_dto.additional_properties = d
        return parse_exception_dto

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
