from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.get_start_form_variables_response_200 import GetStartFormVariablesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    variable_names: Union[Unset, None, str] = UNSET,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/process-definition/{id}/form-variables".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, GetStartFormVariablesResponse200]]:
    if response.status_code == 200:
        response_200 = GetStartFormVariablesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, GetStartFormVariablesResponse200]]:
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
    variable_names: Union[Unset, None, str] = UNSET,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Response[Union[ExceptionDto, GetStartFormVariablesResponse200]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        variable_names=variable_names,
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
    variable_names: Union[Unset, None, str] = UNSET,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Optional[Union[ExceptionDto, GetStartFormVariablesResponse200]]:
    """Retrieves the start form variables for a process definition
    (only if they are defined via the
    [Generated Task Form](https://docs.camunda.org/manual/7.15/user-guide/task-forms/#generated-task-forms) approach).
    The start form variables take form data specified on the start event into account.
    If form fields are defined, the variable types and default values
    of the form fields are taken into account."""

    return sync_detailed(
        id=id,
        client=client,
        variable_names=variable_names,
        deserialize_values=deserialize_values,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    variable_names: Union[Unset, None, str] = UNSET,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Response[Union[ExceptionDto, GetStartFormVariablesResponse200]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        variable_names=variable_names,
        deserialize_values=deserialize_values,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    variable_names: Union[Unset, None, str] = UNSET,
    deserialize_values: Union[Unset, None, bool] = True,
) -> Optional[Union[ExceptionDto, GetStartFormVariablesResponse200]]:
    """Retrieves the start form variables for a process definition
    (only if they are defined via the
    [Generated Task Form](https://docs.camunda.org/manual/7.15/user-guide/task-forms/#generated-task-forms) approach).
    The start form variables take form data specified on the start event into account.
    If form fields are defined, the variable types and default values
    of the form fields are taken into account."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            variable_names=variable_names,
            deserialize_values=deserialize_values,
        )
    ).parsed
