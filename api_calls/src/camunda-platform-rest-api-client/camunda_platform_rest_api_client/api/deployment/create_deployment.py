from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.deployment_with_definitions_dto import DeploymentWithDefinitionsDto
from ...models.multi_form_deployment_dto import MultiFormDeploymentDto
from ...models.parse_exception_dto import ParseExceptionDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    multipart_data: MultiFormDeploymentDto,
) -> Dict[str, Any]:
    url = "{}/deployment/create".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[DeploymentWithDefinitionsDto, ParseExceptionDto]]:
    if response.status_code == 200:
        response_200 = DeploymentWithDefinitionsDto.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ParseExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DeploymentWithDefinitionsDto, ParseExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    multipart_data: MultiFormDeploymentDto,
) -> Response[Union[DeploymentWithDefinitionsDto, ParseExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    multipart_data: MultiFormDeploymentDto,
) -> Optional[Union[DeploymentWithDefinitionsDto, ParseExceptionDto]]:
    """Creates a deployment.

    **Security Consideration**

    Deployments can contain custom code in form of scripts or EL expressions to customize process behavior.
    This may be abused for remote execution of arbitrary code."""

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: MultiFormDeploymentDto,
) -> Response[Union[DeploymentWithDefinitionsDto, ParseExceptionDto]]:
    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: MultiFormDeploymentDto,
) -> Optional[Union[DeploymentWithDefinitionsDto, ParseExceptionDto]]:
    """Creates a deployment.

    **Security Consideration**

    Deployments can contain custom code in form of scripts or EL expressions to customize process behavior.
    This may be abused for remote execution of arbitrary code."""

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
