from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...types import Response


def _get_kwargs(
    id: str,
    group_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/tenant/{id}/group-members/{groupId}".format(client.base_url, id=id, groupId=group_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ExceptionDto]]:
    if response.status_code == 204:
        response_204 = None

        return response_204
    if response.status_code == 403:
        response_403 = ExceptionDto.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = ExceptionDto.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    group_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        group_id=group_id,
        client=client,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    group_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ExceptionDto]]:
    """Creates a membership between a tenant and a group."""

    return sync_detailed(
        id=id,
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    group_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        group_id=group_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    group_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ExceptionDto]]:
    """Creates a membership between a tenant and a group."""

    return (
        await asyncio_detailed(
            id=id,
            group_id=group_id,
            client=client,
        )
    ).parsed
