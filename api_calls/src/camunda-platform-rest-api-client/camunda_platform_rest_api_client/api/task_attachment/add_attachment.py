from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.attachment_dto import AttachmentDto
from ...models.authorization_exception_dto import AuthorizationExceptionDto
from ...models.exception_dto import ExceptionDto
from ...models.multi_form_attachment_dto import MultiFormAttachmentDto
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    multipart_data: MultiFormAttachmentDto,
) -> Dict[str, Any]:
    url = "{}/task/{id}/attachment/create".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[AttachmentDto, AuthorizationExceptionDto, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = AttachmentDto.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = AuthorizationExceptionDto.from_dict(response.json())

        return response_403
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[AttachmentDto, AuthorizationExceptionDto, ExceptionDto]]:
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
    multipart_data: MultiFormAttachmentDto,
) -> Response[Union[AttachmentDto, AuthorizationExceptionDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    multipart_data: MultiFormAttachmentDto,
) -> Optional[Union[AttachmentDto, AuthorizationExceptionDto, ExceptionDto]]:
    """Creates an attachment for a task."""

    return sync_detailed(
        id=id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    multipart_data: MultiFormAttachmentDto,
) -> Response[Union[AttachmentDto, AuthorizationExceptionDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    multipart_data: MultiFormAttachmentDto,
) -> Optional[Union[AttachmentDto, AuthorizationExceptionDto, ExceptionDto]]:
    """Creates an attachment for a task."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
