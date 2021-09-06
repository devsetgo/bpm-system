from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.authorization_exception_dto import AuthorizationExceptionDto
from ...models.exception_dto import ExceptionDto
from ...models.signal_dto import SignalDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SignalDto,
) -> Dict[str, Any]:
    url = "{}/signal".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    if response.status_code == 204:
        response_204 = None

        return response_204
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = AuthorizationExceptionDto.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = ExceptionDto.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SignalDto,
) -> Response[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: SignalDto,
) -> Optional[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    """A signal is an event of global scope (broadcast semantics) and is delivered to all
    active handlers. Internally this maps to the engine's signal event received builder
    method `RuntimeService#createSignalEvent()`. For more information about the signal
    behavior, see the [Signal Events](https://docs.camunda.org/manual/7.15/reference/bpmn20/events/signal-events/)
    section of the [BPMN 2.0 Implementation Reference](https://docs.camunda.org/manual/7.15/reference/bpmn20/)."""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SignalDto,
) -> Response[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SignalDto,
) -> Optional[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    """A signal is an event of global scope (broadcast semantics) and is delivered to all
    active handlers. Internally this maps to the engine's signal event received builder
    method `RuntimeService#createSignalEvent()`. For more information about the signal
    behavior, see the [Signal Events](https://docs.camunda.org/manual/7.15/reference/bpmn20/events/signal-events/)
    section of the [BPMN 2.0 Implementation Reference](https://docs.camunda.org/manual/7.15/reference/bpmn20/)."""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
