from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.fetch_external_tasks_dto import FetchExternalTasksDto
from ...models.locked_external_task_dto import LockedExternalTaskDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: FetchExternalTasksDto,
) -> Dict[str, Any]:
    url = "{}/external-task/fetchAndLock".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[LockedExternalTaskDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LockedExternalTaskDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[LockedExternalTaskDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: FetchExternalTasksDto,
) -> Response[Union[ExceptionDto, List[LockedExternalTaskDto]]]:
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
    json_body: FetchExternalTasksDto,
) -> Optional[Union[ExceptionDto, List[LockedExternalTaskDto]]]:
    """Fetches and locks a specific number of external tasks for execution by a worker. Query can be restricted
    to specific task topics and for each task topic an individual lock time can be provided."""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: FetchExternalTasksDto,
) -> Response[Union[ExceptionDto, List[LockedExternalTaskDto]]]:
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
    json_body: FetchExternalTasksDto,
) -> Optional[Union[ExceptionDto, List[LockedExternalTaskDto]]]:
    """Fetches and locks a specific number of external tasks for execution by a worker. Query can be restricted
    to specific task topics and for each task topic an individual lock time can be provided."""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
