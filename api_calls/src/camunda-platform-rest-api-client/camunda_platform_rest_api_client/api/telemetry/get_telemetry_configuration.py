from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.telemetry_configuration_dto import TelemetryConfigurationDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/telemetry/configuration".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, TelemetryConfigurationDto]]:
    if response.status_code == 200:
        response_200 = TelemetryConfigurationDto.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ExceptionDto.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, TelemetryConfigurationDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[ExceptionDto, TelemetryConfigurationDto]]:
    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[ExceptionDto, TelemetryConfigurationDto]]:
    """Fetches Telemetry Configuration."""

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[ExceptionDto, TelemetryConfigurationDto]]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[ExceptionDto, TelemetryConfigurationDto]]:
    """Fetches Telemetry Configuration."""

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
