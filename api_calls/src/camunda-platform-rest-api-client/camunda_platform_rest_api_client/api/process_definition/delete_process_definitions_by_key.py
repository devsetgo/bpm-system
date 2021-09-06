from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.authorization_exception_dto import AuthorizationExceptionDto
from ...models.exception_dto import ExceptionDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key: str,
    *,
    client: Client,
    cascade: Union[Unset, None, bool] = UNSET,
    skip_custom_listeners: Union[Unset, None, bool] = False,
    skip_io_mappings: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/process-definition/key/{key}".format(client.base_url, key=key)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "cascade": cascade,
        "skipCustomListeners": skip_custom_listeners,
        "skipIoMappings": skip_io_mappings,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    if response.status_code == 204:
        response_204 = None

        return response_204
    if response.status_code == 403:
        response_403 = AuthorizationExceptionDto.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
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
    cascade: Union[Unset, None, bool] = UNSET,
    skip_custom_listeners: Union[Unset, None, bool] = False,
    skip_io_mappings: Union[Unset, None, bool] = False,
) -> Response[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
        cascade=cascade,
        skip_custom_listeners=skip_custom_listeners,
        skip_io_mappings=skip_io_mappings,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    key: str,
    *,
    client: Client,
    cascade: Union[Unset, None, bool] = UNSET,
    skip_custom_listeners: Union[Unset, None, bool] = False,
    skip_io_mappings: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    """Deletes process definitions by a given key which belong to no tenant id."""

    return sync_detailed(
        key=key,
        client=client,
        cascade=cascade,
        skip_custom_listeners=skip_custom_listeners,
        skip_io_mappings=skip_io_mappings,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: Client,
    cascade: Union[Unset, None, bool] = UNSET,
    skip_custom_listeners: Union[Unset, None, bool] = False,
    skip_io_mappings: Union[Unset, None, bool] = False,
) -> Response[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
        cascade=cascade,
        skip_custom_listeners=skip_custom_listeners,
        skip_io_mappings=skip_io_mappings,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    key: str,
    *,
    client: Client,
    cascade: Union[Unset, None, bool] = UNSET,
    skip_custom_listeners: Union[Unset, None, bool] = False,
    skip_io_mappings: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    """Deletes process definitions by a given key which belong to no tenant id."""

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            cascade=cascade,
            skip_custom_listeners=skip_custom_listeners,
            skip_io_mappings=skip_io_mappings,
        )
    ).parsed
