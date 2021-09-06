from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.complete_external_task_dto_local_variables import CompleteExternalTaskDtoLocalVariables
from ..models.complete_external_task_dto_variables import CompleteExternalTaskDtoVariables
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompleteExternalTaskDto")


@attr.s(auto_attribs=True)
class CompleteExternalTaskDto:
    """ """

    worker_id: Union[Unset, str] = UNSET
    variables: Union[Unset, None, CompleteExternalTaskDtoVariables] = UNSET
    local_variables: Union[Unset, None, CompleteExternalTaskDtoLocalVariables] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        worker_id = self.worker_id
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
        if variables is not UNSET:
            field_dict["variables"] = variables
        if local_variables is not UNSET:
            field_dict["localVariables"] = local_variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        worker_id = d.pop("workerId", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, None, CompleteExternalTaskDtoVariables]
        if _variables is None:
            variables = None
        elif isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = CompleteExternalTaskDtoVariables.from_dict(_variables)

        _local_variables = d.pop("localVariables", UNSET)
        local_variables: Union[Unset, None, CompleteExternalTaskDtoLocalVariables]
        if _local_variables is None:
            local_variables = None
        elif isinstance(_local_variables, Unset):
            local_variables = UNSET
        else:
            local_variables = CompleteExternalTaskDtoLocalVariables.from_dict(_local_variables)

        complete_external_task_dto = cls(
            worker_id=worker_id,
            variables=variables,
            local_variables=local_variables,
        )

        complete_external_task_dto.additional_properties = d
        return complete_external_task_dto

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
