from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.evaluate_decision_dto import EvaluateDecisionDto
from ...models.exception_dto import ExceptionDto
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: EvaluateDecisionDto,
) -> Dict[str, Any]:
    url = "{}/decision-definition/{id}/evaluate".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[Any]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = response_200_item_data

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[Any]]]:
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
    json_body: EvaluateDecisionDto,
) -> Response[Union[ExceptionDto, List[Any]]]:
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
    json_body: EvaluateDecisionDto,
) -> Optional[Union[ExceptionDto, List[Any]]]:
    """Evaluates a given decision and returns the result.
    The input values of the decision have to be supplied in the request body."""

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: EvaluateDecisionDto,
) -> Response[Union[ExceptionDto, List[Any]]]:
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
    json_body: EvaluateDecisionDto,
) -> Optional[Union[ExceptionDto, List[Any]]]:
    """Evaluates a given decision and returns the result.
    The input values of the decision have to be supplied in the request body."""

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
