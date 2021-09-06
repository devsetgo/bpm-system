from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.authorization_exception_dto import AuthorizationExceptionDto
from ...models.exception_dto import ExceptionDto
from ...models.task_bpmn_error_dto import TaskBpmnErrorDto
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: TaskBpmnErrorDto,
) -> Dict[str, Any]:
    url = "{}/task/{id}/bpmnError".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    if response.status_code == 204:
        response_204 = None

        return response_204
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = AuthorizationExceptionDto.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
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
    json_body: TaskBpmnErrorDto,
) -> Response[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
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
    json_body: TaskBpmnErrorDto,
) -> Optional[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    """Reports a business error in the context of a running task by id. The error code must
    be specified to identify the BPMN error handler. See the documentation for
    [Reporting Bpmn Error](https://docs.camunda.org/manual/7.15/reference/bpmn20/tasks/user-task/#reporting-bpmn-error)
    in User Tasks."""

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: TaskBpmnErrorDto,
) -> Response[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
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
    json_body: TaskBpmnErrorDto,
) -> Optional[Union[Any, AuthorizationExceptionDto, ExceptionDto]]:
    """Reports a business error in the context of a running task by id. The error code must
    be specified to identify the BPMN error handler. See the documentation for
    [Reporting Bpmn Error](https://docs.camunda.org/manual/7.15/reference/bpmn20/tasks/user-task/#reporting-bpmn-error)
    in User Tasks."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
