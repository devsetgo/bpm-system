from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.get_jobs_sort_by import GetJobsSortBy
from ...models.get_jobs_sort_order import GetJobsSortOrder
from ...models.job_dto import JobDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    job_id: Union[Unset, None, str] = UNSET,
    job_ids: Union[Unset, None, str] = UNSET,
    job_definition_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
    executable: Union[Unset, None, bool] = UNSET,
    timers: Union[Unset, None, bool] = UNSET,
    messages: Union[Unset, None, bool] = UNSET,
    due_dates: Union[Unset, None, str] = UNSET,
    create_times: Union[Unset, None, str] = UNSET,
    with_exception: Union[Unset, None, bool] = UNSET,
    exception_message: Union[Unset, None, str] = UNSET,
    failed_activity_id: Union[Unset, None, str] = UNSET,
    no_retries_left: Union[Unset, None, bool] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    priority_lower_than_or_equals: Union[Unset, None, int] = UNSET,
    priority_higher_than_or_equals: Union[Unset, None, int] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_jobs_without_tenant_id: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetJobsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetJobsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/job".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params: Dict[str, Any] = {
        "jobId": job_id,
        "jobIds": job_ids,
        "jobDefinitionId": job_definition_id,
        "processInstanceId": process_instance_id,
        "processInstanceIds": process_instance_ids,
        "executionId": execution_id,
        "processDefinitionId": process_definition_id,
        "processDefinitionKey": process_definition_key,
        "activityId": activity_id,
        "withRetriesLeft": with_retries_left,
        "executable": executable,
        "timers": timers,
        "messages": messages,
        "dueDates": due_dates,
        "createTimes": create_times,
        "withException": with_exception,
        "exceptionMessage": exception_message,
        "failedActivityId": failed_activity_id,
        "noRetriesLeft": no_retries_left,
        "active": active,
        "suspended": suspended,
        "priorityLowerThanOrEquals": priority_lower_than_or_equals,
        "priorityHigherThanOrEquals": priority_higher_than_or_equals,
        "tenantIdIn": tenant_id_in,
        "withoutTenantId": without_tenant_id,
        "includeJobsWithoutTenantId": include_jobs_without_tenant_id,
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[JobDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = JobDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[JobDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    job_id: Union[Unset, None, str] = UNSET,
    job_ids: Union[Unset, None, str] = UNSET,
    job_definition_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
    executable: Union[Unset, None, bool] = UNSET,
    timers: Union[Unset, None, bool] = UNSET,
    messages: Union[Unset, None, bool] = UNSET,
    due_dates: Union[Unset, None, str] = UNSET,
    create_times: Union[Unset, None, str] = UNSET,
    with_exception: Union[Unset, None, bool] = UNSET,
    exception_message: Union[Unset, None, str] = UNSET,
    failed_activity_id: Union[Unset, None, str] = UNSET,
    no_retries_left: Union[Unset, None, bool] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    priority_lower_than_or_equals: Union[Unset, None, int] = UNSET,
    priority_higher_than_or_equals: Union[Unset, None, int] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_jobs_without_tenant_id: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetJobsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetJobsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[JobDto]]]:
    kwargs = _get_kwargs(
        client=client,
        job_id=job_id,
        job_ids=job_ids,
        job_definition_id=job_definition_id,
        process_instance_id=process_instance_id,
        process_instance_ids=process_instance_ids,
        execution_id=execution_id,
        process_definition_id=process_definition_id,
        process_definition_key=process_definition_key,
        activity_id=activity_id,
        with_retries_left=with_retries_left,
        executable=executable,
        timers=timers,
        messages=messages,
        due_dates=due_dates,
        create_times=create_times,
        with_exception=with_exception,
        exception_message=exception_message,
        failed_activity_id=failed_activity_id,
        no_retries_left=no_retries_left,
        active=active,
        suspended=suspended,
        priority_lower_than_or_equals=priority_lower_than_or_equals,
        priority_higher_than_or_equals=priority_higher_than_or_equals,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_jobs_without_tenant_id=include_jobs_without_tenant_id,
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
    job_id: Union[Unset, None, str] = UNSET,
    job_ids: Union[Unset, None, str] = UNSET,
    job_definition_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
    executable: Union[Unset, None, bool] = UNSET,
    timers: Union[Unset, None, bool] = UNSET,
    messages: Union[Unset, None, bool] = UNSET,
    due_dates: Union[Unset, None, str] = UNSET,
    create_times: Union[Unset, None, str] = UNSET,
    with_exception: Union[Unset, None, bool] = UNSET,
    exception_message: Union[Unset, None, str] = UNSET,
    failed_activity_id: Union[Unset, None, str] = UNSET,
    no_retries_left: Union[Unset, None, bool] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    priority_lower_than_or_equals: Union[Unset, None, int] = UNSET,
    priority_higher_than_or_equals: Union[Unset, None, int] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_jobs_without_tenant_id: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetJobsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetJobsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[JobDto]]]:
    """Queries for jobs that fulfill given parameters.
    The size of the result set can be retrieved by using the [Get Job
    Count](https://docs.camunda.org/manual/7.15/reference/rest/job/get-query-count/) method."""

    return sync_detailed(
        client=client,
        job_id=job_id,
        job_ids=job_ids,
        job_definition_id=job_definition_id,
        process_instance_id=process_instance_id,
        process_instance_ids=process_instance_ids,
        execution_id=execution_id,
        process_definition_id=process_definition_id,
        process_definition_key=process_definition_key,
        activity_id=activity_id,
        with_retries_left=with_retries_left,
        executable=executable,
        timers=timers,
        messages=messages,
        due_dates=due_dates,
        create_times=create_times,
        with_exception=with_exception,
        exception_message=exception_message,
        failed_activity_id=failed_activity_id,
        no_retries_left=no_retries_left,
        active=active,
        suspended=suspended,
        priority_lower_than_or_equals=priority_lower_than_or_equals,
        priority_higher_than_or_equals=priority_higher_than_or_equals,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_jobs_without_tenant_id=include_jobs_without_tenant_id,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    job_id: Union[Unset, None, str] = UNSET,
    job_ids: Union[Unset, None, str] = UNSET,
    job_definition_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
    executable: Union[Unset, None, bool] = UNSET,
    timers: Union[Unset, None, bool] = UNSET,
    messages: Union[Unset, None, bool] = UNSET,
    due_dates: Union[Unset, None, str] = UNSET,
    create_times: Union[Unset, None, str] = UNSET,
    with_exception: Union[Unset, None, bool] = UNSET,
    exception_message: Union[Unset, None, str] = UNSET,
    failed_activity_id: Union[Unset, None, str] = UNSET,
    no_retries_left: Union[Unset, None, bool] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    priority_lower_than_or_equals: Union[Unset, None, int] = UNSET,
    priority_higher_than_or_equals: Union[Unset, None, int] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_jobs_without_tenant_id: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetJobsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetJobsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[JobDto]]]:
    kwargs = _get_kwargs(
        client=client,
        job_id=job_id,
        job_ids=job_ids,
        job_definition_id=job_definition_id,
        process_instance_id=process_instance_id,
        process_instance_ids=process_instance_ids,
        execution_id=execution_id,
        process_definition_id=process_definition_id,
        process_definition_key=process_definition_key,
        activity_id=activity_id,
        with_retries_left=with_retries_left,
        executable=executable,
        timers=timers,
        messages=messages,
        due_dates=due_dates,
        create_times=create_times,
        with_exception=with_exception,
        exception_message=exception_message,
        failed_activity_id=failed_activity_id,
        no_retries_left=no_retries_left,
        active=active,
        suspended=suspended,
        priority_lower_than_or_equals=priority_lower_than_or_equals,
        priority_higher_than_or_equals=priority_higher_than_or_equals,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_jobs_without_tenant_id=include_jobs_without_tenant_id,
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
    job_id: Union[Unset, None, str] = UNSET,
    job_ids: Union[Unset, None, str] = UNSET,
    job_definition_id: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    execution_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    with_retries_left: Union[Unset, None, bool] = UNSET,
    executable: Union[Unset, None, bool] = UNSET,
    timers: Union[Unset, None, bool] = UNSET,
    messages: Union[Unset, None, bool] = UNSET,
    due_dates: Union[Unset, None, str] = UNSET,
    create_times: Union[Unset, None, str] = UNSET,
    with_exception: Union[Unset, None, bool] = UNSET,
    exception_message: Union[Unset, None, str] = UNSET,
    failed_activity_id: Union[Unset, None, str] = UNSET,
    no_retries_left: Union[Unset, None, bool] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    priority_lower_than_or_equals: Union[Unset, None, int] = UNSET,
    priority_higher_than_or_equals: Union[Unset, None, int] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_jobs_without_tenant_id: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetJobsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetJobsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[JobDto]]]:
    """Queries for jobs that fulfill given parameters.
    The size of the result set can be retrieved by using the [Get Job
    Count](https://docs.camunda.org/manual/7.15/reference/rest/job/get-query-count/) method."""

    return (
        await asyncio_detailed(
            client=client,
            job_id=job_id,
            job_ids=job_ids,
            job_definition_id=job_definition_id,
            process_instance_id=process_instance_id,
            process_instance_ids=process_instance_ids,
            execution_id=execution_id,
            process_definition_id=process_definition_id,
            process_definition_key=process_definition_key,
            activity_id=activity_id,
            with_retries_left=with_retries_left,
            executable=executable,
            timers=timers,
            messages=messages,
            due_dates=due_dates,
            create_times=create_times,
            with_exception=with_exception,
            exception_message=exception_message,
            failed_activity_id=failed_activity_id,
            no_retries_left=no_retries_left,
            active=active,
            suspended=suspended,
            priority_lower_than_or_equals=priority_lower_than_or_equals,
            priority_higher_than_or_equals=priority_higher_than_or_equals,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
            include_jobs_without_tenant_id=include_jobs_without_tenant_id,
            sort_by=sort_by,
            sort_order=sort_order,
            first_result=first_result,
            max_results=max_results,
        )
    ).parsed
