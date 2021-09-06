from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentStatisticsResultDto")


@attr.s(auto_attribs=True)
class IncidentStatisticsResultDto:
    """ """

    incident_type: Union[Unset, None, str] = UNSET
    incident_count: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_type = self.incident_type
        incident_count = self.incident_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incident_type is not UNSET:
            field_dict["incidentType"] = incident_type
        if incident_count is not UNSET:
            field_dict["incidentCount"] = incident_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incident_type = d.pop("incidentType", UNSET)

        incident_count = d.pop("incidentCount", UNSET)

        incident_statistics_result_dto = cls(
            incident_type=incident_type,
            incident_count=incident_count,
        )

        incident_statistics_result_dto.additional_properties = d
        return incident_statistics_result_dto

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
