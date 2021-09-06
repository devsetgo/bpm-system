from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.multi_form_variable_binary_dto import MultiFormVariableBinaryDto
from ...types import Response


def _get_kwargs(
    id: str,
    var_name: str,
    *,
    client: Client,
    multipart_data: MultiFormVariableBinaryDto,
) -> Dict[str, Any]:
    url = "{}/execution/{id}/localVariables/{varName}/data".format(client.base_url, id=id, varName=var_name)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ExceptionDto]]:
    if response.status_code == 204:
        response_204 = None

        return response_204
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
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
    multipart_data: MultiFormVariableBinaryDto,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        var_name=var_name,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    var_name: str,
    *,
    client: Client,
    multipart_data: MultiFormVariableBinaryDto,
) -> Optional[Union[Any, ExceptionDto]]:
    """Sets the serialized value for a binary variable or the binary value for a file
    variable in the context of a given execution by id."""

    return sync_detailed(
        id=id,
        var_name=var_name,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    id: str,
    var_name: str,
    *,
    client: Client,
    multipart_data: MultiFormVariableBinaryDto,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        var_name=var_name,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    var_name: str,
    *,
    client: Client,
    multipart_data: MultiFormVariableBinaryDto,
) -> Optional[Union[Any, ExceptionDto]]:
    """Sets the serialized value for a binary variable or the binary value for a file
    variable in the context of a given execution by id."""

    return (
        await asyncio_detailed(
            id=id,
            var_name=var_name,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
