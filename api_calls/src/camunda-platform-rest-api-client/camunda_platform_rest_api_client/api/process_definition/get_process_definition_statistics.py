from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.process_definition_statistics_result_dto import ProcessDefinitionStatisticsResultDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    failed_jobs: Union[Unset, None, bool] = UNSET,
    incidents: Union[Unset, None, bool] = UNSET,
    incidents_for_type: Union[Unset, None, str] = UNSET,
    root_incidents: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/process-definition/statistics".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "failedJobs": failed_jobs,
        "incidents": incidents,
        "incidentsForType": incidents_for_type,
        "rootIncidents": root_incidents,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ExceptionDto, List[ProcessDefinitionStatisticsResultDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProcessDefinitionStatisticsResultDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ExceptionDto, List[ProcessDefinitionStatisticsResultDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    failed_jobs: Union[Unset, None, bool] = UNSET,
    incidents: Union[Unset, None, bool] = UNSET,
    incidents_for_type: Union[Unset, None, str] = UNSET,
    root_incidents: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[ProcessDefinitionStatisticsResultDto]]]:
    kwargs = _get_kwargs(
        client=client,
        failed_jobs=failed_jobs,
        incidents=incidents,
        incidents_for_type=incidents_for_type,
        root_incidents=root_incidents,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    failed_jobs: Union[Unset, None, bool] = UNSET,
    incidents: Union[Unset, None, bool] = UNSET,
    incidents_for_type: Union[Unset, None, str] = UNSET,
    root_incidents: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[ProcessDefinitionStatisticsResultDto]]]:
    """Retrieves runtime statistics of the process engine, grouped by process definitions.
    These statistics include the number of running process instances, optionally the number of failed jobs
    and also optionally the number of incidents either grouped by incident types or
    for a specific incident type.
    **Note**: This does not include historic data."""

    return sync_detailed(
        client=client,
        failed_jobs=failed_jobs,
        incidents=incidents,
        incidents_for_type=incidents_for_type,
        root_incidents=root_incidents,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    failed_jobs: Union[Unset, None, bool] = UNSET,
    incidents: Union[Unset, None, bool] = UNSET,
    incidents_for_type: Union[Unset, None, str] = UNSET,
    root_incidents: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[ProcessDefinitionStatisticsResultDto]]]:
    kwargs = _get_kwargs(
        client=client,
        failed_jobs=failed_jobs,
        incidents=incidents,
        incidents_for_type=incidents_for_type,
        root_incidents=root_incidents,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    failed_jobs: Union[Unset, None, bool] = UNSET,
    incidents: Union[Unset, None, bool] = UNSET,
    incidents_for_type: Union[Unset, None, str] = UNSET,
    root_incidents: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[ProcessDefinitionStatisticsResultDto]]]:
    """Retrieves runtime statistics of the process engine, grouped by process definitions.
    These statistics include the number of running process instances, optionally the number of failed jobs
    and also optionally the number of incidents either grouped by incident types or
    for a specific incident type.
    **Note**: This does not include historic data."""

    return (
        await asyncio_detailed(
            client=client,
            failed_jobs=failed_jobs,
            incidents=incidents,
            incidents_for_type=incidents_for_type,
            root_incidents=root_incidents,
        )
    ).parsed
