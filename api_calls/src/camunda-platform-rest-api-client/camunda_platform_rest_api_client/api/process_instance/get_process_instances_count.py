from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.count_result_dto import CountResultDto
from ...models.exception_dto import ExceptionDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    business_key: Union[Unset, None, str] = UNSET,
    business_key_like: Union[Unset, None, str] = UNSET,
    case_instance_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_definition_key_not_in: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    super_process_instance: Union[Unset, None, str] = UNSET,
    sub_process_instance: Union[Unset, None, str] = UNSET,
    super_case_instance: Union[Unset, None, str] = UNSET,
    sub_case_instance: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = False,
    suspended: Union[Unset, None, bool] = False,
    with_incident: Union[Unset, None, bool] = False,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = False,
    process_definition_without_tenant_id: Union[Unset, None, bool] = False,
    activity_id_in: Union[Unset, None, str] = UNSET,
    root_process_instances: Union[Unset, None, bool] = False,
    leaf_process_instances: Union[Unset, None, bool] = False,
    variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = False,
    variable_values_ignore_case: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/process-instance/count".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "processInstanceIds": process_instance_ids,
        "businessKey": business_key,
        "businessKeyLike": business_key_like,
        "caseInstanceId": case_instance_id,
        "processDefinitionId": process_definition_id,
        "processDefinitionKey": process_definition_key,
        "processDefinitionKeyIn": process_definition_key_in,
        "processDefinitionKeyNotIn": process_definition_key_not_in,
        "deploymentId": deployment_id,
        "superProcessInstance": super_process_instance,
        "subProcessInstance": sub_process_instance,
        "superCaseInstance": super_case_instance,
        "subCaseInstance": sub_case_instance,
        "active": active,
        "suspended": suspended,
        "withIncident": with_incident,
        "incidentId": incident_id,
        "incidentType": incident_type,
        "incidentMessage": incident_message,
        "incidentMessageLike": incident_message_like,
        "tenantIdIn": tenant_id_in,
        "withoutTenantId": without_tenant_id,
        "processDefinitionWithoutTenantId": process_definition_without_tenant_id,
        "activityIdIn": activity_id_in,
        "rootProcessInstances": root_process_instances,
        "leafProcessInstances": leaf_process_instances,
        "variables": variables,
        "variableNamesIgnoreCase": variable_names_ignore_case,
        "variableValuesIgnoreCase": variable_values_ignore_case,
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
    process_instance_ids: Union[Unset, None, str] = UNSET,
    business_key: Union[Unset, None, str] = UNSET,
    business_key_like: Union[Unset, None, str] = UNSET,
    case_instance_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_definition_key_not_in: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    super_process_instance: Union[Unset, None, str] = UNSET,
    sub_process_instance: Union[Unset, None, str] = UNSET,
    super_case_instance: Union[Unset, None, str] = UNSET,
    sub_case_instance: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = False,
    suspended: Union[Unset, None, bool] = False,
    with_incident: Union[Unset, None, bool] = False,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = False,
    process_definition_without_tenant_id: Union[Unset, None, bool] = False,
    activity_id_in: Union[Unset, None, str] = UNSET,
    root_process_instances: Union[Unset, None, bool] = False,
    leaf_process_instances: Union[Unset, None, bool] = False,
    variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = False,
    variable_values_ignore_case: Union[Unset, None, bool] = False,
) -> Response[Union[CountResultDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        process_instance_ids=process_instance_ids,
        business_key=business_key,
        business_key_like=business_key_like,
        case_instance_id=case_instance_id,
        process_definition_id=process_definition_id,
        process_definition_key=process_definition_key,
        process_definition_key_in=process_definition_key_in,
        process_definition_key_not_in=process_definition_key_not_in,
        deployment_id=deployment_id,
        super_process_instance=super_process_instance,
        sub_process_instance=sub_process_instance,
        super_case_instance=super_case_instance,
        sub_case_instance=sub_case_instance,
        active=active,
        suspended=suspended,
        with_incident=with_incident,
        incident_id=incident_id,
        incident_type=incident_type,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        process_definition_without_tenant_id=process_definition_without_tenant_id,
        activity_id_in=activity_id_in,
        root_process_instances=root_process_instances,
        leaf_process_instances=leaf_process_instances,
        variables=variables,
        variable_names_ignore_case=variable_names_ignore_case,
        variable_values_ignore_case=variable_values_ignore_case,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    business_key: Union[Unset, None, str] = UNSET,
    business_key_like: Union[Unset, None, str] = UNSET,
    case_instance_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_definition_key_not_in: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    super_process_instance: Union[Unset, None, str] = UNSET,
    sub_process_instance: Union[Unset, None, str] = UNSET,
    super_case_instance: Union[Unset, None, str] = UNSET,
    sub_case_instance: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = False,
    suspended: Union[Unset, None, bool] = False,
    with_incident: Union[Unset, None, bool] = False,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = False,
    process_definition_without_tenant_id: Union[Unset, None, bool] = False,
    activity_id_in: Union[Unset, None, str] = UNSET,
    root_process_instances: Union[Unset, None, bool] = False,
    leaf_process_instances: Union[Unset, None, bool] = False,
    variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = False,
    variable_values_ignore_case: Union[Unset, None, bool] = False,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for the number of process instances that fulfill given parameters."""

    return sync_detailed(
        client=client,
        process_instance_ids=process_instance_ids,
        business_key=business_key,
        business_key_like=business_key_like,
        case_instance_id=case_instance_id,
        process_definition_id=process_definition_id,
        process_definition_key=process_definition_key,
        process_definition_key_in=process_definition_key_in,
        process_definition_key_not_in=process_definition_key_not_in,
        deployment_id=deployment_id,
        super_process_instance=super_process_instance,
        sub_process_instance=sub_process_instance,
        super_case_instance=super_case_instance,
        sub_case_instance=sub_case_instance,
        active=active,
        suspended=suspended,
        with_incident=with_incident,
        incident_id=incident_id,
        incident_type=incident_type,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        process_definition_without_tenant_id=process_definition_without_tenant_id,
        activity_id_in=activity_id_in,
        root_process_instances=root_process_instances,
        leaf_process_instances=leaf_process_instances,
        variables=variables,
        variable_names_ignore_case=variable_names_ignore_case,
        variable_values_ignore_case=variable_values_ignore_case,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    business_key: Union[Unset, None, str] = UNSET,
    business_key_like: Union[Unset, None, str] = UNSET,
    case_instance_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_definition_key_not_in: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    super_process_instance: Union[Unset, None, str] = UNSET,
    sub_process_instance: Union[Unset, None, str] = UNSET,
    super_case_instance: Union[Unset, None, str] = UNSET,
    sub_case_instance: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = False,
    suspended: Union[Unset, None, bool] = False,
    with_incident: Union[Unset, None, bool] = False,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = False,
    process_definition_without_tenant_id: Union[Unset, None, bool] = False,
    activity_id_in: Union[Unset, None, str] = UNSET,
    root_process_instances: Union[Unset, None, bool] = False,
    leaf_process_instances: Union[Unset, None, bool] = False,
    variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = False,
    variable_values_ignore_case: Union[Unset, None, bool] = False,
) -> Response[Union[CountResultDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        process_instance_ids=process_instance_ids,
        business_key=business_key,
        business_key_like=business_key_like,
        case_instance_id=case_instance_id,
        process_definition_id=process_definition_id,
        process_definition_key=process_definition_key,
        process_definition_key_in=process_definition_key_in,
        process_definition_key_not_in=process_definition_key_not_in,
        deployment_id=deployment_id,
        super_process_instance=super_process_instance,
        sub_process_instance=sub_process_instance,
        super_case_instance=super_case_instance,
        sub_case_instance=sub_case_instance,
        active=active,
        suspended=suspended,
        with_incident=with_incident,
        incident_id=incident_id,
        incident_type=incident_type,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        tenant_id_in=tenant_id_in,
        without_tenant_id=without_tenant_id,
        process_definition_without_tenant_id=process_definition_without_tenant_id,
        activity_id_in=activity_id_in,
        root_process_instances=root_process_instances,
        leaf_process_instances=leaf_process_instances,
        variables=variables,
        variable_names_ignore_case=variable_names_ignore_case,
        variable_values_ignore_case=variable_values_ignore_case,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    process_instance_ids: Union[Unset, None, str] = UNSET,
    business_key: Union[Unset, None, str] = UNSET,
    business_key_like: Union[Unset, None, str] = UNSET,
    case_instance_id: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_definition_key_in: Union[Unset, None, str] = UNSET,
    process_definition_key_not_in: Union[Unset, None, str] = UNSET,
    deployment_id: Union[Unset, None, str] = UNSET,
    super_process_instance: Union[Unset, None, str] = UNSET,
    sub_process_instance: Union[Unset, None, str] = UNSET,
    super_case_instance: Union[Unset, None, str] = UNSET,
    sub_case_instance: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = False,
    suspended: Union[Unset, None, bool] = False,
    with_incident: Union[Unset, None, bool] = False,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    without_tenant_id: Union[Unset, None, bool] = False,
    process_definition_without_tenant_id: Union[Unset, None, bool] = False,
    activity_id_in: Union[Unset, None, str] = UNSET,
    root_process_instances: Union[Unset, None, bool] = False,
    leaf_process_instances: Union[Unset, None, bool] = False,
    variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = False,
    variable_values_ignore_case: Union[Unset, None, bool] = False,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for the number of process instances that fulfill given parameters."""

    return (
        await asyncio_detailed(
            client=client,
            process_instance_ids=process_instance_ids,
            business_key=business_key,
            business_key_like=business_key_like,
            case_instance_id=case_instance_id,
            process_definition_id=process_definition_id,
            process_definition_key=process_definition_key,
            process_definition_key_in=process_definition_key_in,
            process_definition_key_not_in=process_definition_key_not_in,
            deployment_id=deployment_id,
            super_process_instance=super_process_instance,
            sub_process_instance=sub_process_instance,
            super_case_instance=super_case_instance,
            sub_case_instance=sub_case_instance,
            active=active,
            suspended=suspended,
            with_incident=with_incident,
            incident_id=incident_id,
            incident_type=incident_type,
            incident_message=incident_message,
            incident_message_like=incident_message_like,
            tenant_id_in=tenant_id_in,
            without_tenant_id=without_tenant_id,
            process_definition_without_tenant_id=process_definition_without_tenant_id,
            activity_id_in=activity_id_in,
            root_process_instances=root_process_instances,
            leaf_process_instances=leaf_process_instances,
            variables=variables,
            variable_names_ignore_case=variable_names_ignore_case,
            variable_values_ignore_case=variable_values_ignore_case,
        )
    ).parsed
