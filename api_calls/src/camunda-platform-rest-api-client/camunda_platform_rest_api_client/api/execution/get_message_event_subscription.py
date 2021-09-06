from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.event_subscription_dto import EventSubscriptionDto
from ...models.exception_dto import ExceptionDto
from ...types import Response


def _get_kwargs(
    id: str,
    message_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/execution/{id}/messageSubscriptions/{messageName}".format(
        client.base_url, id=id, messageName=message_name
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[EventSubscriptionDto, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = EventSubscriptionDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[EventSubscriptionDto, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    message_name: str,
    *,
    client: Client,
) -> Response[Union[EventSubscriptionDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        message_name=message_name,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    message_name: str,
    *,
    client: Client,
) -> Optional[Union[EventSubscriptionDto, ExceptionDto]]:
    """Retrieves a message event subscription for a given execution by id and a message
    name."""

    return sync_detailed(
        id=id,
        message_name=message_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    message_name: str,
    *,
    client: Client,
) -> Response[Union[EventSubscriptionDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        message_name=message_name,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    message_name: str,
    *,
    client: Client,
) -> Optional[Union[EventSubscriptionDto, ExceptionDto]]:
    """Retrieves a message event subscription for a given execution by id and a message
    name."""

    return (
        await asyncio_detailed(
            id=id,
            message_name=message_name,
            client=client,
        )
    ).parsed
