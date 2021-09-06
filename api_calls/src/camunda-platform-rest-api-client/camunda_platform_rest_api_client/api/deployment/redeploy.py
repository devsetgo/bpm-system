from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.deployment_with_definitions_dto import DeploymentWithDefinitionsDto
from ...models.exception_dto import ExceptionDto
from ...models.redeployment_dto import RedeploymentDto
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: RedeploymentDto,
) -> Dict[str, Any]:
    url = "{}/deployment/{id}/redeploy".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[DeploymentWithDefinitionsDto, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = DeploymentWithDefinitionsDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DeploymentWithDefinitionsDto, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: RedeploymentDto,
) -> Response[Union[DeploymentWithDefinitionsDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: RedeploymentDto,
) -> Optional[Union[DeploymentWithDefinitionsDto, ExceptionDto]]:
    """Re-deploys an existing deployment.

    The deployment resources to re-deploy can be restricted by using the properties `resourceIds` or
    `resourceNames`. If no deployment resources to re-deploy are passed then all existing resources of the
    given deployment are re-deployed.

    **Warning**: Deployments can contain custom code in form of scripts or EL expressions to customize
    process behavior. This may be abused for remote execution of arbitrary code. See the section on
    [security considerations for custom code](https://docs.camunda.org/manual/7.15/user-guide/process-engine/securing-custom-code/) in
    the user guide for details."""

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: RedeploymentDto,
) -> Response[Union[DeploymentWithDefinitionsDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: RedeploymentDto,
) -> Optional[Union[DeploymentWithDefinitionsDto, ExceptionDto]]:
    """Re-deploys an existing deployment.

    The deployment resources to re-deploy can be restricted by using the properties `resourceIds` or
    `resourceNames`. If no deployment resources to re-deploy are passed then all existing resources of the
    given deployment are re-deployed.

    **Warning**: Deployments can contain custom code in form of scripts or EL expressions to customize
    process behavior. This may be abused for remote execution of arbitrary code. See the section on
    [security considerations for custom code](https://docs.camunda.org/manual/7.15/user-guide/process-engine/securing-custom-code/) in
    the user guide for details."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
