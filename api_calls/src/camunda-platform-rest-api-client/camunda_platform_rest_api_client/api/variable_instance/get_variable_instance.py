from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.variable_instance_dto import VariableInstanceDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    deserialize_value: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/variable-instance/{id}".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, VariableInstanceDto]]:
    if response.status_code == 200:
        response_200 = VariableInstanceDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, VariableInstanceDto]]:
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
    deserialize_value: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, VariableInstanceDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        deserialize_value=deserialize_value,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    deserialize_value: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, VariableInstanceDto]]:
    """Retrieves a variable by id."""

    return sync_detailed(
        id=id,
        client=client,
        deserialize_value=deserialize_value,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    deserialize_value: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, VariableInstanceDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        deserialize_value=deserialize_value,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    deserialize_value: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, VariableInstanceDto]]:
    """Retrieves a variable by id."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            deserialize_value=deserialize_value,
        )
    ).parsed
