from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.user_credentials_dto import UserCredentialsDto
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: UserCredentialsDto,
    password: str,
    authenticated_user_password: str,
) -> Dict[str, Any]:
    url = "{}/user/{id}/credentials".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "password": password,
        "authenticatedUserPassword": authenticated_user_password,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = response.json()

        return response_200
    if response.status_code == 403:
        response_403 = response.json()

        return response_403
    if response.status_code == 400:
        response_400 = response.json()

        return response_400
    if response.status_code == 404:
        response_404 = response.json()

        return response_404
    if response.status_code == 500:
        response_500 = ExceptionDto.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ExceptionDto]]:
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
    json_body: UserCredentialsDto,
    password: str,
    authenticated_user_password: str,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        password=password,
        authenticated_user_password=authenticated_user_password,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: UserCredentialsDto,
    password: str,
    authenticated_user_password: str,
) -> Optional[Union[Any, ExceptionDto]]:
    """Updates a user's credentials (password)"""

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        password=password,
        authenticated_user_password=authenticated_user_password,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: UserCredentialsDto,
    password: str,
    authenticated_user_password: str,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        password=password,
        authenticated_user_password=authenticated_user_password,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: UserCredentialsDto,
    password: str,
    authenticated_user_password: str,
) -> Optional[Union[Any, ExceptionDto]]:
    """Updates a user's credentials (password)"""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            password=password,
            authenticated_user_password=authenticated_user_password,
        )
    ).parsed
