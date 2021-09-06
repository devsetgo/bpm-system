from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.count_result_dto import CountResultDto
from ...models.exception_dto import ExceptionDto
from ...models.job_query_dto import JobQueryDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: JobQueryDto,
) -> Dict[str, Any]:
    url = "{}/job/count".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[CountResultDto, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = CountResultDto.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CountResultDto, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: JobQueryDto,
) -> Response[Union[CountResultDto, ExceptionDto]]:
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
    json_body: JobQueryDto,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for jobs that fulfill given parameters. This method takes the same message
    body as the [Get Jobs POST](https://docs.camunda.org/manual/7.15/reference/rest/job/post-
    query/) method and therefore it is slightly more powerful than the
    [Get Job Count](https://docs.camunda.org/manual/7.15/reference/rest/job/get-query-count/)
    method."""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: JobQueryDto,
) -> Response[Union[CountResultDto, ExceptionDto]]:
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
    json_body: JobQueryDto,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for jobs that fulfill given parameters. This method takes the same message
    body as the [Get Jobs POST](https://docs.camunda.org/manual/7.15/reference/rest/job/post-
    query/) method and therefore it is slightly more powerful than the
    [Get Job Count](https://docs.camunda.org/manual/7.15/reference/rest/job/get-query-count/)
    method."""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
