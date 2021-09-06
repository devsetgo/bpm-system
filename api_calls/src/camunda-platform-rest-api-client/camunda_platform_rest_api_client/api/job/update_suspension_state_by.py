from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.job_suspension_state_dto import JobSuspensionStateDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: JobSuspensionStateDto,
) -> Dict[str, Any]:
    url = "{}/job/suspended".format(client.base_url)

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
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: JobSuspensionStateDto,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: JobSuspensionStateDto,
) -> Optional[Union[Any, ExceptionDto]]:
    """Activates or suspends jobs matching the given criterion.
    This can only be on of:
    * `jobDefinitionId`
    * `processDefinitionId`
    * `processInstanceId`
    * `processDefinitionKey`"""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: JobSuspensionStateDto,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: JobSuspensionStateDto,
) -> Optional[Union[Any, ExceptionDto]]:
    """Activates or suspends jobs matching the given criterion.
    This can only be on of:
    * `jobDefinitionId`
    * `processDefinitionId`
    * `processInstanceId`
    * `processDefinitionKey`"""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
