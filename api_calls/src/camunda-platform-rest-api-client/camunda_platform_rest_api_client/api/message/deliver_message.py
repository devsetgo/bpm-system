from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.correlation_message_dto import CorrelationMessageDto
from ...models.exception_dto import ExceptionDto
from ...models.message_correlation_result_with_variable_dto import MessageCorrelationResultWithVariableDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CorrelationMessageDto,
) -> Dict[str, Any]:
    url = "{}/message".format(client.base_url)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, ExceptionDto, List[MessageCorrelationResultWithVariableDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MessageCorrelationResultWithVariableDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 204:
        response_204 = None

        return response_204
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, ExceptionDto, List[MessageCorrelationResultWithVariableDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CorrelationMessageDto,
) -> Response[Union[Any, ExceptionDto, List[MessageCorrelationResultWithVariableDto]]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: CorrelationMessageDto,
) -> Optional[Union[Any, ExceptionDto, List[MessageCorrelationResultWithVariableDto]]]:
    """Correlates a message to the process engine to either trigger a message start event or an intermediate message
    catching event. Internally this maps to the engine's message correlation builder methods
    `MessageCorrelationBuilder#correlateWithResult()` and `MessageCorrelationBuilder#correlateAllWithResult()`.
    For more information about the correlation behavior, see the [Message Events](https://docs.camunda.org/manual/7.15/bpmn20/events/message-events/)
    section of the [BPMN 2.0 Implementation Reference](https://docs.camunda.org/manual/7.15/reference/bpmn20/)."""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CorrelationMessageDto,
) -> Response[Union[Any, ExceptionDto, List[MessageCorrelationResultWithVariableDto]]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CorrelationMessageDto,
) -> Optional[Union[Any, ExceptionDto, List[MessageCorrelationResultWithVariableDto]]]:
    """Correlates a message to the process engine to either trigger a message start event or an intermediate message
    catching event. Internally this maps to the engine's message correlation builder methods
    `MessageCorrelationBuilder#correlateWithResult()` and `MessageCorrelationBuilder#correlateAllWithResult()`.
    For more information about the correlation behavior, see the [Message Events](https://docs.camunda.org/manual/7.15/bpmn20/events/message-events/)
    section of the [BPMN 2.0 Implementation Reference](https://docs.camunda.org/manual/7.15/reference/bpmn20/)."""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
