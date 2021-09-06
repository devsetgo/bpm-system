import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.historic_activity_instance_query_dto_sorting_item import HistoricActivityInstanceQueryDtoSortingItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="HistoricActivityInstanceQueryDto")


@attr.s(auto_attribs=True)
class HistoricActivityInstanceQueryDto:
    """A historic activity instance query which defines a group of historic activity instances"""

    activity_instance_id: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    process_definition_id: Union[Unset, None, str] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    activity_id: Union[Unset, None, str] = UNSET
    activity_name: Union[Unset, None, str] = UNSET
    activity_type: Union[Unset, None, str] = UNSET
    task_assignee: Union[Unset, None, str] = UNSET
    finished: Union[Unset, None, bool] = UNSET
    unfinished: Union[Unset, None, bool] = UNSET
    canceled: Union[Unset, None, bool] = UNSET
    complete_scope: Union[Unset, None, bool] = UNSET
    started_before: Union[Unset, None, datetime.datetime] = UNSET
    started_after: Union[Unset, None, datetime.datetime] = UNSET
    finished_before: Union[Unset, None, datetime.datetime] = UNSET
    finished_after: Union[Unset, None, datetime.datetime] = UNSET
    tenant_id_in: Union[Unset, None, List[str]] = UNSET
    without_tenant_id: Union[Unset, None, bool] = UNSET
    sorting: Union[Unset, List[HistoricActivityInstanceQueryDtoSortingItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        activity_instance_id = self.activity_instance_id
        process_instance_id = self.process_instance_id
        process_definition_id = self.process_definition_id
        execution_id = self.execution_id
        activity_id = self.activity_id
        activity_name = self.activity_name
        activity_type = self.activity_type
        task_assignee = self.task_assignee
        finished = self.finished
        unfinished = self.unfinished
        canceled = self.canceled
        complete_scope = self.complete_scope
        started_before: Union[Unset, None, str] = UNSET
        if not isinstance(self.started_before, Unset):
            started_before = self.started_before.isoformat() if self.started_before else None

        started_after: Union[Unset, None, str] = UNSET
        if not isinstance(self.started_after, Unset):
            started_after = self.started_after.isoformat() if self.started_after else None

        finished_before: Union[Unset, None, str] = UNSET
        if not isinstance(self.finished_before, Unset):
            finished_before = self.finished_before.isoformat() if self.finished_before else None

        finished_after: Union[Unset, None, str] = UNSET
        if not isinstance(self.finished_after, Unset):
            finished_after = self.finished_after.isoformat() if self.finished_after else None

        tenant_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tenant_id_in, Unset):
            if self.tenant_id_in is None:
                tenant_id_in = None
            else:
                tenant_id_in = self.tenant_id_in

        without_tenant_id = self.without_tenant_id
        sorting: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sorting, Unset):
            sorting = []
            for sorting_item_data in self.sorting:
                sorting_item = sorting_item_data.to_dict()

                sorting.append(sorting_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_instance_id is not UNSET:
            field_dict["activityInstanceId"] = activity_instance_id
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if activity_name is not UNSET:
            field_dict["activityName"] = activity_name
        if activity_type is not UNSET:
            field_dict["activityType"] = activity_type
        if task_assignee is not UNSET:
            field_dict["taskAssignee"] = task_assignee
        if finished is not UNSET:
            field_dict["finished"] = finished
        if unfinished is not UNSET:
            field_dict["unfinished"] = unfinished
        if canceled is not UNSET:
            field_dict["canceled"] = canceled
        if complete_scope is not UNSET:
            field_dict["completeScope"] = complete_scope
        if started_before is not UNSET:
            field_dict["startedBefore"] = started_before
        if started_after is not UNSET:
            field_dict["startedAfter"] = started_after
        if finished_before is not UNSET:
            field_dict["finishedBefore"] = finished_before
        if finished_after is not UNSET:
            field_dict["finishedAfter"] = finished_after
        if tenant_id_in is not UNSET:
            field_dict["tenantIdIn"] = tenant_id_in
        if without_tenant_id is not UNSET:
            field_dict["withoutTenantId"] = without_tenant_id
        if sorting is not UNSET:
            field_dict["sorting"] = sorting

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        activity_instance_id = d.pop("activityInstanceId", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        execution_id = d.pop("executionId", UNSET)

        activity_id = d.pop("activityId", UNSET)

        activity_name = d.pop("activityName", UNSET)

        activity_type = d.pop("activityType", UNSET)

        task_assignee = d.pop("taskAssignee", UNSET)

        finished = d.pop("finished", UNSET)

        unfinished = d.pop("unfinished", UNSET)

        canceled = d.pop("canceled", UNSET)

        complete_scope = d.pop("completeScope", UNSET)

        _started_before = d.pop("startedBefore", UNSET)
        started_before: Union[Unset, None, datetime.datetime]
        if _started_before is None:
            started_before = None
        elif isinstance(_started_before, Unset):
            started_before = UNSET
        else:
            started_before = isoparse(_started_before)

        _started_after = d.pop("startedAfter", UNSET)
        started_after: Union[Unset, None, datetime.datetime]
        if _started_after is None:
            started_after = None
        elif isinstance(_started_after, Unset):
            started_after = UNSET
        else:
            started_after = isoparse(_started_after)

        _finished_before = d.pop("finishedBefore", UNSET)
        finished_before: Union[Unset, None, datetime.datetime]
        if _finished_before is None:
            finished_before = None
        elif isinstance(_finished_before, Unset):
            finished_before = UNSET
        else:
            finished_before = isoparse(_finished_before)

        _finished_after = d.pop("finishedAfter", UNSET)
        finished_after: Union[Unset, None, datetime.datetime]
        if _finished_after is None:
            finished_after = None
        elif isinstance(_finished_after, Unset):
            finished_after = UNSET
        else:
            finished_after = isoparse(_finished_after)

        tenant_id_in = cast(List[str], d.pop("tenantIdIn", UNSET))

        without_tenant_id = d.pop("withoutTenantId", UNSET)

        sorting = []
        _sorting = d.pop("sorting", UNSET)
        for sorting_item_data in _sorting or []:
            sorting_item = HistoricActivityInstanceQueryDtoSortingItem.from_dict(sorting_item_data)

            sorting.append(sorting_item)

        historic_activity_instance_query_dto = cls(
            activity_instance_id=activity_instance_id,
            process_instance_id=process_instance_id,
            process_definition_id=process_definition_id,
            execution_id=execution_id,
            activity_id=activity_id,
            activity_name=activity_name,
            activity_type=activity_type,
            task_assignee=task_assignee,
            finished=finished,
            unfinished=unfinished,
            canceled=canceled,
            complete_scope=complete_scope,
            started_before=started_before,
            started_after=started_after,
            finished_before=finished_before,
            finished_after=finished_after,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
            sorting=sorting,
        )

        historic_activity_instance_query_dto.additional_properties = d
        return historic_activity_instance_query_dto

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
