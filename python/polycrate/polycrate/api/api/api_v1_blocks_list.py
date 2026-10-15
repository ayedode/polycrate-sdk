from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_blocks_list_kind_item import ApiV1BlocksListKindItem
from ...models.api_v1_blocks_list_state import ApiV1BlocksListState
from ...models.api_v1_blocks_list_state_not import ApiV1BlocksListStateNot
from ...models.api_v1_blocks_list_time_range import ApiV1BlocksListTimeRange
from ...models.paginated_block_list_list import PaginatedBlockListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: bool | Unset = UNSET,
    artifact_packages: list[UUID] | Unset = UNSET,
    checksum: str | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    from_block: str | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    is_behind_stable: bool | Unset = UNSET,
    kind: list[ApiV1BlocksListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    registry_url: str | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1BlocksListState | Unset = UNSET,
    state_not: ApiV1BlocksListStateNot | Unset = UNSET,
    template: bool | Unset = UNSET,
    template_block: UUID | Unset = UNSET,
    time_range: ApiV1BlocksListTimeRange | Unset = UNSET,
    unique_latest: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["archived"] = archived

    json_artifact_packages: list[str] | Unset = UNSET
    if not isinstance(artifact_packages, Unset):
        json_artifact_packages = []
        for artifact_packages_item_data in artifact_packages:
            artifact_packages_item = str(artifact_packages_item_data)
            json_artifact_packages.append(artifact_packages_item)

    params["artifact_packages"] = json_artifact_packages

    params["checksum"] = checksum

    json_created_by_users: list[list[int]] | Unset = UNSET
    if not isinstance(created_by_users, Unset):
        json_created_by_users = []
        for created_by_users_item_data in created_by_users:
            created_by_users_item = created_by_users_item_data

            json_created_by_users.append(created_by_users_item)

    params["created_by_users"] = json_created_by_users

    params["from_block"] = from_block

    params["has_conditions"] = has_conditions

    params["is_behind_stable"] = is_behind_stable

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

    params["registry_url"] = registry_url

    params["search"] = search

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    json_state_not: str | Unset = UNSET
    if not isinstance(state_not, Unset):
        json_state_not = state_not

    params["state_not"] = json_state_not

    params["template"] = template

    json_template_block: str | Unset = UNSET
    if not isinstance(template_block, Unset):
        json_template_block = str(template_block)
    params["template_block"] = json_template_block

    json_time_range: str | Unset = UNSET
    if not isinstance(time_range, Unset):
        json_time_range = time_range

    params["time_range"] = json_time_range

    params["unique_latest"] = unique_latest

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
        "url": "/api/v1/blocks/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedBlockListList | None:
    if response.status_code == 200:
        response_200 = PaginatedBlockListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedBlockListList]:
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
    artifact_packages: list[UUID] | Unset = UNSET,
    checksum: str | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    from_block: str | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    is_behind_stable: bool | Unset = UNSET,
    kind: list[ApiV1BlocksListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    registry_url: str | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1BlocksListState | Unset = UNSET,
    state_not: ApiV1BlocksListStateNot | Unset = UNSET,
    template: bool | Unset = UNSET,
    template_block: UUID | Unset = UNSET,
    time_range: ApiV1BlocksListTimeRange | Unset = UNSET,
    unique_latest: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedBlockListList]:
    """API endpoint that allows Blocks to be viewed or edited.

    Archived filter, user permissions (workspace-based), and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        archived (bool | Unset):
        artifact_packages (list[UUID] | Unset):
        checksum (str | Unset):
        created_by_users (list[list[int]] | Unset):
        from_block (str | Unset):
        has_conditions (bool | Unset):
        is_behind_stable (bool | Unset):
        kind (list[ApiV1BlocksListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        registry_url (str | Unset):
        search (str | Unset):
        state (ApiV1BlocksListState | Unset):
        state_not (ApiV1BlocksListStateNot | Unset):
        template (bool | Unset):
        template_block (UUID | Unset):
        time_range (ApiV1BlocksListTimeRange | Unset):
        unique_latest (bool | Unset):
        version (str | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedBlockListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        artifact_packages=artifact_packages,
        checksum=checksum,
        created_by_users=created_by_users,
        from_block=from_block,
        has_conditions=has_conditions,
        is_behind_stable=is_behind_stable,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        registry_url=registry_url,
        search=search,
        state=state,
        state_not=state_not,
        template=template,
        template_block=template_block,
        time_range=time_range,
        unique_latest=unique_latest,
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
    artifact_packages: list[UUID] | Unset = UNSET,
    checksum: str | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    from_block: str | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    is_behind_stable: bool | Unset = UNSET,
    kind: list[ApiV1BlocksListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    registry_url: str | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1BlocksListState | Unset = UNSET,
    state_not: ApiV1BlocksListStateNot | Unset = UNSET,
    template: bool | Unset = UNSET,
    template_block: UUID | Unset = UNSET,
    time_range: ApiV1BlocksListTimeRange | Unset = UNSET,
    unique_latest: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedBlockListList | None:
    """API endpoint that allows Blocks to be viewed or edited.

    Archived filter, user permissions (workspace-based), and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        archived (bool | Unset):
        artifact_packages (list[UUID] | Unset):
        checksum (str | Unset):
        created_by_users (list[list[int]] | Unset):
        from_block (str | Unset):
        has_conditions (bool | Unset):
        is_behind_stable (bool | Unset):
        kind (list[ApiV1BlocksListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        registry_url (str | Unset):
        search (str | Unset):
        state (ApiV1BlocksListState | Unset):
        state_not (ApiV1BlocksListStateNot | Unset):
        template (bool | Unset):
        template_block (UUID | Unset):
        time_range (ApiV1BlocksListTimeRange | Unset):
        unique_latest (bool | Unset):
        version (str | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedBlockListList
    """

    return sync_detailed(
        client=client,
        archived=archived,
        artifact_packages=artifact_packages,
        checksum=checksum,
        created_by_users=created_by_users,
        from_block=from_block,
        has_conditions=has_conditions,
        is_behind_stable=is_behind_stable,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        registry_url=registry_url,
        search=search,
        state=state,
        state_not=state_not,
        template=template,
        template_block=template_block,
        time_range=time_range,
        unique_latest=unique_latest,
        version=version,
        workspaces=workspaces,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    artifact_packages: list[UUID] | Unset = UNSET,
    checksum: str | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    from_block: str | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    is_behind_stable: bool | Unset = UNSET,
    kind: list[ApiV1BlocksListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    registry_url: str | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1BlocksListState | Unset = UNSET,
    state_not: ApiV1BlocksListStateNot | Unset = UNSET,
    template: bool | Unset = UNSET,
    template_block: UUID | Unset = UNSET,
    time_range: ApiV1BlocksListTimeRange | Unset = UNSET,
    unique_latest: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[PaginatedBlockListList]:
    """API endpoint that allows Blocks to be viewed or edited.

    Archived filter, user permissions (workspace-based), and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        archived (bool | Unset):
        artifact_packages (list[UUID] | Unset):
        checksum (str | Unset):
        created_by_users (list[list[int]] | Unset):
        from_block (str | Unset):
        has_conditions (bool | Unset):
        is_behind_stable (bool | Unset):
        kind (list[ApiV1BlocksListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        registry_url (str | Unset):
        search (str | Unset):
        state (ApiV1BlocksListState | Unset):
        state_not (ApiV1BlocksListStateNot | Unset):
        template (bool | Unset):
        template_block (UUID | Unset):
        time_range (ApiV1BlocksListTimeRange | Unset):
        unique_latest (bool | Unset):
        version (str | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedBlockListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        artifact_packages=artifact_packages,
        checksum=checksum,
        created_by_users=created_by_users,
        from_block=from_block,
        has_conditions=has_conditions,
        is_behind_stable=is_behind_stable,
        kind=kind,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        registry_url=registry_url,
        search=search,
        state=state,
        state_not=state_not,
        template=template,
        template_block=template_block,
        time_range=time_range,
        unique_latest=unique_latest,
        version=version,
        workspaces=workspaces,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    artifact_packages: list[UUID] | Unset = UNSET,
    checksum: str | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    from_block: str | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    is_behind_stable: bool | Unset = UNSET,
    kind: list[ApiV1BlocksListKindItem] | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    registry_url: str | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1BlocksListState | Unset = UNSET,
    state_not: ApiV1BlocksListStateNot | Unset = UNSET,
    template: bool | Unset = UNSET,
    template_block: UUID | Unset = UNSET,
    time_range: ApiV1BlocksListTimeRange | Unset = UNSET,
    unique_latest: bool | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> PaginatedBlockListList | None:
    """API endpoint that allows Blocks to be viewed or edited.

    Archived filter, user permissions (workspace-based), and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        archived (bool | Unset):
        artifact_packages (list[UUID] | Unset):
        checksum (str | Unset):
        created_by_users (list[list[int]] | Unset):
        from_block (str | Unset):
        has_conditions (bool | Unset):
        is_behind_stable (bool | Unset):
        kind (list[ApiV1BlocksListKindItem] | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        registry_url (str | Unset):
        search (str | Unset):
        state (ApiV1BlocksListState | Unset):
        state_not (ApiV1BlocksListStateNot | Unset):
        template (bool | Unset):
        template_block (UUID | Unset):
        time_range (ApiV1BlocksListTimeRange | Unset):
        unique_latest (bool | Unset):
        version (str | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedBlockListList
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            artifact_packages=artifact_packages,
            checksum=checksum,
            created_by_users=created_by_users,
            from_block=from_block,
            has_conditions=has_conditions,
            is_behind_stable=is_behind_stable,
            kind=kind,
            name_exact=name_exact,
            ordering=ordering,
            organizations=organizations,
            page=page,
            page_size=page_size,
            platform_service=platform_service,
            registry_url=registry_url,
            search=search,
            state=state,
            state_not=state_not,
            template=template,
            template_block=template_block,
            time_range=time_range,
            unique_latest=unique_latest,
            version=version,
            workspaces=workspaces,
        )
    ).parsed
