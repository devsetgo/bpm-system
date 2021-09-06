from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_dto import ExceptionDto
from ...models.password_policy_dto import PasswordPolicyDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/identity/password-policy".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionDto, PasswordPolicyDto]]:
    if response.status_code == 200:
        response_200 = PasswordPolicyDto.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ExceptionDto.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionDto, PasswordPolicyDto]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[ExceptionDto, PasswordPolicyDto]]:
    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[ExceptionDto, PasswordPolicyDto]]:
    """A password policy consists of a list of rules that new passwords must follow to be
    policy compliant. This end point returns a JSON representation of the
    list of policy rules. More information on password policies in Camunda can be found in the password policy
    [user guide](https://docs.camunda.org/manual/7.15/user-guide/process-engine/password-policy/) and in
    the [security instructions](https://docs.camunda.org/manual/7.15/user-guide/security/)."""

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[ExceptionDto, PasswordPolicyDto]]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[ExceptionDto, PasswordPolicyDto]]:
    """A password policy consists of a list of rules that new passwords must follow to be
    policy compliant. This end point returns a JSON representation of the
    list of policy rules. More information on password policies in Camunda can be found in the password policy
    [user guide](https://docs.camunda.org/manual/7.15/user-guide/process-engine/password-policy/) and in
    the [security instructions](https://docs.camunda.org/manual/7.15/user-guide/security/)."""

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
