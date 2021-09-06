from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.count_result_dto import CountResultDto
from ...models.exception_dto import ExceptionDto
from ...models.get_event_subscriptions_count_event_type import GetEventSubscriptionsCountEventType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    event_subscription_id: Union[Unset, None, str] = UNSET,
    event_name: Union[Unset, None, str] = UNSET,
    event_type: Union[Unset, None, GetEventSubscriptionsCountEventType] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_event_subscriptions_without_tenant_id: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/event-subscription/count".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_event_type: Union[Unset, None, str] = UNSET
    if not isinstance(event_type, Unset):
        json_event_type = event_type.value if event_type else None

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
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[CountResultDto, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = CountResultDto.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CountResultDto, ExceptionDto]]:
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
    event_type: Union[Unset, None, GetEventSubscriptionsCountEventType] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_event_subscriptions_without_tenant_id: Union[Unset, None, bool] = UNSET,
) -> Response[Union[CountResultDto, ExceptionDto]]:
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
    event_type: Union[Unset, None, GetEventSubscriptionsCountEventType] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_event_subscriptions_without_tenant_id: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for the number of event subscriptions that fulfill given parameters.
    Takes the same parameters as the
    [Get Event Subscriptions](https://docs.camunda.org/manual/7.15/reference/rest/event-subscription/get-query/) method."""

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
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    event_subscription_id: Union[Unset, None, str] = UNSET,
    event_name: Union[Unset, None, str] = UNSET,
    event_type: Union[Unset, None, GetEventSubscriptionsCountEventType] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_event_subscriptions_without_tenant_id: Union[Unset, None, bool] = UNSET,
) -> Response[Union[CountResultDto, ExceptionDto]]:
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
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    event_subscription_id: Union[Unset, None, str] = UNSET,
    event_name: Union[Unset, None, str] = UNSET,
    event_type: Union[Unset, None, GetEventSubscriptionsCountEventType] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_event_subscriptions_without_tenant_id: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for the number of event subscriptions that fulfill given parameters.
    Takes the same parameters as the
    [Get Event Subscriptions](https://docs.camunda.org/manual/7.15/reference/rest/event-subscription/get-query/) method."""

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
        )
    ).parsed
