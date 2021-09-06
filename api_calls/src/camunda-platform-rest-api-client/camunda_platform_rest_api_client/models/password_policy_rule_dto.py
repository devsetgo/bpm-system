from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.password_policy_rule_dto_parameter import PasswordPolicyRuleDtoParameter
from ..types import UNSET, Unset

T = TypeVar("T", bound="PasswordPolicyRuleDto")


@attr.s(auto_attribs=True)
class PasswordPolicyRuleDto:
    """Describes a rule of a password policy."""

    placeholder: Union[Unset, None, str] = UNSET
    parameter: Union[Unset, PasswordPolicyRuleDtoParameter] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        placeholder = self.placeholder
        parameter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameter, Unset):
            parameter = self.parameter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if parameter is not UNSET:
            field_dict["parameter"] = parameter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        placeholder = d.pop("placeholder", UNSET)

        _parameter = d.pop("parameter", UNSET)
        parameter: Union[Unset, PasswordPolicyRuleDtoParameter]
        if isinstance(_parameter, Unset):
            parameter = UNSET
        else:
            parameter = PasswordPolicyRuleDtoParameter.from_dict(_parameter)

        password_policy_rule_dto = cls(
            placeholder=placeholder,
            parameter=parameter,
        )

        password_policy_rule_dto.additional_properties = d
        return password_policy_rule_dto

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
