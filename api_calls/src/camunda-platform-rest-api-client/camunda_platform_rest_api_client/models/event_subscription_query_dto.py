from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.event_subscription_query_dto_event_type import EventSubscriptionQueryDtoEventType
from ..models.event_subscription_query_dto_sorting_item import EventSubscriptionQueryDtoSortingItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventSubscriptionQueryDto")


@attr.s(auto_attribs=True)
class EventSubscriptionQueryDto:
    """A event subscription query which retrieves a list of event subscriptions"""

    event_subscription_id: Union[Unset, None, str] = UNSET
    event_name: Union[Unset, None, str] = UNSET
    event_type: Union[Unset, None, EventSubscriptionQueryDtoEventType] = UNSET
    execution_id: Union[Unset, None, str] = UNSET
    process_instance_id: Union[Unset, None, str] = UNSET
    activity_id: Union[Unset, None, str] = UNSET
    tenant_id_in: Union[Unset, None, List[str]] = UNSET
    without_tenant_id: Union[Unset, None, bool] = UNSET
    include_event_subscriptions_without_tenant_id: Union[Unset, None, bool] = UNSET
    sorting: Union[Unset, List[EventSubscriptionQueryDtoSortingItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_subscription_id = self.event_subscription_id
        event_name = self.event_name
        event_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value if self.event_type else None

        execution_id = self.execution_id
        process_instance_id = self.process_instance_id
        activity_id = self.activity_id
        tenant_id_in: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tenant_id_in, Unset):
            if self.tenant_id_in is None:
                tenant_id_in = None
            else:
                tenant_id_in = self.tenant_id_in

        without_tenant_id = self.without_tenant_id
        include_event_subscriptions_without_tenant_id = self.include_event_subscriptions_without_tenant_id
        sorting: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sorting, Unset):
            sorting = []
            for sorting_item_data in self.sorting:
                sorting_item = sorting_item_data.to_dict()

                sorting.append(sorting_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_subscription_id is not UNSET:
            field_dict["eventSubscriptionId"] = event_subscription_id
        if event_name is not UNSET:
            field_dict["eventName"] = event_name
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
        if process_instance_id is not UNSET:
            field_dict["processInstanceId"] = process_instance_id
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if tenant_id_in is not UNSET:
            field_dict["tenantIdIn"] = tenant_id_in
        if without_tenant_id is not UNSET:
            field_dict["withoutTenantId"] = without_tenant_id
        if include_event_subscriptions_without_tenant_id is not UNSET:
            field_dict["includeEventSubscriptionsWithoutTenantId"] = include_event_subscriptions_without_tenant_id
        if sorting is not UNSET:
            field_dict["sorting"] = sorting

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_subscription_id = d.pop("eventSubscriptionId", UNSET)

        event_name = d.pop("eventName", UNSET)

        _event_type = d.pop("eventType", UNSET)
        event_type: Union[Unset, None, EventSubscriptionQueryDtoEventType]
        if _event_type is None:
            event_type = None
        elif isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = EventSubscriptionQueryDtoEventType(_event_type)

        execution_id = d.pop("executionId", UNSET)

        process_instance_id = d.pop("processInstanceId", UNSET)

        activity_id = d.pop("activityId", UNSET)

        tenant_id_in = cast(List[str], d.pop("tenantIdIn", UNSET))

        without_tenant_id = d.pop("withoutTenantId", UNSET)

        include_event_subscriptions_without_tenant_id = d.pop("includeEventSubscriptionsWithoutTenantId", UNSET)

        sorting = []
        _sorting = d.pop("sorting", UNSET)
        for sorting_item_data in _sorting or []:
            sorting_item = EventSubscriptionQueryDtoSortingItem.from_dict(sorting_item_data)

            sorting.append(sorting_item)

        event_subscription_query_dto = cls(
            event_subscription_id=event_subscription_id,
            event_name=event_name,
            event_type=event_type,
            execution_id=execution_id,
            process_instance_id=process_instance_id,
            activity_id=activity_id,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
            include_event_subscriptions_without_tenant_id=include_event_subscriptions_without_tenant_id,
            sorting=sorting,
        )

        event_subscription_query_dto.additional_properties = d
        return event_subscription_query_dto

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
