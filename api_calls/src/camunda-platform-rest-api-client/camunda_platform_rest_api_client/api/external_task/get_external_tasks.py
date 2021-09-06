import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.external_task_dto import ExternalTaskDto
from ...models.get_external_tasks_sort_by import GetExternalTasksSortBy
from ...models.get_external_tasks_sort_order import GetExternalTasksSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    external_task_id: Union[Unset, None, str] = UNSET,
    external_task_id_in: Union[Unset, None, str] = UNSET,
    topic_name: Union[Unset, None, str] = UNSET,
    worker_id: Union[Unset, None, str] = UNSET,
    locked: Union[Unset, None, bool] = UNSET,
    not_locked: Union[Unset, None, bool] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
    no_retries_left: Union[Unset, None, bool] = UNSET,
    lock_expiration_after: Union[Unset, None, datetime.datetime] = UNSET,
    lock_expiration_before: Union[Unset, None, datetime.datetime] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    activity_id_in: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_id_in: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    priority_higher_than_or_equals: Union[Unset, None, int] = UNSET,
    priority_lower_than_or_equals: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, GetExternalTasksSortBy] = UNSET,
    sort_order: Union[Unset, None, GetExternalTasksSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/external-task".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_lock_expiration_after: Union[Unset, None, str] = UNSET
    if not isinstance(lock_expiration_after, Unset):
        json_lock_expiration_after = lock_expiration_after.isoformat() if lock_expiration_after else None

    json_lock_expiration_before: Union[Unset, None, str] = UNSET
    if not isinstance(lock_expiration_before, Unset):
        json_lock_expiration_before = lock_expiration_before.isoformat() if lock_expiration_before else None

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params: Dict[str, Any] = {
        "externalTaskId": external_task_id,
        "externalTaskIdIn": external_task_id_in,
        "topicName": topic_name,
        "workerId": worker_id,
        "locked": locked,
        "notLocked": not_locked,
        "withRetriesLeft": with_retries_left,
        "noRetriesLeft": no_retries_left,
        "lockExpirationAfter": json_lock_expiration_after,
        "lockExpirationBefore": json_lock_expiration_before,
        "activityId": activity_id,
        "activityIdIn": activity_id_in,
        "executionId": execution_id,
        "processInstanceId": process_instance_id,
        "processInstanceIdIn": process_instance_id_in,
        "processDefinitionId": process_definition_id,
        "tenantIdIn": tenant_id_in,
        "active": active,
        "suspended": suspended,
        "priorityHigherThanOrEquals": priority_higher_than_or_equals,
        "priorityLowerThanOrEquals": priority_lower_than_or_equals,
        "sortBy": json_sort_by,
        "sortOrder": json_sort_order,
        "firstResult": first_result,
        "maxResults": max_results,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[ExternalTaskDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ExternalTaskDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[ExternalTaskDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    external_task_id: Union[Unset, None, str] = UNSET,
    external_task_id_in: Union[Unset, None, str] = UNSET,
    topic_name: Union[Unset, None, str] = UNSET,
    worker_id: Union[Unset, None, str] = UNSET,
    locked: Union[Unset, None, bool] = UNSET,
    not_locked: Union[Unset, None, bool] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
    no_retries_left: Union[Unset, None, bool] = UNSET,
    lock_expiration_after: Union[Unset, None, datetime.datetime] = UNSET,
    lock_expiration_before: Union[Unset, None, datetime.datetime] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    activity_id_in: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_id_in: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    priority_higher_than_or_equals: Union[Unset, None, int] = UNSET,
    priority_lower_than_or_equals: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, GetExternalTasksSortBy] = UNSET,
    sort_order: Union[Unset, None, GetExternalTasksSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[ExternalTaskDto]]]:
    kwargs = _get_kwargs(
        client=client,
        external_task_id=external_task_id,
        external_task_id_in=external_task_id_in,
        topic_name=topic_name,
        worker_id=worker_id,
        locked=locked,
        not_locked=not_locked,
        with_retries_left=with_retries_left,
        no_retries_left=no_retries_left,
        lock_expiration_after=lock_expiration_after,
        lock_expiration_before=lock_expiration_before,
        activity_id=activity_id,
        activity_id_in=activity_id_in,
        execution_id=execution_id,
        process_instance_id=process_instance_id,
        process_instance_id_in=process_instance_id_in,
        process_definition_id=process_definition_id,
        tenant_id_in=tenant_id_in,
        active=active,
        suspended=suspended,
        priority_higher_than_or_equals=priority_higher_than_or_equals,
        priority_lower_than_or_equals=priority_lower_than_or_equals,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    external_task_id: Union[Unset, None, str] = UNSET,
    external_task_id_in: Union[Unset, None, str] = UNSET,
    topic_name: Union[Unset, None, str] = UNSET,
    worker_id: Union[Unset, None, str] = UNSET,
    locked: Union[Unset, None, bool] = UNSET,
    not_locked: Union[Unset, None, bool] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
    no_retries_left: Union[Unset, None, bool] = UNSET,
    lock_expiration_after: Union[Unset, None, datetime.datetime] = UNSET,
    lock_expiration_before: Union[Unset, None, datetime.datetime] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    activity_id_in: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_id_in: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    priority_higher_than_or_equals: Union[Unset, None, int] = UNSET,
    priority_lower_than_or_equals: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, GetExternalTasksSortBy] = UNSET,
    sort_order: Union[Unset, None, GetExternalTasksSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[ExternalTaskDto]]]:
    """Queries for the external tasks that fulfill given parameters. Parameters may be static as well as dynamic
    runtime properties of executions. The size of the result set can be retrieved by using the
    [Get External Task Count](https://docs.camunda.org/manual/7.15/reference/rest/external-task/get-query-count/) method."""

    return sync_detailed(
        client=client,
        external_task_id=external_task_id,
        external_task_id_in=external_task_id_in,
        topic_name=topic_name,
        worker_id=worker_id,
        locked=locked,
        not_locked=not_locked,
        with_retries_left=with_retries_left,
        no_retries_left=no_retries_left,
        lock_expiration_after=lock_expiration_after,
        lock_expiration_before=lock_expiration_before,
        activity_id=activity_id,
        activity_id_in=activity_id_in,
        execution_id=execution_id,
        process_instance_id=process_instance_id,
        process_instance_id_in=process_instance_id_in,
        process_definition_id=process_definition_id,
        tenant_id_in=tenant_id_in,
        active=active,
        suspended=suspended,
        priority_higher_than_or_equals=priority_higher_than_or_equals,
        priority_lower_than_or_equals=priority_lower_than_or_equals,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    external_task_id: Union[Unset, None, str] = UNSET,
    external_task_id_in: Union[Unset, None, str] = UNSET,
    topic_name: Union[Unset, None, str] = UNSET,
    worker_id: Union[Unset, None, str] = UNSET,
    locked: Union[Unset, None, bool] = UNSET,
    not_locked: Union[Unset, None, bool] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
    no_retries_left: Union[Unset, None, bool] = UNSET,
    lock_expiration_after: Union[Unset, None, datetime.datetime] = UNSET,
    lock_expiration_before: Union[Unset, None, datetime.datetime] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    activity_id_in: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_id_in: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    priority_higher_than_or_equals: Union[Unset, None, int] = UNSET,
    priority_lower_than_or_equals: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, GetExternalTasksSortBy] = UNSET,
    sort_order: Union[Unset, None, GetExternalTasksSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[ExternalTaskDto]]]:
    kwargs = _get_kwargs(
        client=client,
        external_task_id=external_task_id,
        external_task_id_in=external_task_id_in,
        topic_name=topic_name,
        worker_id=worker_id,
        locked=locked,
        not_locked=not_locked,
        with_retries_left=with_retries_left,
        no_retries_left=no_retries_left,
        lock_expiration_after=lock_expiration_after,
        lock_expiration_before=lock_expiration_before,
        activity_id=activity_id,
        activity_id_in=activity_id_in,
        execution_id=execution_id,
        process_instance_id=process_instance_id,
        process_instance_id_in=process_instance_id_in,
        process_definition_id=process_definition_id,
        tenant_id_in=tenant_id_in,
        active=active,
        suspended=suspended,
        priority_higher_than_or_equals=priority_higher_than_or_equals,
        priority_lower_than_or_equals=priority_lower_than_or_equals,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    external_task_id: Union[Unset, None, str] = UNSET,
    external_task_id_in: Union[Unset, None, str] = UNSET,
    topic_name: Union[Unset, None, str] = UNSET,
    worker_id: Union[Unset, None, str] = UNSET,
    locked: Union[Unset, None, bool] = UNSET,
    not_locked: Union[Unset, None, bool] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
    no_retries_left: Union[Unset, None, bool] = UNSET,
    lock_expiration_after: Union[Unset, None, datetime.datetime] = UNSET,
    lock_expiration_before: Union[Unset, None, datetime.datetime] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    activity_id_in: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_id_in: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    priority_higher_than_or_equals: Union[Unset, None, int] = UNSET,
    priority_lower_than_or_equals: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, GetExternalTasksSortBy] = UNSET,
    sort_order: Union[Unset, None, GetExternalTasksSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[ExternalTaskDto]]]:
    """Queries for the external tasks that fulfill given parameters. Parameters may be static as well as dynamic
    runtime properties of executions. The size of the result set can be retrieved by using the
    [Get External Task Count](https://docs.camunda.org/manual/7.15/reference/rest/external-task/get-query-count/) method."""

    return (
        await asyncio_detailed(
            client=client,
            external_task_id=external_task_id,
            external_task_id_in=external_task_id_in,
            topic_name=topic_name,
            worker_id=worker_id,
            locked=locked,
            not_locked=not_locked,
            with_retries_left=with_retries_left,
            no_retries_left=no_retries_left,
            lock_expiration_after=lock_expiration_after,
            lock_expiration_before=lock_expiration_before,
            activity_id=activity_id,
            activity_id_in=activity_id_in,
            execution_id=execution_id,
            process_instance_id=process_instance_id,
            process_instance_id_in=process_instance_id_in,
            process_definition_id=process_definition_id,
            tenant_id_in=tenant_id_in,
            active=active,
            suspended=suspended,
            priority_higher_than_or_equals=priority_higher_than_or_equals,
            priority_lower_than_or_equals=priority_lower_than_or_equals,
            sort_by=sort_by,
            sort_order=sort_order,
            first_result=first_result,
            max_results=max_results,
        )
    ).parsed
