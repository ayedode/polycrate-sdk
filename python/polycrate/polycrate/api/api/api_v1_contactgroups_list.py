from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_contactgroups_list_kind_item import (
    ApiV1ContactgroupsListKindItem,
)
from ...models.api_v1_contactgroups_list_state import ApiV1ContactgroupsListState
from ...models.api_v1_contactgroups_list_state_not import (
    ApiV1ContactgroupsListStateNot,
)
from ...models.api_v1_contactgroups_list_time_range import (
    ApiV1ContactgroupsListTimeRange,
)
from ...models.paginated_contact_group_list_list import PaginatedContactGroupListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: bool | Unset = UNSET,
    contacts: list[UUID] | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    identity_providers: list[UUID] | Unset = UNSET,
    kind: list[ApiV1ContactgroupsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ContactgroupsListState | Unset = UNSET,
    state_not: ApiV1ContactgroupsListStateNot | Unset = UNSET,
    time_range: ApiV1ContactgroupsListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["archived"] = archived

    json_contacts: list[str] | Unset = UNSET
    if not isinstance(contacts, Unset):
        json_contacts = []
        for contacts_item_data in contacts:
            contacts_item = str(contacts_item_data)
            json_contacts.append(contacts_item)

    params["contacts"] = json_contacts

    json_created_by_users: list[list[int]] | Unset = UNSET
    if not isinstance(created_by_users, Unset):
        json_created_by_users = []
        for created_by_users_item_data in created_by_users:
            created_by_users_item = created_by_users_item_data

            json_created_by_users.append(created_by_users_item)

    params["created_by_users"] = json_created_by_users

    params["has_conditions"] = has_conditions

    json_identity_providers: list[str] | Unset = UNSET
    if not isinstance(identity_providers, Unset):
        json_identity_providers = []
        for identity_providers_item_data in identity_providers:
            identity_providers_item = str(identity_providers_item_data)
            json_identity_providers.append(identity_providers_item)

    params["identity_providers"] = json_identity_providers

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
        "url": "/api/v1/contactgroups/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedContactGroupListList | None:
    if response.status_code == 200:
        response_200 = PaginatedContactGroupListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedContactGroupListList]:
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
    contacts: list[UUID] | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    identity_providers: list[UUID] | Unset = UNSET,
    kind: list[ApiV1ContactgroupsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ContactgroupsListState | Unset = UNSET,
    state_not: ApiV1ContactgroupsListStateNot | Unset = UNSET,
    time_range: ApiV1ContactgroupsListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedContactGroupListList]:
    """API ViewSet for ContactGroups.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        archived (bool | Unset):
        contacts (list[UUID] | Unset):
        created_by_users (list[list[int]] | Unset):
        has_conditions (bool | Unset):
        identity_providers (list[UUID] | Unset):
        kind (list[ApiV1ContactgroupsListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        search (str | Unset):
        state (ApiV1ContactgroupsListState | Unset):
        state_not (ApiV1ContactgroupsListStateNot | Unset):
        time_range (ApiV1ContactgroupsListTimeRange | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedContactGroupListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        contacts=contacts,
        created_by_users=created_by_users,
        has_conditions=has_conditions,
        identity_providers=identity_providers,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
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
    contacts: list[UUID] | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    identity_providers: list[UUID] | Unset = UNSET,
    kind: list[ApiV1ContactgroupsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ContactgroupsListState | Unset = UNSET,
    state_not: ApiV1ContactgroupsListStateNot | Unset = UNSET,
    time_range: ApiV1ContactgroupsListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedContactGroupListList | None:
    """API ViewSet for ContactGroups.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        archived (bool | Unset):
        contacts (list[UUID] | Unset):
        created_by_users (list[list[int]] | Unset):
        has_conditions (bool | Unset):
        identity_providers (list[UUID] | Unset):
        kind (list[ApiV1ContactgroupsListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        search (str | Unset):
        state (ApiV1ContactgroupsListState | Unset):
        state_not (ApiV1ContactgroupsListStateNot | Unset):
        time_range (ApiV1ContactgroupsListTimeRange | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedContactGroupListList
    """

    return sync_detailed(
        client=client,
        archived=archived,
        contacts=contacts,
        created_by_users=created_by_users,
        has_conditions=has_conditions,
        identity_providers=identity_providers,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
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
    contacts: list[UUID] | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    identity_providers: list[UUID] | Unset = UNSET,
    kind: list[ApiV1ContactgroupsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ContactgroupsListState | Unset = UNSET,
    state_not: ApiV1ContactgroupsListStateNot | Unset = UNSET,
    time_range: ApiV1ContactgroupsListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedContactGroupListList]:
    """API ViewSet for ContactGroups.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        archived (bool | Unset):
        contacts (list[UUID] | Unset):
        created_by_users (list[list[int]] | Unset):
        has_conditions (bool | Unset):
        identity_providers (list[UUID] | Unset):
        kind (list[ApiV1ContactgroupsListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        search (str | Unset):
        state (ApiV1ContactgroupsListState | Unset):
        state_not (ApiV1ContactgroupsListStateNot | Unset):
        time_range (ApiV1ContactgroupsListTimeRange | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedContactGroupListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        contacts=contacts,
        created_by_users=created_by_users,
        has_conditions=has_conditions,
        identity_providers=identity_providers,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
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
    contacts: list[UUID] | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    identity_providers: list[UUID] | Unset = UNSET,
    kind: list[ApiV1ContactgroupsListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ContactgroupsListState | Unset = UNSET,
    state_not: ApiV1ContactgroupsListStateNot | Unset = UNSET,
    time_range: ApiV1ContactgroupsListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedContactGroupListList | None:
    """API ViewSet for ContactGroups.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        archived (bool | Unset):
        contacts (list[UUID] | Unset):
        created_by_users (list[list[int]] | Unset):
        has_conditions (bool | Unset):
        identity_providers (list[UUID] | Unset):
        kind (list[ApiV1ContactgroupsListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        search (str | Unset):
        state (ApiV1ContactgroupsListState | Unset):
        state_not (ApiV1ContactgroupsListStateNot | Unset):
        time_range (ApiV1ContactgroupsListTimeRange | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedContactGroupListList
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            contacts=contacts,
            created_by_users=created_by_users,
            has_conditions=has_conditions,
            identity_providers=identity_providers,
            kind=kind,
            name_exact=name_exact,
            ordering=ordering,
            organizations=organizations,
            page=page,
            page_size=page_size,
            platform_service=platform_service,
            search=search,
            state=state,
            state_not=state_not,
            time_range=time_range,
            workspaces=workspaces,
        )
    ).parsed
