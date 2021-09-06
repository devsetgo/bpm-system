import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventSubscriptionDto")


@attr.s(auto_attribs=True)
class EventSubscriptionDto:
    """ """

    id: Union[Unset, None, str] = UNSET
    event_type: Union[Unset, None, str] = UNSET
    event_name: Union[Unset, None, str] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    activity_id: Union[Unset, None, str] = UNSET
    created_date: Union[Unset, None, datetime.datetime] = UNSET
    tenant_id: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        event_type = self.event_type
        event_name = self.event_name
        execution_id = self.execution_id
        process_instance_id = self.process_instance_id
        activity_id = self.activity_id
        created_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat() if self.created_date else None

        tenant_id = self.tenant_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if event_name is not UNSET:
            field_dict["eventName"] = event_name
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        event_type = d.pop("eventType", UNSET)

        event_name = d.pop("eventName", UNSET)

        execution_id = d.pop("executionId", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        activity_id = d.pop("activityId", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, None, datetime.datetime]
        if _created_date is None:
            created_date = None
        elif isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        tenant_id = d.pop("tenantId", UNSET)

        event_subscription_dto = cls(
            id=id,
            event_type=event_type,
            event_name=event_name,
            execution_id=execution_id,
            process_instance_id=process_instance_id,
            activity_id=activity_id,
            created_date=created_date,
            tenant_id=tenant_id,
        )

        event_subscription_dto.additional_properties = d
        return event_subscription_dto

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
