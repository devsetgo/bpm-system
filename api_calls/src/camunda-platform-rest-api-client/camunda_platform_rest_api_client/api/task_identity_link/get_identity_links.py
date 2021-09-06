from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.identity_link_dto import IdentityLinkDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/task/{id}/identity-links".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "type": type,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[IdentityLinkDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IdentityLinkDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[IdentityLinkDto]]]:
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
    type: Union[Unset, None, str] = UNSET,
) -> Response[Union[ExceptionDto, List[IdentityLinkDto]]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        type=type,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ExceptionDto, List[IdentityLinkDto]]]:
    """Gets the identity links for a task by id, which are the users and groups that are in
    *some* relation to it (including assignee and owner)."""

    return sync_detailed(
        id=id,
        client=client,
        type=type,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    type: Union[Unset, None, str] = UNSET,
) -> Response[Union[ExceptionDto, List[IdentityLinkDto]]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        type=type,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ExceptionDto, List[IdentityLinkDto]]]:
    """Gets the identity links for a task by id, which are the users and groups that are in
    *some* relation to it (including assignee and owner)."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            type=type,
        )
    ).parsed
