import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_loadbalancers_instances_list_created_by_component import (
    ApiV1LoadbalancersInstancesListCreatedByComponent,
)
from ...models.api_v1_loadbalancers_instances_list_kind_item import (
    ApiV1LoadbalancersInstancesListKindItem,
)
from ...models.api_v1_loadbalancers_instances_list_scope import (
    ApiV1LoadbalancersInstancesListScope,
)
from ...models.api_v1_loadbalancers_instances_list_session_affinity import (
    ApiV1LoadbalancersInstancesListSessionAffinity,
)
from ...models.api_v1_loadbalancers_instances_list_state import (
    ApiV1LoadbalancersInstancesListState,
)
from ...models.api_v1_loadbalancers_instances_list_state_not import (
    ApiV1LoadbalancersInstancesListStateNot,
)
from ...models.api_v1_loadbalancers_instances_list_time_range import (
    ApiV1LoadbalancersInstancesListTimeRange,
)
from ...models.api_v1_loadbalancers_instances_list_validation_error import (
    ApiV1LoadbalancersInstancesListValidationError,
)
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
from ...models.paginated_loadbalancer_instance_list_list import PaginatedLoadbalancerInstanceListList
from ...models.parse_error_response import ParseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1LoadbalancersInstancesListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    enable_ssl: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1LoadbalancersInstancesListKindItem] | Unset = UNSET,
    loadbalancer_region: UUID | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    prefix: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    region: UUID | Unset = UNSET,
    scope: ApiV1LoadbalancersInstancesListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    session_affinity: ApiV1LoadbalancersInstancesListSessionAffinity | Unset = UNSET,
    state: ApiV1LoadbalancersInstancesListState | Unset = UNSET,
    state_not: ApiV1LoadbalancersInstancesListStateNot | Unset = UNSET,
    time_range: ApiV1LoadbalancersInstancesListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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

    params["enable_ssl"] = enable_ssl

    params["has_conditions"] = has_conditions

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item: str = kind_item_data
            json_kind.append(kind_item)

    params["kind"] = json_kind

    json_loadbalancer_region: str | Unset = UNSET
    if not isinstance(loadbalancer_region, Unset):
        json_loadbalancer_region = str(loadbalancer_region)
    params["loadbalancer_region"] = json_loadbalancer_region

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

    json_prefix: str | Unset = UNSET
    if not isinstance(prefix, Unset):
        json_prefix = str(prefix)
    params["prefix"] = json_prefix

    params["reconciliation_running"] = reconciliation_running

    json_region: str | Unset = UNSET
    if not isinstance(region, Unset):
        json_region = str(region)
    params["region"] = json_region

    json_scope: str | Unset = UNSET
    if not isinstance(scope, Unset):
        json_scope = scope

    params["scope"] = json_scope

    params["search"] = search

    json_session_affinity: str | Unset = UNSET
    if not isinstance(session_affinity, Unset):
        json_session_affinity = session_affinity

    params["session_affinity"] = json_session_affinity

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
        "url": "/api/v1/loadbalancers/instances/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiV1LoadbalancersInstancesListValidationError
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
    | PaginatedLoadbalancerInstanceListList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedLoadbalancerInstanceListList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1LoadbalancersInstancesListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_loadbalancers_instances_list_error_response_400_type_0 = (
                    ApiV1LoadbalancersInstancesListValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_loadbalancers_instances_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_loadbalancers_instances_list_error_response_400_type_1 = (
                ParseErrorResponse.from_dict(data)
            )

            return componentsschemas_api_v1_loadbalancers_instances_list_error_response_400_type_1

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
    ApiV1LoadbalancersInstancesListValidationError
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
    | PaginatedLoadbalancerInstanceListList
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
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1LoadbalancersInstancesListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    enable_ssl: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1LoadbalancersInstancesListKindItem] | Unset = UNSET,
    loadbalancer_region: UUID | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    prefix: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    region: UUID | Unset = UNSET,
    scope: ApiV1LoadbalancersInstancesListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    session_affinity: ApiV1LoadbalancersInstancesListSessionAffinity | Unset = UNSET,
    state: ApiV1LoadbalancersInstancesListState | Unset = UNSET,
    state_not: ApiV1LoadbalancersInstancesListStateNot | Unset = UNSET,
    time_range: ApiV1LoadbalancersInstancesListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[
    ApiV1LoadbalancersInstancesListValidationError
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
    | PaginatedLoadbalancerInstanceListList
]:
    """API endpoint that allows LoadBalancer Instances to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1LoadbalancersInstancesListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        enable_ssl (bool | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1LoadbalancersInstancesListKindItem] | Unset):
        loadbalancer_region (UUID | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        prefix (UUID | Unset):
        reconciliation_running (bool | Unset):
        region (UUID | Unset):
        scope (ApiV1LoadbalancersInstancesListScope | Unset):
        search (str | Unset):
        session_affinity (ApiV1LoadbalancersInstancesListSessionAffinity | Unset):
        state (ApiV1LoadbalancersInstancesListState | Unset):
        state_not (ApiV1LoadbalancersInstancesListStateNot | Unset):
        time_range (ApiV1LoadbalancersInstancesListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1LoadbalancersInstancesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedLoadbalancerInstanceListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        enable_ssl=enable_ssl,
        has_conditions=has_conditions,
        kind=kind,
        loadbalancer_region=loadbalancer_region,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        prefix=prefix,
        reconciliation_running=reconciliation_running,
        region=region,
        scope=scope,
        search=search,
        session_affinity=session_affinity,
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
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1LoadbalancersInstancesListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    enable_ssl: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1LoadbalancersInstancesListKindItem] | Unset = UNSET,
    loadbalancer_region: UUID | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    prefix: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    region: UUID | Unset = UNSET,
    scope: ApiV1LoadbalancersInstancesListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    session_affinity: ApiV1LoadbalancersInstancesListSessionAffinity | Unset = UNSET,
    state: ApiV1LoadbalancersInstancesListState | Unset = UNSET,
    state_not: ApiV1LoadbalancersInstancesListStateNot | Unset = UNSET,
    time_range: ApiV1LoadbalancersInstancesListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> (
    ApiV1LoadbalancersInstancesListValidationError
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
    | PaginatedLoadbalancerInstanceListList
    | None
):
    """API endpoint that allows LoadBalancer Instances to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1LoadbalancersInstancesListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        enable_ssl (bool | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1LoadbalancersInstancesListKindItem] | Unset):
        loadbalancer_region (UUID | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        prefix (UUID | Unset):
        reconciliation_running (bool | Unset):
        region (UUID | Unset):
        scope (ApiV1LoadbalancersInstancesListScope | Unset):
        search (str | Unset):
        session_affinity (ApiV1LoadbalancersInstancesListSessionAffinity | Unset):
        state (ApiV1LoadbalancersInstancesListState | Unset):
        state_not (ApiV1LoadbalancersInstancesListStateNot | Unset):
        time_range (ApiV1LoadbalancersInstancesListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1LoadbalancersInstancesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedLoadbalancerInstanceListList
    """

    return sync_detailed(
        client=client,
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        enable_ssl=enable_ssl,
        has_conditions=has_conditions,
        kind=kind,
        loadbalancer_region=loadbalancer_region,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        prefix=prefix,
        reconciliation_running=reconciliation_running,
        region=region,
        scope=scope,
        search=search,
        session_affinity=session_affinity,
        state=state,
        state_not=state_not,
        time_range=time_range,
        updated_at=updated_at,
        workspaces=workspaces,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1LoadbalancersInstancesListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    enable_ssl: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1LoadbalancersInstancesListKindItem] | Unset = UNSET,
    loadbalancer_region: UUID | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    prefix: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    region: UUID | Unset = UNSET,
    scope: ApiV1LoadbalancersInstancesListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    session_affinity: ApiV1LoadbalancersInstancesListSessionAffinity | Unset = UNSET,
    state: ApiV1LoadbalancersInstancesListState | Unset = UNSET,
    state_not: ApiV1LoadbalancersInstancesListStateNot | Unset = UNSET,
    time_range: ApiV1LoadbalancersInstancesListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[
    ApiV1LoadbalancersInstancesListValidationError
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
    | PaginatedLoadbalancerInstanceListList
]:
    """API endpoint that allows LoadBalancer Instances to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1LoadbalancersInstancesListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        enable_ssl (bool | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1LoadbalancersInstancesListKindItem] | Unset):
        loadbalancer_region (UUID | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        prefix (UUID | Unset):
        reconciliation_running (bool | Unset):
        region (UUID | Unset):
        scope (ApiV1LoadbalancersInstancesListScope | Unset):
        search (str | Unset):
        session_affinity (ApiV1LoadbalancersInstancesListSessionAffinity | Unset):
        state (ApiV1LoadbalancersInstancesListState | Unset):
        state_not (ApiV1LoadbalancersInstancesListStateNot | Unset):
        time_range (ApiV1LoadbalancersInstancesListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1LoadbalancersInstancesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedLoadbalancerInstanceListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        enable_ssl=enable_ssl,
        has_conditions=has_conditions,
        kind=kind,
        loadbalancer_region=loadbalancer_region,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        prefix=prefix,
        reconciliation_running=reconciliation_running,
        region=region,
        scope=scope,
        search=search,
        session_affinity=session_affinity,
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
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1LoadbalancersInstancesListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    enable_ssl: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1LoadbalancersInstancesListKindItem] | Unset = UNSET,
    loadbalancer_region: UUID | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    prefix: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    region: UUID | Unset = UNSET,
    scope: ApiV1LoadbalancersInstancesListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    session_affinity: ApiV1LoadbalancersInstancesListSessionAffinity | Unset = UNSET,
    state: ApiV1LoadbalancersInstancesListState | Unset = UNSET,
    state_not: ApiV1LoadbalancersInstancesListStateNot | Unset = UNSET,
    time_range: ApiV1LoadbalancersInstancesListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> (
    ApiV1LoadbalancersInstancesListValidationError
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
    | PaginatedLoadbalancerInstanceListList
    | None
):
    """API endpoint that allows LoadBalancer Instances to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1LoadbalancersInstancesListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        enable_ssl (bool | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1LoadbalancersInstancesListKindItem] | Unset):
        loadbalancer_region (UUID | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        prefix (UUID | Unset):
        reconciliation_running (bool | Unset):
        region (UUID | Unset):
        scope (ApiV1LoadbalancersInstancesListScope | Unset):
        search (str | Unset):
        session_affinity (ApiV1LoadbalancersInstancesListSessionAffinity | Unset):
        state (ApiV1LoadbalancersInstancesListState | Unset):
        state_not (ApiV1LoadbalancersInstancesListStateNot | Unset):
        time_range (ApiV1LoadbalancersInstancesListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1LoadbalancersInstancesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedLoadbalancerInstanceListList
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            created_at=created_at,
            created_by_component=created_by_component,
            created_by_users=created_by_users,
            debug_mode=debug_mode,
            enable_ssl=enable_ssl,
            has_conditions=has_conditions,
            kind=kind,
            loadbalancer_region=loadbalancer_region,
            name=name,
            name_exact=name_exact,
            ordering=ordering,
            organizations=organizations,
            page=page,
            page_size=page_size,
            platform_service=platform_service,
            prefix=prefix,
            reconciliation_running=reconciliation_running,
            region=region,
            scope=scope,
            search=search,
            session_affinity=session_affinity,
            state=state,
            state_not=state_not,
            time_range=time_range,
            updated_at=updated_at,
            workspaces=workspaces,
        )
    ).parsed
