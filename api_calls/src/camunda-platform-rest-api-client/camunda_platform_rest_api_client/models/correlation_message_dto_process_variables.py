from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.variable_value_dto import VariableValueDto

T = TypeVar("T", bound="CorrelationMessageDtoProcessVariables")


@attr.s(auto_attribs=True)
class CorrelationMessageDtoProcessVariables:
    """A map of variables that is injected into the triggered execution or process instance after the message
    has been delivered. Each key is a variable name and each value a JSON variable value object with
    the following properties."""

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
        correlation_message_dto_process_variables = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = VariableValueDto.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        correlation_message_dto_process_variables.additional_properties = additional_properties
        return correlation_message_dto_process_variables

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
