from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.variable_value_dto import VariableValueDto

T = TypeVar("T", bound="TaskBpmnErrorDtoVariables")


@attr.s(auto_attribs=True)
class TaskBpmnErrorDtoVariables:
    """A JSON object containing variable key-value pairs."""

    additional_properties: Dict[str, VariableValueDto] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        task_bpmn_error_dto_variables = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = VariableValueDto.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        task_bpmn_error_dto_variables.additional_properties = additional_properties
        return task_bpmn_error_dto_variables

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> VariableValueDto:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: VariableValueDto) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
