import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_domains_domain_contacts_list_created_by_component import (
    ApiV1DomainsDomainContactsListCreatedByComponent,
)
from ...models.api_v1_domains_domain_contacts_list_kind import (
    ApiV1DomainsDomainContactsListKind,
)
from ...models.api_v1_domains_domain_contacts_list_scope import (
    ApiV1DomainsDomainContactsListScope,
)
from ...models.api_v1_domains_domain_contacts_list_state import (
    ApiV1DomainsDomainContactsListState,
)
from ...models.api_v1_domains_domain_contacts_list_state_not import (
    ApiV1DomainsDomainContactsListStateNot,
)
from ...models.api_v1_domains_domain_contacts_list_time_range import (
    ApiV1DomainsDomainContactsListTimeRange,
)
from ...models.paginated_domain_contact_list_list import PaginatedDomainContactListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1DomainsDomainContactsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    email: str | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: ApiV1DomainsDomainContactsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1DomainsDomainContactsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1DomainsDomainContactsListState | Unset = UNSET,
    state_not: ApiV1DomainsDomainContactsListStateNot | Unset = UNSET,
    time_range: ApiV1DomainsDomainContactsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["archived"] = archived

    json_created_at: str | Unset = UNSET
    if not isinstance(created_at, Unset):
        json_created_at = created_at.isoformat()
    params["created_at"] = json_created_at

    json_created_by_component: str | Unset = UNSET
    if not isinstance(created_by_component, Unset):
        json_created_by_component = created_by_component

    params["created_by_component"] = json_created_by_component

    json_created_by_users: list[list[int]] | Unset = UNSET
    if not isinstance(created_by_users, Unset):
        json_created_by_users = []
        for created_by_users_item_data in created_by_users:
            created_by_users_item = created_by_users_item_data

            json_created_by_users.append(created_by_users_item)

    params["created_by_users"] = json_created_by_users

    params["debug_mode"] = debug_mode

    params["email"] = email

    params["has_conditions"] = has_conditions

    json_kind: str | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind

    params["kind"] = json_kind

    params["name"] = name

    params["name_exact"] = name_exact

    params["ordering"] = ordering

    json_organization: str | Unset = UNSET
    if not isinstance(organization, Unset):
        json_organization = str(organization)
    params["organization"] = json_organization

    json_organizations: list[list[str]] | Unset = UNSET
    if not isinstance(organizations, Unset):
        json_organizations = []
        for organizations_item_data in organizations:
            organizations_item = []
            for organizations_item_item_data in organizations_item_data:
                organizations_item_item = str(organizations_item_item_data)
                organizations_item.append(organizations_item_item)

            json_organizations.append(organizations_item)

    params["organizations"] = json_organizations

    params["page"] = page

    params["page_size"] = page_size

    params["platform_service"] = platform_service

    params["reconciliation_running"] = reconciliation_running

    json_scope: str | Unset = UNSET
    if not isinstance(scope, Unset):
        json_scope = scope

    params["scope"] = json_scope

    params["search"] = search

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    json_state_not: str | Unset = UNSET
    if not isinstance(state_not, Unset):
        json_state_not = state_not

    params["state_not"] = json_state_not

    json_time_range: str | Unset = UNSET
    if not isinstance(time_range, Unset):
        json_time_range = time_range

    params["time_range"] = json_time_range

    json_updated_at: str | Unset = UNSET
    if not isinstance(updated_at, Unset):
        json_updated_at = updated_at.isoformat()
    params["updated_at"] = json_updated_at

    json_workspaces: list[list[str]] | Unset = UNSET
    if not isinstance(workspaces, Unset):
        json_workspaces = []
        for workspaces_item_data in workspaces:
            workspaces_item = []
            for workspaces_item_item_data in workspaces_item_data:
                workspaces_item_item = str(workspaces_item_item_data)
                workspaces_item.append(workspaces_item_item)

            json_workspaces.append(workspaces_item)

    params["workspaces"] = json_workspaces

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/domains/domain-contacts/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedDomainContactListList | None:
    if response.status_code == 200:
        response_200 = PaginatedDomainContactListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedDomainContactListList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1DomainsDomainContactsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    email: str | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: ApiV1DomainsDomainContactsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1DomainsDomainContactsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1DomainsDomainContactsListState | Unset = UNSET,
    state_not: ApiV1DomainsDomainContactsListStateNot | Unset = UNSET,
    time_range: ApiV1DomainsDomainContactsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedDomainContactListList]:
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
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1DomainsDomainContactsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        email (str | Unset):
        has_conditions (bool | Unset):
        kind (ApiV1DomainsDomainContactsListKind | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1DomainsDomainContactsListScope | Unset):
        search (str | Unset):
        state (ApiV1DomainsDomainContactsListState | Unset):
        state_not (ApiV1DomainsDomainContactsListStateNot | Unset):
        time_range (ApiV1DomainsDomainContactsListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDomainContactListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        email=email,
        has_conditions=has_conditions,
        kind=kind,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
        organization=organization,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        reconciliation_running=reconciliation_running,
        scope=scope,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        updated_at=updated_at,
        workspaces=workspaces,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1DomainsDomainContactsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    email: str | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: ApiV1DomainsDomainContactsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1DomainsDomainContactsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1DomainsDomainContactsListState | Unset = UNSET,
    state_not: ApiV1DomainsDomainContactsListStateNot | Unset = UNSET,
    time_range: ApiV1DomainsDomainContactsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedDomainContactListList | None:
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
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1DomainsDomainContactsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        email (str | Unset):
        has_conditions (bool | Unset):
        kind (ApiV1DomainsDomainContactsListKind | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1DomainsDomainContactsListScope | Unset):
        search (str | Unset):
        state (ApiV1DomainsDomainContactsListState | Unset):
        state_not (ApiV1DomainsDomainContactsListStateNot | Unset):
        time_range (ApiV1DomainsDomainContactsListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDomainContactListList
    """

    return sync_detailed(
        client=client,
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        email=email,
        has_conditions=has_conditions,
        kind=kind,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
        organization=organization,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        reconciliation_running=reconciliation_running,
        scope=scope,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        updated_at=updated_at,
        workspaces=workspaces,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1DomainsDomainContactsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    email: str | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: ApiV1DomainsDomainContactsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1DomainsDomainContactsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1DomainsDomainContactsListState | Unset = UNSET,
    state_not: ApiV1DomainsDomainContactsListStateNot | Unset = UNSET,
    time_range: ApiV1DomainsDomainContactsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedDomainContactListList]:
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
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1DomainsDomainContactsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        email (str | Unset):
        has_conditions (bool | Unset):
        kind (ApiV1DomainsDomainContactsListKind | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1DomainsDomainContactsListScope | Unset):
        search (str | Unset):
        state (ApiV1DomainsDomainContactsListState | Unset):
        state_not (ApiV1DomainsDomainContactsListStateNot | Unset):
        time_range (ApiV1DomainsDomainContactsListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDomainContactListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        email=email,
        has_conditions=has_conditions,
        kind=kind,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
        organization=organization,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        reconciliation_running=reconciliation_running,
        scope=scope,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        updated_at=updated_at,
        workspaces=workspaces,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1DomainsDomainContactsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    email: str | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: ApiV1DomainsDomainContactsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1DomainsDomainContactsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1DomainsDomainContactsListState | Unset = UNSET,
    state_not: ApiV1DomainsDomainContactsListStateNot | Unset = UNSET,
    time_range: ApiV1DomainsDomainContactsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedDomainContactListList | None:
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
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1DomainsDomainContactsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        email (str | Unset):
        has_conditions (bool | Unset):
        kind (ApiV1DomainsDomainContactsListKind | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1DomainsDomainContactsListScope | Unset):
        search (str | Unset):
        state (ApiV1DomainsDomainContactsListState | Unset):
        state_not (ApiV1DomainsDomainContactsListStateNot | Unset):
        time_range (ApiV1DomainsDomainContactsListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDomainContactListList
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            created_at=created_at,
            created_by_component=created_by_component,
            created_by_users=created_by_users,
            debug_mode=debug_mode,
            email=email,
            has_conditions=has_conditions,
            kind=kind,
            name=name,
            name_exact=name_exact,
            ordering=ordering,
            organization=organization,
            organizations=organizations,
            page=page,
            page_size=page_size,
            platform_service=platform_service,
            reconciliation_running=reconciliation_running,
            scope=scope,
            search=search,
            state=state,
            state_not=state_not,
            time_range=time_range,
            updated_at=updated_at,
            workspaces=workspaces,
        )
    ).parsed
