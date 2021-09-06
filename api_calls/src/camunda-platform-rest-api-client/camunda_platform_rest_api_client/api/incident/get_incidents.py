import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.get_incidents_sort_by import GetIncidentsSortBy
from ...models.get_incidents_sort_order import GetIncidentsSortOrder
from ...models.incident_dto import IncidentDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    incident_timestamp_before: Union[Unset, None, datetime.datetime] = UNSET,
    incident_timestamp_after: Union[Unset, None, datetime.datetime] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    failed_activity_id: Union[Unset, None, str] = UNSET,
    cause_incident_id: Union[Unset, None, str] = UNSET,
    root_cause_incident_id: Union[Unset, None, str] = UNSET,
    configuration: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    job_definition_id_in: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, GetIncidentsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetIncidentsSortOrder] = UNSET,
) -> Dict[str, Any]:
    url = "{}/incident".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_incident_timestamp_before: Union[Unset, None, str] = UNSET
    if not isinstance(incident_timestamp_before, Unset):
        json_incident_timestamp_before = incident_timestamp_before.isoformat() if incident_timestamp_before else None

    json_incident_timestamp_after: Union[Unset, None, str] = UNSET
    if not isinstance(incident_timestamp_after, Unset):
        json_incident_timestamp_after = incident_timestamp_after.isoformat() if incident_timestamp_after else None

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params: Dict[str, Any] = {
        "incidentId": incident_id,
        "incidentType": incident_type,
        "incidentMessage": incident_message,
        "incidentMessageLike": incident_message_like,
        "processDefinitionId": process_definition_id,
        "processDefinitionKeyIn": process_definition_key_in,
        "processInstanceId": process_instance_id,
        "executionId": execution_id,
        "incidentTimestampBefore": json_incident_timestamp_before,
        "incidentTimestampAfter": json_incident_timestamp_after,
        "activityId": activity_id,
        "failedActivityId": failed_activity_id,
        "causeIncidentId": cause_incident_id,
        "rootCauseIncidentId": root_cause_incident_id,
        "configuration": configuration,
        "tenantIdIn": tenant_id_in,
        "jobDefinitionIdIn": job_definition_id_in,
        "sortBy": json_sort_by,
        "sortOrder": json_sort_order,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[IncidentDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IncidentDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[IncidentDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    incident_timestamp_before: Union[Unset, None, datetime.datetime] = UNSET,
    incident_timestamp_after: Union[Unset, None, datetime.datetime] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    failed_activity_id: Union[Unset, None, str] = UNSET,
    cause_incident_id: Union[Unset, None, str] = UNSET,
    root_cause_incident_id: Union[Unset, None, str] = UNSET,
    configuration: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    job_definition_id_in: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, GetIncidentsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetIncidentsSortOrder] = UNSET,
) -> Response[Union[ExceptionDto, List[IncidentDto]]]:
    kwargs = _get_kwargs(
        client=client,
        incident_id=incident_id,
        incident_type=incident_type,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        process_definition_id=process_definition_id,
        process_definition_key_in=process_definition_key_in,
        process_instance_id=process_instance_id,
        execution_id=execution_id,
        incident_timestamp_before=incident_timestamp_before,
        incident_timestamp_after=incident_timestamp_after,
        activity_id=activity_id,
        failed_activity_id=failed_activity_id,
        cause_incident_id=cause_incident_id,
        root_cause_incident_id=root_cause_incident_id,
        configuration=configuration,
        tenant_id_in=tenant_id_in,
        job_definition_id_in=job_definition_id_in,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    incident_timestamp_before: Union[Unset, None, datetime.datetime] = UNSET,
    incident_timestamp_after: Union[Unset, None, datetime.datetime] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    failed_activity_id: Union[Unset, None, str] = UNSET,
    cause_incident_id: Union[Unset, None, str] = UNSET,
    root_cause_incident_id: Union[Unset, None, str] = UNSET,
    configuration: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    job_definition_id_in: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, GetIncidentsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetIncidentsSortOrder] = UNSET,
) -> Optional[Union[ExceptionDto, List[IncidentDto]]]:
    """Queries for incidents that fulfill given parameters. The size of the result set can be retrieved by using
    the [Get Incident Count](https://docs.camunda.org/manual/7.15/reference/rest/incident/get-query-count/) method."""

    return sync_detailed(
        client=client,
        incident_id=incident_id,
        incident_type=incident_type,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        process_definition_id=process_definition_id,
        process_definition_key_in=process_definition_key_in,
        process_instance_id=process_instance_id,
        execution_id=execution_id,
        incident_timestamp_before=incident_timestamp_before,
        incident_timestamp_after=incident_timestamp_after,
        activity_id=activity_id,
        failed_activity_id=failed_activity_id,
        cause_incident_id=cause_incident_id,
        root_cause_incident_id=root_cause_incident_id,
        configuration=configuration,
        tenant_id_in=tenant_id_in,
        job_definition_id_in=job_definition_id_in,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    incident_timestamp_before: Union[Unset, None, datetime.datetime] = UNSET,
    incident_timestamp_after: Union[Unset, None, datetime.datetime] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    failed_activity_id: Union[Unset, None, str] = UNSET,
    cause_incident_id: Union[Unset, None, str] = UNSET,
    root_cause_incident_id: Union[Unset, None, str] = UNSET,
    configuration: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    job_definition_id_in: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, GetIncidentsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetIncidentsSortOrder] = UNSET,
) -> Response[Union[ExceptionDto, List[IncidentDto]]]:
    kwargs = _get_kwargs(
        client=client,
        incident_id=incident_id,
        incident_type=incident_type,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        process_definition_id=process_definition_id,
        process_definition_key_in=process_definition_key_in,
        process_instance_id=process_instance_id,
        execution_id=execution_id,
        incident_timestamp_before=incident_timestamp_before,
        incident_timestamp_after=incident_timestamp_after,
        activity_id=activity_id,
        failed_activity_id=failed_activity_id,
        cause_incident_id=cause_incident_id,
        root_cause_incident_id=root_cause_incident_id,
        configuration=configuration,
        tenant_id_in=tenant_id_in,
        job_definition_id_in=job_definition_id_in,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    incident_timestamp_before: Union[Unset, None, datetime.datetime] = UNSET,
    incident_timestamp_after: Union[Unset, None, datetime.datetime] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    failed_activity_id: Union[Unset, None, str] = UNSET,
    cause_incident_id: Union[Unset, None, str] = UNSET,
    root_cause_incident_id: Union[Unset, None, str] = UNSET,
    configuration: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    job_definition_id_in: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, GetIncidentsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetIncidentsSortOrder] = UNSET,
) -> Optional[Union[ExceptionDto, List[IncidentDto]]]:
    """Queries for incidents that fulfill given parameters. The size of the result set can be retrieved by using
    the [Get Incident Count](https://docs.camunda.org/manual/7.15/reference/rest/incident/get-query-count/) method."""

    return (
        await asyncio_detailed(
            client=client,
            incident_id=incident_id,
            incident_type=incident_type,
            incident_message=incident_message,
            incident_message_like=incident_message_like,
            process_definition_id=process_definition_id,
            process_definition_key_in=process_definition_key_in,
            process_instance_id=process_instance_id,
            execution_id=execution_id,
            incident_timestamp_before=incident_timestamp_before,
            incident_timestamp_after=incident_timestamp_after,
            activity_id=activity_id,
            failed_activity_id=failed_activity_id,
            cause_incident_id=cause_incident_id,
            root_cause_incident_id=root_cause_incident_id,
            configuration=configuration,
            tenant_id_in=tenant_id_in,
            job_definition_id_in=job_definition_id_in,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
