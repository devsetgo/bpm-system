from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.complete_task_dto import CompleteTaskDto
from ...models.exception_dto import ExceptionDto
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: CompleteTaskDto,
) -> Dict[str, Any]:
    url = "{}/task/{id}/resolve".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ExceptionDto]]:
    if response.status_code == 204:
        response_204 = None

        return response_204
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
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
    json_body: CompleteTaskDto,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: CompleteTaskDto,
) -> Optional[Union[Any, ExceptionDto]]:
    """Resolves a task and updates execution variables.

    Resolving a task marks that the assignee is done with the task delegated to them, and
    that it can be sent back to the owner. Can only be executed when the task has been
    delegated. The assignee will be set to the owner, who performed the delegation."""

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: CompleteTaskDto,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: CompleteTaskDto,
) -> Optional[Union[Any, ExceptionDto]]:
    """Resolves a task and updates execution variables.

    Resolving a task marks that the assignee is done with the task delegated to them, and
    that it can be sent back to the owner. Can only be executed when the task has been
    delegated. The assignee will be set to the owner, who performed the delegation."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
