import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="HistoricActivityInstanceDto")


@attr.s(auto_attribs=True)
class HistoricActivityInstanceDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    parent_activity_instance_id: Union[Unset, None, str] = UNSET
    activity_id: Union[Unset, None, str] = UNSET
    activity_name: Union[Unset, None, str] = UNSET
    activity_type: Union[Unset, None, str] = UNSET
    process_definition_key: Union[Unset, None, str] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    task_id: Union[Unset, None, str] = UNSET
    assignee: Union[Unset, None, str] = UNSET
    called_process_instance_id: Union[Unset, None, str] = UNSET
    called_case_instance_id: Union[Unset, None, str] = UNSET
    start_time: Union[Unset, None, datetime.datetime] = UNSET
    end_time: Union[Unset, None, datetime.datetime] = UNSET
    duration_in_millis: Union[Unset, None, int] = UNSET
    canceled: Union[Unset, None, bool] = UNSET
    complete_scope: Union[Unset, None, bool] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    removal_time: Union[Unset, None, datetime.datetime] = UNSET
    root_process_instance_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        parent_activity_instance_id = self.parent_activity_instance_id
        activity_id = self.activity_id
        activity_name = self.activity_name
        activity_type = self.activity_type
        process_definition_key = self.process_definition_key
        process_definition_id = self.process_definition_id
        process_instance_id = self.process_instance_id
        execution_id = self.execution_id
        task_id = self.task_id
        assignee = self.assignee
        called_process_instance_id = self.called_process_instance_id
        called_case_instance_id = self.called_case_instance_id
        start_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat() if self.start_time else None

        end_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat() if self.end_time else None

        duration_in_millis = self.duration_in_millis
        canceled = self.canceled
        complete_scope = self.complete_scope
        tenant_id = self.tenant_id
        removal_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.removal_time, Unset):
            removal_time = self.removal_time.isoformat() if self.removal_time else None

        root_process_instance_id = self.root_process_instance_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parent_activity_instance_id is not UNSET:
            field_dict["parentActivityInstanceId"] = parent_activity_instance_id
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if activity_name is not UNSET:
            field_dict["activityName"] = activity_name
        if activity_type is not UNSET:
            field_dict["activityType"] = activity_type
        if process_definition_key is not UNSET:
            field_dict["processDefinitionKey"] = process_definition_key
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if called_process_instance_id is not UNSET:
            field_dict["calledProcessInstanceId"] = called_process_instance_id
        if called_case_instance_id is not UNSET:
            field_dict["calledCaseInstanceId"] = called_case_instance_id
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if duration_in_millis is not UNSET:
            field_dict["durationInMillis"] = duration_in_millis
        if canceled is not UNSET:
            field_dict["canceled"] = canceled
        if complete_scope is not UNSET:
            field_dict["completeScope"] = complete_scope
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if removal_time is not UNSET:
            field_dict["removalTime"] = removal_time
        if root_process_instance_id is not UNSET:
            field_dict["rootProcessInstanceId"] = root_process_instance_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        parent_activity_instance_id = d.pop("parentActivityInstanceId", UNSET)

        activity_id = d.pop("activityId", UNSET)

        activity_name = d.pop("activityName", UNSET)

        activity_type = d.pop("activityType", UNSET)

        process_definition_key = d.pop("processDefinitionKey", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        execution_id = d.pop("executionId", UNSET)

        task_id = d.pop("taskId", UNSET)

        assignee = d.pop("assignee", UNSET)

        called_process_instance_id = d.pop("calledProcessInstanceId", UNSET)

        called_case_instance_id = d.pop("calledCaseInstanceId", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, None, datetime.datetime]
        if _start_time is None:
            start_time = None
        elif isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, None, datetime.datetime]
        if _end_time is None:
            end_time = None
        elif isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        duration_in_millis = d.pop("durationInMillis", UNSET)

        canceled = d.pop("canceled", UNSET)

        complete_scope = d.pop("completeScope", UNSET)

        tenant_id = d.pop("tenantId", UNSET)

        _removal_time = d.pop("removalTime", UNSET)
        removal_time: Union[Unset, None, datetime.datetime]
        if _removal_time is None:
            removal_time = None
        elif isinstance(_removal_time, Unset):
            removal_time = UNSET
        else:
            removal_time = isoparse(_removal_time)

        root_process_instance_id = d.pop("rootProcessInstanceId", UNSET)

        historic_activity_instance_dto = cls(
            id=id,
            parent_activity_instance_id=parent_activity_instance_id,
            activity_id=activity_id,
            activity_name=activity_name,
            activity_type=activity_type,
            process_definition_key=process_definition_key,
            process_definition_id=process_definition_id,
            process_instance_id=process_instance_id,
            execution_id=execution_id,
            task_id=task_id,
            assignee=assignee,
            called_process_instance_id=called_process_instance_id,
            called_case_instance_id=called_case_instance_id,
            start_time=start_time,
            end_time=end_time,
            duration_in_millis=duration_in_millis,
            canceled=canceled,
            complete_scope=complete_scope,
            tenant_id=tenant_id,
            removal_time=removal_time,
            root_process_instance_id=root_process_instance_id,
        )

        historic_activity_instance_dto.additional_properties = d
        return historic_activity_instance_dto

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
