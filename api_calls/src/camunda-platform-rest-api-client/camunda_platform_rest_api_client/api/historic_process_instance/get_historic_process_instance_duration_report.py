import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.duration_report_result_dto import DurationReportResultDto
from ...models.exception_dto import ExceptionDto
from ...models.get_historic_process_instance_duration_report_period_unit import (
    GetHistoricProcessInstanceDurationReportPeriodUnit,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    report_type: str,
    period_unit: GetHistoricProcessInstanceDurationReportPeriodUnit,
    process_definition_id_in: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/history/process-instance/report".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_period_unit = period_unit.value

    json_started_before: Union[Unset, None, str] = UNSET
    if not isinstance(started_before, Unset):
        json_started_before = started_before.isoformat() if started_before else None

    json_started_after: Union[Unset, None, str] = UNSET
    if not isinstance(started_after, Unset):
        json_started_after = started_after.isoformat() if started_after else None

    params: Dict[str, Any] = {
        "reportType": report_type,
        "periodUnit": json_period_unit,
        "processDefinitionIdIn": process_definition_id_in,
        "processDefinitionKeyIn": process_definition_key_in,
        "startedBefore": json_started_before,
        "startedAfter": json_started_after,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[DurationReportResultDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DurationReportResultDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = ExceptionDto.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[DurationReportResultDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    report_type: str,
    period_unit: GetHistoricProcessInstanceDurationReportPeriodUnit,
    process_definition_id_in: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Union[ExceptionDto, List[DurationReportResultDto]]]:
    kwargs = _get_kwargs(
        client=client,
        report_type=report_type,
        period_unit=period_unit,
        process_definition_id_in=process_definition_id_in,
        process_definition_key_in=process_definition_key_in,
        started_before=started_before,
        started_after=started_after,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    report_type: str,
    period_unit: GetHistoricProcessInstanceDurationReportPeriodUnit,
    process_definition_id_in: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Union[ExceptionDto, List[DurationReportResultDto]]]:
    """Retrieves a report about the duration of completed process instances, grouped by a period.
    These reports include the maximum, minimum and average duration of all completed process instances which were started in a given period.

    **Note:** This only includes historic data."""

    return sync_detailed(
        client=client,
        report_type=report_type,
        period_unit=period_unit,
        process_definition_id_in=process_definition_id_in,
        process_definition_key_in=process_definition_key_in,
        started_before=started_before,
        started_after=started_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    report_type: str,
    period_unit: GetHistoricProcessInstanceDurationReportPeriodUnit,
    process_definition_id_in: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Union[ExceptionDto, List[DurationReportResultDto]]]:
    kwargs = _get_kwargs(
        client=client,
        report_type=report_type,
        period_unit=period_unit,
        process_definition_id_in=process_definition_id_in,
        process_definition_key_in=process_definition_key_in,
        started_before=started_before,
        started_after=started_after,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    report_type: str,
    period_unit: GetHistoricProcessInstanceDurationReportPeriodUnit,
    process_definition_id_in: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Union[ExceptionDto, List[DurationReportResultDto]]]:
    """Retrieves a report about the duration of completed process instances, grouped by a period.
    These reports include the maximum, minimum and average duration of all completed process instances which were started in a given period.

    **Note:** This only includes historic data."""

    return (
        await asyncio_detailed(
            client=client,
            report_type=report_type,
            period_unit=period_unit,
            process_definition_id_in=process_definition_id_in,
            process_definition_key_in=process_definition_key_in,
            started_before=started_before,
            started_after=started_after,
        )
    ).parsed
