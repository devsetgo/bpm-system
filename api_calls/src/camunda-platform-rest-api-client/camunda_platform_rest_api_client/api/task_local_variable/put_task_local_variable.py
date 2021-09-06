from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.variable_value_dto import VariableValueDto
from ...types import Response


def _get_kwargs(
    id: str,
    var_name: str,
    *,
    client: Client,
    json_body: VariableValueDto,
) -> Dict[str, Any]:
    url = "{}/task/{id}/localVariables/{varName}".format(client.base_url, id=id, varName=var_name)

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
    var_name: str,
    *,
    client: Client,
    json_body: VariableValueDto,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        var_name=var_name,
        client=client,
        json_body=json_body,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    var_name: str,
    *,
    client: Client,
    json_body: VariableValueDto,
) -> Optional[Union[Any, ExceptionDto]]:
    """Sets a variable in the context of a given task."""

    return sync_detailed(
        id=id,
        var_name=var_name,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    var_name: str,
    *,
    client: Client,
    json_body: VariableValueDto,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        var_name=var_name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    var_name: str,
    *,
    client: Client,
    json_body: VariableValueDto,
) -> Optional[Union[Any, ExceptionDto]]:
    """Sets a variable in the context of a given task."""

    return (
        await asyncio_detailed(
            id=id,
            var_name=var_name,
            client=client,
            json_body=json_body,
        )
    ).parsed
