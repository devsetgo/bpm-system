from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.get_variable_instances_sort_by import GetVariableInstancesSortBy
from ...models.get_variable_instances_sort_order import GetVariableInstancesSortOrder
from ...models.variable_instance_dto import VariableInstanceDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    variable_name: Union[Unset, None, str] = UNSET,
    variable_name_like: Union[Unset, None, str] = UNSET,
    process_instance_id_in: Union[Unset, None, str] = UNSET,
    execution_id_in: Union[Unset, None, str] = UNSET,
    case_instance_id_in: Union[Unset, None, str] = UNSET,
    case_execution_id_in: Union[Unset, None, str] = UNSET,
    task_id_in: Union[Unset, None, str] = UNSET,
    batch_id_in: Union[Unset, None, str] = UNSET,
    activity_instance_id_in: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    variable_values: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetVariableInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetVariableInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    deserialize_values: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/variable-instance".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params: Dict[str, Any] = {
        "variableName": variable_name,
        "variableNameLike": variable_name_like,
        "processInstanceIdIn": process_instance_id_in,
        "executionIdIn": execution_id_in,
        "caseInstanceIdIn": case_instance_id_in,
        "caseExecutionIdIn": case_execution_id_in,
        "taskIdIn": task_id_in,
        "batchIdIn": batch_id_in,
        "activityInstanceIdIn": activity_instance_id_in,
        "tenantIdIn": tenant_id_in,
        "variableValues": variable_values,
        "variableNamesIgnoreCase": variable_names_ignore_case,
        "variableValuesIgnoreCase": variable_values_ignore_case,
        "sortBy": json_sort_by,
        "sortOrder": json_sort_order,
        "firstResult": first_result,
        "maxResults": max_results,
        "deserializeValues": deserialize_values,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[VariableInstanceDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VariableInstanceDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[VariableInstanceDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    variable_name: Union[Unset, None, str] = UNSET,
    variable_name_like: Union[Unset, None, str] = UNSET,
    process_instance_id_in: Union[Unset, None, str] = UNSET,
    execution_id_in: Union[Unset, None, str] = UNSET,
    case_instance_id_in: Union[Unset, None, str] = UNSET,
    case_execution_id_in: Union[Unset, None, str] = UNSET,
    task_id_in: Union[Unset, None, str] = UNSET,
    batch_id_in: Union[Unset, None, str] = UNSET,
    activity_instance_id_in: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    variable_values: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetVariableInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetVariableInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    deserialize_values: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[VariableInstanceDto]]]:
    kwargs = _get_kwargs(
        client=client,
        variable_name=variable_name,
        variable_name_like=variable_name_like,
        process_instance_id_in=process_instance_id_in,
        execution_id_in=execution_id_in,
        case_instance_id_in=case_instance_id_in,
        case_execution_id_in=case_execution_id_in,
        task_id_in=task_id_in,
        batch_id_in=batch_id_in,
        activity_instance_id_in=activity_instance_id_in,
        tenant_id_in=tenant_id_in,
        variable_values=variable_values,
        variable_names_ignore_case=variable_names_ignore_case,
        variable_values_ignore_case=variable_values_ignore_case,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        deserialize_values=deserialize_values,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    variable_name: Union[Unset, None, str] = UNSET,
    variable_name_like: Union[Unset, None, str] = UNSET,
    process_instance_id_in: Union[Unset, None, str] = UNSET,
    execution_id_in: Union[Unset, None, str] = UNSET,
    case_instance_id_in: Union[Unset, None, str] = UNSET,
    case_execution_id_in: Union[Unset, None, str] = UNSET,
    task_id_in: Union[Unset, None, str] = UNSET,
    batch_id_in: Union[Unset, None, str] = UNSET,
    activity_instance_id_in: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    variable_values: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetVariableInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetVariableInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    deserialize_values: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[VariableInstanceDto]]]:
    """Query for variable instances that fulfill given parameters. Parameters may be the
    properties of variable instances, such as the name or type. The size
    of the result set can be retrieved by using the [Get Variable Instance
    Count](https://docs.camunda.org/manual/7.15/reference/rest/variable-instance/get-query-count/)
    method."""

    return sync_detailed(
        client=client,
        variable_name=variable_name,
        variable_name_like=variable_name_like,
        process_instance_id_in=process_instance_id_in,
        execution_id_in=execution_id_in,
        case_instance_id_in=case_instance_id_in,
        case_execution_id_in=case_execution_id_in,
        task_id_in=task_id_in,
        batch_id_in=batch_id_in,
        activity_instance_id_in=activity_instance_id_in,
        tenant_id_in=tenant_id_in,
        variable_values=variable_values,
        variable_names_ignore_case=variable_names_ignore_case,
        variable_values_ignore_case=variable_values_ignore_case,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        deserialize_values=deserialize_values,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    variable_name: Union[Unset, None, str] = UNSET,
    variable_name_like: Union[Unset, None, str] = UNSET,
    process_instance_id_in: Union[Unset, None, str] = UNSET,
    execution_id_in: Union[Unset, None, str] = UNSET,
    case_instance_id_in: Union[Unset, None, str] = UNSET,
    case_execution_id_in: Union[Unset, None, str] = UNSET,
    task_id_in: Union[Unset, None, str] = UNSET,
    batch_id_in: Union[Unset, None, str] = UNSET,
    activity_instance_id_in: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    variable_values: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetVariableInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetVariableInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    deserialize_values: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[VariableInstanceDto]]]:
    kwargs = _get_kwargs(
        client=client,
        variable_name=variable_name,
        variable_name_like=variable_name_like,
        process_instance_id_in=process_instance_id_in,
        execution_id_in=execution_id_in,
        case_instance_id_in=case_instance_id_in,
        case_execution_id_in=case_execution_id_in,
        task_id_in=task_id_in,
        batch_id_in=batch_id_in,
        activity_instance_id_in=activity_instance_id_in,
        tenant_id_in=tenant_id_in,
        variable_values=variable_values,
        variable_names_ignore_case=variable_names_ignore_case,
        variable_values_ignore_case=variable_values_ignore_case,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        deserialize_values=deserialize_values,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    variable_name: Union[Unset, None, str] = UNSET,
    variable_name_like: Union[Unset, None, str] = UNSET,
    process_instance_id_in: Union[Unset, None, str] = UNSET,
    execution_id_in: Union[Unset, None, str] = UNSET,
    case_instance_id_in: Union[Unset, None, str] = UNSET,
    case_execution_id_in: Union[Unset, None, str] = UNSET,
    task_id_in: Union[Unset, None, str] = UNSET,
    batch_id_in: Union[Unset, None, str] = UNSET,
    activity_instance_id_in: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    variable_values: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetVariableInstancesSortBy] = UNSET,
    sort_order: Union[Unset, None, GetVariableInstancesSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    deserialize_values: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[VariableInstanceDto]]]:
    """Query for variable instances that fulfill given parameters. Parameters may be the
    properties of variable instances, such as the name or type. The size
    of the result set can be retrieved by using the [Get Variable Instance
    Count](https://docs.camunda.org/manual/7.15/reference/rest/variable-instance/get-query-count/)
    method."""

    return (
        await asyncio_detailed(
            client=client,
            variable_name=variable_name,
            variable_name_like=variable_name_like,
            process_instance_id_in=process_instance_id_in,
            execution_id_in=execution_id_in,
            case_instance_id_in=case_instance_id_in,
            case_execution_id_in=case_execution_id_in,
            task_id_in=task_id_in,
            batch_id_in=batch_id_in,
            activity_instance_id_in=activity_instance_id_in,
            tenant_id_in=tenant_id_in,
            variable_values=variable_values,
            variable_names_ignore_case=variable_names_ignore_case,
            variable_values_ignore_case=variable_values_ignore_case,
            sort_by=sort_by,
            sort_order=sort_order,
            first_result=first_result,
            max_results=max_results,
            deserialize_values=deserialize_values,
        )
    ).parsed
