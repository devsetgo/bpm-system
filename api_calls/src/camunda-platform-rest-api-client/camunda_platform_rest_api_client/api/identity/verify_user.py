from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.authentication_result import AuthenticationResult
from ...models.basic_user_credentials_dto import BasicUserCredentialsDto
from ...models.exception_dto import ExceptionDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: BasicUserCredentialsDto,
) -> Dict[str, Any]:
    url = "{}/identity/verify".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[AuthenticationResult, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = AuthenticationResult.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[AuthenticationResult, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: BasicUserCredentialsDto,
) -> Response[Union[AuthenticationResult, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: BasicUserCredentialsDto,
) -> Optional[Union[AuthenticationResult, ExceptionDto]]:
    """Verifies that user credentials are valid."""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: BasicUserCredentialsDto,
) -> Response[Union[AuthenticationResult, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: BasicUserCredentialsDto,
) -> Optional[Union[AuthenticationResult, ExceptionDto]]:
    """Verifies that user credentials are valid."""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
