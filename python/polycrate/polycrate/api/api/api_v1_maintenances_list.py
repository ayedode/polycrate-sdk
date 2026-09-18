import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_maintenances_list_kind_item import (
    ApiV1MaintenancesListKindItem,
)
from ...models.api_v1_maintenances_list_state import ApiV1MaintenancesListState
from ...models.api_v1_maintenances_list_state_not import (
    ApiV1MaintenancesListStateNot,
)
from ...models.api_v1_maintenances_list_time_range import (
    ApiV1MaintenancesListTimeRange,
)
from ...models.api_v1_maintenances_list_validation_error import ApiV1MaintenancesListValidationError
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
from ...models.paginated_maintenance_list_list import PaginatedMaintenanceListList
from ...models.parse_error_response import ParseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    affected_organization: UUID | Unset = UNSET,
    affected_pops: UUID | Unset = UNSET,
    affected_workspace: UUID | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    draft: bool | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1MaintenancesListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: UUID | Unset = UNSET,
    pop_provider_entity: UUID | Unset = UNSET,
    project: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    source_datasource: UUID | Unset = UNSET,
    source_note: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    state: ApiV1MaintenancesListState | Unset = UNSET,
    state_not: ApiV1MaintenancesListStateNot | Unset = UNSET,
    time_range: ApiV1MaintenancesListTimeRange | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_affected_organization: str | Unset = UNSET
    if not isinstance(affected_organization, Unset):
        json_affected_organization = str(affected_organization)
    params["affected_organization"] = json_affected_organization

    json_affected_pops: str | Unset = UNSET
    if not isinstance(affected_pops, Unset):
        json_affected_pops = str(affected_pops)
    params["affected_pops"] = json_affected_pops

    json_affected_workspace: str | Unset = UNSET
    if not isinstance(affected_workspace, Unset):
        json_affected_workspace = str(affected_workspace)
    params["affected_workspace"] = json_affected_workspace

    params["archived"] = archived

    json_created_by_users: list[list[int]] | Unset = UNSET
    if not isinstance(created_by_users, Unset):
        json_created_by_users = []
        for created_by_users_item_data in created_by_users:
            created_by_users_item = created_by_users_item_data

            json_created_by_users.append(created_by_users_item)

    params["created_by_users"] = json_created_by_users

    params["draft"] = draft

    json_end: str | Unset = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

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

    json_pop: str | Unset = UNSET
    if not isinstance(pop, Unset):
        json_pop = str(pop)
    params["pop"] = json_pop

    json_pop_provider_entity: str | Unset = UNSET
    if not isinstance(pop_provider_entity, Unset):
        json_pop_provider_entity = str(pop_provider_entity)
    params["pop_provider_entity"] = json_pop_provider_entity

    json_project: str | Unset = UNSET
    if not isinstance(project, Unset):
        json_project = str(project)
    params["project"] = json_project

    params["search"] = search

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    json_source_datasource: str | Unset = UNSET
    if not isinstance(source_datasource, Unset):
        json_source_datasource = str(source_datasource)
    params["source_datasource"] = json_source_datasource

    json_source_note: str | Unset = UNSET
    if not isinstance(source_note, Unset):
        json_source_note = str(source_note)
    params["source_note"] = json_source_note

    json_start: str | Unset = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

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

    json_until: str | Unset = UNSET
    if not isinstance(until, Unset):
        json_until = until.isoformat()
    params["until"] = json_until

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
        "url": "/api/v1/maintenances/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiV1MaintenancesListValidationError
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
    | PaginatedMaintenanceListList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedMaintenanceListList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1MaintenancesListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_maintenances_list_error_response_400_type_0 = (
                    ApiV1MaintenancesListValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_maintenances_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_maintenances_list_error_response_400_type_1 = ParseErrorResponse.from_dict(data)

            return componentsschemas_api_v1_maintenances_list_error_response_400_type_1

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
    ApiV1MaintenancesListValidationError
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
    | PaginatedMaintenanceListList
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
    affected_organization: UUID | Unset = UNSET,
    affected_pops: UUID | Unset = UNSET,
    affected_workspace: UUID | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    draft: bool | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1MaintenancesListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: UUID | Unset = UNSET,
    pop_provider_entity: UUID | Unset = UNSET,
    project: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    source_datasource: UUID | Unset = UNSET,
    source_note: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    state: ApiV1MaintenancesListState | Unset = UNSET,
    state_not: ApiV1MaintenancesListStateNot | Unset = UNSET,
    time_range: ApiV1MaintenancesListTimeRange | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[
    ApiV1MaintenancesListValidationError
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
    | PaginatedMaintenanceListList
]:
    """API endpoint that allows Maintenances to be viewed or edited.

    Archived filter handled by ManagedObjectBaseViewset.
    Spec 532: non-superusers see their org maintenances OR system-wide (organization=NULL).

    Args:
        affected_organization (UUID | Unset):
        affected_pops (UUID | Unset):
        affected_workspace (UUID | Unset):
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        draft (bool | Unset):
        end (datetime.datetime | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1MaintenancesListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pop (UUID | Unset):
        pop_provider_entity (UUID | Unset):
        project (UUID | Unset):
        search (str | Unset):
        since (datetime.datetime | Unset):
        source_datasource (UUID | Unset):
        source_note (UUID | Unset):
        start (datetime.datetime | Unset):
        state (ApiV1MaintenancesListState | Unset):
        state_not (ApiV1MaintenancesListStateNot | Unset):
        time_range (ApiV1MaintenancesListTimeRange | Unset):
        until (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1MaintenancesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedMaintenanceListList]
    """

    kwargs = _get_kwargs(
        affected_organization=affected_organization,
        affected_pops=affected_pops,
        affected_workspace=affected_workspace,
        archived=archived,
        created_by_users=created_by_users,
        draft=draft,
        end=end,
        has_conditions=has_conditions,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        pop=pop,
        pop_provider_entity=pop_provider_entity,
        project=project,
        search=search,
        since=since,
        source_datasource=source_datasource,
        source_note=source_note,
        start=start,
        state=state,
        state_not=state_not,
        time_range=time_range,
        until=until,
        workspaces=workspaces,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    affected_organization: UUID | Unset = UNSET,
    affected_pops: UUID | Unset = UNSET,
    affected_workspace: UUID | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    draft: bool | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1MaintenancesListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: UUID | Unset = UNSET,
    pop_provider_entity: UUID | Unset = UNSET,
    project: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    source_datasource: UUID | Unset = UNSET,
    source_note: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    state: ApiV1MaintenancesListState | Unset = UNSET,
    state_not: ApiV1MaintenancesListStateNot | Unset = UNSET,
    time_range: ApiV1MaintenancesListTimeRange | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> (
    ApiV1MaintenancesListValidationError
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
    | PaginatedMaintenanceListList
    | None
):
    """API endpoint that allows Maintenances to be viewed or edited.

    Archived filter handled by ManagedObjectBaseViewset.
    Spec 532: non-superusers see their org maintenances OR system-wide (organization=NULL).

    Args:
        affected_organization (UUID | Unset):
        affected_pops (UUID | Unset):
        affected_workspace (UUID | Unset):
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        draft (bool | Unset):
        end (datetime.datetime | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1MaintenancesListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pop (UUID | Unset):
        pop_provider_entity (UUID | Unset):
        project (UUID | Unset):
        search (str | Unset):
        since (datetime.datetime | Unset):
        source_datasource (UUID | Unset):
        source_note (UUID | Unset):
        start (datetime.datetime | Unset):
        state (ApiV1MaintenancesListState | Unset):
        state_not (ApiV1MaintenancesListStateNot | Unset):
        time_range (ApiV1MaintenancesListTimeRange | Unset):
        until (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1MaintenancesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedMaintenanceListList
    """

    return sync_detailed(
        client=client,
        affected_organization=affected_organization,
        affected_pops=affected_pops,
        affected_workspace=affected_workspace,
        archived=archived,
        created_by_users=created_by_users,
        draft=draft,
        end=end,
        has_conditions=has_conditions,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        pop=pop,
        pop_provider_entity=pop_provider_entity,
        project=project,
        search=search,
        since=since,
        source_datasource=source_datasource,
        source_note=source_note,
        start=start,
        state=state,
        state_not=state_not,
        time_range=time_range,
        until=until,
        workspaces=workspaces,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    affected_organization: UUID | Unset = UNSET,
    affected_pops: UUID | Unset = UNSET,
    affected_workspace: UUID | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    draft: bool | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1MaintenancesListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: UUID | Unset = UNSET,
    pop_provider_entity: UUID | Unset = UNSET,
    project: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    source_datasource: UUID | Unset = UNSET,
    source_note: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    state: ApiV1MaintenancesListState | Unset = UNSET,
    state_not: ApiV1MaintenancesListStateNot | Unset = UNSET,
    time_range: ApiV1MaintenancesListTimeRange | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[
    ApiV1MaintenancesListValidationError
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
    | PaginatedMaintenanceListList
]:
    """API endpoint that allows Maintenances to be viewed or edited.

    Archived filter handled by ManagedObjectBaseViewset.
    Spec 532: non-superusers see their org maintenances OR system-wide (organization=NULL).

    Args:
        affected_organization (UUID | Unset):
        affected_pops (UUID | Unset):
        affected_workspace (UUID | Unset):
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        draft (bool | Unset):
        end (datetime.datetime | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1MaintenancesListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pop (UUID | Unset):
        pop_provider_entity (UUID | Unset):
        project (UUID | Unset):
        search (str | Unset):
        since (datetime.datetime | Unset):
        source_datasource (UUID | Unset):
        source_note (UUID | Unset):
        start (datetime.datetime | Unset):
        state (ApiV1MaintenancesListState | Unset):
        state_not (ApiV1MaintenancesListStateNot | Unset):
        time_range (ApiV1MaintenancesListTimeRange | Unset):
        until (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1MaintenancesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedMaintenanceListList]
    """

    kwargs = _get_kwargs(
        affected_organization=affected_organization,
        affected_pops=affected_pops,
        affected_workspace=affected_workspace,
        archived=archived,
        created_by_users=created_by_users,
        draft=draft,
        end=end,
        has_conditions=has_conditions,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        pop=pop,
        pop_provider_entity=pop_provider_entity,
        project=project,
        search=search,
        since=since,
        source_datasource=source_datasource,
        source_note=source_note,
        start=start,
        state=state,
        state_not=state_not,
        time_range=time_range,
        until=until,
        workspaces=workspaces,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    affected_organization: UUID | Unset = UNSET,
    affected_pops: UUID | Unset = UNSET,
    affected_workspace: UUID | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    draft: bool | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1MaintenancesListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: UUID | Unset = UNSET,
    pop_provider_entity: UUID | Unset = UNSET,
    project: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    source_datasource: UUID | Unset = UNSET,
    source_note: UUID | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    state: ApiV1MaintenancesListState | Unset = UNSET,
    state_not: ApiV1MaintenancesListStateNot | Unset = UNSET,
    time_range: ApiV1MaintenancesListTimeRange | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> (
    ApiV1MaintenancesListValidationError
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
    | PaginatedMaintenanceListList
    | None
):
    """API endpoint that allows Maintenances to be viewed or edited.

    Archived filter handled by ManagedObjectBaseViewset.
    Spec 532: non-superusers see their org maintenances OR system-wide (organization=NULL).

    Args:
        affected_organization (UUID | Unset):
        affected_pops (UUID | Unset):
        affected_workspace (UUID | Unset):
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        draft (bool | Unset):
        end (datetime.datetime | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1MaintenancesListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pop (UUID | Unset):
        pop_provider_entity (UUID | Unset):
        project (UUID | Unset):
        search (str | Unset):
        since (datetime.datetime | Unset):
        source_datasource (UUID | Unset):
        source_note (UUID | Unset):
        start (datetime.datetime | Unset):
        state (ApiV1MaintenancesListState | Unset):
        state_not (ApiV1MaintenancesListStateNot | Unset):
        time_range (ApiV1MaintenancesListTimeRange | Unset):
        until (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1MaintenancesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedMaintenanceListList
    """

    return (
        await asyncio_detailed(
            client=client,
            affected_organization=affected_organization,
            affected_pops=affected_pops,
            affected_workspace=affected_workspace,
            archived=archived,
            created_by_users=created_by_users,
            draft=draft,
            end=end,
            has_conditions=has_conditions,
            kind=kind,
            name_exact=name_exact,
            ordering=ordering,
            organizations=organizations,
            page=page,
            page_size=page_size,
            platform_service=platform_service,
            pop=pop,
            pop_provider_entity=pop_provider_entity,
            project=project,
            search=search,
            since=since,
            source_datasource=source_datasource,
            source_note=source_note,
            start=start,
            state=state,
            state_not=state_not,
            time_range=time_range,
            until=until,
            workspaces=workspaces,
        )
    ).parsed
