from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.count_result_dto import CountResultDto
from ...models.exception_dto import ExceptionDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    user_member: Union[Unset, None, str] = UNSET,
    group_member: Union[Unset, None, str] = UNSET,
    including_groups_of_user: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/tenant/count".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "id": id,
        "name": name,
        "nameLike": name_like,
        "userMember": user_member,
        "groupMember": group_member,
        "includingGroupsOfUser": including_groups_of_user,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[CountResultDto, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = CountResultDto.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CountResultDto, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    user_member: Union[Unset, None, str] = UNSET,
    group_member: Union[Unset, None, str] = UNSET,
    including_groups_of_user: Union[Unset, None, bool] = UNSET,
) -> Response[Union[CountResultDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        name=name,
        name_like=name_like,
        user_member=user_member,
        group_member=group_member,
        including_groups_of_user=including_groups_of_user,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    user_member: Union[Unset, None, str] = UNSET,
    group_member: Union[Unset, None, str] = UNSET,
    including_groups_of_user: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Query for tenants using a list of parameters and retrieves the count."""

    return sync_detailed(
        client=client,
        id=id,
        name=name,
        name_like=name_like,
        user_member=user_member,
        group_member=group_member,
        including_groups_of_user=including_groups_of_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    user_member: Union[Unset, None, str] = UNSET,
    group_member: Union[Unset, None, str] = UNSET,
    including_groups_of_user: Union[Unset, None, bool] = UNSET,
) -> Response[Union[CountResultDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        name=name,
        name_like=name_like,
        user_member=user_member,
        group_member=group_member,
        including_groups_of_user=including_groups_of_user,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    user_member: Union[Unset, None, str] = UNSET,
    group_member: Union[Unset, None, str] = UNSET,
    including_groups_of_user: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Query for tenants using a list of parameters and retrieves the count."""

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            name=name,
            name_like=name_like,
            user_member=user_member,
            group_member=group_member,
            including_groups_of_user=including_groups_of_user,
        )
    ).parsed
