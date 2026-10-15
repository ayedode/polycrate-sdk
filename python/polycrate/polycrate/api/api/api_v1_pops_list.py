import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_pops_list_api_type import ApiV1PopsListApiType
from ...models.api_v1_pops_list_bgp_status import ApiV1PopsListBgpStatus
from ...models.api_v1_pops_list_c5_status import ApiV1PopsListC5Status
from ...models.api_v1_pops_list_created_by_component import (
    ApiV1PopsListCreatedByComponent,
)
from ...models.api_v1_pops_list_en_50600_status import (
    ApiV1PopsListEn50600Status,
)
from ...models.api_v1_pops_list_ipv_6_status import ApiV1PopsListIpv6Status
from ...models.api_v1_pops_list_iso_27001_status import (
    ApiV1PopsListIso27001Status,
)
from ...models.api_v1_pops_list_kind import ApiV1PopsListKind
from ...models.api_v1_pops_list_scope import ApiV1PopsListScope
from ...models.api_v1_pops_list_scs_iaas_status import (
    ApiV1PopsListScsIaasStatus,
)
from ...models.api_v1_pops_list_scs_kaas_status import (
    ApiV1PopsListScsKaasStatus,
)
from ...models.api_v1_pops_list_state import ApiV1PopsListState
from ...models.api_v1_pops_list_tier import ApiV1PopsListTier
from ...models.paginated_pop_catalog_list import PaginatedPopCatalogList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    affected_incidents: UUID | Unset = UNSET,
    affected_maintenances: UUID | Unset = UNSET,
    api_type: ApiV1PopsListApiType | Unset = UNSET,
    archived: bool | Unset = UNSET,
    bgp_status: ApiV1PopsListBgpStatus | Unset = UNSET,
    c5_status: ApiV1PopsListC5Status | Unset = UNSET,
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1PopsListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    en50600_status: ApiV1PopsListEn50600Status | Unset = UNSET,
    ipv6_status: ApiV1PopsListIpv6Status | Unset = UNSET,
    iso27001_status: ApiV1PopsListIso27001Status | Unset = UNSET,
    kind: ApiV1PopsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    provider_entity: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1PopsListScope | Unset = UNSET,
    scs_iaas_status: ApiV1PopsListScsIaasStatus | Unset = UNSET,
    scs_kaas_status: ApiV1PopsListScsKaasStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1PopsListState | Unset = UNSET,
    technologies: str | Unset = UNSET,
    tier: ApiV1PopsListTier | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_affected_incidents: str | Unset = UNSET
    if not isinstance(affected_incidents, Unset):
        json_affected_incidents = str(affected_incidents)
    params["affected_incidents"] = json_affected_incidents

    json_affected_maintenances: str | Unset = UNSET
    if not isinstance(affected_maintenances, Unset):
        json_affected_maintenances = str(affected_maintenances)
    params["affected_maintenances"] = json_affected_maintenances

    json_api_type: str | Unset = UNSET
    if not isinstance(api_type, Unset):
        json_api_type = api_type

    params["api_type"] = json_api_type

    params["archived"] = archived

    json_bgp_status: str | Unset = UNSET
    if not isinstance(bgp_status, Unset):
        json_bgp_status = bgp_status

    params["bgp_status"] = json_bgp_status

    json_c5_status: str | Unset = UNSET
    if not isinstance(c5_status, Unset):
        json_c5_status = c5_status

    params["c5_status"] = json_c5_status

    params["city"] = city

    params["country"] = country

    json_created_at: str | Unset = UNSET
    if not isinstance(created_at, Unset):
        json_created_at = created_at.isoformat()
    params["created_at"] = json_created_at

    json_created_by_component: str | Unset = UNSET
    if not isinstance(created_by_component, Unset):
        json_created_by_component = created_by_component

    params["created_by_component"] = json_created_by_component

    params["debug_mode"] = debug_mode

    json_en50600_status: str | Unset = UNSET
    if not isinstance(en50600_status, Unset):
        json_en50600_status = en50600_status

    params["en50600_status"] = json_en50600_status

    json_ipv6_status: str | Unset = UNSET
    if not isinstance(ipv6_status, Unset):
        json_ipv6_status = ipv6_status

    params["ipv6_status"] = json_ipv6_status

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

    json_provider_entity: str | Unset = UNSET
    if not isinstance(provider_entity, Unset):
        json_provider_entity = str(provider_entity)
    params["provider_entity"] = json_provider_entity

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

    params["technologies"] = technologies

    json_tier: str | Unset = UNSET
    if not isinstance(tier, Unset):
        json_tier = tier

    params["tier"] = json_tier

    json_updated_at: str | Unset = UNSET
    if not isinstance(updated_at, Unset):
        json_updated_at = updated_at.isoformat()
    params["updated_at"] = json_updated_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/pops/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedPopCatalogList | None:
    if response.status_code == 200:
        response_200 = PaginatedPopCatalogList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedPopCatalogList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    affected_incidents: UUID | Unset = UNSET,
    affected_maintenances: UUID | Unset = UNSET,
    api_type: ApiV1PopsListApiType | Unset = UNSET,
    archived: bool | Unset = UNSET,
    bgp_status: ApiV1PopsListBgpStatus | Unset = UNSET,
    c5_status: ApiV1PopsListC5Status | Unset = UNSET,
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1PopsListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    en50600_status: ApiV1PopsListEn50600Status | Unset = UNSET,
    ipv6_status: ApiV1PopsListIpv6Status | Unset = UNSET,
    iso27001_status: ApiV1PopsListIso27001Status | Unset = UNSET,
    kind: ApiV1PopsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    provider_entity: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1PopsListScope | Unset = UNSET,
    scs_iaas_status: ApiV1PopsListScsIaasStatus | Unset = UNSET,
    scs_kaas_status: ApiV1PopsListScsKaasStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1PopsListState | Unset = UNSET,
    technologies: str | Unset = UNSET,
    tier: ApiV1PopsListTier | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> Response[PaginatedPopCatalogList]:
    """API endpoint that allows points of presence to be viewed or edited.

    Admin-only resource (global, not org-scoped).
    Archived filter handled by ManagedObjectBaseViewset.

    Args:
        affected_incidents (UUID | Unset):
        affected_maintenances (UUID | Unset):
        api_type (ApiV1PopsListApiType | Unset):
        archived (bool | Unset):
        bgp_status (ApiV1PopsListBgpStatus | Unset):
        c5_status (ApiV1PopsListC5Status | Unset):
        city (str | Unset):
        country (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1PopsListCreatedByComponent | Unset):
        debug_mode (bool | Unset):
        en50600_status (ApiV1PopsListEn50600Status | Unset):
        ipv6_status (ApiV1PopsListIpv6Status | Unset):
        iso27001_status (ApiV1PopsListIso27001Status | Unset):
        kind (ApiV1PopsListKind | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        provider_entity (UUID | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1PopsListScope | Unset):
        scs_iaas_status (ApiV1PopsListScsIaasStatus | Unset):
        scs_kaas_status (ApiV1PopsListScsKaasStatus | Unset):
        search (str | Unset):
        state (ApiV1PopsListState | Unset):
        technologies (str | Unset):
        tier (ApiV1PopsListTier | Unset):
        updated_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPopCatalogList]
    """

    kwargs = _get_kwargs(
        affected_incidents=affected_incidents,
        affected_maintenances=affected_maintenances,
        api_type=api_type,
        archived=archived,
        bgp_status=bgp_status,
        c5_status=c5_status,
        city=city,
        country=country,
        created_at=created_at,
        created_by_component=created_by_component,
        debug_mode=debug_mode,
        en50600_status=en50600_status,
        ipv6_status=ipv6_status,
        iso27001_status=iso27001_status,
        kind=kind,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        provider_entity=provider_entity,
        reconciliation_running=reconciliation_running,
        scope=scope,
        scs_iaas_status=scs_iaas_status,
        scs_kaas_status=scs_kaas_status,
        search=search,
        state=state,
        technologies=technologies,
        tier=tier,
        updated_at=updated_at,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    affected_incidents: UUID | Unset = UNSET,
    affected_maintenances: UUID | Unset = UNSET,
    api_type: ApiV1PopsListApiType | Unset = UNSET,
    archived: bool | Unset = UNSET,
    bgp_status: ApiV1PopsListBgpStatus | Unset = UNSET,
    c5_status: ApiV1PopsListC5Status | Unset = UNSET,
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1PopsListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    en50600_status: ApiV1PopsListEn50600Status | Unset = UNSET,
    ipv6_status: ApiV1PopsListIpv6Status | Unset = UNSET,
    iso27001_status: ApiV1PopsListIso27001Status | Unset = UNSET,
    kind: ApiV1PopsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    provider_entity: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1PopsListScope | Unset = UNSET,
    scs_iaas_status: ApiV1PopsListScsIaasStatus | Unset = UNSET,
    scs_kaas_status: ApiV1PopsListScsKaasStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1PopsListState | Unset = UNSET,
    technologies: str | Unset = UNSET,
    tier: ApiV1PopsListTier | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> PaginatedPopCatalogList | None:
    """API endpoint that allows points of presence to be viewed or edited.

    Admin-only resource (global, not org-scoped).
    Archived filter handled by ManagedObjectBaseViewset.

    Args:
        affected_incidents (UUID | Unset):
        affected_maintenances (UUID | Unset):
        api_type (ApiV1PopsListApiType | Unset):
        archived (bool | Unset):
        bgp_status (ApiV1PopsListBgpStatus | Unset):
        c5_status (ApiV1PopsListC5Status | Unset):
        city (str | Unset):
        country (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1PopsListCreatedByComponent | Unset):
        debug_mode (bool | Unset):
        en50600_status (ApiV1PopsListEn50600Status | Unset):
        ipv6_status (ApiV1PopsListIpv6Status | Unset):
        iso27001_status (ApiV1PopsListIso27001Status | Unset):
        kind (ApiV1PopsListKind | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        provider_entity (UUID | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1PopsListScope | Unset):
        scs_iaas_status (ApiV1PopsListScsIaasStatus | Unset):
        scs_kaas_status (ApiV1PopsListScsKaasStatus | Unset):
        search (str | Unset):
        state (ApiV1PopsListState | Unset):
        technologies (str | Unset):
        tier (ApiV1PopsListTier | Unset):
        updated_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPopCatalogList
    """

    return sync_detailed(
        client=client,
        affected_incidents=affected_incidents,
        affected_maintenances=affected_maintenances,
        api_type=api_type,
        archived=archived,
        bgp_status=bgp_status,
        c5_status=c5_status,
        city=city,
        country=country,
        created_at=created_at,
        created_by_component=created_by_component,
        debug_mode=debug_mode,
        en50600_status=en50600_status,
        ipv6_status=ipv6_status,
        iso27001_status=iso27001_status,
        kind=kind,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        provider_entity=provider_entity,
        reconciliation_running=reconciliation_running,
        scope=scope,
        scs_iaas_status=scs_iaas_status,
        scs_kaas_status=scs_kaas_status,
        search=search,
        state=state,
        technologies=technologies,
        tier=tier,
        updated_at=updated_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    affected_incidents: UUID | Unset = UNSET,
    affected_maintenances: UUID | Unset = UNSET,
    api_type: ApiV1PopsListApiType | Unset = UNSET,
    archived: bool | Unset = UNSET,
    bgp_status: ApiV1PopsListBgpStatus | Unset = UNSET,
    c5_status: ApiV1PopsListC5Status | Unset = UNSET,
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1PopsListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    en50600_status: ApiV1PopsListEn50600Status | Unset = UNSET,
    ipv6_status: ApiV1PopsListIpv6Status | Unset = UNSET,
    iso27001_status: ApiV1PopsListIso27001Status | Unset = UNSET,
    kind: ApiV1PopsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    provider_entity: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1PopsListScope | Unset = UNSET,
    scs_iaas_status: ApiV1PopsListScsIaasStatus | Unset = UNSET,
    scs_kaas_status: ApiV1PopsListScsKaasStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1PopsListState | Unset = UNSET,
    technologies: str | Unset = UNSET,
    tier: ApiV1PopsListTier | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> Response[PaginatedPopCatalogList]:
    """API endpoint that allows points of presence to be viewed or edited.

    Admin-only resource (global, not org-scoped).
    Archived filter handled by ManagedObjectBaseViewset.

    Args:
        affected_incidents (UUID | Unset):
        affected_maintenances (UUID | Unset):
        api_type (ApiV1PopsListApiType | Unset):
        archived (bool | Unset):
        bgp_status (ApiV1PopsListBgpStatus | Unset):
        c5_status (ApiV1PopsListC5Status | Unset):
        city (str | Unset):
        country (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1PopsListCreatedByComponent | Unset):
        debug_mode (bool | Unset):
        en50600_status (ApiV1PopsListEn50600Status | Unset):
        ipv6_status (ApiV1PopsListIpv6Status | Unset):
        iso27001_status (ApiV1PopsListIso27001Status | Unset):
        kind (ApiV1PopsListKind | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        provider_entity (UUID | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1PopsListScope | Unset):
        scs_iaas_status (ApiV1PopsListScsIaasStatus | Unset):
        scs_kaas_status (ApiV1PopsListScsKaasStatus | Unset):
        search (str | Unset):
        state (ApiV1PopsListState | Unset):
        technologies (str | Unset):
        tier (ApiV1PopsListTier | Unset):
        updated_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPopCatalogList]
    """

    kwargs = _get_kwargs(
        affected_incidents=affected_incidents,
        affected_maintenances=affected_maintenances,
        api_type=api_type,
        archived=archived,
        bgp_status=bgp_status,
        c5_status=c5_status,
        city=city,
        country=country,
        created_at=created_at,
        created_by_component=created_by_component,
        debug_mode=debug_mode,
        en50600_status=en50600_status,
        ipv6_status=ipv6_status,
        iso27001_status=iso27001_status,
        kind=kind,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        provider_entity=provider_entity,
        reconciliation_running=reconciliation_running,
        scope=scope,
        scs_iaas_status=scs_iaas_status,
        scs_kaas_status=scs_kaas_status,
        search=search,
        state=state,
        technologies=technologies,
        tier=tier,
        updated_at=updated_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    affected_incidents: UUID | Unset = UNSET,
    affected_maintenances: UUID | Unset = UNSET,
    api_type: ApiV1PopsListApiType | Unset = UNSET,
    archived: bool | Unset = UNSET,
    bgp_status: ApiV1PopsListBgpStatus | Unset = UNSET,
    c5_status: ApiV1PopsListC5Status | Unset = UNSET,
    city: str | Unset = UNSET,
    country: str | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1PopsListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    en50600_status: ApiV1PopsListEn50600Status | Unset = UNSET,
    ipv6_status: ApiV1PopsListIpv6Status | Unset = UNSET,
    iso27001_status: ApiV1PopsListIso27001Status | Unset = UNSET,
    kind: ApiV1PopsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    provider_entity: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1PopsListScope | Unset = UNSET,
    scs_iaas_status: ApiV1PopsListScsIaasStatus | Unset = UNSET,
    scs_kaas_status: ApiV1PopsListScsKaasStatus | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1PopsListState | Unset = UNSET,
    technologies: str | Unset = UNSET,
    tier: ApiV1PopsListTier | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> PaginatedPopCatalogList | None:
    """API endpoint that allows points of presence to be viewed or edited.

    Admin-only resource (global, not org-scoped).
    Archived filter handled by ManagedObjectBaseViewset.

    Args:
        affected_incidents (UUID | Unset):
        affected_maintenances (UUID | Unset):
        api_type (ApiV1PopsListApiType | Unset):
        archived (bool | Unset):
        bgp_status (ApiV1PopsListBgpStatus | Unset):
        c5_status (ApiV1PopsListC5Status | Unset):
        city (str | Unset):
        country (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1PopsListCreatedByComponent | Unset):
        debug_mode (bool | Unset):
        en50600_status (ApiV1PopsListEn50600Status | Unset):
        ipv6_status (ApiV1PopsListIpv6Status | Unset):
        iso27001_status (ApiV1PopsListIso27001Status | Unset):
        kind (ApiV1PopsListKind | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        provider_entity (UUID | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1PopsListScope | Unset):
        scs_iaas_status (ApiV1PopsListScsIaasStatus | Unset):
        scs_kaas_status (ApiV1PopsListScsKaasStatus | Unset):
        search (str | Unset):
        state (ApiV1PopsListState | Unset):
        technologies (str | Unset):
        tier (ApiV1PopsListTier | Unset):
        updated_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPopCatalogList
    """

    return (
        await asyncio_detailed(
            client=client,
            affected_incidents=affected_incidents,
            affected_maintenances=affected_maintenances,
            api_type=api_type,
            archived=archived,
            bgp_status=bgp_status,
            c5_status=c5_status,
            city=city,
            country=country,
            created_at=created_at,
            created_by_component=created_by_component,
            debug_mode=debug_mode,
            en50600_status=en50600_status,
            ipv6_status=ipv6_status,
            iso27001_status=iso27001_status,
            kind=kind,
            name=name,
            ordering=ordering,
            page=page,
            page_size=page_size,
            provider_entity=provider_entity,
            reconciliation_running=reconciliation_running,
            scope=scope,
            scs_iaas_status=scs_iaas_status,
            scs_kaas_status=scs_kaas_status,
            search=search,
            state=state,
            technologies=technologies,
            tier=tier,
            updated_at=updated_at,
        )
    ).parsed
