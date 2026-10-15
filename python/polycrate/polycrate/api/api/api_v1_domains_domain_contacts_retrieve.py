from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_contact_detail import DomainContactDetail
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/domains/domain-contacts/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DomainContactDetail | None:
    if response.status_code == 200:
        response_200 = DomainContactDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DomainContactDetail]:
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
) -> Response[DomainContactDetail]:
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainContactDetail]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> DomainContactDetail | None:
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainContactDetail
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[DomainContactDetail]:
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainContactDetail]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> DomainContactDetail | None:
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainContactDetail
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
