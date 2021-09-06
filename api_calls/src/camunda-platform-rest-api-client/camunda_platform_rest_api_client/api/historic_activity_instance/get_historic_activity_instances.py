import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.get_historic_activity_instances_sort_by import GetHistoricActivityInstancesSortBy
from ...models.get_historic_activity_instances_sort_order import GetHistoricActivityInstancesSortOrder
from ...models.historic_activity_instance_dto import HistoricActivityInstanceDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetHistoricActivityInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetHistoricActivityInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    activity_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    activity_name: Union[Unset, None, str] = UNSET,
    activity_type: Union[Unset, None, str] = UNSET,
    task_assignee: Union[Unset, None, str] = UNSET,
    finished: Union[Unset, None, bool] = UNSET,
    unfinished: Union[Unset, None, bool] = UNSET,
    canceled: Union[Unset, None, bool] = UNSET,
    complete_scope: Union[Unset, None, bool] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
    finished_before: Union[Unset, None, datetime.datetime] = UNSET,
    finished_after: Union[Unset, None, datetime.datetime] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/history/activity-instance".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

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

    params: Dict[str, Any] = {
        "sortBy": json_sort_by,
        "sortOrder": json_sort_order,
        "firstResult": first_result,
        "maxResults": max_results,
        "activityInstanceId": activity_instance_id,
        "processInstanceId": process_instance_id,
        "processDefinitionId": process_definition_id,
        "executionId": execution_id,
        "activityId": activity_id,
        "activityName": activity_name,
        "activityType": activity_type,
        "taskAssignee": task_assignee,
        "finished": finished,
        "unfinished": unfinished,
        "canceled": canceled,
        "completeScope": complete_scope,
        "startedBefore": json_started_before,
        "startedAfter": json_started_after,
        "finishedBefore": json_finished_before,
        "finishedAfter": json_finished_after,
        "tenantIdIn": tenant_id_in,
        "withoutTenantId": without_tenant_id,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[HistoricActivityInstanceDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = HistoricActivityInstanceDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[HistoricActivityInstanceDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetHistoricActivityInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetHistoricActivityInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    activity_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    activity_name: Union[Unset, None, str] = UNSET,
    activity_type: Union[Unset, None, str] = UNSET,
    task_assignee: Union[Unset, None, str] = UNSET,
    finished: Union[Unset, None, bool] = UNSET,
    unfinished: Union[Unset, None, bool] = UNSET,
    canceled: Union[Unset, None, bool] = UNSET,
    complete_scope: Union[Unset, None, bool] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
    finished_before: Union[Unset, None, datetime.datetime] = UNSET,
    finished_after: Union[Unset, None, datetime.datetime] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[HistoricActivityInstanceDto]]]:
    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        activity_instance_id=activity_instance_id,
        process_instance_id=process_instance_id,
        process_definition_id=process_definition_id,
        execution_id=execution_id,
        activity_id=activity_id,
        activity_name=activity_name,
        activity_type=activity_type,
        task_assignee=task_assignee,
        finished=finished,
        unfinished=unfinished,
        canceled=canceled,
        complete_scope=complete_scope,
        started_before=started_before,
        started_after=started_after,
        finished_before=finished_before,
        finished_after=finished_after,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetHistoricActivityInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetHistoricActivityInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    activity_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    activity_name: Union[Unset, None, str] = UNSET,
    activity_type: Union[Unset, None, str] = UNSET,
    task_assignee: Union[Unset, None, str] = UNSET,
    finished: Union[Unset, None, bool] = UNSET,
    unfinished: Union[Unset, None, bool] = UNSET,
    canceled: Union[Unset, None, bool] = UNSET,
    complete_scope: Union[Unset, None, bool] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
    finished_before: Union[Unset, None, datetime.datetime] = UNSET,
    finished_after: Union[Unset, None, datetime.datetime] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[HistoricActivityInstanceDto]]]:
    """Queries for historic activity instances that fulfill the given parameters.
    The size of the result set can be retrieved by using the
    [Get Historic Activity Instance Count](https://docs.camunda.org/manual/7.15/reference/rest/history/activity-instance/get-activity-instance-query-count/) method."""

    return sync_detailed(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        activity_instance_id=activity_instance_id,
        process_instance_id=process_instance_id,
        process_definition_id=process_definition_id,
        execution_id=execution_id,
        activity_id=activity_id,
        activity_name=activity_name,
        activity_type=activity_type,
        task_assignee=task_assignee,
        finished=finished,
        unfinished=unfinished,
        canceled=canceled,
        complete_scope=complete_scope,
        started_before=started_before,
        started_after=started_after,
        finished_before=finished_before,
        finished_after=finished_after,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetHistoricActivityInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetHistoricActivityInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    activity_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    activity_name: Union[Unset, None, str] = UNSET,
    activity_type: Union[Unset, None, str] = UNSET,
    task_assignee: Union[Unset, None, str] = UNSET,
    finished: Union[Unset, None, bool] = UNSET,
    unfinished: Union[Unset, None, bool] = UNSET,
    canceled: Union[Unset, None, bool] = UNSET,
    complete_scope: Union[Unset, None, bool] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
    finished_before: Union[Unset, None, datetime.datetime] = UNSET,
    finished_after: Union[Unset, None, datetime.datetime] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[HistoricActivityInstanceDto]]]:
    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        activity_instance_id=activity_instance_id,
        process_instance_id=process_instance_id,
        process_definition_id=process_definition_id,
        execution_id=execution_id,
        activity_id=activity_id,
        activity_name=activity_name,
        activity_type=activity_type,
        task_assignee=task_assignee,
        finished=finished,
        unfinished=unfinished,
        canceled=canceled,
        complete_scope=complete_scope,
        started_before=started_before,
        started_after=started_after,
        finished_before=finished_before,
        finished_after=finished_after,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetHistoricActivityInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetHistoricActivityInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    activity_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    activity_name: Union[Unset, None, str] = UNSET,
    activity_type: Union[Unset, None, str] = UNSET,
    task_assignee: Union[Unset, None, str] = UNSET,
    finished: Union[Unset, None, bool] = UNSET,
    unfinished: Union[Unset, None, bool] = UNSET,
    canceled: Union[Unset, None, bool] = UNSET,
    complete_scope: Union[Unset, None, bool] = UNSET,
    started_before: Union[Unset, None, datetime.datetime] = UNSET,
    started_after: Union[Unset, None, datetime.datetime] = UNSET,
    finished_before: Union[Unset, None, datetime.datetime] = UNSET,
    finished_after: Union[Unset, None, datetime.datetime] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[HistoricActivityInstanceDto]]]:
    """Queries for historic activity instances that fulfill the given parameters.
    The size of the result set can be retrieved by using the
    [Get Historic Activity Instance Count](https://docs.camunda.org/manual/7.15/reference/rest/history/activity-instance/get-activity-instance-query-count/) method."""

    return (
        await asyncio_detailed(
            client=client,
            sort_by=sort_by,
            sort_order=sort_order,
            first_result=first_result,
            max_results=max_results,
            activity_instance_id=activity_instance_id,
            process_instance_id=process_instance_id,
            process_definition_id=process_definition_id,
            execution_id=execution_id,
            activity_id=activity_id,
            activity_name=activity_name,
            activity_type=activity_type,
            task_assignee=task_assignee,
            finished=finished,
            unfinished=unfinished,
            canceled=canceled,
            complete_scope=complete_scope,
            started_before=started_before,
            started_after=started_after,
            finished_before=finished_before,
            finished_after=finished_after,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
        )
    ).parsed
