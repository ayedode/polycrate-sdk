import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_kubernetes_volumes_list_created_by_component import (
    ApiV1KubernetesVolumesListCreatedByComponent,
)
from ...models.api_v1_kubernetes_volumes_list_kind_item import (
    ApiV1KubernetesVolumesListKindItem,
)
from ...models.api_v1_kubernetes_volumes_list_phase import (
    ApiV1KubernetesVolumesListPhase,
)
from ...models.api_v1_kubernetes_volumes_list_scope import (
    ApiV1KubernetesVolumesListScope,
)
from ...models.api_v1_kubernetes_volumes_list_state import (
    ApiV1KubernetesVolumesListState,
)
from ...models.api_v1_kubernetes_volumes_list_state_not import (
    ApiV1KubernetesVolumesListStateNot,
)
from ...models.api_v1_kubernetes_volumes_list_time_range import (
    ApiV1KubernetesVolumesListTimeRange,
)
from ...models.api_v1_kubernetes_volumes_list_validation_error import ApiV1KubernetesVolumesListValidationError
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
from ...models.paginated_k8s_volume_list_list import PaginatedK8SVolumeListList
from ...models.parse_error_response import ParseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: bool | Unset = UNSET,
    cloud_provider_volume_id: str | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1KubernetesVolumesListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    csi_driver: str | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    incidents: UUID | Unset = UNSET,
    k8s_app: UUID | Unset = UNSET,
    k8s_cluster: UUID | Unset = UNSET,
    kind: list[ApiV1KubernetesVolumesListKindItem] | Unset = UNSET,
    maintenances: UUID | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    phase: ApiV1KubernetesVolumesListPhase | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1KubernetesVolumesListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1KubernetesVolumesListState | Unset = UNSET,
    state_not: ApiV1KubernetesVolumesListStateNot | Unset = UNSET,
    storage_class: str | Unset = UNSET,
    time_range: ApiV1KubernetesVolumesListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["archived"] = archived

    params["cloud_provider_volume_id"] = cloud_provider_volume_id

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

    params["csi_driver"] = csi_driver

    params["debug_mode"] = debug_mode

    params["has_conditions"] = has_conditions

    json_incidents: str | Unset = UNSET
    if not isinstance(incidents, Unset):
        json_incidents = str(incidents)
    params["incidents"] = json_incidents

    json_k8s_app: str | Unset = UNSET
    if not isinstance(k8s_app, Unset):
        json_k8s_app = str(k8s_app)
    params["k8s_app"] = json_k8s_app

    json_k8s_cluster: str | Unset = UNSET
    if not isinstance(k8s_cluster, Unset):
        json_k8s_cluster = str(k8s_cluster)
    params["k8s_cluster"] = json_k8s_cluster

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item: str = kind_item_data
            json_kind.append(kind_item)

    params["kind"] = json_kind

    json_maintenances: str | Unset = UNSET
    if not isinstance(maintenances, Unset):
        json_maintenances = str(maintenances)
    params["maintenances"] = json_maintenances

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

    json_phase: str | Unset = UNSET
    if not isinstance(phase, Unset):
        json_phase = phase

    params["phase"] = json_phase

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

    params["storage_class"] = storage_class

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
        "url": "/api/v1/kubernetes/volumes/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiV1KubernetesVolumesListValidationError
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
    | PaginatedK8SVolumeListList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedK8SVolumeListList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1KubernetesVolumesListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_volumes_list_error_response_400_type_0 = (
                    ApiV1KubernetesVolumesListValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_volumes_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_kubernetes_volumes_list_error_response_400_type_1 = ParseErrorResponse.from_dict(
                data
            )

            return componentsschemas_api_v1_kubernetes_volumes_list_error_response_400_type_1

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
    ApiV1KubernetesVolumesListValidationError
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
    | PaginatedK8SVolumeListList
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
    cloud_provider_volume_id: str | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1KubernetesVolumesListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    csi_driver: str | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    incidents: UUID | Unset = UNSET,
    k8s_app: UUID | Unset = UNSET,
    k8s_cluster: UUID | Unset = UNSET,
    kind: list[ApiV1KubernetesVolumesListKindItem] | Unset = UNSET,
    maintenances: UUID | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    phase: ApiV1KubernetesVolumesListPhase | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1KubernetesVolumesListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1KubernetesVolumesListState | Unset = UNSET,
    state_not: ApiV1KubernetesVolumesListStateNot | Unset = UNSET,
    storage_class: str | Unset = UNSET,
    time_range: ApiV1KubernetesVolumesListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[
    ApiV1KubernetesVolumesListValidationError
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
    | PaginatedK8SVolumeListList
]:
    """API endpoint for K8sVolume — PersistentVolume tracking.

    Read/Write via Operator Agent Token. No user-facing Create/Delete in UI.
    Spec: polycrate spec inspect 31

    Args:
        archived (bool | Unset):
        cloud_provider_volume_id (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1KubernetesVolumesListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        csi_driver (str | Unset):
        debug_mode (bool | Unset):
        has_conditions (bool | Unset):
        incidents (UUID | Unset):
        k8s_app (UUID | Unset):
        k8s_cluster (UUID | Unset):
        kind (list[ApiV1KubernetesVolumesListKindItem] | Unset):
        maintenances (UUID | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        phase (ApiV1KubernetesVolumesListPhase | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1KubernetesVolumesListScope | Unset):
        search (str | Unset):
        state (ApiV1KubernetesVolumesListState | Unset):
        state_not (ApiV1KubernetesVolumesListStateNot | Unset):
        storage_class (str | Unset):
        time_range (ApiV1KubernetesVolumesListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1KubernetesVolumesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedK8SVolumeListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        cloud_provider_volume_id=cloud_provider_volume_id,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        csi_driver=csi_driver,
        debug_mode=debug_mode,
        has_conditions=has_conditions,
        incidents=incidents,
        k8s_app=k8s_app,
        k8s_cluster=k8s_cluster,
        kind=kind,
        maintenances=maintenances,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        phase=phase,
        platform_service=platform_service,
        reconciliation_running=reconciliation_running,
        scope=scope,
        search=search,
        state=state,
        state_not=state_not,
        storage_class=storage_class,
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
    cloud_provider_volume_id: str | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1KubernetesVolumesListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    csi_driver: str | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    incidents: UUID | Unset = UNSET,
    k8s_app: UUID | Unset = UNSET,
    k8s_cluster: UUID | Unset = UNSET,
    kind: list[ApiV1KubernetesVolumesListKindItem] | Unset = UNSET,
    maintenances: UUID | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    phase: ApiV1KubernetesVolumesListPhase | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1KubernetesVolumesListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1KubernetesVolumesListState | Unset = UNSET,
    state_not: ApiV1KubernetesVolumesListStateNot | Unset = UNSET,
    storage_class: str | Unset = UNSET,
    time_range: ApiV1KubernetesVolumesListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> (
    ApiV1KubernetesVolumesListValidationError
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
    | PaginatedK8SVolumeListList
    | None
):
    """API endpoint for K8sVolume — PersistentVolume tracking.

    Read/Write via Operator Agent Token. No user-facing Create/Delete in UI.
    Spec: polycrate spec inspect 31

    Args:
        archived (bool | Unset):
        cloud_provider_volume_id (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1KubernetesVolumesListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        csi_driver (str | Unset):
        debug_mode (bool | Unset):
        has_conditions (bool | Unset):
        incidents (UUID | Unset):
        k8s_app (UUID | Unset):
        k8s_cluster (UUID | Unset):
        kind (list[ApiV1KubernetesVolumesListKindItem] | Unset):
        maintenances (UUID | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        phase (ApiV1KubernetesVolumesListPhase | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1KubernetesVolumesListScope | Unset):
        search (str | Unset):
        state (ApiV1KubernetesVolumesListState | Unset):
        state_not (ApiV1KubernetesVolumesListStateNot | Unset):
        storage_class (str | Unset):
        time_range (ApiV1KubernetesVolumesListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1KubernetesVolumesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedK8SVolumeListList
    """

    return sync_detailed(
        client=client,
        archived=archived,
        cloud_provider_volume_id=cloud_provider_volume_id,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        csi_driver=csi_driver,
        debug_mode=debug_mode,
        has_conditions=has_conditions,
        incidents=incidents,
        k8s_app=k8s_app,
        k8s_cluster=k8s_cluster,
        kind=kind,
        maintenances=maintenances,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        phase=phase,
        platform_service=platform_service,
        reconciliation_running=reconciliation_running,
        scope=scope,
        search=search,
        state=state,
        state_not=state_not,
        storage_class=storage_class,
        time_range=time_range,
        updated_at=updated_at,
        workspaces=workspaces,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    cloud_provider_volume_id: str | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1KubernetesVolumesListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    csi_driver: str | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    incidents: UUID | Unset = UNSET,
    k8s_app: UUID | Unset = UNSET,
    k8s_cluster: UUID | Unset = UNSET,
    kind: list[ApiV1KubernetesVolumesListKindItem] | Unset = UNSET,
    maintenances: UUID | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    phase: ApiV1KubernetesVolumesListPhase | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1KubernetesVolumesListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1KubernetesVolumesListState | Unset = UNSET,
    state_not: ApiV1KubernetesVolumesListStateNot | Unset = UNSET,
    storage_class: str | Unset = UNSET,
    time_range: ApiV1KubernetesVolumesListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[
    ApiV1KubernetesVolumesListValidationError
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
    | PaginatedK8SVolumeListList
]:
    """API endpoint for K8sVolume — PersistentVolume tracking.

    Read/Write via Operator Agent Token. No user-facing Create/Delete in UI.
    Spec: polycrate spec inspect 31

    Args:
        archived (bool | Unset):
        cloud_provider_volume_id (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1KubernetesVolumesListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        csi_driver (str | Unset):
        debug_mode (bool | Unset):
        has_conditions (bool | Unset):
        incidents (UUID | Unset):
        k8s_app (UUID | Unset):
        k8s_cluster (UUID | Unset):
        kind (list[ApiV1KubernetesVolumesListKindItem] | Unset):
        maintenances (UUID | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        phase (ApiV1KubernetesVolumesListPhase | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1KubernetesVolumesListScope | Unset):
        search (str | Unset):
        state (ApiV1KubernetesVolumesListState | Unset):
        state_not (ApiV1KubernetesVolumesListStateNot | Unset):
        storage_class (str | Unset):
        time_range (ApiV1KubernetesVolumesListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1KubernetesVolumesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedK8SVolumeListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        cloud_provider_volume_id=cloud_provider_volume_id,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        csi_driver=csi_driver,
        debug_mode=debug_mode,
        has_conditions=has_conditions,
        incidents=incidents,
        k8s_app=k8s_app,
        k8s_cluster=k8s_cluster,
        kind=kind,
        maintenances=maintenances,
        name=name,
        name_exact=name_exact,
        ordering=ordering,
        organizations=organizations,
        page=page,
        page_size=page_size,
        phase=phase,
        platform_service=platform_service,
        reconciliation_running=reconciliation_running,
        scope=scope,
        search=search,
        state=state,
        state_not=state_not,
        storage_class=storage_class,
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
    cloud_provider_volume_id: str | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1KubernetesVolumesListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    csi_driver: str | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    incidents: UUID | Unset = UNSET,
    k8s_app: UUID | Unset = UNSET,
    k8s_cluster: UUID | Unset = UNSET,
    kind: list[ApiV1KubernetesVolumesListKindItem] | Unset = UNSET,
    maintenances: UUID | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    phase: ApiV1KubernetesVolumesListPhase | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1KubernetesVolumesListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1KubernetesVolumesListState | Unset = UNSET,
    state_not: ApiV1KubernetesVolumesListStateNot | Unset = UNSET,
    storage_class: str | Unset = UNSET,
    time_range: ApiV1KubernetesVolumesListTimeRange | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> (
    ApiV1KubernetesVolumesListValidationError
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
    | PaginatedK8SVolumeListList
    | None
):
    """API endpoint for K8sVolume — PersistentVolume tracking.

    Read/Write via Operator Agent Token. No user-facing Create/Delete in UI.
    Spec: polycrate spec inspect 31

    Args:
        archived (bool | Unset):
        cloud_provider_volume_id (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1KubernetesVolumesListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        csi_driver (str | Unset):
        debug_mode (bool | Unset):
        has_conditions (bool | Unset):
        incidents (UUID | Unset):
        k8s_app (UUID | Unset):
        k8s_cluster (UUID | Unset):
        kind (list[ApiV1KubernetesVolumesListKindItem] | Unset):
        maintenances (UUID | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        phase (ApiV1KubernetesVolumesListPhase | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1KubernetesVolumesListScope | Unset):
        search (str | Unset):
        state (ApiV1KubernetesVolumesListState | Unset):
        state_not (ApiV1KubernetesVolumesListStateNot | Unset):
        storage_class (str | Unset):
        time_range (ApiV1KubernetesVolumesListTimeRange | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1KubernetesVolumesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedK8SVolumeListList
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            cloud_provider_volume_id=cloud_provider_volume_id,
            created_at=created_at,
            created_by_component=created_by_component,
            created_by_users=created_by_users,
            csi_driver=csi_driver,
            debug_mode=debug_mode,
            has_conditions=has_conditions,
            incidents=incidents,
            k8s_app=k8s_app,
            k8s_cluster=k8s_cluster,
            kind=kind,
            maintenances=maintenances,
            name=name,
            name_exact=name_exact,
            ordering=ordering,
            organizations=organizations,
            page=page,
            page_size=page_size,
            phase=phase,
            platform_service=platform_service,
            reconciliation_running=reconciliation_running,
            scope=scope,
            search=search,
            state=state,
            state_not=state_not,
            storage_class=storage_class,
            time_range=time_range,
            updated_at=updated_at,
            workspaces=workspaces,
        )
    ).parsed
