from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.process_instance_dto import ProcessInstanceDto
from ...models.start_process_instance_form_dto import StartProcessInstanceFormDto
from ...types import Response


def _get_kwargs(
    key: str,
    *,
    client: Client,
    json_body: StartProcessInstanceFormDto,
) -> Dict[str, Any]:
    url = "{}/process-definition/key/{key}/submit-form".format(client.base_url, key=key)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, ProcessInstanceDto]]:
    if response.status_code == 200:
        response_200 = ProcessInstanceDto.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ExceptionDto.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, ProcessInstanceDto]]:
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
    json_body: StartProcessInstanceFormDto,
) -> Response[Union[ExceptionDto, ProcessInstanceDto]]:
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
    json_body: StartProcessInstanceFormDto,
) -> Optional[Union[ExceptionDto, ProcessInstanceDto]]:
    """Starts the latest version of the process definition which belongs to no tenant
    using a set of process variables and the business key.
    If the start event has Form Field Metadata defined, the process engine will perform backend validation
    for any form fields which have validators defined.
    See [Documentation on Generated Task Forms](https://docs.camunda.org/manual/7.15/user-guide/task-forms/#generated-task-forms)."""

    return sync_detailed(
        key=key,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: Client,
    json_body: StartProcessInstanceFormDto,
) -> Response[Union[ExceptionDto, ProcessInstanceDto]]:
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
    json_body: StartProcessInstanceFormDto,
) -> Optional[Union[ExceptionDto, ProcessInstanceDto]]:
    """Starts the latest version of the process definition which belongs to no tenant
    using a set of process variables and the business key.
    If the start event has Form Field Metadata defined, the process engine will perform backend validation
    for any form fields which have validators defined.
    See [Documentation on Generated Task Forms](https://docs.camunda.org/manual/7.15/user-guide/task-forms/#generated-task-forms)."""

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            json_body=json_body,
        )
    ).parsed
