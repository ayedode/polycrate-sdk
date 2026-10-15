from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_workspaces_list_endpoint_monitoring_mode import (
    ApiV1WorkspacesListEndpointMonitoringMode,
)
from ...models.api_v1_workspaces_list_kind_item import (
    ApiV1WorkspacesListKindItem,
)
from ...models.api_v1_workspaces_list_state import ApiV1WorkspacesListState
from ...models.api_v1_workspaces_list_state_not import (
    ApiV1WorkspacesListStateNot,
)
from ...models.api_v1_workspaces_list_time_range import (
    ApiV1WorkspacesListTimeRange,
)
from ...models.paginated_workspace_list_list import PaginatedWorkspaceListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: bool | Unset = UNSET,
    backup_enabled: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    endpoint_monitoring_mode: ApiV1WorkspacesListEndpointMonitoringMode | Unset = UNSET,
    git_sync_enabled: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    k8s_addons_enabled: bool | Unset = UNSET,
    kind: list[ApiV1WorkspacesListKindItem] | Unset = UNSET,
    logs_enabled: bool | Unset = UNSET,
    maintenance: bool | Unset = UNSET,
    metrics_enabled: bool | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    notifications_enabled: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_name: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: list[UUID] | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1WorkspacesListState | Unset = UNSET,
    state_not: ApiV1WorkspacesListStateNot | Unset = UNSET,
    time_range: ApiV1WorkspacesListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["archived"] = archived

    params["backup_enabled"] = backup_enabled

    json_created_by_users: list[list[int]] | Unset = UNSET
    if not isinstance(created_by_users, Unset):
        json_created_by_users = []
        for created_by_users_item_data in created_by_users:
            created_by_users_item = created_by_users_item_data

            json_created_by_users.append(created_by_users_item)

    params["created_by_users"] = json_created_by_users

    json_endpoint_monitoring_mode: str | Unset = UNSET
    if not isinstance(endpoint_monitoring_mode, Unset):
        json_endpoint_monitoring_mode = endpoint_monitoring_mode

    params["endpoint_monitoring_mode"] = json_endpoint_monitoring_mode

    params["git_sync_enabled"] = git_sync_enabled

    params["has_conditions"] = has_conditions

    params["k8s_addons_enabled"] = k8s_addons_enabled

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item: str = kind_item_data
            json_kind.append(kind_item)

    params["kind"] = json_kind

    params["logs_enabled"] = logs_enabled

    params["maintenance"] = maintenance

    params["metrics_enabled"] = metrics_enabled

    params["name"] = name

    params["name_exact"] = name_exact

    params["notifications_enabled"] = notifications_enabled

    params["ordering"] = ordering

    params["organization_name"] = organization_name

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

    json_pop: list[str] | Unset = UNSET
    if not isinstance(pop, Unset):
        json_pop = []
        for pop_item_data in pop:
            pop_item = str(pop_item_data)
            json_pop.append(pop_item)

    params["pop"] = json_pop

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
        "url": "/api/v1/workspaces/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedWorkspaceListList | None:
    if response.status_code == 200:
        response_200 = PaginatedWorkspaceListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedWorkspaceListList]:
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
    backup_enabled: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    endpoint_monitoring_mode: ApiV1WorkspacesListEndpointMonitoringMode | Unset = UNSET,
    git_sync_enabled: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    k8s_addons_enabled: bool | Unset = UNSET,
    kind: list[ApiV1WorkspacesListKindItem] | Unset = UNSET,
    logs_enabled: bool | Unset = UNSET,
    maintenance: bool | Unset = UNSET,
    metrics_enabled: bool | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    notifications_enabled: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_name: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: list[UUID] | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1WorkspacesListState | Unset = UNSET,
    state_not: ApiV1WorkspacesListStateNot | Unset = UNSET,
    time_range: ApiV1WorkspacesListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedWorkspaceListList]:
    """API endpoint that allows workspaces to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        archived (bool | Unset):
        backup_enabled (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        endpoint_monitoring_mode (ApiV1WorkspacesListEndpointMonitoringMode | Unset):
        git_sync_enabled (bool | Unset):
        has_conditions (bool | Unset):
        k8s_addons_enabled (bool | Unset):
        kind (list[ApiV1WorkspacesListKindItem] | Unset):
        logs_enabled (bool | Unset):
        maintenance (bool | Unset):
        metrics_enabled (bool | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        notifications_enabled (bool | Unset):
        ordering (str | Unset):
        organization_name (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pop (list[UUID] | Unset):
        search (str | Unset):
        state (ApiV1WorkspacesListState | Unset):
        state_not (ApiV1WorkspacesListStateNot | Unset):
        time_range (ApiV1WorkspacesListTimeRange | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWorkspaceListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        backup_enabled=backup_enabled,
        created_by_users=created_by_users,
        endpoint_monitoring_mode=endpoint_monitoring_mode,
        git_sync_enabled=git_sync_enabled,
        has_conditions=has_conditions,
        k8s_addons_enabled=k8s_addons_enabled,
        kind=kind,
        logs_enabled=logs_enabled,
        maintenance=maintenance,
        metrics_enabled=metrics_enabled,
        name=name,
        name_exact=name_exact,
        notifications_enabled=notifications_enabled,
        ordering=ordering,
        organization_name=organization_name,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        pop=pop,
        search=search,
        state=state,
        state_not=state_not,
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
    backup_enabled: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    endpoint_monitoring_mode: ApiV1WorkspacesListEndpointMonitoringMode | Unset = UNSET,
    git_sync_enabled: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    k8s_addons_enabled: bool | Unset = UNSET,
    kind: list[ApiV1WorkspacesListKindItem] | Unset = UNSET,
    logs_enabled: bool | Unset = UNSET,
    maintenance: bool | Unset = UNSET,
    metrics_enabled: bool | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    notifications_enabled: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_name: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: list[UUID] | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1WorkspacesListState | Unset = UNSET,
    state_not: ApiV1WorkspacesListStateNot | Unset = UNSET,
    time_range: ApiV1WorkspacesListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedWorkspaceListList | None:
    """API endpoint that allows workspaces to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        archived (bool | Unset):
        backup_enabled (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        endpoint_monitoring_mode (ApiV1WorkspacesListEndpointMonitoringMode | Unset):
        git_sync_enabled (bool | Unset):
        has_conditions (bool | Unset):
        k8s_addons_enabled (bool | Unset):
        kind (list[ApiV1WorkspacesListKindItem] | Unset):
        logs_enabled (bool | Unset):
        maintenance (bool | Unset):
        metrics_enabled (bool | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        notifications_enabled (bool | Unset):
        ordering (str | Unset):
        organization_name (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pop (list[UUID] | Unset):
        search (str | Unset):
        state (ApiV1WorkspacesListState | Unset):
        state_not (ApiV1WorkspacesListStateNot | Unset):
        time_range (ApiV1WorkspacesListTimeRange | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWorkspaceListList
    """

    return sync_detailed(
        client=client,
        archived=archived,
        backup_enabled=backup_enabled,
        created_by_users=created_by_users,
        endpoint_monitoring_mode=endpoint_monitoring_mode,
        git_sync_enabled=git_sync_enabled,
        has_conditions=has_conditions,
        k8s_addons_enabled=k8s_addons_enabled,
        kind=kind,
        logs_enabled=logs_enabled,
        maintenance=maintenance,
        metrics_enabled=metrics_enabled,
        name=name,
        name_exact=name_exact,
        notifications_enabled=notifications_enabled,
        ordering=ordering,
        organization_name=organization_name,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        pop=pop,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        workspaces=workspaces,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    backup_enabled: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    endpoint_monitoring_mode: ApiV1WorkspacesListEndpointMonitoringMode | Unset = UNSET,
    git_sync_enabled: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    k8s_addons_enabled: bool | Unset = UNSET,
    kind: list[ApiV1WorkspacesListKindItem] | Unset = UNSET,
    logs_enabled: bool | Unset = UNSET,
    maintenance: bool | Unset = UNSET,
    metrics_enabled: bool | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    notifications_enabled: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_name: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: list[UUID] | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1WorkspacesListState | Unset = UNSET,
    state_not: ApiV1WorkspacesListStateNot | Unset = UNSET,
    time_range: ApiV1WorkspacesListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedWorkspaceListList]:
    """API endpoint that allows workspaces to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        archived (bool | Unset):
        backup_enabled (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        endpoint_monitoring_mode (ApiV1WorkspacesListEndpointMonitoringMode | Unset):
        git_sync_enabled (bool | Unset):
        has_conditions (bool | Unset):
        k8s_addons_enabled (bool | Unset):
        kind (list[ApiV1WorkspacesListKindItem] | Unset):
        logs_enabled (bool | Unset):
        maintenance (bool | Unset):
        metrics_enabled (bool | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        notifications_enabled (bool | Unset):
        ordering (str | Unset):
        organization_name (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pop (list[UUID] | Unset):
        search (str | Unset):
        state (ApiV1WorkspacesListState | Unset):
        state_not (ApiV1WorkspacesListStateNot | Unset):
        time_range (ApiV1WorkspacesListTimeRange | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWorkspaceListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        backup_enabled=backup_enabled,
        created_by_users=created_by_users,
        endpoint_monitoring_mode=endpoint_monitoring_mode,
        git_sync_enabled=git_sync_enabled,
        has_conditions=has_conditions,
        k8s_addons_enabled=k8s_addons_enabled,
        kind=kind,
        logs_enabled=logs_enabled,
        maintenance=maintenance,
        metrics_enabled=metrics_enabled,
        name=name,
        name_exact=name_exact,
        notifications_enabled=notifications_enabled,
        ordering=ordering,
        organization_name=organization_name,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        pop=pop,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        workspaces=workspaces,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    backup_enabled: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    endpoint_monitoring_mode: ApiV1WorkspacesListEndpointMonitoringMode | Unset = UNSET,
    git_sync_enabled: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    k8s_addons_enabled: bool | Unset = UNSET,
    kind: list[ApiV1WorkspacesListKindItem] | Unset = UNSET,
    logs_enabled: bool | Unset = UNSET,
    maintenance: bool | Unset = UNSET,
    metrics_enabled: bool | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    notifications_enabled: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization_name: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: list[UUID] | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1WorkspacesListState | Unset = UNSET,
    state_not: ApiV1WorkspacesListStateNot | Unset = UNSET,
    time_range: ApiV1WorkspacesListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedWorkspaceListList | None:
    """API endpoint that allows workspaces to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        archived (bool | Unset):
        backup_enabled (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        endpoint_monitoring_mode (ApiV1WorkspacesListEndpointMonitoringMode | Unset):
        git_sync_enabled (bool | Unset):
        has_conditions (bool | Unset):
        k8s_addons_enabled (bool | Unset):
        kind (list[ApiV1WorkspacesListKindItem] | Unset):
        logs_enabled (bool | Unset):
        maintenance (bool | Unset):
        metrics_enabled (bool | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        notifications_enabled (bool | Unset):
        ordering (str | Unset):
        organization_name (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pop (list[UUID] | Unset):
        search (str | Unset):
        state (ApiV1WorkspacesListState | Unset):
        state_not (ApiV1WorkspacesListStateNot | Unset):
        time_range (ApiV1WorkspacesListTimeRange | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWorkspaceListList
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            backup_enabled=backup_enabled,
            created_by_users=created_by_users,
            endpoint_monitoring_mode=endpoint_monitoring_mode,
            git_sync_enabled=git_sync_enabled,
            has_conditions=has_conditions,
            k8s_addons_enabled=k8s_addons_enabled,
            kind=kind,
            logs_enabled=logs_enabled,
            maintenance=maintenance,
            metrics_enabled=metrics_enabled,
            name=name,
            name_exact=name_exact,
            notifications_enabled=notifications_enabled,
            ordering=ordering,
            organization_name=organization_name,
            organizations=organizations,
            page=page,
            page_size=page_size,
            platform_service=platform_service,
            pop=pop,
            search=search,
            state=state,
            state_not=state_not,
            time_range=time_range,
            workspaces=workspaces,
        )
    ).parsed
