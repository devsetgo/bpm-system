import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.deployment_dto import DeploymentDto
from ...models.exception_dto import ExceptionDto
from ...models.get_deployments_sort_by import GetDeploymentsSortBy
from ...models.get_deployments_sort_order import GetDeploymentsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
    without_source: Union[Unset, None, bool] = False,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = False,
    include_deployments_without_tenant_id: Union[Unset, None, bool] = False,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    sort_by: Union[Unset, None, GetDeploymentsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetDeploymentsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/deployment".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_after: Union[Unset, None, str] = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat() if after else None

    json_before: Union[Unset, None, str] = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat() if before else None

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params: Dict[str, Any] = {
        "id": id,
        "name": name,
        "nameLike": name_like,
        "source": source,
        "withoutSource": without_source,
        "tenantIdIn": tenant_id_in,
        "withoutTenantId": without_tenant_id,
        "includeDeploymentsWithoutTenantId": include_deployments_without_tenant_id,
        "after": json_after,
        "before": json_before,
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[DeploymentDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DeploymentDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[DeploymentDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
    without_source: Union[Unset, None, bool] = False,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = False,
    include_deployments_without_tenant_id: Union[Unset, None, bool] = False,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    sort_by: Union[Unset, None, GetDeploymentsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetDeploymentsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[DeploymentDto]]]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        name=name,
        name_like=name_like,
        source=source,
        without_source=without_source,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_deployments_without_tenant_id=include_deployments_without_tenant_id,
        after=after,
        before=before,
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
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
    without_source: Union[Unset, None, bool] = False,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = False,
    include_deployments_without_tenant_id: Union[Unset, None, bool] = False,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    sort_by: Union[Unset, None, GetDeploymentsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetDeploymentsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[DeploymentDto]]]:
    """Queries for deployments that fulfill given parameters. Parameters may be the properties of deployments,
    such as the id or name or a range of the deployment time. The size of the result set can be retrieved by
    using the [Get Deployment count](https://docs.camunda.org/manual/7.15/reference/rest/deployment/get-query-count/) method."""

    return sync_detailed(
        client=client,
        id=id,
        name=name,
        name_like=name_like,
        source=source,
        without_source=without_source,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_deployments_without_tenant_id=include_deployments_without_tenant_id,
        after=after,
        before=before,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
    without_source: Union[Unset, None, bool] = False,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = False,
    include_deployments_without_tenant_id: Union[Unset, None, bool] = False,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    sort_by: Union[Unset, None, GetDeploymentsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetDeploymentsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[DeploymentDto]]]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        name=name,
        name_like=name_like,
        source=source,
        without_source=without_source,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_deployments_without_tenant_id=include_deployments_without_tenant_id,
        after=after,
        before=before,
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
    id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    source: Union[Unset, None, str] = UNSET,
    without_source: Union[Unset, None, bool] = False,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = False,
    include_deployments_without_tenant_id: Union[Unset, None, bool] = False,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    sort_by: Union[Unset, None, GetDeploymentsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetDeploymentsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[DeploymentDto]]]:
    """Queries for deployments that fulfill given parameters. Parameters may be the properties of deployments,
    such as the id or name or a range of the deployment time. The size of the result set can be retrieved by
    using the [Get Deployment count](https://docs.camunda.org/manual/7.15/reference/rest/deployment/get-query-count/) method."""

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            name=name,
            name_like=name_like,
            source=source,
            without_source=without_source,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
            include_deployments_without_tenant_id=include_deployments_without_tenant_id,
            after=after,
            before=before,
            sort_by=sort_by,
            sort_order=sort_order,
            first_result=first_result,
            max_results=max_results,
        )
    ).parsed
