from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_agents_list_kind_item import ApiV1AgentsListKindItem
from ...models.api_v1_agents_list_state import ApiV1AgentsListState
from ...models.api_v1_agents_list_state_not import ApiV1AgentsListStateNot
from ...models.api_v1_agents_list_time_range import ApiV1AgentsListTimeRange
from ...models.paginated_agent_list_list import PaginatedAgentListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1AgentsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    online_status: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pops: list[UUID] | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1AgentsListState | Unset = UNSET,
    state_not: ApiV1AgentsListStateNot | Unset = UNSET,
    time_range: ApiV1AgentsListTimeRange | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["archived"] = archived

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

    params["online_status"] = online_status

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

    json_pops: list[str] | Unset = UNSET
    if not isinstance(pops, Unset):
        json_pops = []
        for pops_item_data in pops:
            pops_item = str(pops_item_data)
            json_pops.append(pops_item)

    params["pops"] = json_pops

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

    params["version"] = version

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
        "url": "/api/v1/agents/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedAgentListList | None:
    if response.status_code == 200:
        response_200 = PaginatedAgentListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedAgentListList]:
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
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1AgentsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    online_status: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pops: list[UUID] | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1AgentsListState | Unset = UNSET,
    state_not: ApiV1AgentsListStateNot | Unset = UNSET,
    time_range: ApiV1AgentsListTimeRange | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedAgentListList]:
    """API endpoint for Agents.

    Provides read-only access to agent data for the Dynamic Table V2.

    Args:
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1AgentsListKindItem] | Unset):
        name_exact (str | Unset):
        online_status (bool | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pops (list[UUID] | Unset):
        search (str | Unset):
        state (ApiV1AgentsListState | Unset):
        state_not (ApiV1AgentsListStateNot | Unset):
        time_range (ApiV1AgentsListTimeRange | Unset):
        version (str | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAgentListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_by_users=created_by_users,
        has_conditions=has_conditions,
        kind=kind,
        name_exact=name_exact,
        online_status=online_status,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        pops=pops,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        version=version,
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
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1AgentsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    online_status: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pops: list[UUID] | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1AgentsListState | Unset = UNSET,
    state_not: ApiV1AgentsListStateNot | Unset = UNSET,
    time_range: ApiV1AgentsListTimeRange | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedAgentListList | None:
    """API endpoint for Agents.

    Provides read-only access to agent data for the Dynamic Table V2.

    Args:
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1AgentsListKindItem] | Unset):
        name_exact (str | Unset):
        online_status (bool | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pops (list[UUID] | Unset):
        search (str | Unset):
        state (ApiV1AgentsListState | Unset):
        state_not (ApiV1AgentsListStateNot | Unset):
        time_range (ApiV1AgentsListTimeRange | Unset):
        version (str | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAgentListList
    """

    return sync_detailed(
        client=client,
        archived=archived,
        created_by_users=created_by_users,
        has_conditions=has_conditions,
        kind=kind,
        name_exact=name_exact,
        online_status=online_status,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        pops=pops,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        version=version,
        workspaces=workspaces,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1AgentsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    online_status: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pops: list[UUID] | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1AgentsListState | Unset = UNSET,
    state_not: ApiV1AgentsListStateNot | Unset = UNSET,
    time_range: ApiV1AgentsListTimeRange | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedAgentListList]:
    """API endpoint for Agents.

    Provides read-only access to agent data for the Dynamic Table V2.

    Args:
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1AgentsListKindItem] | Unset):
        name_exact (str | Unset):
        online_status (bool | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pops (list[UUID] | Unset):
        search (str | Unset):
        state (ApiV1AgentsListState | Unset):
        state_not (ApiV1AgentsListStateNot | Unset):
        time_range (ApiV1AgentsListTimeRange | Unset):
        version (str | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAgentListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_by_users=created_by_users,
        has_conditions=has_conditions,
        kind=kind,
        name_exact=name_exact,
        online_status=online_status,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        pops=pops,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        version=version,
        workspaces=workspaces,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1AgentsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    online_status: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pops: list[UUID] | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1AgentsListState | Unset = UNSET,
    state_not: ApiV1AgentsListStateNot | Unset = UNSET,
    time_range: ApiV1AgentsListTimeRange | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedAgentListList | None:
    """API endpoint for Agents.

    Provides read-only access to agent data for the Dynamic Table V2.

    Args:
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1AgentsListKindItem] | Unset):
        name_exact (str | Unset):
        online_status (bool | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pops (list[UUID] | Unset):
        search (str | Unset):
        state (ApiV1AgentsListState | Unset):
        state_not (ApiV1AgentsListStateNot | Unset):
        time_range (ApiV1AgentsListTimeRange | Unset):
        version (str | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAgentListList
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            created_by_users=created_by_users,
            has_conditions=has_conditions,
            kind=kind,
            name_exact=name_exact,
            online_status=online_status,
            ordering=ordering,
            organizations=organizations,
            page=page,
            page_size=page_size,
            platform_service=platform_service,
            pops=pops,
            search=search,
            state=state,
            state_not=state_not,
            time_range=time_range,
            version=version,
            workspaces=workspaces,
        )
    ).parsed
