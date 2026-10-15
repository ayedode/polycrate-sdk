import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_loadbalancers_regions_list_created_by_component import (
    ApiV1LoadbalancersRegionsListCreatedByComponent,
)
from ...models.api_v1_loadbalancers_regions_list_kind_item import (
    ApiV1LoadbalancersRegionsListKindItem,
)
from ...models.api_v1_loadbalancers_regions_list_scope import (
    ApiV1LoadbalancersRegionsListScope,
)
from ...models.api_v1_loadbalancers_regions_list_state import (
    ApiV1LoadbalancersRegionsListState,
)
from ...models.api_v1_loadbalancers_regions_list_state_not import (
    ApiV1LoadbalancersRegionsListStateNot,
)
from ...models.api_v1_loadbalancers_regions_list_time_range import (
    ApiV1LoadbalancersRegionsListTimeRange,
)
from ...models.paginated_loadbalancer_region_list_list import PaginatedLoadbalancerRegionListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1LoadbalancersRegionsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1LoadbalancersRegionsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1LoadbalancersRegionsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1LoadbalancersRegionsListState | Unset = UNSET,
    state_not: ApiV1LoadbalancersRegionsListStateNot | Unset = UNSET,
    time_range: ApiV1LoadbalancersRegionsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["active"] = active

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

    params["has_conditions"] = has_conditions

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item: str = kind_item_data
            json_kind.append(kind_item)

    params["kind"] = json_kind

    params["name"] = name

    params["name_exact"] = name_exact

    params["ordering"] = ordering

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
        "url": "/api/v1/loadbalancers/regions/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedLoadbalancerRegionListList | None:
    if response.status_code == 200:
        response_200 = PaginatedLoadbalancerRegionListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedLoadbalancerRegionListList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1LoadbalancersRegionsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1LoadbalancersRegionsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1LoadbalancersRegionsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1LoadbalancersRegionsListState | Unset = UNSET,
    state_not: ApiV1LoadbalancersRegionsListStateNot | Unset = UNSET,
    time_range: ApiV1LoadbalancersRegionsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedLoadbalancerRegionListList]:
    """API endpoint that allows LoadBalancer Regions to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        active (bool | Unset):
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1LoadbalancersRegionsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1LoadbalancersRegionsListKindItem] | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1LoadbalancersRegionsListScope | Unset):
        search (str | Unset):
        state (ApiV1LoadbalancersRegionsListState | Unset):
        state_not (ApiV1LoadbalancersRegionsListStateNot | Unset):
        time_range (ApiV1LoadbalancersRegionsListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLoadbalancerRegionListList]
    """

    kwargs = _get_kwargs(
        active=active,
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        has_conditions=has_conditions,
        kind=kind,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
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
    active: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1LoadbalancersRegionsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1LoadbalancersRegionsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1LoadbalancersRegionsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1LoadbalancersRegionsListState | Unset = UNSET,
    state_not: ApiV1LoadbalancersRegionsListStateNot | Unset = UNSET,
    time_range: ApiV1LoadbalancersRegionsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedLoadbalancerRegionListList | None:
    """API endpoint that allows LoadBalancer Regions to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        active (bool | Unset):
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1LoadbalancersRegionsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1LoadbalancersRegionsListKindItem] | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1LoadbalancersRegionsListScope | Unset):
        search (str | Unset):
        state (ApiV1LoadbalancersRegionsListState | Unset):
        state_not (ApiV1LoadbalancersRegionsListStateNot | Unset):
        time_range (ApiV1LoadbalancersRegionsListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLoadbalancerRegionListList
    """

    return sync_detailed(
        client=client,
        active=active,
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        has_conditions=has_conditions,
        kind=kind,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
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
    active: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1LoadbalancersRegionsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1LoadbalancersRegionsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1LoadbalancersRegionsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1LoadbalancersRegionsListState | Unset = UNSET,
    state_not: ApiV1LoadbalancersRegionsListStateNot | Unset = UNSET,
    time_range: ApiV1LoadbalancersRegionsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedLoadbalancerRegionListList]:
    """API endpoint that allows LoadBalancer Regions to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        active (bool | Unset):
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1LoadbalancersRegionsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1LoadbalancersRegionsListKindItem] | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1LoadbalancersRegionsListScope | Unset):
        search (str | Unset):
        state (ApiV1LoadbalancersRegionsListState | Unset):
        state_not (ApiV1LoadbalancersRegionsListStateNot | Unset):
        time_range (ApiV1LoadbalancersRegionsListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLoadbalancerRegionListList]
    """

    kwargs = _get_kwargs(
        active=active,
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        has_conditions=has_conditions,
        kind=kind,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
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
    active: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1LoadbalancersRegionsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1LoadbalancersRegionsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1LoadbalancersRegionsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1LoadbalancersRegionsListState | Unset = UNSET,
    state_not: ApiV1LoadbalancersRegionsListStateNot | Unset = UNSET,
    time_range: ApiV1LoadbalancersRegionsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedLoadbalancerRegionListList | None:
    """API endpoint that allows LoadBalancer Regions to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        active (bool | Unset):
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1LoadbalancersRegionsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1LoadbalancersRegionsListKindItem] | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1LoadbalancersRegionsListScope | Unset):
        search (str | Unset):
        state (ApiV1LoadbalancersRegionsListState | Unset):
        state_not (ApiV1LoadbalancersRegionsListStateNot | Unset):
        time_range (ApiV1LoadbalancersRegionsListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLoadbalancerRegionListList
    """

    return (
        await asyncio_detailed(
            client=client,
            active=active,
            archived=archived,
            created_at=created_at,
            created_by_component=created_by_component,
            created_by_users=created_by_users,
            debug_mode=debug_mode,
            has_conditions=has_conditions,
            kind=kind,
            name=name,
            name_exact=name_exact,
            ordering=ordering,
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
