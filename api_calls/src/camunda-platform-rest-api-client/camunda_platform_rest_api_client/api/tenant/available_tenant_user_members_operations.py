from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.resource_options_dto import ResourceOptionsDto
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/tenant/{id}/user-members".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ResourceOptionsDto]:
    if response.status_code == 200:
        response_200 = ResourceOptionsDto.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ResourceOptionsDto]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
) -> Response[ResourceOptionsDto]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.options(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
) -> Optional[ResourceOptionsDto]:
    """The OPTIONS request allows checking for the set of available operations that the
    currently authenticated user can perform on the resource. If the user
    can perform an operation or not may depend on various things,
    including the users authorizations to interact with this resource and
    the internal configuration of the process engine."""

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[ResourceOptionsDto]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.options(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> Optional[ResourceOptionsDto]:
    """The OPTIONS request allows checking for the set of available operations that the
    currently authenticated user can perform on the resource. If the user
    can perform an operation or not may depend on various things,
    including the users authorizations to interact with this resource and
    the internal configuration of the process engine."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
