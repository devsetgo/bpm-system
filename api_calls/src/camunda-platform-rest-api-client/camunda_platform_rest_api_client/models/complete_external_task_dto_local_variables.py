from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.variable_value_dto import VariableValueDto

T = TypeVar("T", bound="CompleteExternalTaskDtoLocalVariables")


@attr.s(auto_attribs=True)
class CompleteExternalTaskDtoLocalVariables:
    """A JSON object containing local variable key-value pairs. Local variables are set only in the scope of external task. Each key is a variable name and each value a JSON variable value object with the following properties:"""

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
        complete_external_task_dto_local_variables = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = VariableValueDto.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        complete_external_task_dto_local_variables.additional_properties = additional_properties
        return complete_external_task_dto_local_variables

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
