from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_policy_request import PatchedPolicyRequest
from ...models.policy import Policy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedPolicyRequest | PatchedPolicyRequest | PatchedPolicyRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/policies/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedPolicyRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedPolicyRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedPolicyRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Policy | None:
    if response.status_code == 200:
        response_200 = Policy.from_dict(response.json())

        return response_200

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
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedPolicyRequest | PatchedPolicyRequest | PatchedPolicyRequest | Unset = UNSET,
) -> Response[Policy]:
    """API ViewSet for Policy management.

    UNCHANGED from v3.0 - Dry-run endpoint still works the same.

    Args:
        id (UUID):
        body (PatchedPolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PatchedPolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PatchedPolicyRequest | Unset): Serializer for Policy model.
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
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedPolicyRequest | PatchedPolicyRequest | PatchedPolicyRequest | Unset = UNSET,
) -> Policy | None:
    """API ViewSet for Policy management.

    UNCHANGED from v3.0 - Dry-run endpoint still works the same.

    Args:
        id (UUID):
        body (PatchedPolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PatchedPolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PatchedPolicyRequest | Unset): Serializer for Policy model.
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
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedPolicyRequest | PatchedPolicyRequest | PatchedPolicyRequest | Unset = UNSET,
) -> Response[Policy]:
    """API ViewSet for Policy management.

    UNCHANGED from v3.0 - Dry-run endpoint still works the same.

    Args:
        id (UUID):
        body (PatchedPolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PatchedPolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PatchedPolicyRequest | Unset): Serializer for Policy model.
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
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedPolicyRequest | PatchedPolicyRequest | PatchedPolicyRequest | Unset = UNSET,
) -> Policy | None:
    """API ViewSet for Policy management.

    UNCHANGED from v3.0 - Dry-run endpoint still works the same.

    Args:
        id (UUID):
        body (PatchedPolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PatchedPolicyRequest | Unset): Serializer for Policy model.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            organization/workspace werden automatisch von ManagedObjectDetailSerializer
            bereitgestellt.
        body (PatchedPolicyRequest | Unset): Serializer for Policy model.
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
            id=id,
            client=client,
            body=body,
        )
    ).parsed
