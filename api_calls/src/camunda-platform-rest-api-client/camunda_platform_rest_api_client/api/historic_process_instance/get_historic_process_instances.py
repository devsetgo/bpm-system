import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.get_historic_process_instances_incident_status import GetHistoricProcessInstancesIncidentStatus
from ...models.get_historic_process_instances_sort_by import GetHistoricProcessInstancesSortBy
from ...models.get_historic_process_instances_sort_order import GetHistoricProcessInstancesSortOrder
from ...models.historic_process_instance_dto import HistoricProcessInstanceDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetHistoricProcessInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetHistoricProcessInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_definition_name: Union[Unset, None, str] = UNSET,
    process_definition_name_like: Union[Unset, None, str] = UNSET,
    process_definition_key_not_in: Union[Unset, None, str] = UNSET,
    process_instance_business_key: Union[Unset, None, str] = UNSET,
    process_instance_business_key_like: Union[Unset, None, str] = UNSET,
    root_process_instances: Union[Unset, None, bool] = UNSET,
    finished: Union[Unset, None, bool] = UNSET,
    unfinished: Union[Unset, None, bool] = UNSET,
    with_incidents: Union[Unset, None, bool] = UNSET,
    with_root_incidents: Union[Unset, None, bool] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_status: Union[Unset, None, GetHistoricProcessInstancesIncidentStatus] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
    finished_before: Union[Unset, None, datetime.datetime] = UNSET,
    finished_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_activity_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_activity_before: Union[Unset, None, datetime.datetime] = UNSET,
    executed_job_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_job_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_by: Union[Unset, None, str] = UNSET,
    super_process_instance_id: Union[Unset, None, str] = UNSET,
    sub_process_instance_id: Union[Unset, None, str] = UNSET,
    super_case_instance_id: Union[Unset, None, str] = UNSET,
    sub_case_instance_id: Union[Unset, None, str] = UNSET,
    case_instance_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    executed_activity_id_in: Union[Unset, None, str] = UNSET,
    active_activity_id_in: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    completed: Union[Unset, None, bool] = UNSET,
    externally_terminated: Union[Unset, None, bool] = UNSET,
    internally_terminated: Union[Unset, None, bool] = UNSET,
    variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/history/process-instance".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    json_incident_status: Union[Unset, None, str] = UNSET
    if not isinstance(incident_status, Unset):
        json_incident_status = incident_status.value if incident_status else None

    json_started_before: Union[Unset, None, str] = UNSET
    if not isinstance(started_before, Unset):
        json_started_before = started_before.isoformat() if started_before else None

    json_started_after: Union[Unset, None, str] = UNSET
    if not isinstance(started_after, Unset):
        json_started_after = started_after.isoformat() if started_after else None

    json_finished_before: Union[Unset, None, str] = UNSET
    if not isinstance(finished_before, Unset):
        json_finished_before = finished_before.isoformat() if finished_before else None

    json_finished_after: Union[Unset, None, str] = UNSET
    if not isinstance(finished_after, Unset):
        json_finished_after = finished_after.isoformat() if finished_after else None

    json_executed_activity_after: Union[Unset, None, str] = UNSET
    if not isinstance(executed_activity_after, Unset):
        json_executed_activity_after = executed_activity_after.isoformat() if executed_activity_after else None

    json_executed_activity_before: Union[Unset, None, str] = UNSET
    if not isinstance(executed_activity_before, Unset):
        json_executed_activity_before = executed_activity_before.isoformat() if executed_activity_before else None

    json_executed_job_after: Union[Unset, None, str] = UNSET
    if not isinstance(executed_job_after, Unset):
        json_executed_job_after = executed_job_after.isoformat() if executed_job_after else None

    json_executed_job_before: Union[Unset, None, str] = UNSET
    if not isinstance(executed_job_before, Unset):
        json_executed_job_before = executed_job_before.isoformat() if executed_job_before else None

    params: Dict[str, Any] = {
        "sortBy": json_sort_by,
        "sortOrder": json_sort_order,
        "firstResult": first_result,
        "maxResults": max_results,
        "processInstanceId": process_instance_id,
        "processInstanceIds": process_instance_ids,
        "processDefinitionId": process_definition_id,
        "processDefinitionKey": process_definition_key,
        "processDefinitionKeyIn": process_definition_key_in,
        "processDefinitionName": process_definition_name,
        "processDefinitionNameLike": process_definition_name_like,
        "processDefinitionKeyNotIn": process_definition_key_not_in,
        "processInstanceBusinessKey": process_instance_business_key,
        "processInstanceBusinessKeyLike": process_instance_business_key_like,
        "rootProcessInstances": root_process_instances,
        "finished": finished,
        "unfinished": unfinished,
        "withIncidents": with_incidents,
        "withRootIncidents": with_root_incidents,
        "incidentType": incident_type,
        "incidentStatus": json_incident_status,
        "incidentMessage": incident_message,
        "incidentMessageLike": incident_message_like,
        "startedBefore": json_started_before,
        "startedAfter": json_started_after,
        "finishedBefore": json_finished_before,
        "finishedAfter": json_finished_after,
        "executedActivityAfter": json_executed_activity_after,
        "executedActivityBefore": json_executed_activity_before,
        "executedJobAfter": json_executed_job_after,
        "executedJobBefore": json_executed_job_before,
        "startedBy": started_by,
        "superProcessInstanceId": super_process_instance_id,
        "subProcessInstanceId": sub_process_instance_id,
        "superCaseInstanceId": super_case_instance_id,
        "subCaseInstanceId": sub_case_instance_id,
        "caseInstanceId": case_instance_id,
        "tenantIdIn": tenant_id_in,
        "withoutTenantId": without_tenant_id,
        "executedActivityIdIn": executed_activity_id_in,
        "activeActivityIdIn": active_activity_id_in,
        "active": active,
        "suspended": suspended,
        "completed": completed,
        "externallyTerminated": externally_terminated,
        "internallyTerminated": internally_terminated,
        "variables": variables,
        "variableNamesIgnoreCase": variable_names_ignore_case,
        "variableValuesIgnoreCase": variable_values_ignore_case,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[HistoricProcessInstanceDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = HistoricProcessInstanceDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[HistoricProcessInstanceDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetHistoricProcessInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetHistoricProcessInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_definition_name: Union[Unset, None, str] = UNSET,
    process_definition_name_like: Union[Unset, None, str] = UNSET,
    process_definition_key_not_in: Union[Unset, None, str] = UNSET,
    process_instance_business_key: Union[Unset, None, str] = UNSET,
    process_instance_business_key_like: Union[Unset, None, str] = UNSET,
    root_process_instances: Union[Unset, None, bool] = UNSET,
    finished: Union[Unset, None, bool] = UNSET,
    unfinished: Union[Unset, None, bool] = UNSET,
    with_incidents: Union[Unset, None, bool] = UNSET,
    with_root_incidents: Union[Unset, None, bool] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_status: Union[Unset, None, GetHistoricProcessInstancesIncidentStatus] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
    finished_before: Union[Unset, None, datetime.datetime] = UNSET,
    finished_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_activity_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_activity_before: Union[Unset, None, datetime.datetime] = UNSET,
    executed_job_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_job_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_by: Union[Unset, None, str] = UNSET,
    super_process_instance_id: Union[Unset, None, str] = UNSET,
    sub_process_instance_id: Union[Unset, None, str] = UNSET,
    super_case_instance_id: Union[Unset, None, str] = UNSET,
    sub_case_instance_id: Union[Unset, None, str] = UNSET,
    case_instance_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    executed_activity_id_in: Union[Unset, None, str] = UNSET,
    active_activity_id_in: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    completed: Union[Unset, None, bool] = UNSET,
    externally_terminated: Union[Unset, None, bool] = UNSET,
    internally_terminated: Union[Unset, None, bool] = UNSET,
    variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[HistoricProcessInstanceDto]]]:
    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        process_instance_id=process_instance_id,
        process_instance_ids=process_instance_ids,
        process_definition_id=process_definition_id,
        process_definition_key=process_definition_key,
        process_definition_key_in=process_definition_key_in,
        process_definition_name=process_definition_name,
        process_definition_name_like=process_definition_name_like,
        process_definition_key_not_in=process_definition_key_not_in,
        process_instance_business_key=process_instance_business_key,
        process_instance_business_key_like=process_instance_business_key_like,
        root_process_instances=root_process_instances,
        finished=finished,
        unfinished=unfinished,
        with_incidents=with_incidents,
        with_root_incidents=with_root_incidents,
        incident_type=incident_type,
        incident_status=incident_status,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        started_before=started_before,
        started_after=started_after,
        finished_before=finished_before,
        finished_after=finished_after,
        executed_activity_after=executed_activity_after,
        executed_activity_before=executed_activity_before,
        executed_job_after=executed_job_after,
        executed_job_before=executed_job_before,
        started_by=started_by,
        super_process_instance_id=super_process_instance_id,
        sub_process_instance_id=sub_process_instance_id,
        super_case_instance_id=super_case_instance_id,
        sub_case_instance_id=sub_case_instance_id,
        case_instance_id=case_instance_id,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        executed_activity_id_in=executed_activity_id_in,
        active_activity_id_in=active_activity_id_in,
        active=active,
        suspended=suspended,
        completed=completed,
        externally_terminated=externally_terminated,
        internally_terminated=internally_terminated,
        variables=variables,
        variable_names_ignore_case=variable_names_ignore_case,
        variable_values_ignore_case=variable_values_ignore_case,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetHistoricProcessInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetHistoricProcessInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_definition_name: Union[Unset, None, str] = UNSET,
    process_definition_name_like: Union[Unset, None, str] = UNSET,
    process_definition_key_not_in: Union[Unset, None, str] = UNSET,
    process_instance_business_key: Union[Unset, None, str] = UNSET,
    process_instance_business_key_like: Union[Unset, None, str] = UNSET,
    root_process_instances: Union[Unset, None, bool] = UNSET,
    finished: Union[Unset, None, bool] = UNSET,
    unfinished: Union[Unset, None, bool] = UNSET,
    with_incidents: Union[Unset, None, bool] = UNSET,
    with_root_incidents: Union[Unset, None, bool] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_status: Union[Unset, None, GetHistoricProcessInstancesIncidentStatus] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
    finished_before: Union[Unset, None, datetime.datetime] = UNSET,
    finished_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_activity_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_activity_before: Union[Unset, None, datetime.datetime] = UNSET,
    executed_job_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_job_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_by: Union[Unset, None, str] = UNSET,
    super_process_instance_id: Union[Unset, None, str] = UNSET,
    sub_process_instance_id: Union[Unset, None, str] = UNSET,
    super_case_instance_id: Union[Unset, None, str] = UNSET,
    sub_case_instance_id: Union[Unset, None, str] = UNSET,
    case_instance_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    executed_activity_id_in: Union[Unset, None, str] = UNSET,
    active_activity_id_in: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    completed: Union[Unset, None, bool] = UNSET,
    externally_terminated: Union[Unset, None, bool] = UNSET,
    internally_terminated: Union[Unset, None, bool] = UNSET,
    variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[HistoricProcessInstanceDto]]]:
    """Queries for historic process instances that fulfill the given parameters.
    The size of the result set can be retrieved by using the
    [Get Process Instance Count](https://docs.camunda.org/manual/7.15/reference/rest/history/process-instance/get-process-instance-query-count/) method."""

    return sync_detailed(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        process_instance_id=process_instance_id,
        process_instance_ids=process_instance_ids,
        process_definition_id=process_definition_id,
        process_definition_key=process_definition_key,
        process_definition_key_in=process_definition_key_in,
        process_definition_name=process_definition_name,
        process_definition_name_like=process_definition_name_like,
        process_definition_key_not_in=process_definition_key_not_in,
        process_instance_business_key=process_instance_business_key,
        process_instance_business_key_like=process_instance_business_key_like,
        root_process_instances=root_process_instances,
        finished=finished,
        unfinished=unfinished,
        with_incidents=with_incidents,
        with_root_incidents=with_root_incidents,
        incident_type=incident_type,
        incident_status=incident_status,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        started_before=started_before,
        started_after=started_after,
        finished_before=finished_before,
        finished_after=finished_after,
        executed_activity_after=executed_activity_after,
        executed_activity_before=executed_activity_before,
        executed_job_after=executed_job_after,
        executed_job_before=executed_job_before,
        started_by=started_by,
        super_process_instance_id=super_process_instance_id,
        sub_process_instance_id=sub_process_instance_id,
        super_case_instance_id=super_case_instance_id,
        sub_case_instance_id=sub_case_instance_id,
        case_instance_id=case_instance_id,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        executed_activity_id_in=executed_activity_id_in,
        active_activity_id_in=active_activity_id_in,
        active=active,
        suspended=suspended,
        completed=completed,
        externally_terminated=externally_terminated,
        internally_terminated=internally_terminated,
        variables=variables,
        variable_names_ignore_case=variable_names_ignore_case,
        variable_values_ignore_case=variable_values_ignore_case,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetHistoricProcessInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetHistoricProcessInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_definition_name: Union[Unset, None, str] = UNSET,
    process_definition_name_like: Union[Unset, None, str] = UNSET,
    process_definition_key_not_in: Union[Unset, None, str] = UNSET,
    process_instance_business_key: Union[Unset, None, str] = UNSET,
    process_instance_business_key_like: Union[Unset, None, str] = UNSET,
    root_process_instances: Union[Unset, None, bool] = UNSET,
    finished: Union[Unset, None, bool] = UNSET,
    unfinished: Union[Unset, None, bool] = UNSET,
    with_incidents: Union[Unset, None, bool] = UNSET,
    with_root_incidents: Union[Unset, None, bool] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_status: Union[Unset, None, GetHistoricProcessInstancesIncidentStatus] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
    finished_before: Union[Unset, None, datetime.datetime] = UNSET,
    finished_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_activity_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_activity_before: Union[Unset, None, datetime.datetime] = UNSET,
    executed_job_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_job_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_by: Union[Unset, None, str] = UNSET,
    super_process_instance_id: Union[Unset, None, str] = UNSET,
    sub_process_instance_id: Union[Unset, None, str] = UNSET,
    super_case_instance_id: Union[Unset, None, str] = UNSET,
    sub_case_instance_id: Union[Unset, None, str] = UNSET,
    case_instance_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    executed_activity_id_in: Union[Unset, None, str] = UNSET,
    active_activity_id_in: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    completed: Union[Unset, None, bool] = UNSET,
    externally_terminated: Union[Unset, None, bool] = UNSET,
    internally_terminated: Union[Unset, None, bool] = UNSET,
    variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[HistoricProcessInstanceDto]]]:
    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        process_instance_id=process_instance_id,
        process_instance_ids=process_instance_ids,
        process_definition_id=process_definition_id,
        process_definition_key=process_definition_key,
        process_definition_key_in=process_definition_key_in,
        process_definition_name=process_definition_name,
        process_definition_name_like=process_definition_name_like,
        process_definition_key_not_in=process_definition_key_not_in,
        process_instance_business_key=process_instance_business_key,
        process_instance_business_key_like=process_instance_business_key_like,
        root_process_instances=root_process_instances,
        finished=finished,
        unfinished=unfinished,
        with_incidents=with_incidents,
        with_root_incidents=with_root_incidents,
        incident_type=incident_type,
        incident_status=incident_status,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        started_before=started_before,
        started_after=started_after,
        finished_before=finished_before,
        finished_after=finished_after,
        executed_activity_after=executed_activity_after,
        executed_activity_before=executed_activity_before,
        executed_job_after=executed_job_after,
        executed_job_before=executed_job_before,
        started_by=started_by,
        super_process_instance_id=super_process_instance_id,
        sub_process_instance_id=sub_process_instance_id,
        super_case_instance_id=super_case_instance_id,
        sub_case_instance_id=sub_case_instance_id,
        case_instance_id=case_instance_id,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        executed_activity_id_in=executed_activity_id_in,
        active_activity_id_in=active_activity_id_in,
        active=active,
        suspended=suspended,
        completed=completed,
        externally_terminated=externally_terminated,
        internally_terminated=internally_terminated,
        variables=variables,
        variable_names_ignore_case=variable_names_ignore_case,
        variable_values_ignore_case=variable_values_ignore_case,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetHistoricProcessInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetHistoricProcessInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_definition_name: Union[Unset, None, str] = UNSET,
    process_definition_name_like: Union[Unset, None, str] = UNSET,
    process_definition_key_not_in: Union[Unset, None, str] = UNSET,
    process_instance_business_key: Union[Unset, None, str] = UNSET,
    process_instance_business_key_like: Union[Unset, None, str] = UNSET,
    root_process_instances: Union[Unset, None, bool] = UNSET,
    finished: Union[Unset, None, bool] = UNSET,
    unfinished: Union[Unset, None, bool] = UNSET,
    with_incidents: Union[Unset, None, bool] = UNSET,
    with_root_incidents: Union[Unset, None, bool] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_status: Union[Unset, None, GetHistoricProcessInstancesIncidentStatus] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
    finished_before: Union[Unset, None, datetime.datetime] = UNSET,
    finished_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_activity_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_activity_before: Union[Unset, None, datetime.datetime] = UNSET,
    executed_job_after: Union[Unset, None, datetime.datetime] = UNSET,
    executed_job_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_by: Union[Unset, None, str] = UNSET,
    super_process_instance_id: Union[Unset, None, str] = UNSET,
    sub_process_instance_id: Union[Unset, None, str] = UNSET,
    super_case_instance_id: Union[Unset, None, str] = UNSET,
    sub_case_instance_id: Union[Unset, None, str] = UNSET,
    case_instance_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    executed_activity_id_in: Union[Unset, None, str] = UNSET,
    active_activity_id_in: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    completed: Union[Unset, None, bool] = UNSET,
    externally_terminated: Union[Unset, None, bool] = UNSET,
    internally_terminated: Union[Unset, None, bool] = UNSET,
    variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[HistoricProcessInstanceDto]]]:
    """Queries for historic process instances that fulfill the given parameters.
    The size of the result set can be retrieved by using the
    [Get Process Instance Count](https://docs.camunda.org/manual/7.15/reference/rest/history/process-instance/get-process-instance-query-count/) method."""

    return (
        await asyncio_detailed(
            client=client,
            sort_by=sort_by,
            sort_order=sort_order,
            first_result=first_result,
            max_results=max_results,
            process_instance_id=process_instance_id,
            process_instance_ids=process_instance_ids,
            process_definition_id=process_definition_id,
            process_definition_key=process_definition_key,
            process_definition_key_in=process_definition_key_in,
            process_definition_name=process_definition_name,
            process_definition_name_like=process_definition_name_like,
            process_definition_key_not_in=process_definition_key_not_in,
            process_instance_business_key=process_instance_business_key,
            process_instance_business_key_like=process_instance_business_key_like,
            root_process_instances=root_process_instances,
            finished=finished,
            unfinished=unfinished,
            with_incidents=with_incidents,
            with_root_incidents=with_root_incidents,
            incident_type=incident_type,
            incident_status=incident_status,
            incident_message=incident_message,
            incident_message_like=incident_message_like,
            started_before=started_before,
            started_after=started_after,
            finished_before=finished_before,
            finished_after=finished_after,
            executed_activity_after=executed_activity_after,
            executed_activity_before=executed_activity_before,
            executed_job_after=executed_job_after,
            executed_job_before=executed_job_before,
            started_by=started_by,
            super_process_instance_id=super_process_instance_id,
            sub_process_instance_id=sub_process_instance_id,
            super_case_instance_id=super_case_instance_id,
            sub_case_instance_id=sub_case_instance_id,
            case_instance_id=case_instance_id,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
            executed_activity_id_in=executed_activity_id_in,
            active_activity_id_in=active_activity_id_in,
            active=active,
            suspended=suspended,
            completed=completed,
            externally_terminated=externally_terminated,
            internally_terminated=internally_terminated,
            variables=variables,
            variable_names_ignore_case=variable_names_ignore_case,
            variable_values_ignore_case=variable_values_ignore_case,
        )
    ).parsed
