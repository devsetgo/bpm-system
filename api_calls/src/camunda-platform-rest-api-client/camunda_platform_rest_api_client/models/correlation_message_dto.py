from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.correlation_message_dto_correlation_keys import CorrelationMessageDtoCorrelationKeys
from ..models.correlation_message_dto_local_correlation_keys import CorrelationMessageDtoLocalCorrelationKeys
from ..models.correlation_message_dto_process_variables import CorrelationMessageDtoProcessVariables
from ..models.correlation_message_dto_process_variables_local import CorrelationMessageDtoProcessVariablesLocal
from ..types import UNSET, Unset

T = TypeVar("T", bound="CorrelationMessageDto")


@attr.s(auto_attribs=True)
class CorrelationMessageDto:
    """ """

    message_name: Union[Unset, None, str] = UNSET
    business_key: Union[Unset, None, str] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    without_tenant_id: Union[Unset, None, bool] = False
    process_instance_id: Union[Unset, None, str] = UNSET
    correlation_keys: Union[Unset, None, CorrelationMessageDtoCorrelationKeys] = UNSET
    local_correlation_keys: Union[Unset, None, CorrelationMessageDtoLocalCorrelationKeys] = UNSET
    process_variables: Union[Unset, None, CorrelationMessageDtoProcessVariables] = UNSET
    process_variables_local: Union[Unset, None, CorrelationMessageDtoProcessVariablesLocal] = UNSET
    all_: Union[Unset, None, bool] = False
    result_enabled: Union[Unset, None, bool] = False
    variables_in_result_enabled: Union[Unset, None, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message_name = self.message_name
        business_key = self.business_key
        tenant_id = self.tenant_id
        without_tenant_id = self.without_tenant_id
        process_instance_id = self.process_instance_id
        correlation_keys: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.correlation_keys, Unset):
            correlation_keys = self.correlation_keys.to_dict() if self.correlation_keys else None

        local_correlation_keys: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.local_correlation_keys, Unset):
            local_correlation_keys = self.local_correlation_keys.to_dict() if self.local_correlation_keys else None

        process_variables: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.process_variables, Unset):
            process_variables = self.process_variables.to_dict() if self.process_variables else None

        process_variables_local: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.process_variables_local, Unset):
            process_variables_local = self.process_variables_local.to_dict() if self.process_variables_local else None

        all_ = self.all_
        result_enabled = self.result_enabled
        variables_in_result_enabled = self.variables_in_result_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message_name is not UNSET:
            field_dict["messageName"] = message_name
        if business_key is not UNSET:
            field_dict["businessKey"] = business_key
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if without_tenant_id is not UNSET:
            field_dict["withoutTenantId"] = without_tenant_id
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if correlation_keys is not UNSET:
            field_dict["correlationKeys"] = correlation_keys
        if local_correlation_keys is not UNSET:
            field_dict["localCorrelationKeys"] = local_correlation_keys
        if process_variables is not UNSET:
            field_dict["processVariables"] = process_variables
        if process_variables_local is not UNSET:
            field_dict["processVariablesLocal"] = process_variables_local
        if all_ is not UNSET:
            field_dict["all"] = all_
        if result_enabled is not UNSET:
            field_dict["resultEnabled"] = result_enabled
        if variables_in_result_enabled is not UNSET:
            field_dict["variablesInResultEnabled"] = variables_in_result_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message_name = d.pop("messageName", UNSET)

        business_key = d.pop("businessKey", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        without_tenant_id = d.pop("withoutTenantId", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        _correlation_keys = d.pop("correlationKeys", UNSET)
        correlation_keys: Union[Unset, None, CorrelationMessageDtoCorrelationKeys]
        if _correlation_keys is None:
            correlation_keys = None
        elif isinstance(_correlation_keys, Unset):
            correlation_keys = UNSET
        else:
            correlation_keys = CorrelationMessageDtoCorrelationKeys.from_dict(_correlation_keys)

        _local_correlation_keys = d.pop("localCorrelationKeys", UNSET)
        local_correlation_keys: Union[Unset, None, CorrelationMessageDtoLocalCorrelationKeys]
        if _local_correlation_keys is None:
            local_correlation_keys = None
        elif isinstance(_local_correlation_keys, Unset):
            local_correlation_keys = UNSET
        else:
            local_correlation_keys = CorrelationMessageDtoLocalCorrelationKeys.from_dict(_local_correlation_keys)

        _process_variables = d.pop("processVariables", UNSET)
        process_variables: Union[Unset, None, CorrelationMessageDtoProcessVariables]
        if _process_variables is None:
            process_variables = None
        elif isinstance(_process_variables, Unset):
            process_variables = UNSET
        else:
            process_variables = CorrelationMessageDtoProcessVariables.from_dict(_process_variables)

        _process_variables_local = d.pop("processVariablesLocal", UNSET)
        process_variables_local: Union[Unset, None, CorrelationMessageDtoProcessVariablesLocal]
        if _process_variables_local is None:
            process_variables_local = None
        elif isinstance(_process_variables_local, Unset):
            process_variables_local = UNSET
        else:
            process_variables_local = CorrelationMessageDtoProcessVariablesLocal.from_dict(_process_variables_local)

        all_ = d.pop("all", UNSET)

        result_enabled = d.pop("resultEnabled", UNSET)

        variables_in_result_enabled = d.pop("variablesInResultEnabled", UNSET)

        correlation_message_dto = cls(
            message_name=message_name,
            business_key=business_key,
            tenant_id=tenant_id,
            without_tenant_id=without_tenant_id,
            process_instance_id=process_instance_id,
            correlation_keys=correlation_keys,
            local_correlation_keys=local_correlation_keys,
            process_variables=process_variables,
            process_variables_local=process_variables_local,
            all_=all_,
            result_enabled=result_enabled,
            variables_in_result_enabled=variables_in_result_enabled,
        )

        correlation_message_dto.additional_properties = d
        return correlation_message_dto

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
