from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pop import Pop
from ...models.pop_request import PopRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: PopRequest | PopRequest | PopRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/pops/",
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
    if response.status_code == 201:
        response_201 = Pop.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: PopRequest | PopRequest | PopRequest | Unset = UNSET,
) -> Response[Pop]:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
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
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PopRequest | PopRequest | PopRequest | Unset = UNSET,
) -> Pop | None:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
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
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PopRequest | PopRequest | PopRequest | Unset = UNSET,
) -> Response[Pop]:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
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
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PopRequest | PopRequest | PopRequest | Unset = UNSET,
) -> Pop | None:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
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
            client=client,
            body=body,
        )
    ).parsed
