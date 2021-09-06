from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.password_policy_rule_dto import PasswordPolicyRuleDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckPasswordPolicyResultDto")


@attr.s(auto_attribs=True)
class CheckPasswordPolicyResultDto:
    """ """

    rules: Union[Unset, None, List[PasswordPolicyRuleDto]] = UNSET
    valid: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rules: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            if self.rules is None:
                rules = None
            else:
                rules = []
                for rules_item_data in self.rules:
                    rules_item = rules_item_data.to_dict()

                    rules.append(rules_item)

        valid = self.valid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rules is not UNSET:
            field_dict["rules"] = rules
        if valid is not UNSET:
            field_dict["valid"] = valid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = PasswordPolicyRuleDto.from_dict(rules_item_data)

            rules.append(rules_item)

        valid = d.pop("valid", UNSET)

        check_password_policy_result_dto = cls(
            rules=rules,
            valid=valid,
        )

        check_password_policy_result_dto.additional_properties = d
        return check_password_policy_result_dto

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
