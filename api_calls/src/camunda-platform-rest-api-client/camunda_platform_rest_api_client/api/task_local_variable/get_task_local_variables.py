from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.get_task_local_variables_response_200 import GetTaskLocalVariablesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/task/{id}/localVariables".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "deserializeValues": deserialize_values,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, GetTaskLocalVariablesResponse200]]:
    if response.status_code == 200:
        response_200 = GetTaskLocalVariablesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = ExceptionDto.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, GetTaskLocalVariablesResponse200]]:
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
    deserialize_values: Union[Unset, None, bool] = True,
) -> Response[Union[ExceptionDto, GetTaskLocalVariablesResponse200]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        deserialize_values=deserialize_values,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Optional[Union[ExceptionDto, GetTaskLocalVariablesResponse200]]:
    """Retrieves all variables of a given task by id."""

    return sync_detailed(
        id=id,
        client=client,
        deserialize_values=deserialize_values,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Response[Union[ExceptionDto, GetTaskLocalVariablesResponse200]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        deserialize_values=deserialize_values,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Optional[Union[ExceptionDto, GetTaskLocalVariablesResponse200]]:
    """Retrieves all variables of a given task by id."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            deserialize_values=deserialize_values,
        )
    ).parsed
