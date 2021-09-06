from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.authorization_exception_dto import AuthorizationExceptionDto
from ...models.batch_dto import BatchDto
from ...models.exception_dto import ExceptionDto
from ...models.process_instance_modification_dto import ProcessInstanceModificationDto
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: ProcessInstanceModificationDto,
) -> Dict[str, Any]:
    url = "{}/process-instance/{id}/modification-async".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[AuthorizationExceptionDto, BatchDto, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = BatchDto.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = AuthorizationExceptionDto.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = ExceptionDto.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[AuthorizationExceptionDto, BatchDto, ExceptionDto]]:
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
    json_body: ProcessInstanceModificationDto,
) -> Response[Union[AuthorizationExceptionDto, BatchDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: ProcessInstanceModificationDto,
) -> Optional[Union[AuthorizationExceptionDto, BatchDto, ExceptionDto]]:
    """Submits a list of modification instructions to change a process instance's execution state async.
    A modification instruction is one of the following:

    * Starting execution before an activity
    * Starting execution after an activity on its single outgoing sequence flow
    * Starting execution on a specific sequence flow
    * Cancelling an activity instance, transition instance, or all instances (activity or transition) for an activity

    Instructions are executed asynchronous and in the order they are provided in this request's body.
    Variables can be provided with every starting instruction.

    The exact semantics of modification can be read about in the
    [User guide](https://docs.camunda.org/manual/7.15/user-guide/process-engine/process-instance-modification/)."""

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: ProcessInstanceModificationDto,
) -> Response[Union[AuthorizationExceptionDto, BatchDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: ProcessInstanceModificationDto,
) -> Optional[Union[AuthorizationExceptionDto, BatchDto, ExceptionDto]]:
    """Submits a list of modification instructions to change a process instance's execution state async.
    A modification instruction is one of the following:

    * Starting execution before an activity
    * Starting execution after an activity on its single outgoing sequence flow
    * Starting execution on a specific sequence flow
    * Cancelling an activity instance, transition instance, or all instances (activity or transition) for an activity

    Instructions are executed asynchronous and in the order they are provided in this request's body.
    Variables can be provided with every starting instruction.

    The exact semantics of modification can be read about in the
    [User guide](https://docs.camunda.org/manual/7.15/user-guide/process-engine/process-instance-modification/)."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
