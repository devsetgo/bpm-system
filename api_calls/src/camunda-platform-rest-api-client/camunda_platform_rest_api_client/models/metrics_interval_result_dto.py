import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricsIntervalResultDto")


@attr.s(auto_attribs=True)
class MetricsIntervalResultDto:
    """ """

    timestamp: Union[Unset, None, datetime.datetime] = UNSET
    name: Union[Unset, None, str] = UNSET
    reporter: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp: Union[Unset, None, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat() if self.timestamp else None

        name = self.name
        reporter = self.reporter
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if name is not UNSET:
            field_dict["name"] = name
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, None, datetime.datetime]
        if _timestamp is None:
            timestamp = None
        elif isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        name = d.pop("name", UNSET)

        reporter = d.pop("reporter", UNSET)

        value = d.pop("value", UNSET)

        metrics_interval_result_dto = cls(
            timestamp=timestamp,
            name=name,
            reporter=reporter,
            value=value,
        )

        metrics_interval_result_dto.additional_properties = d
        return metrics_interval_result_dto

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
