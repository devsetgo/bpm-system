from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.start_process_instance_form_dto_variables import StartProcessInstanceFormDtoVariables
from ..types import UNSET, Unset

T = TypeVar("T", bound="StartProcessInstanceFormDto")


@attr.s(auto_attribs=True)
class StartProcessInstanceFormDto:
    """ """

    variables: Union[Unset, None, StartProcessInstanceFormDtoVariables] = UNSET
    business_key: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        variables: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict() if self.variables else None

        business_key = self.business_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variables is not UNSET:
            field_dict["variables"] = variables
        if business_key is not UNSET:
            field_dict["businessKey"] = business_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, None, StartProcessInstanceFormDtoVariables]
        if _variables is None:
            variables = None
        elif isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = StartProcessInstanceFormDtoVariables.from_dict(_variables)

        business_key = d.pop("businessKey", UNSET)

        start_process_instance_form_dto = cls(
            variables=variables,
            business_key=business_key,
        )

        start_process_instance_form_dto.additional_properties = d
        return start_process_instance_form_dto

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
