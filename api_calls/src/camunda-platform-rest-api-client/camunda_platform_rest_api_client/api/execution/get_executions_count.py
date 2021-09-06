from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.count_result_dto import CountResultDto
from ...models.exception_dto import ExceptionDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    business_key: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    signal_event_subscription_name: Union[Unset, None, str] = UNSET,
    message_event_subscription_name: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    variables: Union[Unset, None, str] = UNSET,
    process_variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/execution/count".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "businessKey": business_key,
        "processDefinitionId": process_definition_id,
        "processDefinitionKey": process_definition_key,
        "processInstanceId": process_instance_id,
        "activityId": activity_id,
        "signalEventSubscriptionName": signal_event_subscription_name,
        "messageEventSubscriptionName": message_event_subscription_name,
        "active": active,
        "suspended": suspended,
        "incidentId": incident_id,
        "incidentType": incident_type,
        "incidentMessage": incident_message,
        "incidentMessageLike": incident_message_like,
        "tenantIdIn": tenant_id_in,
        "variables": variables,
        "processVariables": process_variables,
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
    business_key: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    signal_event_subscription_name: Union[Unset, None, str] = UNSET,
    message_event_subscription_name: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    variables: Union[Unset, None, str] = UNSET,
    process_variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
) -> Response[Union[CountResultDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        business_key=business_key,
        process_definition_id=process_definition_id,
        process_definition_key=process_definition_key,
        process_instance_id=process_instance_id,
        activity_id=activity_id,
        signal_event_subscription_name=signal_event_subscription_name,
        message_event_subscription_name=message_event_subscription_name,
        active=active,
        suspended=suspended,
        incident_id=incident_id,
        incident_type=incident_type,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        tenant_id_in=tenant_id_in,
        variables=variables,
        process_variables=process_variables,
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
    business_key: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    signal_event_subscription_name: Union[Unset, None, str] = UNSET,
    message_event_subscription_name: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    variables: Union[Unset, None, str] = UNSET,
    process_variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for the number of executions that fulfill given parameters.
    Takes the same parameters as the [Get
    Executions](https://docs.camunda.org/manual/7.15/reference/rest/execution/get-query/) method."""

    return sync_detailed(
        client=client,
        business_key=business_key,
        process_definition_id=process_definition_id,
        process_definition_key=process_definition_key,
        process_instance_id=process_instance_id,
        activity_id=activity_id,
        signal_event_subscription_name=signal_event_subscription_name,
        message_event_subscription_name=message_event_subscription_name,
        active=active,
        suspended=suspended,
        incident_id=incident_id,
        incident_type=incident_type,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        tenant_id_in=tenant_id_in,
        variables=variables,
        process_variables=process_variables,
        variable_names_ignore_case=variable_names_ignore_case,
        variable_values_ignore_case=variable_values_ignore_case,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    business_key: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    signal_event_subscription_name: Union[Unset, None, str] = UNSET,
    message_event_subscription_name: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    variables: Union[Unset, None, str] = UNSET,
    process_variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
) -> Response[Union[CountResultDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        business_key=business_key,
        process_definition_id=process_definition_id,
        process_definition_key=process_definition_key,
        process_instance_id=process_instance_id,
        activity_id=activity_id,
        signal_event_subscription_name=signal_event_subscription_name,
        message_event_subscription_name=message_event_subscription_name,
        active=active,
        suspended=suspended,
        incident_id=incident_id,
        incident_type=incident_type,
        incident_message=incident_message,
        incident_message_like=incident_message_like,
        tenant_id_in=tenant_id_in,
        variables=variables,
        process_variables=process_variables,
        variable_names_ignore_case=variable_names_ignore_case,
        variable_values_ignore_case=variable_values_ignore_case,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    business_key: Union[Unset, None, str] = UNSET,
    process_definition_id: Union[Unset, None, str] = UNSET,
    process_definition_key: Union[Unset, None, str] = UNSET,
    process_instance_id: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    signal_event_subscription_name: Union[Unset, None, str] = UNSET,
    message_event_subscription_name: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    suspended: Union[Unset, None, bool] = UNSET,
    incident_id: Union[Unset, None, str] = UNSET,
    incident_type: Union[Unset, None, str] = UNSET,
    incident_message: Union[Unset, None, str] = UNSET,
    incident_message_like: Union[Unset, None, str] = UNSET,
    tenant_id_in: Union[Unset, None, str] = UNSET,
    variables: Union[Unset, None, str] = UNSET,
    process_variables: Union[Unset, None, str] = UNSET,
    variable_names_ignore_case: Union[Unset, None, bool] = UNSET,
    variable_values_ignore_case: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[CountResultDto, ExceptionDto]]:
    """Queries for the number of executions that fulfill given parameters.
    Takes the same parameters as the [Get
    Executions](https://docs.camunda.org/manual/7.15/reference/rest/execution/get-query/) method."""

    return (
        await asyncio_detailed(
            client=client,
            business_key=business_key,
            process_definition_id=process_definition_id,
            process_definition_key=process_definition_key,
            process_instance_id=process_instance_id,
            activity_id=activity_id,
            signal_event_subscription_name=signal_event_subscription_name,
            message_event_subscription_name=message_event_subscription_name,
            active=active,
            suspended=suspended,
            incident_id=incident_id,
            incident_type=incident_type,
            incident_message=incident_message,
            incident_message_like=incident_message_like,
            tenant_id_in=tenant_id_in,
            variables=variables,
            process_variables=process_variables,
            variable_names_ignore_case=variable_names_ignore_case,
            variable_values_ignore_case=variable_values_ignore_case,
        )
    ).parsed
