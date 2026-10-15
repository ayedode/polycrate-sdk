from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pop import Pop
from ...models.pop_request import PopRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: PopRequest | PopRequest | PopRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/pops/{id}/reconcile/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PopRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PopRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PopRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Pop | None:
    if response.status_code == 200:
        response_200 = Pop.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Pop]:
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
    body: PopRequest | PopRequest | PopRequest | Unset = UNSET,
) -> Response[Pop]:
    """Reconcile the object

    Args:
        id (UUID):
        body (PopRequest): Full serializer for Pop detail views.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            Pop is admin-only and not scoped to org/workspace.

            Spec 526 / 553:
            - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
            - reachability_endpoint: nested RO (managed ICMP endpoint)
        body (PopRequest): Full serializer for Pop detail views.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            Pop is admin-only and not scoped to org/workspace.

            Spec 526 / 553:
            - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
            - reachability_endpoint: nested RO (managed ICMP endpoint)
        body (PopRequest): Full serializer for Pop detail views.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            Pop is admin-only and not scoped to org/workspace.

            Spec 526 / 553:
            - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
            - reachability_endpoint: nested RO (managed ICMP endpoint)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Pop]
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
    body: PopRequest | PopRequest | PopRequest | Unset = UNSET,
) -> Pop | None:
    """Reconcile the object

    Args:
        id (UUID):
        body (PopRequest): Full serializer for Pop detail views.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            Pop is admin-only and not scoped to org/workspace.

            Spec 526 / 553:
            - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
            - reachability_endpoint: nested RO (managed ICMP endpoint)
        body (PopRequest): Full serializer for Pop detail views.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            Pop is admin-only and not scoped to org/workspace.

            Spec 526 / 553:
            - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
            - reachability_endpoint: nested RO (managed ICMP endpoint)
        body (PopRequest): Full serializer for Pop detail views.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            Pop is admin-only and not scoped to org/workspace.

            Spec 526 / 553:
            - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
            - reachability_endpoint: nested RO (managed ICMP endpoint)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Pop
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
    body: PopRequest | PopRequest | PopRequest | Unset = UNSET,
) -> Response[Pop]:
    """Reconcile the object

    Args:
        id (UUID):
        body (PopRequest): Full serializer for Pop detail views.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            Pop is admin-only and not scoped to org/workspace.

            Spec 526 / 553:
            - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
            - reachability_endpoint: nested RO (managed ICMP endpoint)
        body (PopRequest): Full serializer for Pop detail views.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            Pop is admin-only and not scoped to org/workspace.

            Spec 526 / 553:
            - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
            - reachability_endpoint: nested RO (managed ICMP endpoint)
        body (PopRequest): Full serializer for Pop detail views.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            Pop is admin-only and not scoped to org/workspace.

            Spec 526 / 553:
            - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
            - reachability_endpoint: nested RO (managed ICMP endpoint)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Pop]
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
    body: PopRequest | PopRequest | PopRequest | Unset = UNSET,
) -> Pop | None:
    """Reconcile the object

    Args:
        id (UUID):
        body (PopRequest): Full serializer for Pop detail views.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            Pop is admin-only and not scoped to org/workspace.

            Spec 526 / 553:
            - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
            - reachability_endpoint: nested RO (managed ICMP endpoint)
        body (PopRequest): Full serializer for Pop detail views.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            Pop is admin-only and not scoped to org/workspace.

            Spec 526 / 553:
            - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
            - reachability_endpoint: nested RO (managed ICMP endpoint)
        body (PopRequest): Full serializer for Pop detail views.
            Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
            Pop is admin-only and not scoped to org/workspace.

            Spec 526 / 553:
            - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
            - reachability_endpoint: nested RO (managed ICMP endpoint)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Pop
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
