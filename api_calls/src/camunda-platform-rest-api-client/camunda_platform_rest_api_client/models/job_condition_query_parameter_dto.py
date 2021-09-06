import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.job_condition_query_parameter_dto_operator import JobConditionQueryParameterDtoOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobConditionQueryParameterDto")


@attr.s(auto_attribs=True)
class JobConditionQueryParameterDto:
    """ """

    operator: Union[Unset, None, JobConditionQueryParameterDtoOperator] = UNSET
    value: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operator: Union[Unset, None, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value if self.operator else None

        value: Union[Unset, None, str] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.isoformat() if self.value else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operator is not UNSET:
            field_dict["operator"] = operator
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, None, JobConditionQueryParameterDtoOperator]
        if _operator is None:
            operator = None
        elif isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = JobConditionQueryParameterDtoOperator(_operator)

        _value = d.pop("value", UNSET)
        value: Union[Unset, None, datetime.datetime]
        if _value is None:
            value = None
        elif isinstance(_value, Unset):
            value = UNSET
        else:
            value = isoparse(_value)

        job_condition_query_parameter_dto = cls(
            operator=operator,
            value=value,
        )

        job_condition_query_parameter_dto.additional_properties = d
        return job_condition_query_parameter_dto

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
