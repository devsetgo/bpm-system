from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.comment_dto import CommentDto
from ...models.exception_dto import ExceptionDto
from ...types import Response


def _get_kwargs(
    id: str,
    comment_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/task/{id}/comment/{commentId}".format(client.base_url, id=id, commentId=comment_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[CommentDto, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = CommentDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CommentDto, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    comment_id: str,
    *,
    client: Client,
) -> Response[Union[CommentDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        comment_id=comment_id,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    comment_id: str,
    *,
    client: Client,
) -> Optional[Union[CommentDto, ExceptionDto]]:
    """Retrieves a task comment by task id and comment id."""

    return sync_detailed(
        id=id,
        comment_id=comment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    comment_id: str,
    *,
    client: Client,
) -> Response[Union[CommentDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        comment_id=comment_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    comment_id: str,
    *,
    client: Client,
) -> Optional[Union[CommentDto, ExceptionDto]]:
    """Retrieves a task comment by task id and comment id."""

    return (
        await asyncio_detailed(
            id=id,
            comment_id=comment_id,
            client=client,
        )
    ).parsed
