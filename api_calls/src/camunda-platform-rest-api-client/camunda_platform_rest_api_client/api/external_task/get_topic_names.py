from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    with_locked_tasks: Union[Unset, None, bool] = UNSET,
    with_unlocked_tasks: Union[Unset, None, bool] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/external-task/topic-names".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "withLockedTasks": with_locked_tasks,
        "withUnlockedTasks": with_unlocked_tasks,
        "withRetriesLeft": with_retries_left,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[str]]]:
    if response.status_code == 200:
        response_200 = cast(List[str], response.json())

        return response_200
    if response.status_code == 400:
        response_400 = response.json()

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[str]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    with_locked_tasks: Union[Unset, None, bool] = UNSET,
    with_unlocked_tasks: Union[Unset, None, bool] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List[str]]]:
    kwargs = _get_kwargs(
        client=client,
        with_locked_tasks=with_locked_tasks,
        with_unlocked_tasks=with_unlocked_tasks,
        with_retries_left=with_retries_left,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    with_locked_tasks: Union[Unset, None, bool] = UNSET,
    with_unlocked_tasks: Union[Unset, None, bool] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List[str]]]:
    """Queries for distinct topic names of external tasks that fulfill given parameters.
    Query can be restricted to only tasks with retries left, tasks that are locked, or tasks
    that are unlocked. The parameters withLockedTasks and withUnlockedTasks are
    exclusive. Setting them both to true will return an empty list.
    Providing no parameters will return a list of all distinct topic names with external tasks."""

    return sync_detailed(
        client=client,
        with_locked_tasks=with_locked_tasks,
        with_unlocked_tasks=with_unlocked_tasks,
        with_retries_left=with_retries_left,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    with_locked_tasks: Union[Unset, None, bool] = UNSET,
    with_unlocked_tasks: Union[Unset, None, bool] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List[str]]]:
    kwargs = _get_kwargs(
        client=client,
        with_locked_tasks=with_locked_tasks,
        with_unlocked_tasks=with_unlocked_tasks,
        with_retries_left=with_retries_left,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    with_locked_tasks: Union[Unset, None, bool] = UNSET,
    with_unlocked_tasks: Union[Unset, None, bool] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List[str]]]:
    """Queries for distinct topic names of external tasks that fulfill given parameters.
    Query can be restricted to only tasks with retries left, tasks that are locked, or tasks
    that are unlocked. The parameters withLockedTasks and withUnlockedTasks are
    exclusive. Setting them both to true will return an empty list.
    Providing no parameters will return a list of all distinct topic names with external tasks."""

    return (
        await asyncio_detailed(
            client=client,
            with_locked_tasks=with_locked_tasks,
            with_unlocked_tasks=with_unlocked_tasks,
            with_retries_left=with_retries_left,
        )
    ).parsed
