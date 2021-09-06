from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.process_instance_modification_dto import ProcessInstanceModificationDto
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: ProcessInstanceModificationDto,
) -> Dict[str, Any]:
    url = "{}/process-instance/{id}/modification".format(client.base_url, id=id)

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
    *,
    client: Client,
    json_body: ProcessInstanceModificationDto,
) -> Response[Union[Any, ExceptionDto]]:
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
) -> Optional[Union[Any, ExceptionDto]]:
    """Submits a list of modification instructions to change a process instance's execution state.
    A modification instruction is one of the following:

    * Starting execution before an activity
    * Starting execution after an activity on its single outgoing sequence flow
    * Starting execution on a specific sequence flow
    * Canceling an activity instance, transition instance, or all instances (activity or transition) for an activity

    Instructions are executed immediately and in the order they are provided in this request's body.
    Variables can be provided with every starting instruction.

    The exact semantics of modification can be read about in the [User guide](https://docs.camunda.org/manual/develop/user-guide/process-engine/process-instance-modification/)."""

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
) -> Response[Union[Any, ExceptionDto]]:
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
) -> Optional[Union[Any, ExceptionDto]]:
    """Submits a list of modification instructions to change a process instance's execution state.
    A modification instruction is one of the following:

    * Starting execution before an activity
    * Starting execution after an activity on its single outgoing sequence flow
    * Starting execution on a specific sequence flow
    * Canceling an activity instance, transition instance, or all instances (activity or transition) for an activity

    Instructions are executed immediately and in the order they are provided in this request's body.
    Variables can be provided with every starting instruction.

    The exact semantics of modification can be read about in the [User guide](https://docs.camunda.org/manual/develop/user-guide/process-engine/process-instance-modification/)."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
