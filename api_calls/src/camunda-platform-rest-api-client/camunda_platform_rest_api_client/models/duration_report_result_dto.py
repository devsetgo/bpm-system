from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.duration_report_result_dto_period_unit import DurationReportResultDtoPeriodUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="DurationReportResultDto")


@attr.s(auto_attribs=True)
class DurationReportResultDto:
    """ """

    period: Union[Unset, None, int] = UNSET
    period_unit: Union[Unset, None, DurationReportResultDtoPeriodUnit] = UNSET
    minimum: Union[Unset, None, int] = UNSET
    maximum: Union[Unset, None, int] = UNSET
    average: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period
        period_unit: Union[Unset, None, str] = UNSET
        if not isinstance(self.period_unit, Unset):
            period_unit = self.period_unit.value if self.period_unit else None

        minimum = self.minimum
        maximum = self.maximum
        average = self.average

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if period_unit is not UNSET:
            field_dict["periodUnit"] = period_unit
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if average is not UNSET:
            field_dict["average"] = average

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        period = d.pop("period", UNSET)

        _period_unit = d.pop("periodUnit", UNSET)
        period_unit: Union[Unset, None, DurationReportResultDtoPeriodUnit]
        if _period_unit is None:
            period_unit = None
        elif isinstance(_period_unit, Unset):
            period_unit = UNSET
        else:
            period_unit = DurationReportResultDtoPeriodUnit(_period_unit)

        minimum = d.pop("minimum", UNSET)

        maximum = d.pop("maximum", UNSET)

        average = d.pop("average", UNSET)

        duration_report_result_dto = cls(
            period=period,
            period_unit=period_unit,
            minimum=minimum,
            maximum=maximum,
            average=average,
        )

        duration_report_result_dto.additional_properties = d
        return duration_report_result_dto

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
