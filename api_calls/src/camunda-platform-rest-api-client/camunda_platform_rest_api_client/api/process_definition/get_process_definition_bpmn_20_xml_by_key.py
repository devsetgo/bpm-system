from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.authorization_exception_dto import AuthorizationExceptionDto
from ...models.exception_dto import ExceptionDto
from ...models.process_definition_diagram_dto import ProcessDefinitionDiagramDto
from ...types import Response


def _get_kwargs(
    key: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/process-definition/key/{key}/xml".format(client.base_url, key=key)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[AuthorizationExceptionDto, ExceptionDto, ProcessDefinitionDiagramDto]]:
    if response.status_code == 200:
        response_200 = ProcessDefinitionDiagramDto.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = AuthorizationExceptionDto.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[AuthorizationExceptionDto, ExceptionDto, ProcessDefinitionDiagramDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: Client,
) -> Response[Union[AuthorizationExceptionDto, ExceptionDto, ProcessDefinitionDiagramDto]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    key: str,
    *,
    client: Client,
) -> Optional[Union[AuthorizationExceptionDto, ExceptionDto, ProcessDefinitionDiagramDto]]:
    """Retrieves latest version the BPMN 2.0 XML of a process definition."""

    return sync_detailed(
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: Client,
) -> Response[Union[AuthorizationExceptionDto, ExceptionDto, ProcessDefinitionDiagramDto]]:
    kwargs = _get_kwargs(
        key=key,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    key: str,
    *,
    client: Client,
) -> Optional[Union[AuthorizationExceptionDto, ExceptionDto, ProcessDefinitionDiagramDto]]:
    """Retrieves latest version the BPMN 2.0 XML of a process definition."""

    return (
        await asyncio_detailed(
            key=key,
            client=client,
        )
    ).parsed
