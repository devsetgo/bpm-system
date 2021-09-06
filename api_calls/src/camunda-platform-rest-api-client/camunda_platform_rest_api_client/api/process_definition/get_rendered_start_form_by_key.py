from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...types import Response


def _get_kwargs(
    key: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/process-definition/key/{key}/rendered-form".format(client.base_url, key=key)

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
    key: str,
    *,
    client: Client,
) -> Response[ExceptionDto]:
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
) -> Optional[ExceptionDto]:
    """Retrieves  the rendered form for the latest version of the process definition which belongs to no tenant.
    This method can be used to get the HTML rendering of a
    [Generated Task Form](https://docs.camunda.org/manual/7.15/user-guide/task-forms/#generated-task-forms)."""

    return sync_detailed(
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: Client,
) -> Response[ExceptionDto]:
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
) -> Optional[ExceptionDto]:
    """Retrieves  the rendered form for the latest version of the process definition which belongs to no tenant.
    This method can be used to get the HTML rendering of a
    [Generated Task Form](https://docs.camunda.org/manual/7.15/user-guide/task-forms/#generated-task-forms)."""

    return (
        await asyncio_detailed(
            key=key,
            client=client,
        )
    ).parsed
