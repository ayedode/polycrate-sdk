from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_notes_list_kind_item import ApiV1NotesListKindItem
from ...models.api_v1_notes_list_state import ApiV1NotesListState
from ...models.api_v1_notes_list_state_not import ApiV1NotesListStateNot
from ...models.api_v1_notes_list_time_range import ApiV1NotesListTimeRange
from ...models.paginated_note_list_list import PaginatedNoteListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: bool | Unset = UNSET,
    assigned_to: list[int] | Unset = UNSET,
    assigned_to_me: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    datasource: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    has_time_tracked: str | Unset = UNSET,
    kind: list[ApiV1NotesListKindItem] | Unset = UNSET,
    managed_by_object_id: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    parent_note: UUID | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    project: UUID | Unset = UNSET,
    resolved: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1NotesListState | Unset = UNSET,
    state_not: ApiV1NotesListStateNot | Unset = UNSET,
    time_range: ApiV1NotesListTimeRange | Unset = UNSET,
    time_tracked_min: float | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["archived"] = archived

    json_assigned_to: list[int] | Unset = UNSET
    if not isinstance(assigned_to, Unset):
        json_assigned_to = assigned_to

    params["assigned_to"] = json_assigned_to

    params["assigned_to_me"] = assigned_to_me

    json_created_by_users: list[list[int]] | Unset = UNSET
    if not isinstance(created_by_users, Unset):
        json_created_by_users = []
        for created_by_users_item_data in created_by_users:
            created_by_users_item = created_by_users_item_data

            json_created_by_users.append(created_by_users_item)

    params["created_by_users"] = json_created_by_users

    json_datasource: str | Unset = UNSET
    if not isinstance(datasource, Unset):
        json_datasource = str(datasource)
    params["datasource"] = json_datasource

    params["has_conditions"] = has_conditions

    params["has_time_tracked"] = has_time_tracked

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item: str = kind_item_data
            json_kind.append(kind_item)

    params["kind"] = json_kind

    params["managed_by_object_id"] = managed_by_object_id

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

    json_parent_note: str | Unset = UNSET
    if not isinstance(parent_note, Unset):
        json_parent_note = str(parent_note)
    params["parent_note"] = json_parent_note

    params["platform_service"] = platform_service

    json_project: str | Unset = UNSET
    if not isinstance(project, Unset):
        json_project = str(project)
    params["project"] = json_project

    params["resolved"] = resolved

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

    params["time_tracked_min"] = time_tracked_min

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
        "url": "/api/v1/notes/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedNoteListList | None:
    if response.status_code == 200:
        response_200 = PaginatedNoteListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedNoteListList]:
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
    assigned_to: list[int] | Unset = UNSET,
    assigned_to_me: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    datasource: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    has_time_tracked: str | Unset = UNSET,
    kind: list[ApiV1NotesListKindItem] | Unset = UNSET,
    managed_by_object_id: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    parent_note: UUID | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    project: UUID | Unset = UNSET,
    resolved: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1NotesListState | Unset = UNSET,
    state_not: ApiV1NotesListStateNot | Unset = UNSET,
    time_range: ApiV1NotesListTimeRange | Unset = UNSET,
    time_tracked_min: float | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedNoteListList]:
    """API ViewSet for Notes Notes.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Note: filterset_class is only applied for 'list' action to allow
    detail operations (retrieve, update, destroy) on all note kinds
    including comments/replies.
    Per .specs/0.11.12/inline-reply-system.md

    Args:
        archived (bool | Unset):
        assigned_to (list[int] | Unset):
        assigned_to_me (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        datasource (UUID | Unset):
        has_conditions (bool | Unset):
        has_time_tracked (str | Unset):
        kind (list[ApiV1NotesListKindItem] | Unset):
        managed_by_object_id (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        parent_note (UUID | Unset):
        platform_service (bool | Unset):
        project (UUID | Unset):
        resolved (bool | Unset):
        search (str | Unset):
        state (ApiV1NotesListState | Unset):
        state_not (ApiV1NotesListStateNot | Unset):
        time_range (ApiV1NotesListTimeRange | Unset):
        time_tracked_min (float | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedNoteListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        assigned_to=assigned_to,
        assigned_to_me=assigned_to_me,
        created_by_users=created_by_users,
        datasource=datasource,
        has_conditions=has_conditions,
        has_time_tracked=has_time_tracked,
        kind=kind,
        managed_by_object_id=managed_by_object_id,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        parent_note=parent_note,
        platform_service=platform_service,
        project=project,
        resolved=resolved,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        time_tracked_min=time_tracked_min,
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
    assigned_to: list[int] | Unset = UNSET,
    assigned_to_me: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    datasource: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    has_time_tracked: str | Unset = UNSET,
    kind: list[ApiV1NotesListKindItem] | Unset = UNSET,
    managed_by_object_id: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    parent_note: UUID | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    project: UUID | Unset = UNSET,
    resolved: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1NotesListState | Unset = UNSET,
    state_not: ApiV1NotesListStateNot | Unset = UNSET,
    time_range: ApiV1NotesListTimeRange | Unset = UNSET,
    time_tracked_min: float | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedNoteListList | None:
    """API ViewSet for Notes Notes.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Note: filterset_class is only applied for 'list' action to allow
    detail operations (retrieve, update, destroy) on all note kinds
    including comments/replies.
    Per .specs/0.11.12/inline-reply-system.md

    Args:
        archived (bool | Unset):
        assigned_to (list[int] | Unset):
        assigned_to_me (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        datasource (UUID | Unset):
        has_conditions (bool | Unset):
        has_time_tracked (str | Unset):
        kind (list[ApiV1NotesListKindItem] | Unset):
        managed_by_object_id (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        parent_note (UUID | Unset):
        platform_service (bool | Unset):
        project (UUID | Unset):
        resolved (bool | Unset):
        search (str | Unset):
        state (ApiV1NotesListState | Unset):
        state_not (ApiV1NotesListStateNot | Unset):
        time_range (ApiV1NotesListTimeRange | Unset):
        time_tracked_min (float | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedNoteListList
    """

    return sync_detailed(
        client=client,
        archived=archived,
        assigned_to=assigned_to,
        assigned_to_me=assigned_to_me,
        created_by_users=created_by_users,
        datasource=datasource,
        has_conditions=has_conditions,
        has_time_tracked=has_time_tracked,
        kind=kind,
        managed_by_object_id=managed_by_object_id,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        parent_note=parent_note,
        platform_service=platform_service,
        project=project,
        resolved=resolved,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        time_tracked_min=time_tracked_min,
        workspaces=workspaces,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    assigned_to: list[int] | Unset = UNSET,
    assigned_to_me: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    datasource: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    has_time_tracked: str | Unset = UNSET,
    kind: list[ApiV1NotesListKindItem] | Unset = UNSET,
    managed_by_object_id: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    parent_note: UUID | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    project: UUID | Unset = UNSET,
    resolved: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1NotesListState | Unset = UNSET,
    state_not: ApiV1NotesListStateNot | Unset = UNSET,
    time_range: ApiV1NotesListTimeRange | Unset = UNSET,
    time_tracked_min: float | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedNoteListList]:
    """API ViewSet for Notes Notes.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Note: filterset_class is only applied for 'list' action to allow
    detail operations (retrieve, update, destroy) on all note kinds
    including comments/replies.
    Per .specs/0.11.12/inline-reply-system.md

    Args:
        archived (bool | Unset):
        assigned_to (list[int] | Unset):
        assigned_to_me (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        datasource (UUID | Unset):
        has_conditions (bool | Unset):
        has_time_tracked (str | Unset):
        kind (list[ApiV1NotesListKindItem] | Unset):
        managed_by_object_id (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        parent_note (UUID | Unset):
        platform_service (bool | Unset):
        project (UUID | Unset):
        resolved (bool | Unset):
        search (str | Unset):
        state (ApiV1NotesListState | Unset):
        state_not (ApiV1NotesListStateNot | Unset):
        time_range (ApiV1NotesListTimeRange | Unset):
        time_tracked_min (float | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedNoteListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        assigned_to=assigned_to,
        assigned_to_me=assigned_to_me,
        created_by_users=created_by_users,
        datasource=datasource,
        has_conditions=has_conditions,
        has_time_tracked=has_time_tracked,
        kind=kind,
        managed_by_object_id=managed_by_object_id,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        parent_note=parent_note,
        platform_service=platform_service,
        project=project,
        resolved=resolved,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        time_tracked_min=time_tracked_min,
        workspaces=workspaces,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    assigned_to: list[int] | Unset = UNSET,
    assigned_to_me: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    datasource: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    has_time_tracked: str | Unset = UNSET,
    kind: list[ApiV1NotesListKindItem] | Unset = UNSET,
    managed_by_object_id: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    parent_note: UUID | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    project: UUID | Unset = UNSET,
    resolved: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1NotesListState | Unset = UNSET,
    state_not: ApiV1NotesListStateNot | Unset = UNSET,
    time_range: ApiV1NotesListTimeRange | Unset = UNSET,
    time_tracked_min: float | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedNoteListList | None:
    """API ViewSet for Notes Notes.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Note: filterset_class is only applied for 'list' action to allow
    detail operations (retrieve, update, destroy) on all note kinds
    including comments/replies.
    Per .specs/0.11.12/inline-reply-system.md

    Args:
        archived (bool | Unset):
        assigned_to (list[int] | Unset):
        assigned_to_me (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        datasource (UUID | Unset):
        has_conditions (bool | Unset):
        has_time_tracked (str | Unset):
        kind (list[ApiV1NotesListKindItem] | Unset):
        managed_by_object_id (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        parent_note (UUID | Unset):
        platform_service (bool | Unset):
        project (UUID | Unset):
        resolved (bool | Unset):
        search (str | Unset):
        state (ApiV1NotesListState | Unset):
        state_not (ApiV1NotesListStateNot | Unset):
        time_range (ApiV1NotesListTimeRange | Unset):
        time_tracked_min (float | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedNoteListList
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            assigned_to=assigned_to,
            assigned_to_me=assigned_to_me,
            created_by_users=created_by_users,
            datasource=datasource,
            has_conditions=has_conditions,
            has_time_tracked=has_time_tracked,
            kind=kind,
            managed_by_object_id=managed_by_object_id,
            name_exact=name_exact,
            ordering=ordering,
            organizations=organizations,
            page=page,
            page_size=page_size,
            parent_note=parent_note,
            platform_service=platform_service,
            project=project,
            resolved=resolved,
            search=search,
            state=state,
            state_not=state_not,
            time_range=time_range,
            time_tracked_min=time_tracked_min,
            workspaces=workspaces,
        )
    ).parsed
