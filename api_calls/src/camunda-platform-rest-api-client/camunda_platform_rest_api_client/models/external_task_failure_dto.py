from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.external_task_failure_dto_local_variables import ExternalTaskFailureDtoLocalVariables
from ..models.external_task_failure_dto_variables import ExternalTaskFailureDtoVariables
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalTaskFailureDto")


@attr.s(auto_attribs=True)
class ExternalTaskFailureDto:
    """ """

    worker_id: Union[Unset, str] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    error_details: Union[Unset, None, str] = UNSET
    retries: Union[Unset, None, int] = UNSET
    retry_timeout: Union[Unset, None, int] = UNSET
    variables: Union[Unset, None, ExternalTaskFailureDtoVariables] = UNSET
    local_variables: Union[Unset, None, ExternalTaskFailureDtoLocalVariables] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        worker_id = self.worker_id
        error_message = self.error_message
        error_details = self.error_details
        retries = self.retries
        retry_timeout = self.retry_timeout
        variables: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict() if self.variables else None

        local_variables: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.local_variables, Unset):
            local_variables = self.local_variables.to_dict() if self.local_variables else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if worker_id is not UNSET:
            field_dict["workerId"] = worker_id
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if error_details is not UNSET:
            field_dict["errorDetails"] = error_details
        if retries is not UNSET:
            field_dict["retries"] = retries
        if retry_timeout is not UNSET:
            field_dict["retryTimeout"] = retry_timeout
        if variables is not UNSET:
            field_dict["variables"] = variables
        if local_variables is not UNSET:
            field_dict["localVariables"] = local_variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        worker_id = d.pop("workerId", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        error_details = d.pop("errorDetails", UNSET)

        retries = d.pop("retries", UNSET)

        retry_timeout = d.pop("retryTimeout", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, None, ExternalTaskFailureDtoVariables]
        if _variables is None:
            variables = None
        elif isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = ExternalTaskFailureDtoVariables.from_dict(_variables)

        _local_variables = d.pop("localVariables", UNSET)
        local_variables: Union[Unset, None, ExternalTaskFailureDtoLocalVariables]
        if _local_variables is None:
            local_variables = None
        elif isinstance(_local_variables, Unset):
            local_variables = UNSET
        else:
            local_variables = ExternalTaskFailureDtoLocalVariables.from_dict(_local_variables)

        external_task_failure_dto = cls(
            worker_id=worker_id,
            error_message=error_message,
            error_details=error_details,
            retries=retries,
            retry_timeout=retry_timeout,
            variables=variables,
            local_variables=local_variables,
        )

        external_task_failure_dto.additional_properties = d
        return external_task_failure_dto

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
