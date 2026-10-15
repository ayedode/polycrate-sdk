from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.policy import Policy
from ...models.policy_request import PolicyRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PolicyRequest | PolicyRequest | PolicyRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/policies/",
    }

    if isinstance(body, PolicyRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PolicyRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PolicyRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Policy | None:
    if response.status_code == 201:
        response_201 = Policy.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Policy]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyRequest | PolicyRequest | PolicyRequest | Unset = UNSET,
) -> Response[Policy]:
    """API ViewSet for Policy management.

    UNCHANGED from v3.0 - Dry-run endpoint still works the same.

    Args:
        body (PolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Policy]
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
    body: PolicyRequest | PolicyRequest | PolicyRequest | Unset = UNSET,
) -> Policy | None:
    """API ViewSet for Policy management.

    UNCHANGED from v3.0 - Dry-run endpoint still works the same.

    Args:
        body (PolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Policy
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PolicyRequest | PolicyRequest | PolicyRequest | Unset = UNSET,
) -> Response[Policy]:
    """API ViewSet for Policy management.

    UNCHANGED from v3.0 - Dry-run endpoint still works the same.

    Args:
        body (PolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Policy]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PolicyRequest | PolicyRequest | PolicyRequest | Unset = UNSET,
) -> Policy | None:
    """API ViewSet for Policy management.

    UNCHANGED from v3.0 - Dry-run endpoint still works the same.

    Args:
        body (PolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Policy
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
