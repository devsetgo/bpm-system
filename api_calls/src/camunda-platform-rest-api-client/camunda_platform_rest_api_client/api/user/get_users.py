from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.get_users_sort_by import GetUsersSortBy
from ...models.get_users_sort_order import GetUsersSortOrder
from ...models.user_profile_dto import UserProfileDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    first_name: Union[Unset, None, str] = UNSET,
    first_name_like: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
    last_name_like: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    email_like: Union[Unset, None, str] = UNSET,
    member_of_group: Union[Unset, None, str] = UNSET,
    member_of_tenant: Union[Unset, None, str] = UNSET,
    potential_starter: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, GetUsersSortBy] = UNSET,
    sort_order: Union[Unset, None, GetUsersSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/user".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params: Dict[str, Any] = {
        "id": id,
        "idIn": id_in,
        "firstName": first_name,
        "firstNameLike": first_name_like,
        "lastName": last_name,
        "lastNameLike": last_name_like,
        "email": email,
        "emailLike": email_like,
        "memberOfGroup": member_of_group,
        "memberOfTenant": member_of_tenant,
        "potentialStarter": potential_starter,
        "sortBy": json_sort_by,
        "sortOrder": json_sort_order,
        "firstResult": first_result,
        "maxResults": max_results,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[UserProfileDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserProfileDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[UserProfileDto]]]:
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
    id_in: Union[Unset, None, str] = UNSET,
    first_name: Union[Unset, None, str] = UNSET,
    first_name_like: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
    last_name_like: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    email_like: Union[Unset, None, str] = UNSET,
    member_of_group: Union[Unset, None, str] = UNSET,
    member_of_tenant: Union[Unset, None, str] = UNSET,
    potential_starter: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, GetUsersSortBy] = UNSET,
    sort_order: Union[Unset, None, GetUsersSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[UserProfileDto]]]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        id_in=id_in,
        first_name=first_name,
        first_name_like=first_name_like,
        last_name=last_name,
        last_name_like=last_name_like,
        email=email,
        email_like=email_like,
        member_of_group=member_of_group,
        member_of_tenant=member_of_tenant,
        potential_starter=potential_starter,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    first_name: Union[Unset, None, str] = UNSET,
    first_name_like: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
    last_name_like: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    email_like: Union[Unset, None, str] = UNSET,
    member_of_group: Union[Unset, None, str] = UNSET,
    member_of_tenant: Union[Unset, None, str] = UNSET,
    potential_starter: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, GetUsersSortBy] = UNSET,
    sort_order: Union[Unset, None, GetUsersSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[UserProfileDto]]]:
    """Query for a list of users using a list of parameters.
    The size of the result set can be retrieved by using the Get User Count method.
    [Get User Count](https://docs.camunda.org/manual/7.15/reference/rest/user/get-query-count/) method."""

    return sync_detailed(
        client=client,
        id=id,
        id_in=id_in,
        first_name=first_name,
        first_name_like=first_name_like,
        last_name=last_name,
        last_name_like=last_name_like,
        email=email,
        email_like=email_like,
        member_of_group=member_of_group,
        member_of_tenant=member_of_tenant,
        potential_starter=potential_starter,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    first_name: Union[Unset, None, str] = UNSET,
    first_name_like: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
    last_name_like: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    email_like: Union[Unset, None, str] = UNSET,
    member_of_group: Union[Unset, None, str] = UNSET,
    member_of_tenant: Union[Unset, None, str] = UNSET,
    potential_starter: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, GetUsersSortBy] = UNSET,
    sort_order: Union[Unset, None, GetUsersSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[UserProfileDto]]]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        id_in=id_in,
        first_name=first_name,
        first_name_like=first_name_like,
        last_name=last_name,
        last_name_like=last_name_like,
        email=email,
        email_like=email_like,
        member_of_group=member_of_group,
        member_of_tenant=member_of_tenant,
        potential_starter=potential_starter,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    id_in: Union[Unset, None, str] = UNSET,
    first_name: Union[Unset, None, str] = UNSET,
    first_name_like: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
    last_name_like: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    email_like: Union[Unset, None, str] = UNSET,
    member_of_group: Union[Unset, None, str] = UNSET,
    member_of_tenant: Union[Unset, None, str] = UNSET,
    potential_starter: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, GetUsersSortBy] = UNSET,
    sort_order: Union[Unset, None, GetUsersSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[UserProfileDto]]]:
    """Query for a list of users using a list of parameters.
    The size of the result set can be retrieved by using the Get User Count method.
    [Get User Count](https://docs.camunda.org/manual/7.15/reference/rest/user/get-query-count/) method."""

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            id_in=id_in,
            first_name=first_name,
            first_name_like=first_name_like,
            last_name=last_name,
            last_name_like=last_name_like,
            email=email,
            email_like=email_like,
            member_of_group=member_of_group,
            member_of_tenant=member_of_tenant,
            potential_starter=potential_starter,
            sort_by=sort_by,
            sort_order=sort_order,
            first_result=first_result,
            max_results=max_results,
        )
    ).parsed
