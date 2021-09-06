import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.get_process_definitions_sort_by import GetProcessDefinitionsSortBy
from ...models.get_process_definitions_sort_order import GetProcessDefinitionsSortOrder
from ...models.process_definition_dto import ProcessDefinitionDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployed_after: Union[Unset, None, datetime.datetime] = UNSET,
    deployed_at: Union[Unset, None, datetime.datetime] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    keys_in: Union[Unset, None, str] = UNSET,
    key_like: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    category_like: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, int] = UNSET,
    latest_version: Union[Unset, None, bool] = UNSET,
    resource_name: Union[Unset, None, str] = UNSET,
    resource_name_like: Union[Unset, None, str] = UNSET,
    startable_by: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_process_definitions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    version_tag: Union[Unset, None, str] = UNSET,
    version_tag_like: Union[Unset, None, str] = UNSET,
    without_version_tag: Union[Unset, None, bool] = UNSET,
    startable_in_tasklist: Union[Unset, None, bool] = UNSET,
    not_startable_in_tasklist: Union[Unset, None, bool] = UNSET,
    startable_permission_check: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetProcessDefinitionsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetProcessDefinitionsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/process-definition".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_deployed_after: Union[Unset, None, str] = UNSET
    if not isinstance(deployed_after, Unset):
        json_deployed_after = deployed_after.isoformat() if deployed_after else None

    json_deployed_at: Union[Unset, None, str] = UNSET
    if not isinstance(deployed_at, Unset):
        json_deployed_at = deployed_at.isoformat() if deployed_at else None

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params: Dict[str, Any] = {
        "processDefinitionId": process_definition_id,
        "processDefinitionIdIn": process_definition_id_in,
        "name": name,
        "nameLike": name_like,
        "deploymentId": deployment_id,
        "deployedAfter": json_deployed_after,
        "deployedAt": json_deployed_at,
        "key": key,
        "keysIn": keys_in,
        "keyLike": key_like,
        "category": category,
        "categoryLike": category_like,
        "version": version,
        "latestVersion": latest_version,
        "resourceName": resource_name,
        "resourceNameLike": resource_name_like,
        "startableBy": startable_by,
        "active": active,
        "suspended": suspended,
        "incidentId": incident_id,
        "incidentType": incident_type,
        "incidentMessage": incident_message,
        "incidentMessageLike": incident_message_like,
        "tenantIdIn": tenant_id_in,
        "withoutTenantId": without_tenant_id,
        "includeProcessDefinitionsWithoutTenantId": include_process_definitions_without_tenant_id,
        "versionTag": version_tag,
        "versionTagLike": version_tag_like,
        "withoutVersionTag": without_version_tag,
        "startableInTasklist": startable_in_tasklist,
        "notStartableInTasklist": not_startable_in_tasklist,
        "startablePermissionCheck": startable_permission_check,
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[ProcessDefinitionDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProcessDefinitionDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[ProcessDefinitionDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployed_after: Union[Unset, None, datetime.datetime] = UNSET,
    deployed_at: Union[Unset, None, datetime.datetime] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    keys_in: Union[Unset, None, str] = UNSET,
    key_like: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    category_like: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, int] = UNSET,
    latest_version: Union[Unset, None, bool] = UNSET,
    resource_name: Union[Unset, None, str] = UNSET,
    resource_name_like: Union[Unset, None, str] = UNSET,
    startable_by: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_process_definitions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    version_tag: Union[Unset, None, str] = UNSET,
    version_tag_like: Union[Unset, None, str] = UNSET,
    without_version_tag: Union[Unset, None, bool] = UNSET,
    startable_in_tasklist: Union[Unset, None, bool] = UNSET,
    not_startable_in_tasklist: Union[Unset, None, bool] = UNSET,
    startable_permission_check: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetProcessDefinitionsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetProcessDefinitionsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[ProcessDefinitionDto]]]:
    kwargs = _get_kwargs(
        client=client,
        process_definition_id=process_definition_id,
        process_definition_id_in=process_definition_id_in,
        name=name,
        name_like=name_like,
        deployment_id=deployment_id,
        deployed_after=deployed_after,
        deployed_at=deployed_at,
        key=key,
        keys_in=keys_in,
        key_like=key_like,
        category=category,
        category_like=category_like,
        version=version,
        latest_version=latest_version,
        resource_name=resource_name,
        resource_name_like=resource_name_like,
        startable_by=startable_by,
        active=active,
        suspended=suspended,
        incident_id=incident_id,
        incident_type=incident_type,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_process_definitions_without_tenant_id=include_process_definitions_without_tenant_id,
        version_tag=version_tag,
        version_tag_like=version_tag_like,
        without_version_tag=without_version_tag,
        startable_in_tasklist=startable_in_tasklist,
        not_startable_in_tasklist=not_startable_in_tasklist,
        startable_permission_check=startable_permission_check,
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
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployed_after: Union[Unset, None, datetime.datetime] = UNSET,
    deployed_at: Union[Unset, None, datetime.datetime] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    keys_in: Union[Unset, None, str] = UNSET,
    key_like: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    category_like: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, int] = UNSET,
    latest_version: Union[Unset, None, bool] = UNSET,
    resource_name: Union[Unset, None, str] = UNSET,
    resource_name_like: Union[Unset, None, str] = UNSET,
    startable_by: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_process_definitions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    version_tag: Union[Unset, None, str] = UNSET,
    version_tag_like: Union[Unset, None, str] = UNSET,
    without_version_tag: Union[Unset, None, bool] = UNSET,
    startable_in_tasklist: Union[Unset, None, bool] = UNSET,
    not_startable_in_tasklist: Union[Unset, None, bool] = UNSET,
    startable_permission_check: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetProcessDefinitionsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetProcessDefinitionsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[ProcessDefinitionDto]]]:
    """Queries for process definitions that fulfill given parameters. Parameters may be the properties of
    process definitions, such as the name, key or version. The size of the result set can be retrieved
    by using the [Get Definition Count](https://docs.camunda.org/manual/7.15/reference/rest/process-definition/get-query-count/) method."""

    return sync_detailed(
        client=client,
        process_definition_id=process_definition_id,
        process_definition_id_in=process_definition_id_in,
        name=name,
        name_like=name_like,
        deployment_id=deployment_id,
        deployed_after=deployed_after,
        deployed_at=deployed_at,
        key=key,
        keys_in=keys_in,
        key_like=key_like,
        category=category,
        category_like=category_like,
        version=version,
        latest_version=latest_version,
        resource_name=resource_name,
        resource_name_like=resource_name_like,
        startable_by=startable_by,
        active=active,
        suspended=suspended,
        incident_id=incident_id,
        incident_type=incident_type,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_process_definitions_without_tenant_id=include_process_definitions_without_tenant_id,
        version_tag=version_tag,
        version_tag_like=version_tag_like,
        without_version_tag=without_version_tag,
        startable_in_tasklist=startable_in_tasklist,
        not_startable_in_tasklist=not_startable_in_tasklist,
        startable_permission_check=startable_permission_check,
        sort_by=sort_by,
        sort_order=sort_order,
        first_result=first_result,
        max_results=max_results,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployed_after: Union[Unset, None, datetime.datetime] = UNSET,
    deployed_at: Union[Unset, None, datetime.datetime] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    keys_in: Union[Unset, None, str] = UNSET,
    key_like: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    category_like: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, int] = UNSET,
    latest_version: Union[Unset, None, bool] = UNSET,
    resource_name: Union[Unset, None, str] = UNSET,
    resource_name_like: Union[Unset, None, str] = UNSET,
    startable_by: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_process_definitions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    version_tag: Union[Unset, None, str] = UNSET,
    version_tag_like: Union[Unset, None, str] = UNSET,
    without_version_tag: Union[Unset, None, bool] = UNSET,
    startable_in_tasklist: Union[Unset, None, bool] = UNSET,
    not_startable_in_tasklist: Union[Unset, None, bool] = UNSET,
    startable_permission_check: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetProcessDefinitionsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetProcessDefinitionsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Response[Union[ExceptionDto, List[ProcessDefinitionDto]]]:
    kwargs = _get_kwargs(
        client=client,
        process_definition_id=process_definition_id,
        process_definition_id_in=process_definition_id_in,
        name=name,
        name_like=name_like,
        deployment_id=deployment_id,
        deployed_after=deployed_after,
        deployed_at=deployed_at,
        key=key,
        keys_in=keys_in,
        key_like=key_like,
        category=category,
        category_like=category_like,
        version=version,
        latest_version=latest_version,
        resource_name=resource_name,
        resource_name_like=resource_name_like,
        startable_by=startable_by,
        active=active,
        suspended=suspended,
        incident_id=incident_id,
        incident_type=incident_type,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_process_definitions_without_tenant_id=include_process_definitions_without_tenant_id,
        version_tag=version_tag,
        version_tag_like=version_tag_like,
        without_version_tag=without_version_tag,
        startable_in_tasklist=startable_in_tasklist,
        not_startable_in_tasklist=not_startable_in_tasklist,
        startable_permission_check=startable_permission_check,
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
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployed_after: Union[Unset, None, datetime.datetime] = UNSET,
    deployed_at: Union[Unset, None, datetime.datetime] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    keys_in: Union[Unset, None, str] = UNSET,
    key_like: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    category_like: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, int] = UNSET,
    latest_version: Union[Unset, None, bool] = UNSET,
    resource_name: Union[Unset, None, str] = UNSET,
    resource_name_like: Union[Unset, None, str] = UNSET,
    startable_by: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_process_definitions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    version_tag: Union[Unset, None, str] = UNSET,
    version_tag_like: Union[Unset, None, str] = UNSET,
    without_version_tag: Union[Unset, None, bool] = UNSET,
    startable_in_tasklist: Union[Unset, None, bool] = UNSET,
    not_startable_in_tasklist: Union[Unset, None, bool] = UNSET,
    startable_permission_check: Union[Unset, None, bool] = UNSET,
    sort_by: Union[Unset, None, GetProcessDefinitionsSortBy] = UNSET,
    sort_order: Union[Unset, None, GetProcessDefinitionsSortOrder] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ExceptionDto, List[ProcessDefinitionDto]]]:
    """Queries for process definitions that fulfill given parameters. Parameters may be the properties of
    process definitions, such as the name, key or version. The size of the result set can be retrieved
    by using the [Get Definition Count](https://docs.camunda.org/manual/7.15/reference/rest/process-definition/get-query-count/) method."""

    return (
        await asyncio_detailed(
            client=client,
            process_definition_id=process_definition_id,
            process_definition_id_in=process_definition_id_in,
            name=name,
            name_like=name_like,
            deployment_id=deployment_id,
            deployed_after=deployed_after,
            deployed_at=deployed_at,
            key=key,
            keys_in=keys_in,
            key_like=key_like,
            category=category,
            category_like=category_like,
            version=version,
            latest_version=latest_version,
            resource_name=resource_name,
            resource_name_like=resource_name_like,
            startable_by=startable_by,
            active=active,
            suspended=suspended,
            incident_id=incident_id,
            incident_type=incident_type,
            incident_message=incident_message,
            incident_message_like=incident_message_like,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
            include_process_definitions_without_tenant_id=include_process_definitions_without_tenant_id,
            version_tag=version_tag,
            version_tag_like=version_tag_like,
            without_version_tag=without_version_tag,
            startable_in_tasklist=startable_in_tasklist,
            not_startable_in_tasklist=not_startable_in_tasklist,
            startable_permission_check=startable_permission_check,
            sort_by=sort_by,
            sort_order=sort_order,
            first_result=first_result,
            max_results=max_results,
        )
    ).parsed
