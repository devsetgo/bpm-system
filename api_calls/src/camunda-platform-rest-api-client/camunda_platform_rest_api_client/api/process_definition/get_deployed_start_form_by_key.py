from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.authorization_exception_dto import AuthorizationExceptionDto
from ...models.exception_dto import ExceptionDto
from ...types import Response


def _get_kwargs(
    key: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/process-definition/key/{key}/deployed-start-form".format(client.base_url, key=key)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[AuthorizationExceptionDto, ExceptionDto]]:
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = AuthorizationExceptionDto.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[AuthorizationExceptionDto, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: Client,
) -> Response[Union[AuthorizationExceptionDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    key: str,
    *,
    client: Client,
) -> Optional[Union[AuthorizationExceptionDto, ExceptionDto]]:
    """Retrieves the deployed form that can be referenced from a start event.
    For further information please refer to [User Guide](https://docs.camunda.org/manual/7.15/user-guide/task-forms/#embedded-task-forms)."""

    return sync_detailed(
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: Client,
) -> Response[Union[AuthorizationExceptionDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    key: str,
    *,
    client: Client,
) -> Optional[Union[AuthorizationExceptionDto, ExceptionDto]]:
    """Retrieves the deployed form that can be referenced from a start event.
    For further information please refer to [User Guide](https://docs.camunda.org/manual/7.15/user-guide/task-forms/#embedded-task-forms)."""

    return (
        await asyncio_detailed(
            key=key,
            client=client,
        )
    ).parsed
