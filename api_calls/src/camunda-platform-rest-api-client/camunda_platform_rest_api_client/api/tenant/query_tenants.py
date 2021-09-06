from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.query_tenants_sort_by import QueryTenantsSortBy
from ...models.query_tenants_sort_order import QueryTenantsSortOrder
from ...models.tenant_dto import TenantDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    sort_by: Union[Unset, None, QueryTenantsSortBy] = UNSET,
    sort_order: Union[Unset, None, QueryTenantsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    user_member: Union[Unset, None, str] = UNSET,
    group_member: Union[Unset, None, str] = UNSET,
    including_groups_of_user: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/tenant".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[TenantDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TenantDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[TenantDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, QueryTenantsSortBy] = UNSET,
    sort_order: Union[Unset, None, QueryTenantsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    user_member: Union[Unset, None, str] = UNSET,
    group_member: Union[Unset, None, str] = UNSET,
    including_groups_of_user: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[TenantDto]]]:
    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
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
    sort_by: Union[Unset, None, QueryTenantsSortBy] = UNSET,
    sort_order: Union[Unset, None, QueryTenantsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    user_member: Union[Unset, None, str] = UNSET,
    group_member: Union[Unset, None, str] = UNSET,
    including_groups_of_user: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[TenantDto]]]:
    """Query for a list of tenants using a list of parameters. The size of the result set
    can be retrieved by using the [Get Tenant
    Count](https://docs.camunda.org/manual/7.15/reference/rest/tenant/get-query-count/) method."""

    return sync_detailed(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
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
    sort_by: Union[Unset, None, QueryTenantsSortBy] = UNSET,
    sort_order: Union[Unset, None, QueryTenantsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    user_member: Union[Unset, None, str] = UNSET,
    group_member: Union[Unset, None, str] = UNSET,
    including_groups_of_user: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[TenantDto]]]:
    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
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
    sort_by: Union[Unset, None, QueryTenantsSortBy] = UNSET,
    sort_order: Union[Unset, None, QueryTenantsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    user_member: Union[Unset, None, str] = UNSET,
    group_member: Union[Unset, None, str] = UNSET,
    including_groups_of_user: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[TenantDto]]]:
    """Query for a list of tenants using a list of parameters. The size of the result set
    can be retrieved by using the [Get Tenant
    Count](https://docs.camunda.org/manual/7.15/reference/rest/tenant/get-query-count/) method."""

    return (
        await asyncio_detailed(
            client=client,
            sort_by=sort_by,
            sort_order=sort_order,
            first_result=first_result,
            max_results=max_results,
            id=id,
            name=name,
            name_like=name_like,
            user_member=user_member,
            group_member=group_member,
            including_groups_of_user=including_groups_of_user,
        )
    ).parsed
