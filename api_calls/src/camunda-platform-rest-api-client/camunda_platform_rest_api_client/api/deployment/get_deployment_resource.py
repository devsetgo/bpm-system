from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.deployment_resource_dto import DeploymentResourceDto
from ...models.exception_dto import ExceptionDto
from ...types import Response


def _get_kwargs(
    id: str,
    resource_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/deployment/{id}/resources/{resourceId}".format(client.base_url, id=id, resourceId=resource_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[DeploymentResourceDto, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = DeploymentResourceDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DeploymentResourceDto, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    resource_id: str,
    *,
    client: Client,
) -> Response[Union[DeploymentResourceDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        resource_id=resource_id,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    resource_id: str,
    *,
    client: Client,
) -> Optional[Union[DeploymentResourceDto, ExceptionDto]]:
    """Retrieves a deployment resource by resource id for the given deployment."""

    return sync_detailed(
        id=id,
        resource_id=resource_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    resource_id: str,
    *,
    client: Client,
) -> Response[Union[DeploymentResourceDto, ExceptionDto]]:
    kwargs = _get_kwargs(
        id=id,
        resource_id=resource_id,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    resource_id: str,
    *,
    client: Client,
) -> Optional[Union[DeploymentResourceDto, ExceptionDto]]:
    """Retrieves a deployment resource by resource id for the given deployment."""

    return (
        await asyncio_detailed(
            id=id,
            resource_id=resource_id,
            client=client,
        )
    ).parsed
