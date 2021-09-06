from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.check_password_policy_result_dto import CheckPasswordPolicyResultDto
from ...models.exception_dto import ExceptionDto
from ...models.password_policy_request_dto import PasswordPolicyRequestDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PasswordPolicyRequestDto,
) -> Dict[str, Any]:
    url = "{}/identity/password-policy".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[CheckPasswordPolicyResultDto, ExceptionDto]]:
    if response.status_code == 200:
        response_200 = CheckPasswordPolicyResultDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CheckPasswordPolicyResultDto, ExceptionDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PasswordPolicyRequestDto,
) -> Response[Union[CheckPasswordPolicyResultDto, ExceptionDto]]:
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
    json_body: PasswordPolicyRequestDto,
) -> Optional[Union[CheckPasswordPolicyResultDto, ExceptionDto]]:
    """A password policy consists of a list of rules that new passwords must follow to be
    policy compliant. A password can be checked for compliancy via this
    end point. More information on password policies in Camunda can be found in the password policy
    [user guide](https://docs.camunda.org/manual/7.15/user-guide/process-engine/password-policy/) and in
    the [security instructions](https://docs.camunda.org/manual/7.15/user-guide/security/)."""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PasswordPolicyRequestDto,
) -> Response[Union[CheckPasswordPolicyResultDto, ExceptionDto]]:
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
    json_body: PasswordPolicyRequestDto,
) -> Optional[Union[CheckPasswordPolicyResultDto, ExceptionDto]]:
    """A password policy consists of a list of rules that new passwords must follow to be
    policy compliant. A password can be checked for compliancy via this
    end point. More information on password policies in Camunda can be found in the password policy
    [user guide](https://docs.camunda.org/manual/7.15/user-guide/process-engine/password-policy/) and in
    the [security instructions](https://docs.camunda.org/manual/7.15/user-guide/security/)."""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
