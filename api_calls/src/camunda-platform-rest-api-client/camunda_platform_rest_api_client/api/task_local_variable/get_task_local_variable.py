from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.variable_value_dto import VariableValueDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    var_name: str,
    *,
    client: Client,
    deserialize_value: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/task/{id}/localVariables/{varName}".format(client.base_url, id=id, varName=var_name)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "deserializeValue": deserialize_value,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, VariableValueDto]]:
    if response.status_code == 200:
        response_200 = VariableValueDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ExceptionDto.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, VariableValueDto]]:
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
    deserialize_value: Union[Unset, None, bool] = True,
) -> Response[Union[ExceptionDto, VariableValueDto]]:
    kwargs = _get_kwargs(
        id=id,
        var_name=var_name,
        client=client,
        deserialize_value=deserialize_value,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    var_name: str,
    *,
    client: Client,
    deserialize_value: Union[Unset, None, bool] = True,
) -> Optional[Union[ExceptionDto, VariableValueDto]]:
    """Retrieves a variable from the context of a given task by id."""

    return sync_detailed(
        id=id,
        var_name=var_name,
        client=client,
        deserialize_value=deserialize_value,
    ).parsed


async def asyncio_detailed(
    id: str,
    var_name: str,
    *,
    client: Client,
    deserialize_value: Union[Unset, None, bool] = True,
) -> Response[Union[ExceptionDto, VariableValueDto]]:
    kwargs = _get_kwargs(
        id=id,
        var_name=var_name,
        client=client,
        deserialize_value=deserialize_value,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    var_name: str,
    *,
    client: Client,
    deserialize_value: Union[Unset, None, bool] = True,
) -> Optional[Union[ExceptionDto, VariableValueDto]]:
    """Retrieves a variable from the context of a given task by id."""

    return (
        await asyncio_detailed(
            id=id,
            var_name=var_name,
            client=client,
            deserialize_value=deserialize_value,
        )
    ).parsed
