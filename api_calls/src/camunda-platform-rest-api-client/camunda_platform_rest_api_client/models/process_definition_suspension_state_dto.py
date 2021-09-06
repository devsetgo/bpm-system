import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessDefinitionSuspensionStateDto")


@attr.s(auto_attribs=True)
class ProcessDefinitionSuspensionStateDto:
    """ """

    suspended: Union[Unset, None, bool] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    process_definition_key: Union[Unset, None, str] = UNSET
    include_process_instances: Union[Unset, None, bool] = UNSET
    execution_date: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        suspended = self.suspended
        process_definition_id = self.process_definition_id
        process_definition_key = self.process_definition_key
        include_process_instances = self.include_process_instances
        execution_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.execution_date, Unset):
            execution_date = self.execution_date.isoformat() if self.execution_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if process_definition_key is not UNSET:
            field_dict["processDefinitionKey"] = process_definition_key
        if include_process_instances is not UNSET:
            field_dict["includeProcessInstances"] = include_process_instances
        if execution_date is not UNSET:
            field_dict["executionDate"] = execution_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        suspended = d.pop("suspended", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        process_definition_key = d.pop("processDefinitionKey", UNSET)

        include_process_instances = d.pop("includeProcessInstances", UNSET)

        _execution_date = d.pop("executionDate", UNSET)
        execution_date: Union[Unset, None, datetime.datetime]
        if _execution_date is None:
            execution_date = None
        elif isinstance(_execution_date, Unset):
            execution_date = UNSET
        else:
            execution_date = isoparse(_execution_date)

        process_definition_suspension_state_dto = cls(
            suspended=suspended,
            process_definition_id=process_definition_id,
            process_definition_key=process_definition_key,
            include_process_instances=include_process_instances,
            execution_date=execution_date,
        )

        process_definition_suspension_state_dto.additional_properties = d
        return process_definition_suspension_state_dto

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
