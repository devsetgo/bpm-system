from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.evaluate_decision_dto_variables import EvaluateDecisionDtoVariables
from ..types import UNSET, Unset

T = TypeVar("T", bound="EvaluateDecisionDto")


@attr.s(auto_attribs=True)
class EvaluateDecisionDto:
    """ """

    variables: Union[Unset, None, EvaluateDecisionDtoVariables] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        variables: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict() if self.variables else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, None, EvaluateDecisionDtoVariables]
        if _variables is None:
            variables = None
        elif isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = EvaluateDecisionDtoVariables.from_dict(_variables)

        evaluate_decision_dto = cls(
            variables=variables,
        )

        evaluate_decision_dto.additional_properties = d
        return evaluate_decision_dto

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
