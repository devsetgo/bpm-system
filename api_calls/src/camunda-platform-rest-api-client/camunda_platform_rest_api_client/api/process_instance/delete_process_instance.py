from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    skip_custom_listeners: Union[Unset, None, bool] = False,
    skip_io_mappings: Union[Unset, None, bool] = False,
    skip_subprocesses: Union[Unset, None, bool] = False,
    fail_if_not_exists: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/process-instance/{id}".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "skipCustomListeners": skip_custom_listeners,
        "skipIoMappings": skip_io_mappings,
        "skipSubprocesses": skip_subprocesses,
        "failIfNotExists": fail_if_not_exists,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ExceptionDto]]:
    if response.status_code == 204:
        response_204 = None

        return response_204
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
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
    skip_custom_listeners: Union[Unset, None, bool] = False,
    skip_io_mappings: Union[Unset, None, bool] = False,
    skip_subprocesses: Union[Unset, None, bool] = False,
    fail_if_not_exists: Union[Unset, None, bool] = True,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        skip_custom_listeners=skip_custom_listeners,
        skip_io_mappings=skip_io_mappings,
        skip_subprocesses=skip_subprocesses,
        fail_if_not_exists=fail_if_not_exists,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    skip_custom_listeners: Union[Unset, None, bool] = False,
    skip_io_mappings: Union[Unset, None, bool] = False,
    skip_subprocesses: Union[Unset, None, bool] = False,
    fail_if_not_exists: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, ExceptionDto]]:
    """Deletes a running process instance by id."""

    return sync_detailed(
        id=id,
        client=client,
        skip_custom_listeners=skip_custom_listeners,
        skip_io_mappings=skip_io_mappings,
        skip_subprocesses=skip_subprocesses,
        fail_if_not_exists=fail_if_not_exists,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    skip_custom_listeners: Union[Unset, None, bool] = False,
    skip_io_mappings: Union[Unset, None, bool] = False,
    skip_subprocesses: Union[Unset, None, bool] = False,
    fail_if_not_exists: Union[Unset, None, bool] = True,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        skip_custom_listeners=skip_custom_listeners,
        skip_io_mappings=skip_io_mappings,
        skip_subprocesses=skip_subprocesses,
        fail_if_not_exists=fail_if_not_exists,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    skip_custom_listeners: Union[Unset, None, bool] = False,
    skip_io_mappings: Union[Unset, None, bool] = False,
    skip_subprocesses: Union[Unset, None, bool] = False,
    fail_if_not_exists: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, ExceptionDto]]:
    """Deletes a running process instance by id."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            skip_custom_listeners=skip_custom_listeners,
            skip_io_mappings=skip_io_mappings,
            skip_subprocesses=skip_subprocesses,
            fail_if_not_exists=fail_if_not_exists,
        )
    ).parsed
