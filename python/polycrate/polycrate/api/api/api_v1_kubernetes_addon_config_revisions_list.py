import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_kubernetes_addon_config_revisions_list_created_by_component import (
    ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent,
)
from ...models.api_v1_kubernetes_addon_config_revisions_list_kind_item import (
    ApiV1KubernetesAddonConfigRevisionsListKindItem,
)
from ...models.api_v1_kubernetes_addon_config_revisions_list_scope import (
    ApiV1KubernetesAddonConfigRevisionsListScope,
)
from ...models.api_v1_kubernetes_addon_config_revisions_list_state import (
    ApiV1KubernetesAddonConfigRevisionsListState,
)
from ...models.api_v1_kubernetes_addon_config_revisions_list_state_not import (
    ApiV1KubernetesAddonConfigRevisionsListStateNot,
)
from ...models.api_v1_kubernetes_addon_config_revisions_list_time_range import (
    ApiV1KubernetesAddonConfigRevisionsListTimeRange,
)
from ...models.api_v1_kubernetes_addon_config_revisions_list_validation_error import (
    ApiV1KubernetesAddonConfigRevisionsListValidationError,
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
from ...models.paginated_k8s_addon_config_revision_list_list import PaginatedK8SAddonConfigRevisionListList
from ...models.parse_error_response import ParseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    addon: UUID | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1KubernetesAddonConfigRevisionsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1KubernetesAddonConfigRevisionsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1KubernetesAddonConfigRevisionsListState | Unset = UNSET,
    state_not: ApiV1KubernetesAddonConfigRevisionsListStateNot | Unset = UNSET,
    time_range: ApiV1KubernetesAddonConfigRevisionsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_addon: str | Unset = UNSET
    if not isinstance(addon, Unset):
        json_addon = str(addon)
    params["addon"] = json_addon

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

    params["has_conditions"] = has_conditions

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item: str = kind_item_data
            json_kind.append(kind_item)

    params["kind"] = json_kind

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

    params["reconciliation_running"] = reconciliation_running

    json_scope: str | Unset = UNSET
    if not isinstance(scope, Unset):
        json_scope = scope

    params["scope"] = json_scope

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

    json_updated_at: str | Unset = UNSET
    if not isinstance(updated_at, Unset):
        json_updated_at = updated_at.isoformat()
    params["updated_at"] = json_updated_at

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
        "url": "/api/v1/kubernetes/addon-config-revisions/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiV1KubernetesAddonConfigRevisionsListValidationError
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
    | PaginatedK8SAddonConfigRevisionListList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedK8SAddonConfigRevisionListList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(
            data: object,
        ) -> ApiV1KubernetesAddonConfigRevisionsListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_response_400_type_0 = (
                    ApiV1KubernetesAddonConfigRevisionsListValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_response_400_type_1 = (
                ParseErrorResponse.from_dict(data)
            )

            return componentsschemas_api_v1_kubernetes_addon_config_revisions_list_error_response_400_type_1

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
    ApiV1KubernetesAddonConfigRevisionsListValidationError
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
    | PaginatedK8SAddonConfigRevisionListList
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
    addon: UUID | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1KubernetesAddonConfigRevisionsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1KubernetesAddonConfigRevisionsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1KubernetesAddonConfigRevisionsListState | Unset = UNSET,
    state_not: ApiV1KubernetesAddonConfigRevisionsListStateNot | Unset = UNSET,
    time_range: ApiV1KubernetesAddonConfigRevisionsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[
    ApiV1KubernetesAddonConfigRevisionsListValidationError
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
    | PaginatedK8SAddonConfigRevisionListList
]:
    """API endpoint for K8sAddonConfigRevision.
    Mutate: admin via PERMISSION_CONFIG. Spec: polycrate spec inspect 745

    Args:
        addon (UUID | Unset):
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1KubernetesAddonConfigRevisionsListKindItem] | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1KubernetesAddonConfigRevisionsListScope | Unset):
        search (str | Unset):
        state (ApiV1KubernetesAddonConfigRevisionsListState | Unset):
        state_not (ApiV1KubernetesAddonConfigRevisionsListStateNot | Unset):
        time_range (ApiV1KubernetesAddonConfigRevisionsListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        version (str | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1KubernetesAddonConfigRevisionsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedK8SAddonConfigRevisionListList]
    """

    kwargs = _get_kwargs(
        addon=addon,
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        has_conditions=has_conditions,
        kind=kind,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        reconciliation_running=reconciliation_running,
        scope=scope,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        updated_at=updated_at,
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
    addon: UUID | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1KubernetesAddonConfigRevisionsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1KubernetesAddonConfigRevisionsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1KubernetesAddonConfigRevisionsListState | Unset = UNSET,
    state_not: ApiV1KubernetesAddonConfigRevisionsListStateNot | Unset = UNSET,
    time_range: ApiV1KubernetesAddonConfigRevisionsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> (
    ApiV1KubernetesAddonConfigRevisionsListValidationError
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
    | PaginatedK8SAddonConfigRevisionListList
    | None
):
    """API endpoint for K8sAddonConfigRevision.
    Mutate: admin via PERMISSION_CONFIG. Spec: polycrate spec inspect 745

    Args:
        addon (UUID | Unset):
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1KubernetesAddonConfigRevisionsListKindItem] | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1KubernetesAddonConfigRevisionsListScope | Unset):
        search (str | Unset):
        state (ApiV1KubernetesAddonConfigRevisionsListState | Unset):
        state_not (ApiV1KubernetesAddonConfigRevisionsListStateNot | Unset):
        time_range (ApiV1KubernetesAddonConfigRevisionsListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        version (str | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1KubernetesAddonConfigRevisionsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedK8SAddonConfigRevisionListList
    """

    return sync_detailed(
        client=client,
        addon=addon,
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        has_conditions=has_conditions,
        kind=kind,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        reconciliation_running=reconciliation_running,
        scope=scope,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        updated_at=updated_at,
        version=version,
        workspaces=workspaces,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    addon: UUID | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1KubernetesAddonConfigRevisionsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1KubernetesAddonConfigRevisionsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1KubernetesAddonConfigRevisionsListState | Unset = UNSET,
    state_not: ApiV1KubernetesAddonConfigRevisionsListStateNot | Unset = UNSET,
    time_range: ApiV1KubernetesAddonConfigRevisionsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[
    ApiV1KubernetesAddonConfigRevisionsListValidationError
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
    | PaginatedK8SAddonConfigRevisionListList
]:
    """API endpoint for K8sAddonConfigRevision.
    Mutate: admin via PERMISSION_CONFIG. Spec: polycrate spec inspect 745

    Args:
        addon (UUID | Unset):
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1KubernetesAddonConfigRevisionsListKindItem] | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1KubernetesAddonConfigRevisionsListScope | Unset):
        search (str | Unset):
        state (ApiV1KubernetesAddonConfigRevisionsListState | Unset):
        state_not (ApiV1KubernetesAddonConfigRevisionsListStateNot | Unset):
        time_range (ApiV1KubernetesAddonConfigRevisionsListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        version (str | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1KubernetesAddonConfigRevisionsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedK8SAddonConfigRevisionListList]
    """

    kwargs = _get_kwargs(
        addon=addon,
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        has_conditions=has_conditions,
        kind=kind,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        reconciliation_running=reconciliation_running,
        scope=scope,
        search=search,
        state=state,
        state_not=state_not,
        time_range=time_range,
        updated_at=updated_at,
        version=version,
        workspaces=workspaces,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    addon: UUID | Unset = UNSET,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1KubernetesAddonConfigRevisionsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1KubernetesAddonConfigRevisionsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1KubernetesAddonConfigRevisionsListState | Unset = UNSET,
    state_not: ApiV1KubernetesAddonConfigRevisionsListStateNot | Unset = UNSET,
    time_range: ApiV1KubernetesAddonConfigRevisionsListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    version: str | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> (
    ApiV1KubernetesAddonConfigRevisionsListValidationError
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
    | PaginatedK8SAddonConfigRevisionListList
    | None
):
    """API endpoint for K8sAddonConfigRevision.
    Mutate: admin via PERMISSION_CONFIG. Spec: polycrate spec inspect 745

    Args:
        addon (UUID | Unset):
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1KubernetesAddonConfigRevisionsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1KubernetesAddonConfigRevisionsListKindItem] | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1KubernetesAddonConfigRevisionsListScope | Unset):
        search (str | Unset):
        state (ApiV1KubernetesAddonConfigRevisionsListState | Unset):
        state_not (ApiV1KubernetesAddonConfigRevisionsListStateNot | Unset):
        time_range (ApiV1KubernetesAddonConfigRevisionsListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        version (str | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1KubernetesAddonConfigRevisionsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedK8SAddonConfigRevisionListList
    """

    return (
        await asyncio_detailed(
            client=client,
            addon=addon,
            archived=archived,
            created_at=created_at,
            created_by_component=created_by_component,
            created_by_users=created_by_users,
            debug_mode=debug_mode,
            has_conditions=has_conditions,
            kind=kind,
            name=name,
            name_exact=name_exact,
            ordering=ordering,
            organizations=organizations,
            page=page,
            page_size=page_size,
            platform_service=platform_service,
            reconciliation_running=reconciliation_running,
            scope=scope,
            search=search,
            state=state,
            state_not=state_not,
            time_range=time_range,
            updated_at=updated_at,
            version=version,
            workspaces=workspaces,
        )
    ).parsed
