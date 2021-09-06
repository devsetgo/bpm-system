from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.process_instance_with_variables_dto import ProcessInstanceWithVariablesDto
from ...models.start_process_instance_dto import StartProcessInstanceDto
from ...types import Response


def _get_kwargs(
    key: str,
    *,
    client: Client,
    json_body: StartProcessInstanceDto,
) -> Dict[str, Any]:
    url = "{}/process-definition/key/{key}/start".format(client.base_url, key=key)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, ProcessInstanceWithVariablesDto]]:
    if response.status_code == 200:
        response_200 = ProcessInstanceWithVariablesDto.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = ExceptionDto.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, ProcessInstanceWithVariablesDto]]:
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
    json_body: StartProcessInstanceDto,
) -> Response[Union[ExceptionDto, ProcessInstanceWithVariablesDto]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    key: str,
    *,
    client: Client,
    json_body: StartProcessInstanceDto,
) -> Optional[Union[ExceptionDto, ProcessInstanceWithVariablesDto]]:
    """Instantiates a given process definition, starts the latest version of the process definition
    which belongs to no tenant.
    Process variables and business key may be supplied in the request body."""

    return sync_detailed(
        key=key,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: Client,
    json_body: StartProcessInstanceDto,
) -> Response[Union[ExceptionDto, ProcessInstanceWithVariablesDto]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    key: str,
    *,
    client: Client,
    json_body: StartProcessInstanceDto,
) -> Optional[Union[ExceptionDto, ProcessInstanceWithVariablesDto]]:
    """Instantiates a given process definition, starts the latest version of the process definition
    which belongs to no tenant.
    Process variables and business key may be supplied in the request body."""

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            json_body=json_body,
        )
    ).parsed
