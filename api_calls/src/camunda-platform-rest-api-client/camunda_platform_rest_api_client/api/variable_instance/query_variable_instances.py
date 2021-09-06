from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.variable_instance_dto import VariableInstanceDto
from ...models.variable_instance_query_dto import VariableInstanceQueryDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: VariableInstanceQueryDto,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    deserialize_values: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/variable-instance".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "firstResult": first_result,
        "maxResults": max_results,
        "deserializeValues": deserialize_values,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, List[VariableInstanceDto]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VariableInstanceDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ExceptionDto.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, List[VariableInstanceDto]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: VariableInstanceQueryDto,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    deserialize_values: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[VariableInstanceDto]]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        first_result=first_result,
        max_results=max_results,
        deserialize_values=deserialize_values,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: VariableInstanceQueryDto,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    deserialize_values: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[VariableInstanceDto]]]:
    """Query for variable instances that fulfill given parameters through a JSON object.
    This method is slightly more powerful than the
    [Get Variable Instances](https://docs.camunda.org/manual/7.15/reference/rest/variable-
    instance/get-query/) method because it allows filtering by multiple
    variable instances of types `String`, `Number` or `Boolean`."""

    return sync_detailed(
        client=client,
        json_body=json_body,
        first_result=first_result,
        max_results=max_results,
        deserialize_values=deserialize_values,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: VariableInstanceQueryDto,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    deserialize_values: Union[Unset, None, bool] = UNSET,
) -> Response[Union[ExceptionDto, List[VariableInstanceDto]]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        first_result=first_result,
        max_results=max_results,
        deserialize_values=deserialize_values,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: VariableInstanceQueryDto,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = UNSET,
    deserialize_values: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[ExceptionDto, List[VariableInstanceDto]]]:
    """Query for variable instances that fulfill given parameters through a JSON object.
    This method is slightly more powerful than the
    [Get Variable Instances](https://docs.camunda.org/manual/7.15/reference/rest/variable-
    instance/get-query/) method because it allows filtering by multiple
    variable instances of types `String`, `Number` or `Boolean`."""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            first_result=first_result,
            max_results=max_results,
            deserialize_values=deserialize_values,
        )
    ).parsed
