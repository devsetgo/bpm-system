from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.activity_statistics_result_dto import ActivityStatisticsResultDto
from ...models.exception_dto import ExceptionDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key: str,
    *,
    client: Client,
    failed_jobs: Union[Unset, None, bool] = UNSET,
    incidents: Union[Unset, None, bool] = UNSET,
    incidents_for_type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/process-definition/key/{key}/statistics".format(client.base_url, key=key)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "failedJobs": failed_jobs,
        "incidents": incidents,
        "incidentsForType": incidents_for_type,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[ActivityStatisticsResultDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ActivityStatisticsResultDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[ActivityStatisticsResultDto]]]:
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
    failed_jobs: Union[Unset, None, bool] = UNSET,
    incidents: Union[Unset, None, bool] = UNSET,
    incidents_for_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[ExceptionDto, List[ActivityStatisticsResultDto]]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
        failed_jobs=failed_jobs,
        incidents=incidents,
        incidents_for_type=incidents_for_type,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    key: str,
    *,
    client: Client,
    failed_jobs: Union[Unset, None, bool] = UNSET,
    incidents: Union[Unset, None, bool] = UNSET,
    incidents_for_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ExceptionDto, List[ActivityStatisticsResultDto]]]:
    """Retrieves runtime statistics of the latest version of the given process definition
    which belongs to no tenant, grouped by activities.
    These statistics include the number of running activity instances, optionally the number of failed jobs
    and also optionally the number of incidents either grouped by incident types or
    for a specific incident type.
    **Note**: This does not include historic data."""

    return sync_detailed(
        key=key,
        client=client,
        failed_jobs=failed_jobs,
        incidents=incidents,
        incidents_for_type=incidents_for_type,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: Client,
    failed_jobs: Union[Unset, None, bool] = UNSET,
    incidents: Union[Unset, None, bool] = UNSET,
    incidents_for_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[ExceptionDto, List[ActivityStatisticsResultDto]]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
        failed_jobs=failed_jobs,
        incidents=incidents,
        incidents_for_type=incidents_for_type,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    key: str,
    *,
    client: Client,
    failed_jobs: Union[Unset, None, bool] = UNSET,
    incidents: Union[Unset, None, bool] = UNSET,
    incidents_for_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ExceptionDto, List[ActivityStatisticsResultDto]]]:
    """Retrieves runtime statistics of the latest version of the given process definition
    which belongs to no tenant, grouped by activities.
    These statistics include the number of running activity instances, optionally the number of failed jobs
    and also optionally the number of incidents either grouped by incident types or
    for a specific incident type.
    **Note**: This does not include historic data."""

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            failed_jobs=failed_jobs,
            incidents=incidents,
            incidents_for_type=incidents_for_type,
        )
    ).parsed
