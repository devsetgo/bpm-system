import datetime
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    date: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/metrics/task-worker".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_date: Union[Unset, None, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat() if date else None

    params: Dict[str, Any] = {
        "date": json_date,
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
    if response.status_code == 403:
        response_403 = ExceptionDto.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    date: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        date=date,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    date: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Union[Any, ExceptionDto]]:
    """Deletes all task worker metrics prior to the given date or all if no date is provided."""

    return sync_detailed(
        client=client,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    date: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        date=date,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    date: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Union[Any, ExceptionDto]]:
    """Deletes all task worker metrics prior to the given date or all if no date is provided."""

    return (
        await asyncio_detailed(
            client=client,
            date=date,
        )
    ).parsed
