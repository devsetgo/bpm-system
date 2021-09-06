from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.variable_value_dto_value import VariableValueDtoValue
from ..models.variable_value_dto_value_info import VariableValueDtoValueInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="VariableValueDto")


@attr.s(auto_attribs=True)
class VariableValueDto:
    """ """

    value: Union[Unset, VariableValueDtoValue] = UNSET
    type: Union[Unset, None, str] = UNSET
    value_info: Union[Unset, VariableValueDtoValueInfo] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        type = self.type
        value_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value_info, Unset):
            value_info = self.value_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if type is not UNSET:
            field_dict["type"] = type
        if value_info is not UNSET:
            field_dict["valueInfo"] = value_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _value = d.pop("value", UNSET)
        value: Union[Unset, VariableValueDtoValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = VariableValueDtoValue.from_dict(_value)

        type = d.pop("type", UNSET)

        _value_info = d.pop("valueInfo", UNSET)
        value_info: Union[Unset, VariableValueDtoValueInfo]
        if isinstance(_value_info, Unset):
            value_info = UNSET
        else:
            value_info = VariableValueDtoValueInfo.from_dict(_value_info)

        variable_value_dto = cls(
            value=value,
            type=type,
            value_info=value_info,
        )

        variable_value_dto.additional_properties = d
        return variable_value_dto

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
