from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelemetryConfigurationDto")


@attr.s(auto_attribs=True)
class TelemetryConfigurationDto:
    """ """

    enable_telemetry: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable_telemetry = self.enable_telemetry

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_telemetry is not UNSET:
            field_dict["enableTelemetry"] = enable_telemetry

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable_telemetry = d.pop("enableTelemetry", UNSET)

        telemetry_configuration_dto = cls(
            enable_telemetry=enable_telemetry,
        )

        telemetry_configuration_dto.additional_properties = d
        return telemetry_configuration_dto

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
