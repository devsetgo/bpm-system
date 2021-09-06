from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.signal_dto_variables import SignalDtoVariables
from ..types import UNSET, Unset

T = TypeVar("T", bound="SignalDto")


@attr.s(auto_attribs=True)
class SignalDto:
    """ """

    name: Union[Unset, str] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    variables: Union[Unset, None, SignalDtoVariables] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    without_tenant_id: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        execution_id = self.execution_id
        variables: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict() if self.variables else None

        tenant_id = self.tenant_id
        without_tenant_id = self.without_tenant_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if variables is not UNSET:
            field_dict["variables"] = variables
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if without_tenant_id is not UNSET:
            field_dict["withoutTenantId"] = without_tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        execution_id = d.pop("executionId", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, None, SignalDtoVariables]
        if _variables is None:
            variables = None
        elif isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = SignalDtoVariables.from_dict(_variables)

        tenant_id = d.pop("tenantId", UNSET)

        without_tenant_id = d.pop("withoutTenantId", UNSET)

        signal_dto = cls(
            name=name,
            execution_id=execution_id,
            variables=variables,
            tenant_id=tenant_id,
            without_tenant_id=without_tenant_id,
        )

        signal_dto.additional_properties = d
        return signal_dto

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
