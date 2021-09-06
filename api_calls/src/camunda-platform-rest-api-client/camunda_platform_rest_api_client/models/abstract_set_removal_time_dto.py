import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AbstractSetRemovalTimeDto")


@attr.s(auto_attribs=True)
class AbstractSetRemovalTimeDto:
    """ """

    absolute_removal_time: Union[Unset, None, datetime.datetime] = UNSET
    cleared_removal_time: Union[Unset, None, bool] = UNSET
    calculated_removal_time: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        absolute_removal_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.absolute_removal_time, Unset):
            absolute_removal_time = self.absolute_removal_time.isoformat() if self.absolute_removal_time else None

        cleared_removal_time = self.cleared_removal_time
        calculated_removal_time = self.calculated_removal_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if absolute_removal_time is not UNSET:
            field_dict["absoluteRemovalTime"] = absolute_removal_time
        if cleared_removal_time is not UNSET:
            field_dict["clearedRemovalTime"] = cleared_removal_time
        if calculated_removal_time is not UNSET:
            field_dict["calculatedRemovalTime"] = calculated_removal_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _absolute_removal_time = d.pop("absoluteRemovalTime", UNSET)
        absolute_removal_time: Union[Unset, None, datetime.datetime]
        if _absolute_removal_time is None:
            absolute_removal_time = None
        elif isinstance(_absolute_removal_time, Unset):
            absolute_removal_time = UNSET
        else:
            absolute_removal_time = isoparse(_absolute_removal_time)

        cleared_removal_time = d.pop("clearedRemovalTime", UNSET)

        calculated_removal_time = d.pop("calculatedRemovalTime", UNSET)

        abstract_set_removal_time_dto = cls(
            absolute_removal_time=absolute_removal_time,
            cleared_removal_time=cleared_removal_time,
            calculated_removal_time=calculated_removal_time,
        )

        abstract_set_removal_time_dto.additional_properties = d
        return abstract_set_removal_time_dto

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
