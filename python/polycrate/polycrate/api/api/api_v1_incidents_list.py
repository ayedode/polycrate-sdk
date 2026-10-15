import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_incidents_list_kind_item import ApiV1IncidentsListKindItem
from ...models.api_v1_incidents_list_state import ApiV1IncidentsListState
from ...models.api_v1_incidents_list_state_not import ApiV1IncidentsListStateNot
from ...models.api_v1_incidents_list_status import ApiV1IncidentsListStatus
from ...models.api_v1_incidents_list_time_range import (
    ApiV1IncidentsListTimeRange,
)
from ...models.paginated_incident_list_list import PaginatedIncidentListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    affected_organization: UUID | Unset = UNSET,
    affected_pops: UUID | Unset = UNSET,
    affected_workspace: UUID | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    downtimes: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1IncidentsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    state: ApiV1IncidentsListState | Unset = UNSET,
    state_not: ApiV1IncidentsListStateNot | Unset = UNSET,
    status: ApiV1IncidentsListStatus | Unset = UNSET,
    time_range: ApiV1IncidentsListTimeRange | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    vulnerability_findings: UUID | Unset = UNSET,
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

    json_downtimes: str | Unset = UNSET
    if not isinstance(downtimes, Unset):
        json_downtimes = str(downtimes)
    params["downtimes"] = json_downtimes

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

    params["search"] = search

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

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

    json_until: str | Unset = UNSET
    if not isinstance(until, Unset):
        json_until = until.isoformat()
    params["until"] = json_until

    json_vulnerability_findings: str | Unset = UNSET
    if not isinstance(vulnerability_findings, Unset):
        json_vulnerability_findings = str(vulnerability_findings)
    params["vulnerability_findings"] = json_vulnerability_findings

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
        "url": "/api/v1/incidents/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedIncidentListList | None:
    if response.status_code == 200:
        response_200 = PaginatedIncidentListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedIncidentListList]:
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
    downtimes: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1IncidentsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    state: ApiV1IncidentsListState | Unset = UNSET,
    state_not: ApiV1IncidentsListStateNot | Unset = UNSET,
    status: ApiV1IncidentsListStatus | Unset = UNSET,
    time_range: ApiV1IncidentsListTimeRange | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    vulnerability_findings: UUID | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedIncidentListList]:
    """API endpoint that allows Incidents to be viewed or edited.

    Archived filter handled by ManagedObjectBaseViewset.
    Spec 531: non-superusers see their org incidents OR system-wide (organization=NULL).

    Args:
        affected_organization (UUID | Unset):
        affected_pops (UUID | Unset):
        affected_workspace (UUID | Unset):
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        downtimes (UUID | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1IncidentsListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pop (UUID | Unset):
        search (str | Unset):
        since (datetime.datetime | Unset):
        state (ApiV1IncidentsListState | Unset):
        state_not (ApiV1IncidentsListStateNot | Unset):
        status (ApiV1IncidentsListStatus | Unset):
        time_range (ApiV1IncidentsListTimeRange | Unset):
        until (datetime.datetime | Unset):
        vulnerability_findings (UUID | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIncidentListList]
    """

    kwargs = _get_kwargs(
        affected_organization=affected_organization,
        affected_pops=affected_pops,
        affected_workspace=affected_workspace,
        archived=archived,
        created_by_users=created_by_users,
        downtimes=downtimes,
        has_conditions=has_conditions,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        pop=pop,
        search=search,
        since=since,
        state=state,
        state_not=state_not,
        status=status,
        time_range=time_range,
        until=until,
        vulnerability_findings=vulnerability_findings,
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
    downtimes: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1IncidentsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    state: ApiV1IncidentsListState | Unset = UNSET,
    state_not: ApiV1IncidentsListStateNot | Unset = UNSET,
    status: ApiV1IncidentsListStatus | Unset = UNSET,
    time_range: ApiV1IncidentsListTimeRange | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    vulnerability_findings: UUID | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedIncidentListList | None:
    """API endpoint that allows Incidents to be viewed or edited.

    Archived filter handled by ManagedObjectBaseViewset.
    Spec 531: non-superusers see their org incidents OR system-wide (organization=NULL).

    Args:
        affected_organization (UUID | Unset):
        affected_pops (UUID | Unset):
        affected_workspace (UUID | Unset):
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        downtimes (UUID | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1IncidentsListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pop (UUID | Unset):
        search (str | Unset):
        since (datetime.datetime | Unset):
        state (ApiV1IncidentsListState | Unset):
        state_not (ApiV1IncidentsListStateNot | Unset):
        status (ApiV1IncidentsListStatus | Unset):
        time_range (ApiV1IncidentsListTimeRange | Unset):
        until (datetime.datetime | Unset):
        vulnerability_findings (UUID | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIncidentListList
    """

    return sync_detailed(
        client=client,
        affected_organization=affected_organization,
        affected_pops=affected_pops,
        affected_workspace=affected_workspace,
        archived=archived,
        created_by_users=created_by_users,
        downtimes=downtimes,
        has_conditions=has_conditions,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        pop=pop,
        search=search,
        since=since,
        state=state,
        state_not=state_not,
        status=status,
        time_range=time_range,
        until=until,
        vulnerability_findings=vulnerability_findings,
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
    downtimes: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1IncidentsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    state: ApiV1IncidentsListState | Unset = UNSET,
    state_not: ApiV1IncidentsListStateNot | Unset = UNSET,
    status: ApiV1IncidentsListStatus | Unset = UNSET,
    time_range: ApiV1IncidentsListTimeRange | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    vulnerability_findings: UUID | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedIncidentListList]:
    """API endpoint that allows Incidents to be viewed or edited.

    Archived filter handled by ManagedObjectBaseViewset.
    Spec 531: non-superusers see their org incidents OR system-wide (organization=NULL).

    Args:
        affected_organization (UUID | Unset):
        affected_pops (UUID | Unset):
        affected_workspace (UUID | Unset):
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        downtimes (UUID | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1IncidentsListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pop (UUID | Unset):
        search (str | Unset):
        since (datetime.datetime | Unset):
        state (ApiV1IncidentsListState | Unset):
        state_not (ApiV1IncidentsListStateNot | Unset):
        status (ApiV1IncidentsListStatus | Unset):
        time_range (ApiV1IncidentsListTimeRange | Unset):
        until (datetime.datetime | Unset):
        vulnerability_findings (UUID | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIncidentListList]
    """

    kwargs = _get_kwargs(
        affected_organization=affected_organization,
        affected_pops=affected_pops,
        affected_workspace=affected_workspace,
        archived=archived,
        created_by_users=created_by_users,
        downtimes=downtimes,
        has_conditions=has_conditions,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        pop=pop,
        search=search,
        since=since,
        state=state,
        state_not=state_not,
        status=status,
        time_range=time_range,
        until=until,
        vulnerability_findings=vulnerability_findings,
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
    downtimes: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1IncidentsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    pop: UUID | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    state: ApiV1IncidentsListState | Unset = UNSET,
    state_not: ApiV1IncidentsListStateNot | Unset = UNSET,
    status: ApiV1IncidentsListStatus | Unset = UNSET,
    time_range: ApiV1IncidentsListTimeRange | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    vulnerability_findings: UUID | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedIncidentListList | None:
    """API endpoint that allows Incidents to be viewed or edited.

    Archived filter handled by ManagedObjectBaseViewset.
    Spec 531: non-superusers see their org incidents OR system-wide (organization=NULL).

    Args:
        affected_organization (UUID | Unset):
        affected_pops (UUID | Unset):
        affected_workspace (UUID | Unset):
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        downtimes (UUID | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1IncidentsListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        pop (UUID | Unset):
        search (str | Unset):
        since (datetime.datetime | Unset):
        state (ApiV1IncidentsListState | Unset):
        state_not (ApiV1IncidentsListStateNot | Unset):
        status (ApiV1IncidentsListStatus | Unset):
        time_range (ApiV1IncidentsListTimeRange | Unset):
        until (datetime.datetime | Unset):
        vulnerability_findings (UUID | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIncidentListList
    """

    return (
        await asyncio_detailed(
            client=client,
            affected_organization=affected_organization,
            affected_pops=affected_pops,
            affected_workspace=affected_workspace,
            archived=archived,
            created_by_users=created_by_users,
            downtimes=downtimes,
            has_conditions=has_conditions,
            kind=kind,
            name_exact=name_exact,
            ordering=ordering,
            organizations=organizations,
            page=page,
            page_size=page_size,
            platform_service=platform_service,
            pop=pop,
            search=search,
            since=since,
            state=state,
            state_not=state_not,
            status=status,
            time_range=time_range,
            until=until,
            vulnerability_findings=vulnerability_findings,
            workspaces=workspaces,
        )
    ).parsed
