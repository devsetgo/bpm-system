from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.authorization_exception_dto import AuthorizationExceptionDto
from ...models.exception_dto import ExceptionDto
from ...types import Response


def _get_kwargs(
    id: str,
    attachment_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/task/{id}/attachment/{attachmentId}".format(client.base_url, id=id, attachmentId=attachment_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    if response.status_code == 204:
        response_204 = None

        return response_204
    if response.status_code == 403:
        response_403 = AuthorizationExceptionDto.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
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
) -> Response[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        attachment_id=attachment_id,
        client=client,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    attachment_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    """Removes an attachment from a task by id."""

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
) -> Response[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        attachment_id=attachment_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    attachment_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    """Removes an attachment from a task by id."""

    return (
        await asyncio_detailed(
            id=id,
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
