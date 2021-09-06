from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.external_task_dto import ExternalTaskDto
from ...models.external_task_query_dto import ExternalTaskQueryDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: ExternalTaskQueryDto,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/external-task".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "firstResult": first_result,
        "maxResults": max_results,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[ExternalTaskDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ExternalTaskDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[ExternalTaskDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ExternalTaskQueryDto,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[ExternalTaskDto]]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        first_result=first_result,
        max_results=max_results,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: ExternalTaskQueryDto,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[ExternalTaskDto]]]:
    """Queries for external tasks that fulfill given parameters in the form of a JSON object.

    This method is slightly more powerful than the
    [Get External Tasks](https://docs.camunda.org/manual/7.15/reference/rest/external-task/get-query/) method because it allows to
    specify a hierarchical result sorting."""

    return sync_detailed(
        client=client,
        json_body=json_body,
        first_result=first_result,
        max_results=max_results,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: ExternalTaskQueryDto,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[ExternalTaskDto]]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        first_result=first_result,
        max_results=max_results,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: ExternalTaskQueryDto,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[ExternalTaskDto]]]:
    """Queries for external tasks that fulfill given parameters in the form of a JSON object.

    This method is slightly more powerful than the
    [Get External Tasks](https://docs.camunda.org/manual/7.15/reference/rest/external-task/get-query/) method because it allows to
    specify a hierarchical result sorting."""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            first_result=first_result,
            max_results=max_results,
        )
    ).parsed
