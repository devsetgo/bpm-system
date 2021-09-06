from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.execution_dto import ExecutionDto
from ..models.message_correlation_result_with_variable_dto_result_type import (
    MessageCorrelationResultWithVariableDtoResultType,
)
from ..models.message_correlation_result_with_variable_dto_variables import (
    MessageCorrelationResultWithVariableDtoVariables,
)
from ..models.process_instance_dto import ProcessInstanceDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageCorrelationResultWithVariableDto")


@attr.s(auto_attribs=True)
class MessageCorrelationResultWithVariableDto:
    """The `processInstance` property only has a value if the resultType is set to `ProcessDefinition`.
    The processInstance with the properties as described in the
    [get single instance](https://docs.camunda.org/manual/7.15/reference/rest/process-instance/get/) method.

    The `execution` property only has a value if the resultType is set to `Execution`.
    The execution with the properties as described in the
    [get single execution](https://docs.camunda.org/manual/7.15/reference/rest/execution/get/) method."""

    result_type: Union[Unset, None, MessageCorrelationResultWithVariableDtoResultType] = UNSET
    process_instance: Union[Unset, ProcessInstanceDto] = UNSET
    execution: Union[Unset, ExecutionDto] = UNSET
    variables: Union[Unset, None, MessageCorrelationResultWithVariableDtoVariables] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.result_type, Unset):
            result_type = self.result_type.value if self.result_type else None

        process_instance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.process_instance, Unset):
            process_instance = self.process_instance.to_dict()

        execution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.execution, Unset):
            execution = self.execution.to_dict()

        variables: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict() if self.variables else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result_type is not UNSET:
            field_dict["resultType"] = result_type
        if process_instance is not UNSET:
            field_dict["processInstance"] = process_instance
        if execution is not UNSET:
            field_dict["execution"] = execution
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _result_type = d.pop("resultType", UNSET)
        result_type: Union[Unset, None, MessageCorrelationResultWithVariableDtoResultType]
        if _result_type is None:
            result_type = None
        elif isinstance(_result_type, Unset):
            result_type = UNSET
        else:
            result_type = MessageCorrelationResultWithVariableDtoResultType(_result_type)

        _process_instance = d.pop("processInstance", UNSET)
        process_instance: Union[Unset, ProcessInstanceDto]
        if isinstance(_process_instance, Unset):
            process_instance = UNSET
        else:
            process_instance = ProcessInstanceDto.from_dict(_process_instance)

        _execution = d.pop("execution", UNSET)
        execution: Union[Unset, ExecutionDto]
        if isinstance(_execution, Unset):
            execution = UNSET
        else:
            execution = ExecutionDto.from_dict(_execution)

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, None, MessageCorrelationResultWithVariableDtoVariables]
        if _variables is None:
            variables = None
        elif isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = MessageCorrelationResultWithVariableDtoVariables.from_dict(_variables)

        message_correlation_result_with_variable_dto = cls(
            result_type=result_type,
            process_instance=process_instance,
            execution=execution,
            variables=variables,
        )

        message_correlation_result_with_variable_dto.additional_properties = d
        return message_correlation_result_with_variable_dto

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
