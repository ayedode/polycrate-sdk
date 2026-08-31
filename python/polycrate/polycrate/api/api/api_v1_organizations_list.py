from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_organizations_list_endpoint_monitoring_mode import (
    ApiV1OrganizationsListEndpointMonitoringMode,
)
from ...models.api_v1_organizations_list_kind_item import (
    ApiV1OrganizationsListKindItem,
)
from ...models.api_v1_organizations_list_state import ApiV1OrganizationsListState
from ...models.api_v1_organizations_list_state_not import (
    ApiV1OrganizationsListStateNot,
)
from ...models.api_v1_organizations_list_time_range import (
    ApiV1OrganizationsListTimeRange,
)
from ...models.api_v1_organizations_list_validation_error import ApiV1OrganizationsListValidationError
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
from ...models.paginated_organization_list_list import PaginatedOrganizationListList
from ...models.parse_error_response import ParseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: bool | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    endpoint_monitoring_mode: ApiV1OrganizationsListEndpointMonitoringMode | Unset = UNSET,
    grafana_dashboard: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1OrganizationsListKindItem] | Unset = UNSET,
    legal_name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    priority: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1OrganizationsListState | Unset = UNSET,
    state_not: ApiV1OrganizationsListStateNot | Unset = UNSET,
    time_range: ApiV1OrganizationsListTimeRange | Unset = UNSET,
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

    json_endpoint_monitoring_mode: str | Unset = UNSET
    if not isinstance(endpoint_monitoring_mode, Unset):
        json_endpoint_monitoring_mode = endpoint_monitoring_mode

    params["endpoint_monitoring_mode"] = json_endpoint_monitoring_mode

    json_grafana_dashboard: str | Unset = UNSET
    if not isinstance(grafana_dashboard, Unset):
        json_grafana_dashboard = str(grafana_dashboard)
    params["grafana_dashboard"] = json_grafana_dashboard

    params["has_conditions"] = has_conditions

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item: str = kind_item_data
            json_kind.append(kind_item)

    params["kind"] = json_kind

    params["legal_name"] = legal_name

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

    params["priority"] = priority

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
        "url": "/api/v1/organizations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiV1OrganizationsListValidationError
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
    | PaginatedOrganizationListList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedOrganizationListList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1OrganizationsListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_organizations_list_error_response_400_type_0 = (
                    ApiV1OrganizationsListValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_organizations_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_organizations_list_error_response_400_type_1 = ParseErrorResponse.from_dict(data)

            return componentsschemas_api_v1_organizations_list_error_response_400_type_1

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
    ApiV1OrganizationsListValidationError
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
    | PaginatedOrganizationListList
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
    created_by_users: list[list[int]] | Unset = UNSET,
    endpoint_monitoring_mode: ApiV1OrganizationsListEndpointMonitoringMode | Unset = UNSET,
    grafana_dashboard: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1OrganizationsListKindItem] | Unset = UNSET,
    legal_name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    priority: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1OrganizationsListState | Unset = UNSET,
    state_not: ApiV1OrganizationsListStateNot | Unset = UNSET,
    time_range: ApiV1OrganizationsListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[
    ApiV1OrganizationsListValidationError
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
    | PaginatedOrganizationListList
]:
    """API endpoint that allows organizations to be viewed or edited.

    Archived filter handled by ManagedObjectBaseViewset.
    Custom permission filter: Organizations don't have organization FK,
    filter by membership.

    Args:
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        endpoint_monitoring_mode (ApiV1OrganizationsListEndpointMonitoringMode | Unset):
        grafana_dashboard (UUID | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1OrganizationsListKindItem] | Unset):
        legal_name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        priority (bool | Unset):
        search (str | Unset):
        state (ApiV1OrganizationsListState | Unset):
        state_not (ApiV1OrganizationsListStateNot | Unset):
        time_range (ApiV1OrganizationsListTimeRange | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1OrganizationsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedOrganizationListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_by_users=created_by_users,
        endpoint_monitoring_mode=endpoint_monitoring_mode,
        grafana_dashboard=grafana_dashboard,
        has_conditions=has_conditions,
        kind=kind,
        legal_name=legal_name,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        priority=priority,
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
    created_by_users: list[list[int]] | Unset = UNSET,
    endpoint_monitoring_mode: ApiV1OrganizationsListEndpointMonitoringMode | Unset = UNSET,
    grafana_dashboard: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1OrganizationsListKindItem] | Unset = UNSET,
    legal_name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    priority: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1OrganizationsListState | Unset = UNSET,
    state_not: ApiV1OrganizationsListStateNot | Unset = UNSET,
    time_range: ApiV1OrganizationsListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> (
    ApiV1OrganizationsListValidationError
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
    | PaginatedOrganizationListList
    | None
):
    """API endpoint that allows organizations to be viewed or edited.

    Archived filter handled by ManagedObjectBaseViewset.
    Custom permission filter: Organizations don't have organization FK,
    filter by membership.

    Args:
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        endpoint_monitoring_mode (ApiV1OrganizationsListEndpointMonitoringMode | Unset):
        grafana_dashboard (UUID | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1OrganizationsListKindItem] | Unset):
        legal_name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        priority (bool | Unset):
        search (str | Unset):
        state (ApiV1OrganizationsListState | Unset):
        state_not (ApiV1OrganizationsListStateNot | Unset):
        time_range (ApiV1OrganizationsListTimeRange | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1OrganizationsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedOrganizationListList
    """

    return sync_detailed(
        client=client,
        archived=archived,
        created_by_users=created_by_users,
        endpoint_monitoring_mode=endpoint_monitoring_mode,
        grafana_dashboard=grafana_dashboard,
        has_conditions=has_conditions,
        kind=kind,
        legal_name=legal_name,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        priority=priority,
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
    created_by_users: list[list[int]] | Unset = UNSET,
    endpoint_monitoring_mode: ApiV1OrganizationsListEndpointMonitoringMode | Unset = UNSET,
    grafana_dashboard: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1OrganizationsListKindItem] | Unset = UNSET,
    legal_name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    priority: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1OrganizationsListState | Unset = UNSET,
    state_not: ApiV1OrganizationsListStateNot | Unset = UNSET,
    time_range: ApiV1OrganizationsListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[
    ApiV1OrganizationsListValidationError
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
    | PaginatedOrganizationListList
]:
    """API endpoint that allows organizations to be viewed or edited.

    Archived filter handled by ManagedObjectBaseViewset.
    Custom permission filter: Organizations don't have organization FK,
    filter by membership.

    Args:
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        endpoint_monitoring_mode (ApiV1OrganizationsListEndpointMonitoringMode | Unset):
        grafana_dashboard (UUID | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1OrganizationsListKindItem] | Unset):
        legal_name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        priority (bool | Unset):
        search (str | Unset):
        state (ApiV1OrganizationsListState | Unset):
        state_not (ApiV1OrganizationsListStateNot | Unset):
        time_range (ApiV1OrganizationsListTimeRange | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1OrganizationsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedOrganizationListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_by_users=created_by_users,
        endpoint_monitoring_mode=endpoint_monitoring_mode,
        grafana_dashboard=grafana_dashboard,
        has_conditions=has_conditions,
        kind=kind,
        legal_name=legal_name,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        priority=priority,
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
    created_by_users: list[list[int]] | Unset = UNSET,
    endpoint_monitoring_mode: ApiV1OrganizationsListEndpointMonitoringMode | Unset = UNSET,
    grafana_dashboard: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1OrganizationsListKindItem] | Unset = UNSET,
    legal_name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    priority: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1OrganizationsListState | Unset = UNSET,
    state_not: ApiV1OrganizationsListStateNot | Unset = UNSET,
    time_range: ApiV1OrganizationsListTimeRange | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> (
    ApiV1OrganizationsListValidationError
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
    | PaginatedOrganizationListList
    | None
):
    """API endpoint that allows organizations to be viewed or edited.

    Archived filter handled by ManagedObjectBaseViewset.
    Custom permission filter: Organizations don't have organization FK,
    filter by membership.

    Args:
        archived (bool | Unset):
        created_by_users (list[list[int]] | Unset):
        endpoint_monitoring_mode (ApiV1OrganizationsListEndpointMonitoringMode | Unset):
        grafana_dashboard (UUID | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1OrganizationsListKindItem] | Unset):
        legal_name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        priority (bool | Unset):
        search (str | Unset):
        state (ApiV1OrganizationsListState | Unset):
        state_not (ApiV1OrganizationsListStateNot | Unset):
        time_range (ApiV1OrganizationsListTimeRange | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1OrganizationsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedOrganizationListList
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            created_by_users=created_by_users,
            endpoint_monitoring_mode=endpoint_monitoring_mode,
            grafana_dashboard=grafana_dashboard,
            has_conditions=has_conditions,
            kind=kind,
            legal_name=legal_name,
            name_exact=name_exact,
            ordering=ordering,
            organizations=organizations,
            page=page,
            page_size=page_size,
            platform_service=platform_service,
            priority=priority,
            search=search,
            state=state,
            state_not=state_not,
            time_range=time_range,
            workspaces=workspaces,
        )
    ).parsed
