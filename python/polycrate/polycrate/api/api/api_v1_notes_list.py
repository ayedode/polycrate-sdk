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
from ...models.api_v1_notes_list_validation_error import ApiV1NotesListValidationError
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_403 import ErrorResponse403
from ...models.error_response_404 import ErrorResponse404
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_409 import ErrorResponse409
from ...models.error_response_410 import ErrorResponse410
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.error_response_502 import ErrorResponse502
from ...models.paginated_note_list_list import PaginatedNoteListList
from ...models.parse_error_response import ParseErrorResponse
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


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiV1NotesListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedNoteListList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedNoteListList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1NotesListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_notes_list_error_response_400_type_0 = ApiV1NotesListValidationError.from_dict(
                    data
                )

                return componentsschemas_api_v1_notes_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_notes_list_error_response_400_type_1 = ParseErrorResponse.from_dict(data)

            return componentsschemas_api_v1_notes_list_error_response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = ErrorResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = ErrorResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = ErrorResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse410.from_dict(response.json())

        return response_410

    if response.status_code == 415:
        response_415 = ErrorResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 500:
        response_500 = ErrorResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ErrorResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ApiV1NotesListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedNoteListList
]:
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
) -> Response[
    ApiV1NotesListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedNoteListList
]:
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
        Response[ApiV1NotesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedNoteListList]
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
) -> (
    ApiV1NotesListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedNoteListList
    | None
):
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
        ApiV1NotesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedNoteListList
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
) -> Response[
    ApiV1NotesListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedNoteListList
]:
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
        Response[ApiV1NotesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedNoteListList]
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
) -> (
    ApiV1NotesListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedNoteListList
    | None
):
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
        ApiV1NotesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedNoteListList
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
