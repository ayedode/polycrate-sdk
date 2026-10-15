from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.endpoint import Endpoint
from ...models.patched_endpoint_request import PatchedEndpointRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedEndpointRequest | PatchedEndpointRequest | PatchedEndpointRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/endpoints/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedEndpointRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedEndpointRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedEndpointRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Endpoint | None:
    if response.status_code == 200:
        response_200 = Endpoint.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Endpoint]:
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
    body: PatchedEndpointRequest | PatchedEndpointRequest | PatchedEndpointRequest | Unset = UNSET,
) -> Response[Endpoint]:
    """API endpoint that allows endpoints to be viewed or edited.

    Supports Agent Token authentication with workspace isolation.
    Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅

    See: .specs/agent-token-extended-api-access.md

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (PatchedEndpointRequest | Unset): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (PatchedEndpointRequest | Unset): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (PatchedEndpointRequest | Unset): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Endpoint]
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
    body: PatchedEndpointRequest | PatchedEndpointRequest | PatchedEndpointRequest | Unset = UNSET,
) -> Endpoint | None:
    """API endpoint that allows endpoints to be viewed or edited.

    Supports Agent Token authentication with workspace isolation.
    Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅

    See: .specs/agent-token-extended-api-access.md

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (PatchedEndpointRequest | Unset): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (PatchedEndpointRequest | Unset): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (PatchedEndpointRequest | Unset): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Endpoint
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
    body: PatchedEndpointRequest | PatchedEndpointRequest | PatchedEndpointRequest | Unset = UNSET,
) -> Response[Endpoint]:
    """API endpoint that allows endpoints to be viewed or edited.

    Supports Agent Token authentication with workspace isolation.
    Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅

    See: .specs/agent-token-extended-api-access.md

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (PatchedEndpointRequest | Unset): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (PatchedEndpointRequest | Unset): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (PatchedEndpointRequest | Unset): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Endpoint]
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
    body: PatchedEndpointRequest | PatchedEndpointRequest | PatchedEndpointRequest | Unset = UNSET,
) -> Endpoint | None:
    """API endpoint that allows endpoints to be viewed or edited.

    Supports Agent Token authentication with workspace isolation.
    Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅

    See: .specs/agent-token-extended-api-access.md

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (PatchedEndpointRequest | Unset): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (PatchedEndpointRequest | Unset): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (PatchedEndpointRequest | Unset): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Endpoint
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
