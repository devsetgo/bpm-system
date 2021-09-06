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
) -> Dict[str, Any]:
    url = "{}/user/count".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

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
) -> Response[Union[CountResultDto, ExceptionDto]]:
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
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for the number of deployments that fulfill given parameters. Takes the same parameters as the
    [Get Users](https://docs.camunda.org/manual/7.15/reference/rest/user/get-query/) method."""

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
) -> Response[Union[CountResultDto, ExceptionDto]]:
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
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for the number of deployments that fulfill given parameters. Takes the same parameters as the
    [Get Users](https://docs.camunda.org/manual/7.15/reference/rest/user/get-query/) method."""

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
        )
    ).parsed
