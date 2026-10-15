from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.endpoint import Endpoint
from ...models.endpoint_request import EndpointRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: EndpointRequest | EndpointRequest | EndpointRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/endpoints/{id}/discover/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, EndpointRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, EndpointRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, EndpointRequest):
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
    body: EndpointRequest | EndpointRequest | EndpointRequest | Unset = UNSET,
) -> Response[Endpoint]:
    """DEPRECATED: Discovery has been removed in 0.11.11.

    Per .specs/0.11.11/discovery-removal-performance-fix.md:
    - discover_class() and discover_object() tasks removed
    - Discovery logic should be in run_reconciliation() if needed
    - Use reconcile endpoint instead

    Args:
        id (UUID):
        body (EndpointRequest): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (EndpointRequest): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (EndpointRequest): Endpoint detail — same pattern as K8sAppSerializer:
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
    body: EndpointRequest | EndpointRequest | EndpointRequest | Unset = UNSET,
) -> Endpoint | None:
    """DEPRECATED: Discovery has been removed in 0.11.11.

    Per .specs/0.11.11/discovery-removal-performance-fix.md:
    - discover_class() and discover_object() tasks removed
    - Discovery logic should be in run_reconciliation() if needed
    - Use reconcile endpoint instead

    Args:
        id (UUID):
        body (EndpointRequest): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (EndpointRequest): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (EndpointRequest): Endpoint detail — same pattern as K8sAppSerializer:
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
    body: EndpointRequest | EndpointRequest | EndpointRequest | Unset = UNSET,
) -> Response[Endpoint]:
    """DEPRECATED: Discovery has been removed in 0.11.11.

    Per .specs/0.11.11/discovery-removal-performance-fix.md:
    - discover_class() and discover_object() tasks removed
    - Discovery logic should be in run_reconciliation() if needed
    - Use reconcile endpoint instead

    Args:
        id (UUID):
        body (EndpointRequest): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (EndpointRequest): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (EndpointRequest): Endpoint detail — same pattern as K8sAppSerializer:
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
    body: EndpointRequest | EndpointRequest | EndpointRequest | Unset = UNSET,
) -> Endpoint | None:
    """DEPRECATED: Discovery has been removed in 0.11.11.

    Per .specs/0.11.11/discovery-removal-performance-fix.md:
    - discover_class() and discover_object() tasks removed
    - Discovery logic should be in run_reconciliation() if needed
    - Use reconcile endpoint instead

    Args:
        id (UUID):
        body (EndpointRequest): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (EndpointRequest): Endpoint detail — same pattern as K8sAppSerializer:
            ManagedObjectDetailSerializer + exported_fields.

            organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not
            generic dict).
            Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
            spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which
            means
            the generated Go API client has a fully typed Spec struct (no interface{} reimplementation
            needed).
        body (EndpointRequest): Endpoint detail — same pattern as K8sAppSerializer:
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
