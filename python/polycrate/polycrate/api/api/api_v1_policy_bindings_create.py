from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.policy_binding import PolicyBinding
from ...models.policy_binding_request import PolicyBindingRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: PolicyBindingRequest | PolicyBindingRequest | PolicyBindingRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/policy-bindings/",
    }

    if isinstance(body, PolicyBindingRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PolicyBindingRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PolicyBindingRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PolicyBinding | None:
    if response.status_code == 201:
        response_201 = PolicyBinding.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PolicyBinding]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyBindingRequest | PolicyBindingRequest | PolicyBindingRequest | Unset = UNSET,
) -> Response[PolicyBinding]:
    """Create a new PolicyBinding.

    POST /api/v1/policy-bindings/
    {
        "policy_id": "uuid",
        "object_type": "k8s.K8sApp",
        "object_id": "uuid",
        "scope": "user",
        "enabled": true
    }

    Args:
        body (PolicyBindingRequest): Serializer for PolicyBinding model.

            NEW in v4.0 - Replaces active_policies JSONField access via API.
        body (PolicyBindingRequest): Serializer for PolicyBinding model.

            NEW in v4.0 - Replaces active_policies JSONField access via API.
        body (PolicyBindingRequest): Serializer for PolicyBinding model.

            NEW in v4.0 - Replaces active_policies JSONField access via API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PolicyBinding]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PolicyBindingRequest | PolicyBindingRequest | PolicyBindingRequest | Unset = UNSET,
) -> PolicyBinding | None:
    """Create a new PolicyBinding.

    POST /api/v1/policy-bindings/
    {
        "policy_id": "uuid",
        "object_type": "k8s.K8sApp",
        "object_id": "uuid",
        "scope": "user",
        "enabled": true
    }

    Args:
        body (PolicyBindingRequest): Serializer for PolicyBinding model.

            NEW in v4.0 - Replaces active_policies JSONField access via API.
        body (PolicyBindingRequest): Serializer for PolicyBinding model.

            NEW in v4.0 - Replaces active_policies JSONField access via API.
        body (PolicyBindingRequest): Serializer for PolicyBinding model.

            NEW in v4.0 - Replaces active_policies JSONField access via API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PolicyBinding
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyBindingRequest | PolicyBindingRequest | PolicyBindingRequest | Unset = UNSET,
) -> Response[PolicyBinding]:
    """Create a new PolicyBinding.

    POST /api/v1/policy-bindings/
    {
        "policy_id": "uuid",
        "object_type": "k8s.K8sApp",
        "object_id": "uuid",
        "scope": "user",
        "enabled": true
    }

    Args:
        body (PolicyBindingRequest): Serializer for PolicyBinding model.

            NEW in v4.0 - Replaces active_policies JSONField access via API.
        body (PolicyBindingRequest): Serializer for PolicyBinding model.

            NEW in v4.0 - Replaces active_policies JSONField access via API.
        body (PolicyBindingRequest): Serializer for PolicyBinding model.

            NEW in v4.0 - Replaces active_policies JSONField access via API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PolicyBinding]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PolicyBindingRequest | PolicyBindingRequest | PolicyBindingRequest | Unset = UNSET,
) -> PolicyBinding | None:
    """Create a new PolicyBinding.

    POST /api/v1/policy-bindings/
    {
        "policy_id": "uuid",
        "object_type": "k8s.K8sApp",
        "object_id": "uuid",
        "scope": "user",
        "enabled": true
    }

    Args:
        body (PolicyBindingRequest): Serializer for PolicyBinding model.

            NEW in v4.0 - Replaces active_policies JSONField access via API.
        body (PolicyBindingRequest): Serializer for PolicyBinding model.

            NEW in v4.0 - Replaces active_policies JSONField access via API.
        body (PolicyBindingRequest): Serializer for PolicyBinding model.

            NEW in v4.0 - Replaces active_policies JSONField access via API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PolicyBinding
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
