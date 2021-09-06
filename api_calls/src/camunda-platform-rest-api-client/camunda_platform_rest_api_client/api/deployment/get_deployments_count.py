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
) -> Dict[str, Any]:
    url = "{}/deployment/count".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_after: Union[Unset, None, str] = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat() if after else None

    json_before: Union[Unset, None, str] = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat() if before else None

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
) -> Response[Union[CountResultDto, ExceptionDto]]:
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
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for the number of deployments that fulfill given parameters. Takes the same parameters as the
    [Get Deployments](https://docs.camunda.org/manual/7.15/reference/rest/deployment/get-query/) method."""

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
) -> Response[Union[CountResultDto, ExceptionDto]]:
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
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for the number of deployments that fulfill given parameters. Takes the same parameters as the
    [Get Deployments](https://docs.camunda.org/manual/7.15/reference/rest/deployment/get-query/) method."""

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
        )
    ).parsed
