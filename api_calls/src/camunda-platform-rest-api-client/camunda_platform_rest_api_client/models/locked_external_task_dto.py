import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.locked_external_task_dto_variables import LockedExternalTaskDtoVariables
from ..types import UNSET, Unset

T = TypeVar("T", bound="LockedExternalTaskDto")


@attr.s(auto_attribs=True)
class LockedExternalTaskDto:
    """ """

    activity_id: Union[Unset, None, str] = UNSET
    activity_instance_id: Union[Unset, None, str] = UNSET
    error_message: Union[Unset, None, str] = UNSET
    error_details: Union[Unset, None, str] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    id: Union[Unset, None, str] = UNSET
    lock_expiration_time: Union[Unset, None, datetime.datetime] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    process_definition_key: Union[Unset, None, str] = UNSET
    process_definition_version_tag: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    retries: Union[Unset, None, int] = UNSET
    suspended: Union[Unset, None, bool] = UNSET
    worker_id: Union[Unset, None, str] = UNSET
    priority: Union[Unset, None, int] = UNSET
    topic_name: Union[Unset, None, str] = UNSET
    business_key: Union[Unset, None, str] = UNSET
    variables: Union[Unset, None, LockedExternalTaskDtoVariables] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        activity_id = self.activity_id
        activity_instance_id = self.activity_instance_id
        error_message = self.error_message
        error_details = self.error_details
        execution_id = self.execution_id
        id = self.id
        lock_expiration_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.lock_expiration_time, Unset):
            lock_expiration_time = self.lock_expiration_time.isoformat() if self.lock_expiration_time else None

        process_definition_id = self.process_definition_id
        process_definition_key = self.process_definition_key
        process_definition_version_tag = self.process_definition_version_tag
        process_instance_id = self.process_instance_id
        tenant_id = self.tenant_id
        retries = self.retries
        suspended = self.suspended
        worker_id = self.worker_id
        priority = self.priority
        topic_name = self.topic_name
        business_key = self.business_key
        variables: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict() if self.variables else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if activity_instance_id is not UNSET:
            field_dict["activityInstanceId"] = activity_instance_id
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if error_details is not UNSET:
            field_dict["errorDetails"] = error_details
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if id is not UNSET:
            field_dict["id"] = id
        if lock_expiration_time is not UNSET:
            field_dict["lockExpirationTime"] = lock_expiration_time
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if process_definition_key is not UNSET:
            field_dict["processDefinitionKey"] = process_definition_key
        if process_definition_version_tag is not UNSET:
            field_dict["processDefinitionVersionTag"] = process_definition_version_tag
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if retries is not UNSET:
            field_dict["retries"] = retries
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if worker_id is not UNSET:
            field_dict["workerId"] = worker_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if topic_name is not UNSET:
            field_dict["topicName"] = topic_name
        if business_key is not UNSET:
            field_dict["businessKey"] = business_key
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        activity_id = d.pop("activityId", UNSET)

        activity_instance_id = d.pop("activityInstanceId", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        error_details = d.pop("errorDetails", UNSET)

        execution_id = d.pop("executionId", UNSET)

        id = d.pop("id", UNSET)

        _lock_expiration_time = d.pop("lockExpirationTime", UNSET)
        lock_expiration_time: Union[Unset, None, datetime.datetime]
        if _lock_expiration_time is None:
            lock_expiration_time = None
        elif isinstance(_lock_expiration_time, Unset):
            lock_expiration_time = UNSET
        else:
            lock_expiration_time = isoparse(_lock_expiration_time)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        process_definition_key = d.pop("processDefinitionKey", UNSET)

        process_definition_version_tag = d.pop("processDefinitionVersionTag", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        retries = d.pop("retries", UNSET)

        suspended = d.pop("suspended", UNSET)

        worker_id = d.pop("workerId", UNSET)

        priority = d.pop("priority", UNSET)

        topic_name = d.pop("topicName", UNSET)

        business_key = d.pop("businessKey", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, None, LockedExternalTaskDtoVariables]
        if _variables is None:
            variables = None
        elif isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = LockedExternalTaskDtoVariables.from_dict(_variables)

        locked_external_task_dto = cls(
            activity_id=activity_id,
            activity_instance_id=activity_instance_id,
            error_message=error_message,
            error_details=error_details,
            execution_id=execution_id,
            id=id,
            lock_expiration_time=lock_expiration_time,
            process_definition_id=process_definition_id,
            process_definition_key=process_definition_key,
            process_definition_version_tag=process_definition_version_tag,
            process_instance_id=process_instance_id,
            tenant_id=tenant_id,
            retries=retries,
            suspended=suspended,
            worker_id=worker_id,
            priority=priority,
            topic_name=topic_name,
            business_key=business_key,
            variables=variables,
        )

        locked_external_task_dto.additional_properties = d
        return locked_external_task_dto

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
