from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.evaluation_condition_dto_variables import EvaluationConditionDtoVariables
from ..types import UNSET, Unset

T = TypeVar("T", bound="EvaluationConditionDto")


@attr.s(auto_attribs=True)
class EvaluationConditionDto:
    """ """

    variables: Union[Unset, None, EvaluationConditionDtoVariables] = UNSET
    business_key: Union[Unset, None, str] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    without_tenant_id: Union[Unset, None, bool] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        variables: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict() if self.variables else None

        business_key = self.business_key
        tenant_id = self.tenant_id
        without_tenant_id = self.without_tenant_id
        process_definition_id = self.process_definition_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variables is not UNSET:
            field_dict["variables"] = variables
        if business_key is not UNSET:
            field_dict["businessKey"] = business_key
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if without_tenant_id is not UNSET:
            field_dict["withoutTenantId"] = without_tenant_id
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, None, EvaluationConditionDtoVariables]
        if _variables is None:
            variables = None
        elif isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = EvaluationConditionDtoVariables.from_dict(_variables)

        business_key = d.pop("businessKey", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        without_tenant_id = d.pop("withoutTenantId", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        evaluation_condition_dto = cls(
            variables=variables,
            business_key=business_key,
            tenant_id=tenant_id,
            without_tenant_id=without_tenant_id,
            process_definition_id=process_definition_id,
        )

        evaluation_condition_dto.additional_properties = d
        return evaluation_condition_dto

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
