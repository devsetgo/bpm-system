from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.event_subscription_dto import EventSubscriptionDto
from ...models.exception_dto import ExceptionDto
from ...models.get_event_subscriptions_event_type import GetEventSubscriptionsEventType
from ...models.get_event_subscriptions_sort_by import GetEventSubscriptionsSortBy
from ...models.get_event_subscriptions_sort_order import GetEventSubscriptionsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    event_subscription_id: Union[Unset, None, str] = UNSET,
    event_name: Union[Unset, None, str] = UNSET,
    event_type: Union[Unset, None, GetEventSubscriptionsEventType] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_event_subscriptions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetEventSubscriptionsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetEventSubscriptionsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/event-subscription".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_event_type: Union[Unset, None, str] = UNSET
    if not isinstance(event_type, Unset):
        json_event_type = event_type.value if event_type else None

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params: Dict[str, Any] = {
        "eventSubscriptionId": event_subscription_id,
        "eventName": event_name,
        "eventType": json_event_type,
        "executionId": execution_id,
        "processInstanceId": process_instance_id,
        "activityId": activity_id,
        "tenantIdIn": tenant_id_in,
        "withoutTenantId": without_tenant_id,
        "includeEventSubscriptionsWithoutTenantId": include_event_subscriptions_without_tenant_id,
        "sortBy": json_sort_by,
        "sortOrder": json_sort_order,
        "firstResult": first_result,
        "maxResults": max_results,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[EventSubscriptionDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EventSubscriptionDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[EventSubscriptionDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    event_subscription_id: Union[Unset, None, str] = UNSET,
    event_name: Union[Unset, None, str] = UNSET,
    event_type: Union[Unset, None, GetEventSubscriptionsEventType] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_event_subscriptions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetEventSubscriptionsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetEventSubscriptionsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[EventSubscriptionDto]]]:
    kwargs = _get_kwargs(
        client=client,
        event_subscription_id=event_subscription_id,
        event_name=event_name,
        event_type=event_type,
        execution_id=execution_id,
        process_instance_id=process_instance_id,
        activity_id=activity_id,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_event_subscriptions_without_tenant_id=include_event_subscriptions_without_tenant_id,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    event_subscription_id: Union[Unset, None, str] = UNSET,
    event_name: Union[Unset, None, str] = UNSET,
    event_type: Union[Unset, None, GetEventSubscriptionsEventType] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_event_subscriptions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetEventSubscriptionsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetEventSubscriptionsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[EventSubscriptionDto]]]:
    """Queries for event subscriptions that fulfill given parameters.
    The size of the result set can be retrieved by using the
    [Get Event Subscriptions count](https://docs.camunda.org/manual/7.15/reference/rest/event-subscription/get-query-count/) method."""

    return sync_detailed(
        client=client,
        event_subscription_id=event_subscription_id,
        event_name=event_name,
        event_type=event_type,
        execution_id=execution_id,
        process_instance_id=process_instance_id,
        activity_id=activity_id,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_event_subscriptions_without_tenant_id=include_event_subscriptions_without_tenant_id,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    event_subscription_id: Union[Unset, None, str] = UNSET,
    event_name: Union[Unset, None, str] = UNSET,
    event_type: Union[Unset, None, GetEventSubscriptionsEventType] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_event_subscriptions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetEventSubscriptionsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetEventSubscriptionsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[EventSubscriptionDto]]]:
    kwargs = _get_kwargs(
        client=client,
        event_subscription_id=event_subscription_id,
        event_name=event_name,
        event_type=event_type,
        execution_id=execution_id,
        process_instance_id=process_instance_id,
        activity_id=activity_id,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_event_subscriptions_without_tenant_id=include_event_subscriptions_without_tenant_id,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    event_subscription_id: Union[Unset, None, str] = UNSET,
    event_name: Union[Unset, None, str] = UNSET,
    event_type: Union[Unset, None, GetEventSubscriptionsEventType] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_event_subscriptions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetEventSubscriptionsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetEventSubscriptionsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[EventSubscriptionDto]]]:
    """Queries for event subscriptions that fulfill given parameters.
    The size of the result set can be retrieved by using the
    [Get Event Subscriptions count](https://docs.camunda.org/manual/7.15/reference/rest/event-subscription/get-query-count/) method."""

    return (
        await asyncio_detailed(
            client=client,
            event_subscription_id=event_subscription_id,
            event_name=event_name,
            event_type=event_type,
            execution_id=execution_id,
            process_instance_id=process_instance_id,
            activity_id=activity_id,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
            include_event_subscriptions_without_tenant_id=include_event_subscriptions_without_tenant_id,
            sort_by=sort_by,
            sort_order=sort_order,
            first_result=first_result,
            max_results=max_results,
        )
    ).parsed
