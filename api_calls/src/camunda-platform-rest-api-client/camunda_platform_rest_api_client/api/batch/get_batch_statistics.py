from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.batch_statistics_dto import BatchStatisticsDto
from ...models.exception_dto import ExceptionDto
from ...models.get_batch_statistics_sort_by import GetBatchStatisticsSortBy
from ...models.get_batch_statistics_sort_order import GetBatchStatisticsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetBatchStatisticsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetBatchStatisticsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    batch_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/batch/statistics".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params: Dict[str, Any] = {
        "sortBy": json_sort_by,
        "sortOrder": json_sort_order,
        "firstResult": first_result,
        "maxResults": max_results,
        "batchId": batch_id,
        "type": type,
        "tenantIdIn": tenant_id_in,
        "withoutTenantId": without_tenant_id,
        "suspended": suspended,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[BatchStatisticsDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BatchStatisticsDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[BatchStatisticsDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetBatchStatisticsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetBatchStatisticsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    batch_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[BatchStatisticsDto]]]:
    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        batch_id=batch_id,
        type=type,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        suspended=suspended,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetBatchStatisticsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetBatchStatisticsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    batch_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[BatchStatisticsDto]]]:
    """Queries for batch statistics that fulfill given parameters.
    Parameters may be the properties of batches, such as the id or type.
    The size of the result set can be retrieved by using the
    [Get Batch Statistics Count](https://docs.camunda.org/manual/7.15/reference/rest/batch/get-statistics-query-count/) method."""

    return sync_detailed(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        batch_id=batch_id,
        type=type,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        suspended=suspended,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetBatchStatisticsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetBatchStatisticsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    batch_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[BatchStatisticsDto]]]:
    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
        batch_id=batch_id,
        type=type,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        suspended=suspended,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    sort_by: Union[Unset, None, GetBatchStatisticsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetBatchStatisticsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    batch_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[BatchStatisticsDto]]]:
    """Queries for batch statistics that fulfill given parameters.
    Parameters may be the properties of batches, such as the id or type.
    The size of the result set can be retrieved by using the
    [Get Batch Statistics Count](https://docs.camunda.org/manual/7.15/reference/rest/batch/get-statistics-query-count/) method."""

    return (
        await asyncio_detailed(
            client=client,
            sort_by=sort_by,
            sort_order=sort_order,
            first_result=first_result,
            max_results=max_results,
            batch_id=batch_id,
            type=type,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
            suspended=suspended,
        )
    ).parsed
