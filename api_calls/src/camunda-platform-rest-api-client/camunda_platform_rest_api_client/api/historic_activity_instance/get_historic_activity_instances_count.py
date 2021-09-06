import datetime
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.count_result_dto import CountResultDto
from ...models.exception_dto import ExceptionDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
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
    url = "{}/history/activity-instance/count".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[CountResultDto, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = CountResultDto.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CountResultDto, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
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
) -> Response[Union[CountResultDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
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
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for the number of historic activity instances that fulfill the given parameters.
    Takes the same parameters as the [Get Historic Activity Instance](https://docs.camunda.org/manual/7.15/reference/rest/history/activity-instance/get-activity-instance-query/)  method."""

    return sync_detailed(
        client=client,
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
) -> Response[Union[CountResultDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
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
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for the number of historic activity instances that fulfill the given parameters.
    Takes the same parameters as the [Get Historic Activity Instance](https://docs.camunda.org/manual/7.15/reference/rest/history/activity-instance/get-activity-instance-query/)  method."""

    return (
        await asyncio_detailed(
            client=client,
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
