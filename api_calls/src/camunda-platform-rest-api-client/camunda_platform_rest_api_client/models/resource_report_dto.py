from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.problem_dto import ProblemDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceReportDto")


@attr.s(auto_attribs=True)
class ResourceReportDto:
    """ """

    errors: Union[Unset, None, List[ProblemDto]] = UNSET
    warnings: Union[Unset, None, List[ProblemDto]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            if self.errors is None:
                errors = None
            else:
                errors = []
                for errors_item_data in self.errors:
                    errors_item = errors_item_data.to_dict()

                    errors.append(errors_item)

        warnings: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            if self.warnings is None:
                warnings = None
            else:
                warnings = []
                for warnings_item_data in self.warnings:
                    warnings_item = warnings_item_data.to_dict()

                    warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ProblemDto.from_dict(errors_item_data)

            errors.append(errors_item)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = ProblemDto.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        resource_report_dto = cls(
            errors=errors,
            warnings=warnings,
        )

        resource_report_dto.additional_properties = d
        return resource_report_dto

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
