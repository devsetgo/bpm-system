from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.count_result_dto import CountResultDto
from ...models.exception_dto import ExceptionDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    batch_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/batch/count".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
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
    batch_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
) -> Response[Union[CountResultDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
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
    batch_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Requests the number of batches that fulfill the query criteria.
    Takes the same filtering parameters as the [Get Batches](https://docs.camunda.org/manual/7.15/reference/rest/batch/get-query/) method."""

    return sync_detailed(
        client=client,
        batch_id=batch_id,
        type=type,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        suspended=suspended,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    batch_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
) -> Response[Union[CountResultDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
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
    batch_id: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Requests the number of batches that fulfill the query criteria.
    Takes the same filtering parameters as the [Get Batches](https://docs.camunda.org/manual/7.15/reference/rest/batch/get-query/) method."""

    return (
        await asyncio_detailed(
            client=client,
            batch_id=batch_id,
            type=type,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
            suspended=suspended,
        )
    ).parsed
