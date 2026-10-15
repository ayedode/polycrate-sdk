import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_providers_list_bsi_grundschutz_status import (
    ApiV1ProvidersListBsiGrundschutzStatus,
)
from ...models.api_v1_providers_list_c5_status import ApiV1ProvidersListC5Status
from ...models.api_v1_providers_list_created_by_component import (
    ApiV1ProvidersListCreatedByComponent,
)
from ...models.api_v1_providers_list_iso_27001_status import (
    ApiV1ProvidersListIso27001Status,
)
from ...models.api_v1_providers_list_kind import ApiV1ProvidersListKind
from ...models.api_v1_providers_list_scope import ApiV1ProvidersListScope
from ...models.api_v1_providers_list_scs_iaas_status import (
    ApiV1ProvidersListScsIaasStatus,
)
from ...models.api_v1_providers_list_scs_kaas_status import (
    ApiV1ProvidersListScsKaasStatus,
)
from ...models.api_v1_providers_list_state import ApiV1ProvidersListState
from ...models.paginated_provider_catalog_list import PaginatedProviderCatalogList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    bsi_grundschutz_status: ApiV1ProvidersListBsiGrundschutzStatus | Unset = UNSET,
    c5_status: ApiV1ProvidersListC5Status | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1ProvidersListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    iso27001_status: ApiV1ProvidersListIso27001Status | Unset = UNSET,
    kind: ApiV1ProvidersListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1ProvidersListScope | Unset = UNSET,
    scs_iaas_status: ApiV1ProvidersListScsIaasStatus | Unset = UNSET,
    scs_kaas_status: ApiV1ProvidersListScsKaasStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ProvidersListState | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["active"] = active

    params["archived"] = archived

    json_bsi_grundschutz_status: str | Unset = UNSET
    if not isinstance(bsi_grundschutz_status, Unset):
        json_bsi_grundschutz_status = bsi_grundschutz_status

    params["bsi_grundschutz_status"] = json_bsi_grundschutz_status

    json_c5_status: str | Unset = UNSET
    if not isinstance(c5_status, Unset):
        json_c5_status = c5_status

    params["c5_status"] = json_c5_status

    json_created_at: str | Unset = UNSET
    if not isinstance(created_at, Unset):
        json_created_at = created_at.isoformat()
    params["created_at"] = json_created_at

    json_created_by_component: str | Unset = UNSET
    if not isinstance(created_by_component, Unset):
        json_created_by_component = created_by_component

    params["created_by_component"] = json_created_by_component

    params["debug_mode"] = debug_mode

    json_iso27001_status: str | Unset = UNSET
    if not isinstance(iso27001_status, Unset):
        json_iso27001_status = iso27001_status

    params["iso27001_status"] = json_iso27001_status

    json_kind: str | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind

    params["kind"] = json_kind

    params["name"] = name

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["reconciliation_running"] = reconciliation_running

    json_scope: str | Unset = UNSET
    if not isinstance(scope, Unset):
        json_scope = scope

    params["scope"] = json_scope

    json_scs_iaas_status: str | Unset = UNSET
    if not isinstance(scs_iaas_status, Unset):
        json_scs_iaas_status = scs_iaas_status

    params["scs_iaas_status"] = json_scs_iaas_status

    json_scs_kaas_status: str | Unset = UNSET
    if not isinstance(scs_kaas_status, Unset):
        json_scs_kaas_status = scs_kaas_status

    params["scs_kaas_status"] = json_scs_kaas_status

    params["search"] = search

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    json_updated_at: str | Unset = UNSET
    if not isinstance(updated_at, Unset):
        json_updated_at = updated_at.isoformat()
    params["updated_at"] = json_updated_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/providers/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedProviderCatalogList | None:
    if response.status_code == 200:
        response_200 = PaginatedProviderCatalogList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedProviderCatalogList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    bsi_grundschutz_status: ApiV1ProvidersListBsiGrundschutzStatus | Unset = UNSET,
    c5_status: ApiV1ProvidersListC5Status | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1ProvidersListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    iso27001_status: ApiV1ProvidersListIso27001Status | Unset = UNSET,
    kind: ApiV1ProvidersListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1ProvidersListScope | Unset = UNSET,
    scs_iaas_status: ApiV1ProvidersListScsIaasStatus | Unset = UNSET,
    scs_kaas_status: ApiV1ProvidersListScsKaasStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ProvidersListState | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> Response[PaginatedProviderCatalogList]:
    """API endpoint for Provider CRUD.
    Admin-only, system-level (no org/workspace scope).

    Args:
        active (bool | Unset):
        archived (bool | Unset):
        bsi_grundschutz_status (ApiV1ProvidersListBsiGrundschutzStatus | Unset):
        c5_status (ApiV1ProvidersListC5Status | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1ProvidersListCreatedByComponent | Unset):
        debug_mode (bool | Unset):
        iso27001_status (ApiV1ProvidersListIso27001Status | Unset):
        kind (ApiV1ProvidersListKind | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1ProvidersListScope | Unset):
        scs_iaas_status (ApiV1ProvidersListScsIaasStatus | Unset):
        scs_kaas_status (ApiV1ProvidersListScsKaasStatus | Unset):
        search (str | Unset):
        state (ApiV1ProvidersListState | Unset):
        updated_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedProviderCatalogList]
    """

    kwargs = _get_kwargs(
        active=active,
        archived=archived,
        bsi_grundschutz_status=bsi_grundschutz_status,
        c5_status=c5_status,
        created_at=created_at,
        created_by_component=created_by_component,
        debug_mode=debug_mode,
        iso27001_status=iso27001_status,
        kind=kind,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        reconciliation_running=reconciliation_running,
        scope=scope,
        scs_iaas_status=scs_iaas_status,
        scs_kaas_status=scs_kaas_status,
        search=search,
        state=state,
        updated_at=updated_at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    bsi_grundschutz_status: ApiV1ProvidersListBsiGrundschutzStatus | Unset = UNSET,
    c5_status: ApiV1ProvidersListC5Status | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1ProvidersListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    iso27001_status: ApiV1ProvidersListIso27001Status | Unset = UNSET,
    kind: ApiV1ProvidersListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1ProvidersListScope | Unset = UNSET,
    scs_iaas_status: ApiV1ProvidersListScsIaasStatus | Unset = UNSET,
    scs_kaas_status: ApiV1ProvidersListScsKaasStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ProvidersListState | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> PaginatedProviderCatalogList | None:
    """API endpoint for Provider CRUD.
    Admin-only, system-level (no org/workspace scope).

    Args:
        active (bool | Unset):
        archived (bool | Unset):
        bsi_grundschutz_status (ApiV1ProvidersListBsiGrundschutzStatus | Unset):
        c5_status (ApiV1ProvidersListC5Status | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1ProvidersListCreatedByComponent | Unset):
        debug_mode (bool | Unset):
        iso27001_status (ApiV1ProvidersListIso27001Status | Unset):
        kind (ApiV1ProvidersListKind | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1ProvidersListScope | Unset):
        scs_iaas_status (ApiV1ProvidersListScsIaasStatus | Unset):
        scs_kaas_status (ApiV1ProvidersListScsKaasStatus | Unset):
        search (str | Unset):
        state (ApiV1ProvidersListState | Unset):
        updated_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedProviderCatalogList
    """

    return sync_detailed(
        client=client,
        active=active,
        archived=archived,
        bsi_grundschutz_status=bsi_grundschutz_status,
        c5_status=c5_status,
        created_at=created_at,
        created_by_component=created_by_component,
        debug_mode=debug_mode,
        iso27001_status=iso27001_status,
        kind=kind,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        reconciliation_running=reconciliation_running,
        scope=scope,
        scs_iaas_status=scs_iaas_status,
        scs_kaas_status=scs_kaas_status,
        search=search,
        state=state,
        updated_at=updated_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    bsi_grundschutz_status: ApiV1ProvidersListBsiGrundschutzStatus | Unset = UNSET,
    c5_status: ApiV1ProvidersListC5Status | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1ProvidersListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    iso27001_status: ApiV1ProvidersListIso27001Status | Unset = UNSET,
    kind: ApiV1ProvidersListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1ProvidersListScope | Unset = UNSET,
    scs_iaas_status: ApiV1ProvidersListScsIaasStatus | Unset = UNSET,
    scs_kaas_status: ApiV1ProvidersListScsKaasStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ProvidersListState | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> Response[PaginatedProviderCatalogList]:
    """API endpoint for Provider CRUD.
    Admin-only, system-level (no org/workspace scope).

    Args:
        active (bool | Unset):
        archived (bool | Unset):
        bsi_grundschutz_status (ApiV1ProvidersListBsiGrundschutzStatus | Unset):
        c5_status (ApiV1ProvidersListC5Status | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1ProvidersListCreatedByComponent | Unset):
        debug_mode (bool | Unset):
        iso27001_status (ApiV1ProvidersListIso27001Status | Unset):
        kind (ApiV1ProvidersListKind | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1ProvidersListScope | Unset):
        scs_iaas_status (ApiV1ProvidersListScsIaasStatus | Unset):
        scs_kaas_status (ApiV1ProvidersListScsKaasStatus | Unset):
        search (str | Unset):
        state (ApiV1ProvidersListState | Unset):
        updated_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedProviderCatalogList]
    """

    kwargs = _get_kwargs(
        active=active,
        archived=archived,
        bsi_grundschutz_status=bsi_grundschutz_status,
        c5_status=c5_status,
        created_at=created_at,
        created_by_component=created_by_component,
        debug_mode=debug_mode,
        iso27001_status=iso27001_status,
        kind=kind,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        reconciliation_running=reconciliation_running,
        scope=scope,
        scs_iaas_status=scs_iaas_status,
        scs_kaas_status=scs_kaas_status,
        search=search,
        state=state,
        updated_at=updated_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    bsi_grundschutz_status: ApiV1ProvidersListBsiGrundschutzStatus | Unset = UNSET,
    c5_status: ApiV1ProvidersListC5Status | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1ProvidersListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    iso27001_status: ApiV1ProvidersListIso27001Status | Unset = UNSET,
    kind: ApiV1ProvidersListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1ProvidersListScope | Unset = UNSET,
    scs_iaas_status: ApiV1ProvidersListScsIaasStatus | Unset = UNSET,
    scs_kaas_status: ApiV1ProvidersListScsKaasStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ProvidersListState | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> PaginatedProviderCatalogList | None:
    """API endpoint for Provider CRUD.
    Admin-only, system-level (no org/workspace scope).

    Args:
        active (bool | Unset):
        archived (bool | Unset):
        bsi_grundschutz_status (ApiV1ProvidersListBsiGrundschutzStatus | Unset):
        c5_status (ApiV1ProvidersListC5Status | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1ProvidersListCreatedByComponent | Unset):
        debug_mode (bool | Unset):
        iso27001_status (ApiV1ProvidersListIso27001Status | Unset):
        kind (ApiV1ProvidersListKind | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1ProvidersListScope | Unset):
        scs_iaas_status (ApiV1ProvidersListScsIaasStatus | Unset):
        scs_kaas_status (ApiV1ProvidersListScsKaasStatus | Unset):
        search (str | Unset):
        state (ApiV1ProvidersListState | Unset):
        updated_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedProviderCatalogList
    """

    return (
        await asyncio_detailed(
            client=client,
            active=active,
            archived=archived,
            bsi_grundschutz_status=bsi_grundschutz_status,
            c5_status=c5_status,
            created_at=created_at,
            created_by_component=created_by_component,
            debug_mode=debug_mode,
            iso27001_status=iso27001_status,
            kind=kind,
            name=name,
            ordering=ordering,
            page=page,
            page_size=page_size,
            reconciliation_running=reconciliation_running,
            scope=scope,
            scs_iaas_status=scs_iaas_status,
            scs_kaas_status=scs_kaas_status,
            search=search,
            state=state,
            updated_at=updated_at,
        )
    ).parsed
