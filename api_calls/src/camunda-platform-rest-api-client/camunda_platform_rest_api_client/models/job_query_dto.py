from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.job_condition_query_parameter_dto import JobConditionQueryParameterDto
from ..models.job_query_dto_sorting_item import JobQueryDtoSortingItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobQueryDto")


@attr.s(auto_attribs=True)
class JobQueryDto:
    """A Job instance query which defines a list of Job instances"""

    job_id: Union[Unset, None, str] = UNSET
    job_ids: Union[Unset, None, List[str]] = UNSET
    job_definition_id: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    process_instance_ids: Union[Unset, None, List[str]] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    process_definition_key: Union[Unset, None, str] = UNSET
    activity_id: Union[Unset, None, str] = UNSET
    with_retries_left: Union[Unset, None, bool] = UNSET
    executable: Union[Unset, None, bool] = UNSET
    timers: Union[Unset, None, bool] = UNSET
    messages: Union[Unset, None, bool] = UNSET
    due_dates: Union[Unset, None, List[JobConditionQueryParameterDto]] = UNSET
    create_times: Union[Unset, None, List[JobConditionQueryParameterDto]] = UNSET
    with_exception: Union[Unset, None, bool] = UNSET
    exception_message: Union[Unset, None, str] = UNSET
    failed_activity_id: Union[Unset, None, str] = UNSET
    no_retries_left: Union[Unset, None, bool] = UNSET
    active: Union[Unset, None, bool] = UNSET
    suspended: Union[Unset, None, bool] = UNSET
    priority_lower_than_or_equals: Union[Unset, None, int] = UNSET
    priority_higher_than_or_equals: Union[Unset, None, int] = UNSET
    tenant_id_in: Union[Unset, None, List[str]] = UNSET
    without_tenant_id: Union[Unset, None, bool] = UNSET
    include_jobs_without_tenant_id: Union[Unset, None, bool] = UNSET
    sorting: Union[Unset, List[JobQueryDtoSortingItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        job_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.job_ids, Unset):
            if self.job_ids is None:
                job_ids = None
            else:
                job_ids = self.job_ids

        job_definition_id = self.job_definition_id
        process_instance_id = self.process_instance_id
        process_instance_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.process_instance_ids, Unset):
            if self.process_instance_ids is None:
                process_instance_ids = None
            else:
                process_instance_ids = self.process_instance_ids

        execution_id = self.execution_id
        process_definition_id = self.process_definition_id
        process_definition_key = self.process_definition_key
        activity_id = self.activity_id
        with_retries_left = self.with_retries_left
        executable = self.executable
        timers = self.timers
        messages = self.messages
        due_dates: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.due_dates, Unset):
            if self.due_dates is None:
                due_dates = None
            else:
                due_dates = []
                for due_dates_item_data in self.due_dates:
                    due_dates_item = due_dates_item_data.to_dict()

                    due_dates.append(due_dates_item)

        create_times: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.create_times, Unset):
            if self.create_times is None:
                create_times = None
            else:
                create_times = []
                for create_times_item_data in self.create_times:
                    create_times_item = create_times_item_data.to_dict()

                    create_times.append(create_times_item)

        with_exception = self.with_exception
        exception_message = self.exception_message
        failed_activity_id = self.failed_activity_id
        no_retries_left = self.no_retries_left
        active = self.active
        suspended = self.suspended
        priority_lower_than_or_equals = self.priority_lower_than_or_equals
        priority_higher_than_or_equals = self.priority_higher_than_or_equals
        tenant_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tenant_id_in, Unset):
            if self.tenant_id_in is None:
                tenant_id_in = None
            else:
                tenant_id_in = self.tenant_id_in

        without_tenant_id = self.without_tenant_id
        include_jobs_without_tenant_id = self.include_jobs_without_tenant_id
        sorting: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sorting, Unset):
            sorting = []
            for sorting_item_data in self.sorting:
                sorting_item = sorting_item_data.to_dict()

                sorting.append(sorting_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if job_ids is not UNSET:
            field_dict["jobIds"] = job_ids
        if job_definition_id is not UNSET:
            field_dict["jobDefinitionId"] = job_definition_id
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if process_instance_ids is not UNSET:
            field_dict["processInstanceIds"] = process_instance_ids
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if process_definition_key is not UNSET:
            field_dict["processDefinitionKey"] = process_definition_key
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if with_retries_left is not UNSET:
            field_dict["withRetriesLeft"] = with_retries_left
        if executable is not UNSET:
            field_dict["executable"] = executable
        if timers is not UNSET:
            field_dict["timers"] = timers
        if messages is not UNSET:
            field_dict["messages"] = messages
        if due_dates is not UNSET:
            field_dict["dueDates"] = due_dates
        if create_times is not UNSET:
            field_dict["createTimes"] = create_times
        if with_exception is not UNSET:
            field_dict["withException"] = with_exception
        if exception_message is not UNSET:
            field_dict["exceptionMessage"] = exception_message
        if failed_activity_id is not UNSET:
            field_dict["failedActivityId"] = failed_activity_id
        if no_retries_left is not UNSET:
            field_dict["noRetriesLeft"] = no_retries_left
        if active is not UNSET:
            field_dict["active"] = active
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if priority_lower_than_or_equals is not UNSET:
            field_dict["priorityLowerThanOrEquals"] = priority_lower_than_or_equals
        if priority_higher_than_or_equals is not UNSET:
            field_dict["priorityHigherThanOrEquals"] = priority_higher_than_or_equals
        if tenant_id_in is not UNSET:
            field_dict["tenantIdIn"] = tenant_id_in
        if without_tenant_id is not UNSET:
            field_dict["withoutTenantId"] = without_tenant_id
        if include_jobs_without_tenant_id is not UNSET:
            field_dict["includeJobsWithoutTenantId"] = include_jobs_without_tenant_id
        if sorting is not UNSET:
            field_dict["sorting"] = sorting

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_id = d.pop("jobId", UNSET)

        job_ids = cast(List[str], d.pop("jobIds", UNSET))

        job_definition_id = d.pop("jobDefinitionId", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        process_instance_ids = cast(List[str], d.pop("processInstanceIds", UNSET))

        execution_id = d.pop("executionId", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        process_definition_key = d.pop("processDefinitionKey", UNSET)

        activity_id = d.pop("activityId", UNSET)

        with_retries_left = d.pop("withRetriesLeft", UNSET)

        executable = d.pop("executable", UNSET)

        timers = d.pop("timers", UNSET)

        messages = d.pop("messages", UNSET)

        due_dates = []
        _due_dates = d.pop("dueDates", UNSET)
        for due_dates_item_data in _due_dates or []:
            due_dates_item = JobConditionQueryParameterDto.from_dict(due_dates_item_data)

            due_dates.append(due_dates_item)

        create_times = []
        _create_times = d.pop("createTimes", UNSET)
        for create_times_item_data in _create_times or []:
            create_times_item = JobConditionQueryParameterDto.from_dict(create_times_item_data)

            create_times.append(create_times_item)

        with_exception = d.pop("withException", UNSET)

        exception_message = d.pop("exceptionMessage", UNSET)

        failed_activity_id = d.pop("failedActivityId", UNSET)

        no_retries_left = d.pop("noRetriesLeft", UNSET)

        active = d.pop("active", UNSET)

        suspended = d.pop("suspended", UNSET)

        priority_lower_than_or_equals = d.pop("priorityLowerThanOrEquals", UNSET)

        priority_higher_than_or_equals = d.pop("priorityHigherThanOrEquals", UNSET)

        tenant_id_in = cast(List[str], d.pop("tenantIdIn", UNSET))

        without_tenant_id = d.pop("withoutTenantId", UNSET)

        include_jobs_without_tenant_id = d.pop("includeJobsWithoutTenantId", UNSET)

        sorting = []
        _sorting = d.pop("sorting", UNSET)
        for sorting_item_data in _sorting or []:
            sorting_item = JobQueryDtoSortingItem.from_dict(sorting_item_data)

            sorting.append(sorting_item)

        job_query_dto = cls(
            job_id=job_id,
            job_ids=job_ids,
            job_definition_id=job_definition_id,
            process_instance_id=process_instance_id,
            process_instance_ids=process_instance_ids,
            execution_id=execution_id,
            process_definition_id=process_definition_id,
            process_definition_key=process_definition_key,
            activity_id=activity_id,
            with_retries_left=with_retries_left,
            executable=executable,
            timers=timers,
            messages=messages,
            due_dates=due_dates,
            create_times=create_times,
            with_exception=with_exception,
            exception_message=exception_message,
            failed_activity_id=failed_activity_id,
            no_retries_left=no_retries_left,
            active=active,
            suspended=suspended,
            priority_lower_than_or_equals=priority_lower_than_or_equals,
            priority_higher_than_or_equals=priority_higher_than_or_equals,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
            include_jobs_without_tenant_id=include_jobs_without_tenant_id,
            sorting=sorting,
        )

        job_query_dto.additional_properties = d
        return job_query_dto

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
