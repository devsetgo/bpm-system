from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...types import Response


def _get_kwargs(
    id: str,
    var_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/task/{id}/variables/{varName}".format(client.base_url, id=id, varName=var_name)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ExceptionDto]]:
    if response.status_code == 204:
        response_204 = None

        return response_204
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
    var_name: str,
    *,
    client: Client,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        var_name=var_name,
        client=client,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    var_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, ExceptionDto]]:
    """Removes a variable that is visible to a task. A variable is visible to a task if it is a local task
    variable or declared in a parent scope of the task. See documentation on
    [visiblity of variables](https://docs.camunda.org/manual/7.15/user-guide/process-engine/variables/)."""

    return sync_detailed(
        id=id,
        var_name=var_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    var_name: str,
    *,
    client: Client,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        var_name=var_name,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    var_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, ExceptionDto]]:
    """Removes a variable that is visible to a task. A variable is visible to a task if it is a local task
    variable or declared in a parent scope of the task. See documentation on
    [visiblity of variables](https://docs.camunda.org/manual/7.15/user-guide/process-engine/variables/)."""

    return (
        await asyncio_detailed(
            id=id,
            var_name=var_name,
            client=client,
        )
    ).parsed
