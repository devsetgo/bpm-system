from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateIncidentDto")


@attr.s(auto_attribs=True)
class CreateIncidentDto:
    """ """

    incident_type: Union[Unset, None, str] = UNSET
    configuration: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_type = self.incident_type
        configuration = self.configuration
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incident_type is not UNSET:
            field_dict["incidentType"] = incident_type
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incident_type = d.pop("incidentType", UNSET)

        configuration = d.pop("configuration", UNSET)

        message = d.pop("message", UNSET)

        create_incident_dto = cls(
            incident_type=incident_type,
            configuration=configuration,
            message=message,
        )

        create_incident_dto.additional_properties = d
        return create_incident_dto

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
