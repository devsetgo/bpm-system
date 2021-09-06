from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="FetchExternalTaskTopicDtoProcessVariables")


@attr.s(auto_attribs=True)
class FetchExternalTaskTopicDtoProcessVariables:
    """A `JSON` object used for filtering tasks based on process instance variable values. A property name of
    the object represents a process variable name, while the property value represents the process variable
    value to filter tasks by."""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fetch_external_task_topic_dto_process_variables = cls()

        fetch_external_task_topic_dto_process_variables.additional_properties = d
        return fetch_external_task_topic_dto_process_variables

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
