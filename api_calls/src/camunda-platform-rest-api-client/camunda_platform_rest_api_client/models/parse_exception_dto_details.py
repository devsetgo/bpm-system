from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.resource_report_dto import ResourceReportDto

T = TypeVar("T", bound="ParseExceptionDtoDetails")


@attr.s(auto_attribs=True)
class ParseExceptionDtoDetails:
    """A JSON Object containing list of errors and warnings occurred during deployment."""

    additional_properties: Dict[str, ResourceReportDto] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        parse_exception_dto_details = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ResourceReportDto.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        parse_exception_dto_details.additional_properties = additional_properties
        return parse_exception_dto_details

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ResourceReportDto:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ResourceReportDto) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
