from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.variable_value_dto_value import VariableValueDtoValue
from ..models.variable_value_dto_value_info import VariableValueDtoValueInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="VariableInstanceDto")


@attr.s(auto_attribs=True)
class VariableInstanceDto:
    """ """

    value: Union[Unset, VariableValueDtoValue] = UNSET
    type: Union[Unset, None, str] = UNSET
    value_info: Union[Unset, VariableValueDtoValueInfo] = UNSET
    id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    case_instance_id: Union[Unset, None, str] = UNSET
    case_execution_id: Union[Unset, None, str] = UNSET
    task_id: Union[Unset, None, str] = UNSET
    batch_id: Union[Unset, None, str] = UNSET
    activity_instance_id: Union[Unset, None, str] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        type = self.type
        value_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value_info, Unset):
            value_info = self.value_info.to_dict()

        id = self.id
        name = self.name
        process_definition_id = self.process_definition_id
        process_instance_id = self.process_instance_id
        execution_id = self.execution_id
        case_instance_id = self.case_instance_id
        case_execution_id = self.case_execution_id
        task_id = self.task_id
        batch_id = self.batch_id
        activity_instance_id = self.activity_instance_id
        tenant_id = self.tenant_id
        error_message = self.error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if type is not UNSET:
            field_dict["type"] = type
        if value_info is not UNSET:
            field_dict["valueInfo"] = value_info
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if case_instance_id is not UNSET:
            field_dict["caseInstanceId"] = case_instance_id
        if case_execution_id is not UNSET:
            field_dict["caseExecutionId"] = case_execution_id
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if batch_id is not UNSET:
            field_dict["batchId"] = batch_id
        if activity_instance_id is not UNSET:
            field_dict["activityInstanceId"] = activity_instance_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _value = d.pop("value", UNSET)
        value: Union[Unset, VariableValueDtoValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = VariableValueDtoValue.from_dict(_value)

        type = d.pop("type", UNSET)

        _value_info = d.pop("valueInfo", UNSET)
        value_info: Union[Unset, VariableValueDtoValueInfo]
        if isinstance(_value_info, Unset):
            value_info = UNSET
        else:
            value_info = VariableValueDtoValueInfo.from_dict(_value_info)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        execution_id = d.pop("executionId", UNSET)

        case_instance_id = d.pop("caseInstanceId", UNSET)

        case_execution_id = d.pop("caseExecutionId", UNSET)

        task_id = d.pop("taskId", UNSET)

        batch_id = d.pop("batchId", UNSET)

        activity_instance_id = d.pop("activityInstanceId", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        variable_instance_dto = cls(
            value=value,
            type=type,
            value_info=value_info,
            id=id,
            name=name,
            process_definition_id=process_definition_id,
            process_instance_id=process_instance_id,
            execution_id=execution_id,
            case_instance_id=case_instance_id,
            case_execution_id=case_execution_id,
            task_id=task_id,
            batch_id=batch_id,
            activity_instance_id=activity_instance_id,
            tenant_id=tenant_id,
            error_message=error_message,
        )

        variable_instance_dto.additional_properties = d
        return variable_instance_dto

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
