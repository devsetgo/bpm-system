from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...types import File, Response


def _get_kwargs(
    id: str,
    resource_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/deployment/{id}/resources/{resourceId}/data".format(client.base_url, id=id, resourceId=resource_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, File]]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, File]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    resource_id: str,
    *,
    client: Client,
) -> Response[Union[ExceptionDto, File]]:
    kwargs = _get_kwargs(
        id=id,
        resource_id=resource_id,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    resource_id: str,
    *,
    client: Client,
) -> Optional[Union[ExceptionDto, File]]:
    """Retrieves the binary content of a deployment resource for the given deployment by id."""

    return sync_detailed(
        id=id,
        resource_id=resource_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    resource_id: str,
    *,
    client: Client,
) -> Response[Union[ExceptionDto, File]]:
    kwargs = _get_kwargs(
        id=id,
        resource_id=resource_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    resource_id: str,
    *,
    client: Client,
) -> Optional[Union[ExceptionDto, File]]:
    """Retrieves the binary content of a deployment resource for the given deployment by id."""

    return (
        await asyncio_detailed(
            id=id,
            resource_id=resource_id,
            client=client,
        )
    ).parsed
