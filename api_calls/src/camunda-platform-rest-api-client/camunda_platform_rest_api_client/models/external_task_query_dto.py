import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.external_task_query_dto_sorting_item import ExternalTaskQueryDtoSortingItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalTaskQueryDto")


@attr.s(auto_attribs=True)
class ExternalTaskQueryDto:
    """A JSON object with the following properties:"""

    external_task_id: Union[Unset, None, str] = UNSET
    external_task_id_in: Union[Unset, None, List[str]] = UNSET
    topic_name: Union[Unset, None, str] = UNSET
    worker_id: Union[Unset, None, str] = UNSET
    locked: Union[Unset, None, bool] = UNSET
    not_locked: Union[Unset, None, bool] = UNSET
    with_retries_left: Union[Unset, None, bool] = UNSET
    no_retries_left: Union[Unset, None, bool] = UNSET
    lock_expiration_after: Union[Unset, None, datetime.datetime] = UNSET
    lock_expiration_before: Union[Unset, None, datetime.datetime] = UNSET
    activity_id: Union[Unset, None, str] = UNSET
    activity_id_in: Union[Unset, None, List[str]] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    process_instance_id_in: Union[Unset, None, List[str]] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    tenant_id_in: Union[Unset, None, List[str]] = UNSET
    active: Union[Unset, None, bool] = UNSET
    suspended: Union[Unset, None, bool] = UNSET
    priority_higher_than_or_equals: Union[Unset, None, int] = UNSET
    priority_lower_than_or_equals: Union[Unset, None, int] = UNSET
    sorting: Union[Unset, List[ExternalTaskQueryDtoSortingItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_task_id = self.external_task_id
        external_task_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.external_task_id_in, Unset):
            if self.external_task_id_in is None:
                external_task_id_in = None
            else:
                external_task_id_in = self.external_task_id_in

        topic_name = self.topic_name
        worker_id = self.worker_id
        locked = self.locked
        not_locked = self.not_locked
        with_retries_left = self.with_retries_left
        no_retries_left = self.no_retries_left
        lock_expiration_after: Union[Unset, None, str] = UNSET
        if not isinstance(self.lock_expiration_after, Unset):
            lock_expiration_after = self.lock_expiration_after.isoformat() if self.lock_expiration_after else None

        lock_expiration_before: Union[Unset, None, str] = UNSET
        if not isinstance(self.lock_expiration_before, Unset):
            lock_expiration_before = self.lock_expiration_before.isoformat() if self.lock_expiration_before else None

        activity_id = self.activity_id
        activity_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.activity_id_in, Unset):
            if self.activity_id_in is None:
                activity_id_in = None
            else:
                activity_id_in = self.activity_id_in

        execution_id = self.execution_id
        process_instance_id = self.process_instance_id
        process_instance_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.process_instance_id_in, Unset):
            if self.process_instance_id_in is None:
                process_instance_id_in = None
            else:
                process_instance_id_in = self.process_instance_id_in

        process_definition_id = self.process_definition_id
        tenant_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tenant_id_in, Unset):
            if self.tenant_id_in is None:
                tenant_id_in = None
            else:
                tenant_id_in = self.tenant_id_in

        active = self.active
        suspended = self.suspended
        priority_higher_than_or_equals = self.priority_higher_than_or_equals
        priority_lower_than_or_equals = self.priority_lower_than_or_equals
        sorting: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sorting, Unset):
            sorting = []
            for sorting_item_data in self.sorting:
                sorting_item = sorting_item_data.to_dict()

                sorting.append(sorting_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_task_id is not UNSET:
            field_dict["externalTaskId"] = external_task_id
        if external_task_id_in is not UNSET:
            field_dict["externalTaskIdIn"] = external_task_id_in
        if topic_name is not UNSET:
            field_dict["topicName"] = topic_name
        if worker_id is not UNSET:
            field_dict["workerId"] = worker_id
        if locked is not UNSET:
            field_dict["locked"] = locked
        if not_locked is not UNSET:
            field_dict["notLocked"] = not_locked
        if with_retries_left is not UNSET:
            field_dict["withRetriesLeft"] = with_retries_left
        if no_retries_left is not UNSET:
            field_dict["noRetriesLeft"] = no_retries_left
        if lock_expiration_after is not UNSET:
            field_dict["lockExpirationAfter"] = lock_expiration_after
        if lock_expiration_before is not UNSET:
            field_dict["lockExpirationBefore"] = lock_expiration_before
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if activity_id_in is not UNSET:
            field_dict["activityIdIn"] = activity_id_in
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if process_instance_id_in is not UNSET:
            field_dict["processInstanceIdIn"] = process_instance_id_in
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if tenant_id_in is not UNSET:
            field_dict["tenantIdIn"] = tenant_id_in
        if active is not UNSET:
            field_dict["active"] = active
        if suspended is not UNSET:
            field_dict["suspended"] = suspended
        if priority_higher_than_or_equals is not UNSET:
            field_dict["priorityHigherThanOrEquals"] = priority_higher_than_or_equals
        if priority_lower_than_or_equals is not UNSET:
            field_dict["priorityLowerThanOrEquals"] = priority_lower_than_or_equals
        if sorting is not UNSET:
            field_dict["sorting"] = sorting

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_task_id = d.pop("externalTaskId", UNSET)

        external_task_id_in = cast(List[str], d.pop("externalTaskIdIn", UNSET))

        topic_name = d.pop("topicName", UNSET)

        worker_id = d.pop("workerId", UNSET)

        locked = d.pop("locked", UNSET)

        not_locked = d.pop("notLocked", UNSET)

        with_retries_left = d.pop("withRetriesLeft", UNSET)

        no_retries_left = d.pop("noRetriesLeft", UNSET)

        _lock_expiration_after = d.pop("lockExpirationAfter", UNSET)
        lock_expiration_after: Union[Unset, None, datetime.datetime]
        if _lock_expiration_after is None:
            lock_expiration_after = None
        elif isinstance(_lock_expiration_after, Unset):
            lock_expiration_after = UNSET
        else:
            lock_expiration_after = isoparse(_lock_expiration_after)

        _lock_expiration_before = d.pop("lockExpirationBefore", UNSET)
        lock_expiration_before: Union[Unset, None, datetime.datetime]
        if _lock_expiration_before is None:
            lock_expiration_before = None
        elif isinstance(_lock_expiration_before, Unset):
            lock_expiration_before = UNSET
        else:
            lock_expiration_before = isoparse(_lock_expiration_before)

        activity_id = d.pop("activityId", UNSET)

        activity_id_in = cast(List[str], d.pop("activityIdIn", UNSET))

        execution_id = d.pop("executionId", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        process_instance_id_in = cast(List[str], d.pop("processInstanceIdIn", UNSET))

        process_definition_id = d.pop("processDefinitionId", UNSET)

        tenant_id_in = cast(List[str], d.pop("tenantIdIn", UNSET))

        active = d.pop("active", UNSET)

        suspended = d.pop("suspended", UNSET)

        priority_higher_than_or_equals = d.pop("priorityHigherThanOrEquals", UNSET)

        priority_lower_than_or_equals = d.pop("priorityLowerThanOrEquals", UNSET)

        sorting = []
        _sorting = d.pop("sorting", UNSET)
        for sorting_item_data in _sorting or []:
            sorting_item = ExternalTaskQueryDtoSortingItem.from_dict(sorting_item_data)

            sorting.append(sorting_item)

        external_task_query_dto = cls(
            external_task_id=external_task_id,
            external_task_id_in=external_task_id_in,
            topic_name=topic_name,
            worker_id=worker_id,
            locked=locked,
            not_locked=not_locked,
            with_retries_left=with_retries_left,
            no_retries_left=no_retries_left,
            lock_expiration_after=lock_expiration_after,
            lock_expiration_before=lock_expiration_before,
            activity_id=activity_id,
            activity_id_in=activity_id_in,
            execution_id=execution_id,
            process_instance_id=process_instance_id,
            process_instance_id_in=process_instance_id_in,
            process_definition_id=process_definition_id,
            tenant_id_in=tenant_id_in,
            active=active,
            suspended=suspended,
            priority_higher_than_or_equals=priority_higher_than_or_equals,
            priority_lower_than_or_equals=priority_lower_than_or_equals,
            sorting=sorting,
        )

        external_task_query_dto.additional_properties = d
        return external_task_query_dto

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
