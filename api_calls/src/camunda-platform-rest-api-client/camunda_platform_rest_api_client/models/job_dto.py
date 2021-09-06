import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobDto")


@attr.s(auto_attribs=True)
class JobDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    job_definition_id: Union[Unset, None, str] = UNSET
    due_date: Union[Unset, None, datetime.datetime] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    process_definition_key: Union[Unset, None, str] = UNSET
    retries: Union[Unset, None, int] = UNSET
    exception_message: Union[Unset, None, str] = UNSET
    failed_activity_id: Union[Unset, None, str] = UNSET
    suspended: Union[Unset, None, bool] = UNSET
    priority: Union[Unset, None, int] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    create_time: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        job_definition_id = self.job_definition_id
        due_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat() if self.due_date else None

        process_instance_id = self.process_instance_id
        execution_id = self.execution_id
        process_definition_id = self.process_definition_id
        process_definition_key = self.process_definition_key
        retries = self.retries
        exception_message = self.exception_message
        failed_activity_id = self.failed_activity_id
        suspended = self.suspended
        priority = self.priority
        tenant_id = self.tenant_id
        create_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat() if self.create_time else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if job_definition_id is not UNSET:
            field_dict["jobDefinitionId"] = job_definition_id
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if process_definition_key is not UNSET:
            field_dict["processDefinitionKey"] = process_definition_key
        if retries is not UNSET:
            field_dict["retries"] = retries
        if exception_message is not UNSET:
            field_dict["exceptionMessage"] = exception_message
        if failed_activity_id is not UNSET:
            field_dict["failedActivityId"] = failed_activity_id
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if priority is not UNSET:
            field_dict["priority"] = priority
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if create_time is not UNSET:
            field_dict["createTime"] = create_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        job_definition_id = d.pop("jobDefinitionId", UNSET)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, None, datetime.datetime]
        if _due_date is None:
            due_date = None
        elif isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        process_instance_id = d.pop("processInstanceId", UNSET)

        execution_id = d.pop("executionId", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        process_definition_key = d.pop("processDefinitionKey", UNSET)

        retries = d.pop("retries", UNSET)

        exception_message = d.pop("exceptionMessage", UNSET)

        failed_activity_id = d.pop("failedActivityId", UNSET)

        suspended = d.pop("suspended", UNSET)

        priority = d.pop("priority", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        _create_time = d.pop("createTime", UNSET)
        create_time: Union[Unset, None, datetime.datetime]
        if _create_time is None:
            create_time = None
        elif isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = isoparse(_create_time)

        job_dto = cls(
            id=id,
            job_definition_id=job_definition_id,
            due_date=due_date,
            process_instance_id=process_instance_id,
            execution_id=execution_id,
            process_definition_id=process_definition_id,
            process_definition_key=process_definition_key,
            retries=retries,
            exception_message=exception_message,
            failed_activity_id=failed_activity_id,
            suspended=suspended,
            priority=priority,
            tenant_id=tenant_id,
            create_time=create_time,
        )

        job_dto.additional_properties = d
        return job_dto

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
