from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.identity_service_group_info_dto import IdentityServiceGroupInfoDto
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    user_id: str,
) -> Dict[str, Any]:
    url = "{}/identity/groups".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "userId": user_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, IdentityServiceGroupInfoDto]]:
    if response.status_code == 200:
        response_200 = IdentityServiceGroupInfoDto.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, IdentityServiceGroupInfoDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    user_id: str,
) -> Response[Union[ExceptionDto, IdentityServiceGroupInfoDto]]:
    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    user_id: str,
) -> Optional[Union[ExceptionDto, IdentityServiceGroupInfoDto]]:
    """Gets the groups of a user by id and includes all users that share a group with the
    given user."""

    return sync_detailed(
        client=client,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    user_id: str,
) -> Response[Union[ExceptionDto, IdentityServiceGroupInfoDto]]:
    kwargs = _get_kwargs(
        client=client,
        user_id=user_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    user_id: str,
) -> Optional[Union[ExceptionDto, IdentityServiceGroupInfoDto]]:
    """Gets the groups of a user by id and includes all users that share a group with the
    given user."""

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
        )
    ).parsed
