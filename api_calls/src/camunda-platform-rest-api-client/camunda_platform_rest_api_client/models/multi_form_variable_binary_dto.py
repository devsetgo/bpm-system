from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.multi_form_variable_binary_dto_value_type import MultiFormVariableBinaryDtoValueType
from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="MultiFormVariableBinaryDto")


@attr.s(auto_attribs=True)
class MultiFormVariableBinaryDto:
    """ """

    data: Union[Unset, None, File] = UNSET
    value_type: Union[Unset, None, MultiFormVariableBinaryDtoValueType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_tuple() if self.data else None

        value_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = self.value_type.value if self.value_type else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if value_type is not UNSET:
            field_dict["valueType"] = value_type

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        data: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_tuple() if self.data else None

        value_type: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = (None, str(self.value_type.value), "text/plain") if self.value_type else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({key: (None, str(value), "text/plain") for key, value in self.additional_properties.items()})
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if value_type is not UNSET:
            field_dict["valueType"] = value_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, None, File]
        if _data is None:
            data = None
        elif isinstance(_data, Unset):
            data = UNSET
        else:
            data = File(payload=BytesIO(_data))

        _value_type = d.pop("valueType", UNSET)
        value_type: Union[Unset, None, MultiFormVariableBinaryDtoValueType]
        if _value_type is None:
            value_type = None
        elif isinstance(_value_type, Unset):
            value_type = UNSET
        else:
            value_type = MultiFormVariableBinaryDtoValueType(_value_type)

        multi_form_variable_binary_dto = cls(
            data=data,
            value_type=value_type,
        )

        multi_form_variable_binary_dto.additional_properties = d
        return multi_form_variable_binary_dto

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
