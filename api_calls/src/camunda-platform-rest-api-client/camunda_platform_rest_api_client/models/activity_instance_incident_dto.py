from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityInstanceIncidentDto")


@attr.s(auto_attribs=True)
class ActivityInstanceIncidentDto:
    """An activity instance, incident pair."""

    id: Union[Unset, None, str] = UNSET
    parent_activity_instance_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        parent_activity_instance_id = self.parent_activity_instance_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parent_activity_instance_id is not UNSET:
            field_dict["parentActivityInstanceId"] = parent_activity_instance_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        parent_activity_instance_id = d.pop("parentActivityInstanceId", UNSET)

        activity_instance_incident_dto = cls(
            id=id,
            parent_activity_instance_id=parent_activity_instance_id,
        )

        activity_instance_incident_dto.additional_properties = d
        return activity_instance_incident_dto

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
