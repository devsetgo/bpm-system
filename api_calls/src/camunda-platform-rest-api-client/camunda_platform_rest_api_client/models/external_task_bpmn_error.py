from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.task_bpmn_error_dto_variables import TaskBpmnErrorDtoVariables
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalTaskBpmnError")


@attr.s(auto_attribs=True)
class ExternalTaskBpmnError:
    """ """

    error_code: Union[Unset, None, str] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    variables: Union[Unset, None, TaskBpmnErrorDtoVariables] = UNSET
    worker_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_code = self.error_code
        error_message = self.error_message
        variables: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict() if self.variables else None

        worker_id = self.worker_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if variables is not UNSET:
            field_dict["variables"] = variables
        if worker_id is not UNSET:
            field_dict["workerId"] = worker_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_code = d.pop("errorCode", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, None, TaskBpmnErrorDtoVariables]
        if _variables is None:
            variables = None
        elif isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = TaskBpmnErrorDtoVariables.from_dict(_variables)

        worker_id = d.pop("workerId", UNSET)

        external_task_bpmn_error = cls(
            error_code=error_code,
            error_message=error_message,
            variables=variables,
            worker_id=worker_id,
        )

        external_task_bpmn_error.additional_properties = d
        return external_task_bpmn_error

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
