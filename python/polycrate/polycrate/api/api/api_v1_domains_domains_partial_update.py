from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_public_detail import DomainPublicDetail
from ...models.patched_domain_public_detail_request import PatchedDomainPublicDetailRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedDomainPublicDetailRequest
    | PatchedDomainPublicDetailRequest
    | PatchedDomainPublicDetailRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/domains/domains/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedDomainPublicDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedDomainPublicDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedDomainPublicDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DomainPublicDetail | None:
    if response.status_code == 200:
        response_200 = DomainPublicDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DomainPublicDetail]:
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
    body: PatchedDomainPublicDetailRequest
    | PatchedDomainPublicDetailRequest
    | PatchedDomainPublicDetailRequest
    | Unset = UNSET,
) -> Response[DomainPublicDetail]:
    """Base ViewSet for all ManagedObject API endpoints.

    Provides:
    - Archived object filtering (excludes archived objects, workspaces, organizations)
    - User permission filtering (org/workspace scoping based on user permissions)
    - Query optimizations via class attributes (select_related, prefetch_related, defer)

    Subclasses can customize behavior via class attributes:
    - select_related_fields: List of fields for select_related()
    - prefetch_related_fields: List of fields for prefetch_related()
    - defer_fields: List of fields to defer loading
    - default_ordering: List of fields for ordering (default: ['-created_at'])
    - skip_user_permission_filter: Set to True for global objects (e.g., Pops)
    - filter_by_workspace: Set to True to filter by workspace instead of organization

    Args:
        id (UUID):
        body (PatchedDomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (PatchedDomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (PatchedDomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainPublicDetail]
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
    body: PatchedDomainPublicDetailRequest
    | PatchedDomainPublicDetailRequest
    | PatchedDomainPublicDetailRequest
    | Unset = UNSET,
) -> DomainPublicDetail | None:
    """Base ViewSet for all ManagedObject API endpoints.

    Provides:
    - Archived object filtering (excludes archived objects, workspaces, organizations)
    - User permission filtering (org/workspace scoping based on user permissions)
    - Query optimizations via class attributes (select_related, prefetch_related, defer)

    Subclasses can customize behavior via class attributes:
    - select_related_fields: List of fields for select_related()
    - prefetch_related_fields: List of fields for prefetch_related()
    - defer_fields: List of fields to defer loading
    - default_ordering: List of fields for ordering (default: ['-created_at'])
    - skip_user_permission_filter: Set to True for global objects (e.g., Pops)
    - filter_by_workspace: Set to True to filter by workspace instead of organization

    Args:
        id (UUID):
        body (PatchedDomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (PatchedDomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (PatchedDomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainPublicDetail
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
    body: PatchedDomainPublicDetailRequest
    | PatchedDomainPublicDetailRequest
    | PatchedDomainPublicDetailRequest
    | Unset = UNSET,
) -> Response[DomainPublicDetail]:
    """Base ViewSet for all ManagedObject API endpoints.

    Provides:
    - Archived object filtering (excludes archived objects, workspaces, organizations)
    - User permission filtering (org/workspace scoping based on user permissions)
    - Query optimizations via class attributes (select_related, prefetch_related, defer)

    Subclasses can customize behavior via class attributes:
    - select_related_fields: List of fields for select_related()
    - prefetch_related_fields: List of fields for prefetch_related()
    - defer_fields: List of fields to defer loading
    - default_ordering: List of fields for ordering (default: ['-created_at'])
    - skip_user_permission_filter: Set to True for global objects (e.g., Pops)
    - filter_by_workspace: Set to True to filter by workspace instead of organization

    Args:
        id (UUID):
        body (PatchedDomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (PatchedDomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (PatchedDomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainPublicDetail]
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
    body: PatchedDomainPublicDetailRequest
    | PatchedDomainPublicDetailRequest
    | PatchedDomainPublicDetailRequest
    | Unset = UNSET,
) -> DomainPublicDetail | None:
    """Base ViewSet for all ManagedObject API endpoints.

    Provides:
    - Archived object filtering (excludes archived objects, workspaces, organizations)
    - User permission filtering (org/workspace scoping based on user permissions)
    - Query optimizations via class attributes (select_related, prefetch_related, defer)

    Subclasses can customize behavior via class attributes:
    - select_related_fields: List of fields for select_related()
    - prefetch_related_fields: List of fields for prefetch_related()
    - defer_fields: List of fields to defer loading
    - default_ordering: List of fields for ordering (default: ['-created_at'])
    - skip_user_permission_filter: Set to True for global objects (e.g., Pops)
    - filter_by_workspace: Set to True to filter by workspace instead of organization

    Args:
        id (UUID):
        body (PatchedDomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (PatchedDomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (PatchedDomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainPublicDetail
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
