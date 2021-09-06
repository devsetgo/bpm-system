from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.batch_dto import BatchDto
from ...models.exception_dto import ExceptionDto
from ...models.set_job_retries_dto import SetJobRetriesDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SetJobRetriesDto,
) -> Dict[str, Any]:
    url = "{}/job/retries".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[BatchDto, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = BatchDto.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[BatchDto, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SetJobRetriesDto,
) -> Response[Union[BatchDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: SetJobRetriesDto,
) -> Optional[Union[BatchDto, ExceptionDto]]:
    """Create a batch to set retries of jobs asynchronously."""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SetJobRetriesDto,
) -> Response[Union[BatchDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SetJobRetriesDto,
) -> Optional[Union[BatchDto, ExceptionDto]]:
    """Create a batch to set retries of jobs asynchronously."""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
