from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/process-definition/{id}/rendered-form".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ExceptionDto]:
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[ExceptionDto]:
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
) -> Response[ExceptionDto]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
) -> Optional[ExceptionDto]:
    """Retrieves the rendered form for a process definition.
    This method can be used to get the HTML rendering of a
    [Generated Task Form](https://docs.camunda.org/manual/7.15/user-guide/task-forms/#generated-task-forms)."""

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[ExceptionDto]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> Optional[ExceptionDto]:
    """Retrieves the rendered form for a process definition.
    This method can be used to get the HTML rendering of a
    [Generated Task Form](https://docs.camunda.org/manual/7.15/user-guide/task-forms/#generated-task-forms)."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
