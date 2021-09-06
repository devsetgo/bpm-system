import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.count_result_dto import CountResultDto
from ...models.exception_dto import ExceptionDto
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
) -> Dict[str, Any]:
    url = "{}/incident/count".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_incident_timestamp_before: Union[Unset, None, str] = UNSET
    if not isinstance(incident_timestamp_before, Unset):
        json_incident_timestamp_before = incident_timestamp_before.isoformat() if incident_timestamp_before else None

    json_incident_timestamp_after: Union[Unset, None, str] = UNSET
    if not isinstance(incident_timestamp_after, Unset):
        json_incident_timestamp_after = incident_timestamp_after.isoformat() if incident_timestamp_after else None

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
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[CountResultDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CountResultDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[CountResultDto]]]:
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
) -> Response[Union[ExceptionDto, List[CountResultDto]]]:
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
) -> Optional[Union[ExceptionDto, List[CountResultDto]]]:
    """Queries for the number of incidents that fulfill given parameters. Takes the same parameters as the
    [Get Incidents](https://docs.camunda.org/manual/7.15/reference/rest/incident/get-query/) method."""

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
) -> Response[Union[ExceptionDto, List[CountResultDto]]]:
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
) -> Optional[Union[ExceptionDto, List[CountResultDto]]]:
    """Queries for the number of incidents that fulfill given parameters. Takes the same parameters as the
    [Get Incidents](https://docs.camunda.org/manual/7.15/reference/rest/incident/get-query/) method."""

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
        )
    ).parsed
