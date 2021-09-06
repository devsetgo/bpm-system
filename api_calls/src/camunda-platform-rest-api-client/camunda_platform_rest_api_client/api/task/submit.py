from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.complete_task_dto import CompleteTaskDto
from ...models.exception_dto import ExceptionDto
from ...models.submit_response_200 import SubmitResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: CompleteTaskDto,
) -> Dict[str, Any]:
    url = "{}/task/{id}/submit-form".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ExceptionDto, SubmitResponse200]]:
    if response.status_code == 200:
        response_200 = SubmitResponse200.from_dict(response.json())

        return response_200
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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ExceptionDto, SubmitResponse200]]:
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
    json_body: CompleteTaskDto,
) -> Response[Union[Any, ExceptionDto, SubmitResponse200]]:
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
    json_body: CompleteTaskDto,
) -> Optional[Union[Any, ExceptionDto, SubmitResponse200]]:
    """Completes a task and updates process variables using a form submit. There are two
    difference between this method and the `complete` method:

    * If the task is in state `PENDING` - i.e., has been delegated before, it is not
    completed but resolved. Otherwise it will be completed.
    * If the task has Form Field Metadata defined, the process engine will perform backend
    validation for any form fields which have validators defined.
    See the
    [Generated Task Forms](https://docs.camunda.org/manual/7.15/user-guide/task-forms/_index/#generated-task-forms)
    section of the [User Guide](https://docs.camunda.org/manual/7.15/user-guide/) for more information."""

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: CompleteTaskDto,
) -> Response[Union[Any, ExceptionDto, SubmitResponse200]]:
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
    json_body: CompleteTaskDto,
) -> Optional[Union[Any, ExceptionDto, SubmitResponse200]]:
    """Completes a task and updates process variables using a form submit. There are two
    difference between this method and the `complete` method:

    * If the task is in state `PENDING` - i.e., has been delegated before, it is not
    completed but resolved. Otherwise it will be completed.
    * If the task has Form Field Metadata defined, the process engine will perform backend
    validation for any form fields which have validators defined.
    See the
    [Generated Task Forms](https://docs.camunda.org/manual/7.15/user-guide/task-forms/_index/#generated-task-forms)
    section of the [User Guide](https://docs.camunda.org/manual/7.15/user-guide/) for more information."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
