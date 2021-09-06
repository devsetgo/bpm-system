from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...types import File, Response


def _get_kwargs(
    id: str,
    attachment_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/task/{id}/attachment/{attachmentId}/data".format(client.base_url, id=id, attachmentId=attachment_id)

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
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
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
    attachment_id: str,
    *,
    client: Client,
) -> Response[Union[ExceptionDto, File]]:
    kwargs = _get_kwargs(
        id=id,
        attachment_id=attachment_id,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    attachment_id: str,
    *,
    client: Client,
) -> Optional[Union[ExceptionDto, File]]:
    """Retrieves the binary content of a task attachment by task id and attachment id."""

    return sync_detailed(
        id=id,
        attachment_id=attachment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    attachment_id: str,
    *,
    client: Client,
) -> Response[Union[ExceptionDto, File]]:
    kwargs = _get_kwargs(
        id=id,
        attachment_id=attachment_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    attachment_id: str,
    *,
    client: Client,
) -> Optional[Union[ExceptionDto, File]]:
    """Retrieves the binary content of a task attachment by task id and attachment id."""

    return (
        await asyncio_detailed(
            id=id,
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
