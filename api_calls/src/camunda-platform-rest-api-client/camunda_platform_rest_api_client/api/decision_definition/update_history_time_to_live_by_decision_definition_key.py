from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.history_time_to_live_dto import HistoryTimeToLiveDto
from ...types import Response


def _get_kwargs(
    key: str,
    *,
    client: Client,
    json_body: HistoryTimeToLiveDto,
) -> Dict[str, Any]:
    url = "{}/decision-definition/key/{key}/history-time-to-live".format(client.base_url, key=key)

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
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ExceptionDto]]:
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
    json_body: HistoryTimeToLiveDto,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
        json_body=json_body,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    key: str,
    *,
    client: Client,
    json_body: HistoryTimeToLiveDto,
) -> Optional[Union[Any, ExceptionDto]]:
    """Updates the latest version of the decision definition which belongs to no tenant.
    The field is used within [History cleanup](https://docs.camunda.org/manual/7.15/user-guide/process-engine/history/#history-cleanup)."""

    return sync_detailed(
        key=key,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: Client,
    json_body: HistoryTimeToLiveDto,
) -> Response[Union[Any, ExceptionDto]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    key: str,
    *,
    client: Client,
    json_body: HistoryTimeToLiveDto,
) -> Optional[Union[Any, ExceptionDto]]:
    """Updates the latest version of the decision definition which belongs to no tenant.
    The field is used within [History cleanup](https://docs.camunda.org/manual/7.15/user-guide/process-engine/history/#history-cleanup)."""

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            json_body=json_body,
        )
    ).parsed
