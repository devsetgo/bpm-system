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
    decision_definition_id: Union[Unset, None, str] = UNSET,
    decision_definition_id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployed_after: Union[Unset, None, datetime.datetime] = UNSET,
    deployed_at: Union[Unset, None, datetime.datetime] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    key_like: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    category_like: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, int] = UNSET,
    latest_version: Union[Unset, None, bool] = UNSET,
    resource_name: Union[Unset, None, str] = UNSET,
    resource_name_like: Union[Unset, None, str] = UNSET,
    decision_requirements_definition_id: Union[Unset, None, str] = UNSET,
    decision_requirements_definition_key: Union[Unset, None, str] = UNSET,
    without_decision_requirements_definition: Union[Unset, None, bool] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_decision_definitions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    version_tag: Union[Unset, None, str] = UNSET,
    version_tag_like: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/decision-definition/count".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_deployed_after: Union[Unset, None, str] = UNSET
    if not isinstance(deployed_after, Unset):
        json_deployed_after = deployed_after.isoformat() if deployed_after else None

    json_deployed_at: Union[Unset, None, str] = UNSET
    if not isinstance(deployed_at, Unset):
        json_deployed_at = deployed_at.isoformat() if deployed_at else None

    params: Dict[str, Any] = {
        "decisionDefinitionId": decision_definition_id,
        "decisionDefinitionIdIn": decision_definition_id_in,
        "name": name,
        "nameLike": name_like,
        "deploymentId": deployment_id,
        "deployedAfter": json_deployed_after,
        "deployedAt": json_deployed_at,
        "key": key,
        "keyLike": key_like,
        "category": category,
        "categoryLike": category_like,
        "version": version,
        "latestVersion": latest_version,
        "resourceName": resource_name,
        "resourceNameLike": resource_name_like,
        "decisionRequirementsDefinitionId": decision_requirements_definition_id,
        "decisionRequirementsDefinitionKey": decision_requirements_definition_key,
        "withoutDecisionRequirementsDefinition": without_decision_requirements_definition,
        "tenantIdIn": tenant_id_in,
        "withoutTenantId": without_tenant_id,
        "includeDecisionDefinitionsWithoutTenantId": include_decision_definitions_without_tenant_id,
        "versionTag": version_tag,
        "versionTagLike": version_tag_like,
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
    decision_definition_id: Union[Unset, None, str] = UNSET,
    decision_definition_id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployed_after: Union[Unset, None, datetime.datetime] = UNSET,
    deployed_at: Union[Unset, None, datetime.datetime] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    key_like: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    category_like: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, int] = UNSET,
    latest_version: Union[Unset, None, bool] = UNSET,
    resource_name: Union[Unset, None, str] = UNSET,
    resource_name_like: Union[Unset, None, str] = UNSET,
    decision_requirements_definition_id: Union[Unset, None, str] = UNSET,
    decision_requirements_definition_key: Union[Unset, None, str] = UNSET,
    without_decision_requirements_definition: Union[Unset, None, bool] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_decision_definitions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    version_tag: Union[Unset, None, str] = UNSET,
    version_tag_like: Union[Unset, None, str] = UNSET,
) -> Response[Union[CountResultDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        decision_definition_id=decision_definition_id,
        decision_definition_id_in=decision_definition_id_in,
        name=name,
        name_like=name_like,
        deployment_id=deployment_id,
        deployed_after=deployed_after,
        deployed_at=deployed_at,
        key=key,
        key_like=key_like,
        category=category,
        category_like=category_like,
        version=version,
        latest_version=latest_version,
        resource_name=resource_name,
        resource_name_like=resource_name_like,
        decision_requirements_definition_id=decision_requirements_definition_id,
        decision_requirements_definition_key=decision_requirements_definition_key,
        without_decision_requirements_definition=without_decision_requirements_definition,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_decision_definitions_without_tenant_id=include_decision_definitions_without_tenant_id,
        version_tag=version_tag,
        version_tag_like=version_tag_like,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    decision_definition_id: Union[Unset, None, str] = UNSET,
    decision_definition_id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployed_after: Union[Unset, None, datetime.datetime] = UNSET,
    deployed_at: Union[Unset, None, datetime.datetime] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    key_like: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    category_like: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, int] = UNSET,
    latest_version: Union[Unset, None, bool] = UNSET,
    resource_name: Union[Unset, None, str] = UNSET,
    resource_name_like: Union[Unset, None, str] = UNSET,
    decision_requirements_definition_id: Union[Unset, None, str] = UNSET,
    decision_requirements_definition_key: Union[Unset, None, str] = UNSET,
    without_decision_requirements_definition: Union[Unset, None, bool] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_decision_definitions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    version_tag: Union[Unset, None, str] = UNSET,
    version_tag_like: Union[Unset, None, str] = UNSET,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Requests the number of decision definitions that fulfill the query criteria.
    Takes the same filtering parameters as the
    [Get Decision Definition](https://docs.camunda.org/manual/7.15/reference/rest/decision-definition/get-query/) method."""

    return sync_detailed(
        client=client,
        decision_definition_id=decision_definition_id,
        decision_definition_id_in=decision_definition_id_in,
        name=name,
        name_like=name_like,
        deployment_id=deployment_id,
        deployed_after=deployed_after,
        deployed_at=deployed_at,
        key=key,
        key_like=key_like,
        category=category,
        category_like=category_like,
        version=version,
        latest_version=latest_version,
        resource_name=resource_name,
        resource_name_like=resource_name_like,
        decision_requirements_definition_id=decision_requirements_definition_id,
        decision_requirements_definition_key=decision_requirements_definition_key,
        without_decision_requirements_definition=without_decision_requirements_definition,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_decision_definitions_without_tenant_id=include_decision_definitions_without_tenant_id,
        version_tag=version_tag,
        version_tag_like=version_tag_like,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    decision_definition_id: Union[Unset, None, str] = UNSET,
    decision_definition_id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployed_after: Union[Unset, None, datetime.datetime] = UNSET,
    deployed_at: Union[Unset, None, datetime.datetime] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    key_like: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    category_like: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, int] = UNSET,
    latest_version: Union[Unset, None, bool] = UNSET,
    resource_name: Union[Unset, None, str] = UNSET,
    resource_name_like: Union[Unset, None, str] = UNSET,
    decision_requirements_definition_id: Union[Unset, None, str] = UNSET,
    decision_requirements_definition_key: Union[Unset, None, str] = UNSET,
    without_decision_requirements_definition: Union[Unset, None, bool] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_decision_definitions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    version_tag: Union[Unset, None, str] = UNSET,
    version_tag_like: Union[Unset, None, str] = UNSET,
) -> Response[Union[CountResultDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        decision_definition_id=decision_definition_id,
        decision_definition_id_in=decision_definition_id_in,
        name=name,
        name_like=name_like,
        deployment_id=deployment_id,
        deployed_after=deployed_after,
        deployed_at=deployed_at,
        key=key,
        key_like=key_like,
        category=category,
        category_like=category_like,
        version=version,
        latest_version=latest_version,
        resource_name=resource_name,
        resource_name_like=resource_name_like,
        decision_requirements_definition_id=decision_requirements_definition_id,
        decision_requirements_definition_key=decision_requirements_definition_key,
        without_decision_requirements_definition=without_decision_requirements_definition,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        include_decision_definitions_without_tenant_id=include_decision_definitions_without_tenant_id,
        version_tag=version_tag,
        version_tag_like=version_tag_like,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    decision_definition_id: Union[Unset, None, str] = UNSET,
    decision_definition_id_in: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_like: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    deployed_after: Union[Unset, None, datetime.datetime] = UNSET,
    deployed_at: Union[Unset, None, datetime.datetime] = UNSET,
    key: Union[Unset, None, str] = UNSET,
    key_like: Union[Unset, None, str] = UNSET,
    category: Union[Unset, None, str] = UNSET,
    category_like: Union[Unset, None, str] = UNSET,
    version: Union[Unset, None, int] = UNSET,
    latest_version: Union[Unset, None, bool] = UNSET,
    resource_name: Union[Unset, None, str] = UNSET,
    resource_name_like: Union[Unset, None, str] = UNSET,
    decision_requirements_definition_id: Union[Unset, None, str] = UNSET,
    decision_requirements_definition_key: Union[Unset, None, str] = UNSET,
    without_decision_requirements_definition: Union[Unset, None, bool] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = UNSET,
    include_decision_definitions_without_tenant_id: Union[Unset, None, bool] = UNSET,
    version_tag: Union[Unset, None, str] = UNSET,
    version_tag_like: Union[Unset, None, str] = UNSET,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Requests the number of decision definitions that fulfill the query criteria.
    Takes the same filtering parameters as the
    [Get Decision Definition](https://docs.camunda.org/manual/7.15/reference/rest/decision-definition/get-query/) method."""

    return (
        await asyncio_detailed(
            client=client,
            decision_definition_id=decision_definition_id,
            decision_definition_id_in=decision_definition_id_in,
            name=name,
            name_like=name_like,
            deployment_id=deployment_id,
            deployed_after=deployed_after,
            deployed_at=deployed_at,
            key=key,
            key_like=key_like,
            category=category,
            category_like=category_like,
            version=version,
            latest_version=latest_version,
            resource_name=resource_name,
            resource_name_like=resource_name_like,
            decision_requirements_definition_id=decision_requirements_definition_id,
            decision_requirements_definition_key=decision_requirements_definition_key,
            without_decision_requirements_definition=without_decision_requirements_definition,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
            include_decision_definitions_without_tenant_id=include_decision_definitions_without_tenant_id,
            version_tag=version_tag,
            version_tag_like=version_tag_like,
        )
    ).parsed
