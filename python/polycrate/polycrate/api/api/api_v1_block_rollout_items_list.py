from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_block_rollout_items_list_kind_item import (
    ApiV1BlockRolloutItemsListKindItem,
)
from ...models.api_v1_block_rollout_items_list_source import (
    ApiV1BlockRolloutItemsListSource,
)
from ...models.api_v1_block_rollout_items_list_state import (
    ApiV1BlockRolloutItemsListState,
)
from ...models.api_v1_block_rollout_items_list_state_not import (
    ApiV1BlockRolloutItemsListStateNot,
)
from ...models.api_v1_block_rollout_items_list_status import (
    ApiV1BlockRolloutItemsListStatus,
)
from ...models.api_v1_block_rollout_items_list_time_range import (
    ApiV1BlockRolloutItemsListTimeRange,
)
from ...models.paginated_block_rollout_item_list_list import PaginatedBlockRolloutItemListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: bool | Unset = UNSET,
    block: UUID | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1BlockRolloutItemsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[UUID] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    rollout: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    source: ApiV1BlockRolloutItemsListSource | Unset = UNSET,
    state: ApiV1BlockRolloutItemsListState | Unset = UNSET,
    state_not: ApiV1BlockRolloutItemsListStateNot | Unset = UNSET,
    status: ApiV1BlockRolloutItemsListStatus | Unset = UNSET,
    time_range: ApiV1BlockRolloutItemsListTimeRange | Unset = UNSET,
    workspaces: list[UUID] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["archived"] = archived

    json_block: str | Unset = UNSET
    if not isinstance(block, Unset):
        json_block = str(block)
    params["block"] = json_block

    json_created_by_users: list[list[int]] | Unset = UNSET
    if not isinstance(created_by_users, Unset):
        json_created_by_users = []
        for created_by_users_item_data in created_by_users:
            created_by_users_item = created_by_users_item_data

            json_created_by_users.append(created_by_users_item)

    params["created_by_users"] = json_created_by_users

    params["has_conditions"] = has_conditions

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item: str = kind_item_data
            json_kind.append(kind_item)

    params["kind"] = json_kind

    params["name_exact"] = name_exact

    params["ordering"] = ordering

    json_organizations: list[str] | Unset = UNSET
    if not isinstance(organizations, Unset):
        json_organizations = []
        for organizations_item_data in organizations:
            organizations_item = str(organizations_item_data)
            json_organizations.append(organizations_item)

    params["organizations"] = json_organizations

    params["page"] = page

    params["page_size"] = page_size

    params["platform_service"] = platform_service

    json_rollout: str | Unset = UNSET
    if not isinstance(rollout, Unset):
        json_rollout = str(rollout)
    params["rollout"] = json_rollout

    params["search"] = search

    json_source: str | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source

    params["source"] = json_source

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    json_state_not: str | Unset = UNSET
    if not isinstance(state_not, Unset):
        json_state_not = state_not

    params["state_not"] = json_state_not

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_time_range: str | Unset = UNSET
    if not isinstance(time_range, Unset):
        json_time_range = time_range

    params["time_range"] = json_time_range

    json_workspaces: list[str] | Unset = UNSET
    if not isinstance(workspaces, Unset):
        json_workspaces = []
        for workspaces_item_data in workspaces:
            workspaces_item = str(workspaces_item_data)
            json_workspaces.append(workspaces_item)

    params["workspaces"] = json_workspaces

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/block-rollout-items/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedBlockRolloutItemListList | None:
    if response.status_code == 200:
        response_200 = PaginatedBlockRolloutItemListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedBlockRolloutItemListList]:
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
    block: UUID | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1BlockRolloutItemsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[UUID] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    rollout: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    source: ApiV1BlockRolloutItemsListSource | Unset = UNSET,
    state: ApiV1BlockRolloutItemsListState | Unset = UNSET,
    state_not: ApiV1BlockRolloutItemsListStateNot | Unset = UNSET,
    status: ApiV1BlockRolloutItemsListStatus | Unset = UNSET,
    time_range: ApiV1BlockRolloutItemsListTimeRange | Unset = UNSET,
    workspaces: list[UUID] | Unset = UNSET,
) -> Response[PaginatedBlockRolloutItemListList]:
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
        block (UUID | Unset):
        created_by_users (list[list[int]] | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1BlockRolloutItemsListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[UUID] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        rollout (UUID | Unset):
        search (str | Unset):
        source (ApiV1BlockRolloutItemsListSource | Unset):
        state (ApiV1BlockRolloutItemsListState | Unset):
        state_not (ApiV1BlockRolloutItemsListStateNot | Unset):
        status (ApiV1BlockRolloutItemsListStatus | Unset):
        time_range (ApiV1BlockRolloutItemsListTimeRange | Unset):
        workspaces (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedBlockRolloutItemListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        block=block,
        created_by_users=created_by_users,
        has_conditions=has_conditions,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        rollout=rollout,
        search=search,
        source=source,
        state=state,
        state_not=state_not,
        status=status,
        time_range=time_range,
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
    block: UUID | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1BlockRolloutItemsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[UUID] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    rollout: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    source: ApiV1BlockRolloutItemsListSource | Unset = UNSET,
    state: ApiV1BlockRolloutItemsListState | Unset = UNSET,
    state_not: ApiV1BlockRolloutItemsListStateNot | Unset = UNSET,
    status: ApiV1BlockRolloutItemsListStatus | Unset = UNSET,
    time_range: ApiV1BlockRolloutItemsListTimeRange | Unset = UNSET,
    workspaces: list[UUID] | Unset = UNSET,
) -> PaginatedBlockRolloutItemListList | None:
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
        block (UUID | Unset):
        created_by_users (list[list[int]] | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1BlockRolloutItemsListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[UUID] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        rollout (UUID | Unset):
        search (str | Unset):
        source (ApiV1BlockRolloutItemsListSource | Unset):
        state (ApiV1BlockRolloutItemsListState | Unset):
        state_not (ApiV1BlockRolloutItemsListStateNot | Unset):
        status (ApiV1BlockRolloutItemsListStatus | Unset):
        time_range (ApiV1BlockRolloutItemsListTimeRange | Unset):
        workspaces (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedBlockRolloutItemListList
    """

    return sync_detailed(
        client=client,
        archived=archived,
        block=block,
        created_by_users=created_by_users,
        has_conditions=has_conditions,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        rollout=rollout,
        search=search,
        source=source,
        state=state,
        state_not=state_not,
        status=status,
        time_range=time_range,
        workspaces=workspaces,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    block: UUID | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1BlockRolloutItemsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[UUID] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    rollout: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    source: ApiV1BlockRolloutItemsListSource | Unset = UNSET,
    state: ApiV1BlockRolloutItemsListState | Unset = UNSET,
    state_not: ApiV1BlockRolloutItemsListStateNot | Unset = UNSET,
    status: ApiV1BlockRolloutItemsListStatus | Unset = UNSET,
    time_range: ApiV1BlockRolloutItemsListTimeRange | Unset = UNSET,
    workspaces: list[UUID] | Unset = UNSET,
) -> Response[PaginatedBlockRolloutItemListList]:
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
        block (UUID | Unset):
        created_by_users (list[list[int]] | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1BlockRolloutItemsListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[UUID] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        rollout (UUID | Unset):
        search (str | Unset):
        source (ApiV1BlockRolloutItemsListSource | Unset):
        state (ApiV1BlockRolloutItemsListState | Unset):
        state_not (ApiV1BlockRolloutItemsListStateNot | Unset):
        status (ApiV1BlockRolloutItemsListStatus | Unset):
        time_range (ApiV1BlockRolloutItemsListTimeRange | Unset):
        workspaces (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedBlockRolloutItemListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        block=block,
        created_by_users=created_by_users,
        has_conditions=has_conditions,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        rollout=rollout,
        search=search,
        source=source,
        state=state,
        state_not=state_not,
        status=status,
        time_range=time_range,
        workspaces=workspaces,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    block: UUID | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1BlockRolloutItemsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[UUID] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    rollout: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    source: ApiV1BlockRolloutItemsListSource | Unset = UNSET,
    state: ApiV1BlockRolloutItemsListState | Unset = UNSET,
    state_not: ApiV1BlockRolloutItemsListStateNot | Unset = UNSET,
    status: ApiV1BlockRolloutItemsListStatus | Unset = UNSET,
    time_range: ApiV1BlockRolloutItemsListTimeRange | Unset = UNSET,
    workspaces: list[UUID] | Unset = UNSET,
) -> PaginatedBlockRolloutItemListList | None:
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
        block (UUID | Unset):
        created_by_users (list[list[int]] | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1BlockRolloutItemsListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[UUID] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        rollout (UUID | Unset):
        search (str | Unset):
        source (ApiV1BlockRolloutItemsListSource | Unset):
        state (ApiV1BlockRolloutItemsListState | Unset):
        state_not (ApiV1BlockRolloutItemsListStateNot | Unset):
        status (ApiV1BlockRolloutItemsListStatus | Unset):
        time_range (ApiV1BlockRolloutItemsListTimeRange | Unset):
        workspaces (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedBlockRolloutItemListList
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            block=block,
            created_by_users=created_by_users,
            has_conditions=has_conditions,
            kind=kind,
            name_exact=name_exact,
            ordering=ordering,
            organizations=organizations,
            page=page,
            page_size=page_size,
            platform_service=platform_service,
            rollout=rollout,
            search=search,
            source=source,
            state=state,
            state_not=state_not,
            status=status,
            time_range=time_range,
            workspaces=workspaces,
        )
    ).parsed
