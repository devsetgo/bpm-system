from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.authorization_exception_dto import AuthorizationExceptionDto
from ...models.evaluation_condition_dto import EvaluationConditionDto
from ...models.exception_dto import ExceptionDto
from ...models.process_instance_dto import ProcessInstanceDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: EvaluationConditionDto,
) -> Dict[str, Any]:
    url = "{}/condition".format(client.base_url)

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
) -> Optional[Union[AuthorizationExceptionDto, ExceptionDto, List[ProcessInstanceDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProcessInstanceDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = AuthorizationExceptionDto.from_dict(response.json())

        return response_403
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[AuthorizationExceptionDto, ExceptionDto, List[ProcessInstanceDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: EvaluationConditionDto,
) -> Response[Union[AuthorizationExceptionDto, ExceptionDto, List[ProcessInstanceDto]]]:
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
    json_body: EvaluationConditionDto,
) -> Optional[Union[AuthorizationExceptionDto, ExceptionDto, List[ProcessInstanceDto]]]:
    """Triggers evaluation of conditions for conditional start event(s).
    Internally this maps to the engines condition evaluation builder method ConditionEvaluationBuilder#evaluateStartConditions().
    For more information see the [Conditional Start Events](https://docs.camunda.org/manual/7.15/reference/bpmn20/events/conditional-events/#conditional-start-event)
    section of the [BPMN 2.0 Implementation Reference](https://docs.camunda.org/manual/7.15/reference/bpmn20/)."""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: EvaluationConditionDto,
) -> Response[Union[AuthorizationExceptionDto, ExceptionDto, List[ProcessInstanceDto]]]:
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
    json_body: EvaluationConditionDto,
) -> Optional[Union[AuthorizationExceptionDto, ExceptionDto, List[ProcessInstanceDto]]]:
    """Triggers evaluation of conditions for conditional start event(s).
    Internally this maps to the engines condition evaluation builder method ConditionEvaluationBuilder#evaluateStartConditions().
    For more information see the [Conditional Start Events](https://docs.camunda.org/manual/7.15/reference/bpmn20/events/conditional-events/#conditional-start-event)
    section of the [BPMN 2.0 Implementation Reference](https://docs.camunda.org/manual/7.15/reference/bpmn20/)."""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
