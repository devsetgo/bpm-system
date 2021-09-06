from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SortTaskQueryParametersDto")


@attr.s(auto_attribs=True)
class SortTaskQueryParametersDto:
    """Mandatory when `sortBy` is one of the following values: `processVariable`, `executionVariable`,
    `taskVariable`, `caseExecutionVariable` or `caseInstanceVariable`. Must be a JSON object with the properties
    `variable` and `type` where `variable` is a variable name and `type` is the name of a variable value type."""

    variable: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        variable = self.variable
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variable is not UNSET:
            field_dict["variable"] = variable
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        variable = d.pop("variable", UNSET)

        type = d.pop("type", UNSET)

        sort_task_query_parameters_dto = cls(
            variable=variable,
            type=type,
        )

        sort_task_query_parameters_dto.additional_properties = d
        return sort_task_query_parameters_dto

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
