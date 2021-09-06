from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.get_start_form_variables_by_key_response_200 import GetStartFormVariablesByKeyResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key: str,
    *,
    client: Client,
    variable_names: Union[Unset, None, str] = UNSET,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/process-definition/key/{key}/form-variables".format(client.base_url, key=key)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "variableNames": variable_names,
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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ExceptionDto, GetStartFormVariablesByKeyResponse200]]:
    if response.status_code == 200:
        response_200 = GetStartFormVariablesByKeyResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ExceptionDto, GetStartFormVariablesByKeyResponse200]]:
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
    variable_names: Union[Unset, None, str] = UNSET,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Response[Union[ExceptionDto, GetStartFormVariablesByKeyResponse200]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
        variable_names=variable_names,
        deserialize_values=deserialize_values,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    key: str,
    *,
    client: Client,
    variable_names: Union[Unset, None, str] = UNSET,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Optional[Union[ExceptionDto, GetStartFormVariablesByKeyResponse200]]:
    """Retrieves the start form variables for the latest process definition which belongs to no tenant
    (only if they are defined via the
    [Generated Task Form](https://docs.camunda.org/manual/7.15/user-guide/task-forms/#generated-task-forms) approach).
    The start form variables take form data specified on the start event into account.
    If form fields are defined, the variable types and default values
    of the form fields are taken into account."""

    return sync_detailed(
        key=key,
        client=client,
        variable_names=variable_names,
        deserialize_values=deserialize_values,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: Client,
    variable_names: Union[Unset, None, str] = UNSET,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Response[Union[ExceptionDto, GetStartFormVariablesByKeyResponse200]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
        variable_names=variable_names,
        deserialize_values=deserialize_values,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    key: str,
    *,
    client: Client,
    variable_names: Union[Unset, None, str] = UNSET,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Optional[Union[ExceptionDto, GetStartFormVariablesByKeyResponse200]]:
    """Retrieves the start form variables for the latest process definition which belongs to no tenant
    (only if they are defined via the
    [Generated Task Form](https://docs.camunda.org/manual/7.15/user-guide/task-forms/#generated-task-forms) approach).
    The start form variables take form data specified on the start event into account.
    If form fields are defined, the variable types and default values
    of the form fields are taken into account."""

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            variable_names=variable_names,
            deserialize_values=deserialize_values,
        )
    ).parsed
