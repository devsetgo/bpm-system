import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.interval_name import IntervalName
from ...models.metrics_interval_result_dto import MetricsIntervalResultDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    name: Union[Unset, None, IntervalName] = UNSET,
    reporter: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    interval: Union[Unset, None, str] = 900,
    aggregate_by_reporter: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/metrics".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_name: Union[Unset, None, str] = UNSET
    if not isinstance(name, Unset):
        json_name = name.value if name else None

    json_start_date: Union[Unset, None, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat() if start_date else None

    json_end_date: Union[Unset, None, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat() if end_date else None

    params: Dict[str, Any] = {
        "name": json_name,
        "reporter": reporter,
        "startDate": json_start_date,
        "endDate": json_end_date,
        "firstResult": first_result,
        "maxResults": max_results,
        "interval": interval,
        "aggregateByReporter": aggregate_by_reporter,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[MetricsIntervalResultDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MetricsIntervalResultDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[MetricsIntervalResultDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    name: Union[Unset, None, IntervalName] = UNSET,
    reporter: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    interval: Union[Unset, None, str] = 900,
    aggregate_by_reporter: Union[Unset, None, str] = UNSET,
) -> Response[Union[ExceptionDto, List[MetricsIntervalResultDto]]]:
    kwargs = _get_kwargs(
        client=client,
        name=name,
        reporter=reporter,
        start_date=start_date,
        end_date=end_date,
        first_result=first_result,
        max_results=max_results,
        interval=interval,
        aggregate_by_reporter=aggregate_by_reporter,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    name: Union[Unset, None, IntervalName] = UNSET,
    reporter: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    interval: Union[Unset, None, str] = 900,
    aggregate_by_reporter: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ExceptionDto, List[MetricsIntervalResultDto]]]:
    """Retrieves a list of metrics, aggregated for a given interval."""

    return sync_detailed(
        client=client,
        name=name,
        reporter=reporter,
        start_date=start_date,
        end_date=end_date,
        first_result=first_result,
        max_results=max_results,
        interval=interval,
        aggregate_by_reporter=aggregate_by_reporter,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    name: Union[Unset, None, IntervalName] = UNSET,
    reporter: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    interval: Union[Unset, None, str] = 900,
    aggregate_by_reporter: Union[Unset, None, str] = UNSET,
) -> Response[Union[ExceptionDto, List[MetricsIntervalResultDto]]]:
    kwargs = _get_kwargs(
        client=client,
        name=name,
        reporter=reporter,
        start_date=start_date,
        end_date=end_date,
        first_result=first_result,
        max_results=max_results,
        interval=interval,
        aggregate_by_reporter=aggregate_by_reporter,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    name: Union[Unset, None, IntervalName] = UNSET,
    reporter: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    interval: Union[Unset, None, str] = 900,
    aggregate_by_reporter: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ExceptionDto, List[MetricsIntervalResultDto]]]:
    """Retrieves a list of metrics, aggregated for a given interval."""

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            reporter=reporter,
            start_date=start_date,
            end_date=end_date,
            first_result=first_result,
            max_results=max_results,
            interval=interval,
            aggregate_by_reporter=aggregate_by_reporter,
        )
    ).parsed
