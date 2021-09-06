from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.get_query_groups_sort_by import GetQueryGroupsSortBy
from ...models.get_query_groups_sort_order import GetQueryGroupsSortOrder
from ...models.group_dto import GroupDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetQueryGroupsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetQueryGroupsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    member: Union[Unset, None, str] = UNSET,
    member_of_tenant: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/group".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params: Dict[str, Any] = {
        "sortBy": json_sort_by,
        "sortOrder": json_sort_order,
        "firstResult": first_result,
        "maxResults": max_results,
        "id": id,
        "idIn": id_in,
        "name": name,
        "nameLike": name_like,
        "type": type,
        "member": member,
        "memberOfTenant": member_of_tenant,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[GroupDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GroupDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[GroupDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetQueryGroupsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetQueryGroupsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    member: Union[Unset, None, str] = UNSET,
    member_of_tenant: Union[Unset, None, str] = UNSET,
) -> Response[Union[ExceptionDto, List[GroupDto]]]:
    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        id=id,
        id_in=id_in,
        name=name,
        name_like=name_like,
        type=type,
        member=member,
        member_of_tenant=member_of_tenant,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetQueryGroupsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetQueryGroupsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    member: Union[Unset, None, str] = UNSET,
    member_of_tenant: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ExceptionDto, List[GroupDto]]]:
    """Queries for a list of groups using a list of parameters. The size of the result set can be retrieved
    by using the [Get Group Count](https://docs.camunda.org/manual/7.15/reference/rest/group/get-query-count) method."""

    return sync_detailed(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        id=id,
        id_in=id_in,
        name=name,
        name_like=name_like,
        type=type,
        member=member,
        member_of_tenant=member_of_tenant,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetQueryGroupsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetQueryGroupsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    member: Union[Unset, None, str] = UNSET,
    member_of_tenant: Union[Unset, None, str] = UNSET,
) -> Response[Union[ExceptionDto, List[GroupDto]]]:
    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        id=id,
        id_in=id_in,
        name=name,
        name_like=name_like,
        type=type,
        member=member,
        member_of_tenant=member_of_tenant,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetQueryGroupsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetQueryGroupsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    member: Union[Unset, None, str] = UNSET,
    member_of_tenant: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ExceptionDto, List[GroupDto]]]:
    """Queries for a list of groups using a list of parameters. The size of the result set can be retrieved
    by using the [Get Group Count](https://docs.camunda.org/manual/7.15/reference/rest/group/get-query-count) method."""

    return (
        await asyncio_detailed(
            client=client,
            sort_by=sort_by,
            sort_order=sort_order,
            first_result=first_result,
            max_results=max_results,
            id=id,
            id_in=id_in,
            name=name,
            name_like=name_like,
            type=type,
            member=member,
            member_of_tenant=member_of_tenant,
        )
    ).parsed
