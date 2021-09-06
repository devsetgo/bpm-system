import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobDuedateDto")


@attr.s(auto_attribs=True)
class JobDuedateDto:
    """ """

    duedate: Union[Unset, None, datetime.datetime] = UNSET
    cascade: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duedate: Union[Unset, None, str] = UNSET
        if not isinstance(self.duedate, Unset):
            duedate = self.duedate.isoformat() if self.duedate else None

        cascade = self.cascade

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duedate is not UNSET:
            field_dict["duedate"] = duedate
        if cascade is not UNSET:
            field_dict["cascade"] = cascade

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _duedate = d.pop("duedate", UNSET)
        duedate: Union[Unset, None, datetime.datetime]
        if _duedate is None:
            duedate = None
        elif isinstance(_duedate, Unset):
            duedate = UNSET
        else:
            duedate = isoparse(_duedate)

        cascade = d.pop("cascade", UNSET)

        job_duedate_dto = cls(
            duedate=duedate,
            cascade=cascade,
        )

        job_duedate_dto.additional_properties = d
        return job_duedate_dto

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
