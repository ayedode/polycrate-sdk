import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_pricing_quote_apps_list_created_by_component import (
    ApiV1PricingQuoteAppsListCreatedByComponent,
)
from ...models.api_v1_pricing_quote_apps_list_kind import (
    ApiV1PricingQuoteAppsListKind,
)
from ...models.api_v1_pricing_quote_apps_list_scope import (
    ApiV1PricingQuoteAppsListScope,
)
from ...models.api_v1_pricing_quote_apps_list_state import (
    ApiV1PricingQuoteAppsListState,
)
from ...models.paginated_pricing_quote_app_list_list import PaginatedPricingQuoteAppListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1PricingQuoteAppsListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    kind: ApiV1PricingQuoteAppsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    quote_workspace: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1PricingQuoteAppsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1PricingQuoteAppsListState | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
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

    params["debug_mode"] = debug_mode

    json_kind: str | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind

    params["kind"] = json_kind

    params["name"] = name

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    json_quote_workspace: str | Unset = UNSET
    if not isinstance(quote_workspace, Unset):
        json_quote_workspace = str(quote_workspace)
    params["quote_workspace"] = json_quote_workspace

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

    json_updated_at: str | Unset = UNSET
    if not isinstance(updated_at, Unset):
        json_updated_at = updated_at.isoformat()
    params["updated_at"] = json_updated_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/pricing/quote-apps/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedPricingQuoteAppListList | None:
    if response.status_code == 200:
        response_200 = PaginatedPricingQuoteAppListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedPricingQuoteAppListList]:
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
    created_by_component: ApiV1PricingQuoteAppsListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    kind: ApiV1PricingQuoteAppsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    quote_workspace: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1PricingQuoteAppsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1PricingQuoteAppsListState | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> Response[PaginatedPricingQuoteAppListList]:
    """App bookings within a quote workspace. Staff-only.
    Spec: .specs/0.13.0/pricing-business-layer.md

    Args:
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1PricingQuoteAppsListCreatedByComponent | Unset):
        debug_mode (bool | Unset):
        kind (ApiV1PricingQuoteAppsListKind | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        quote_workspace (UUID | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1PricingQuoteAppsListScope | Unset):
        search (str | Unset):
        state (ApiV1PricingQuoteAppsListState | Unset):
        updated_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPricingQuoteAppListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        debug_mode=debug_mode,
        kind=kind,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        quote_workspace=quote_workspace,
        reconciliation_running=reconciliation_running,
        scope=scope,
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
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1PricingQuoteAppsListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    kind: ApiV1PricingQuoteAppsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    quote_workspace: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1PricingQuoteAppsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1PricingQuoteAppsListState | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> PaginatedPricingQuoteAppListList | None:
    """App bookings within a quote workspace. Staff-only.
    Spec: .specs/0.13.0/pricing-business-layer.md

    Args:
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1PricingQuoteAppsListCreatedByComponent | Unset):
        debug_mode (bool | Unset):
        kind (ApiV1PricingQuoteAppsListKind | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        quote_workspace (UUID | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1PricingQuoteAppsListScope | Unset):
        search (str | Unset):
        state (ApiV1PricingQuoteAppsListState | Unset):
        updated_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPricingQuoteAppListList
    """

    return sync_detailed(
        client=client,
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        debug_mode=debug_mode,
        kind=kind,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        quote_workspace=quote_workspace,
        reconciliation_running=reconciliation_running,
        scope=scope,
        search=search,
        state=state,
        updated_at=updated_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1PricingQuoteAppsListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    kind: ApiV1PricingQuoteAppsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    quote_workspace: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1PricingQuoteAppsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1PricingQuoteAppsListState | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> Response[PaginatedPricingQuoteAppListList]:
    """App bookings within a quote workspace. Staff-only.
    Spec: .specs/0.13.0/pricing-business-layer.md

    Args:
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1PricingQuoteAppsListCreatedByComponent | Unset):
        debug_mode (bool | Unset):
        kind (ApiV1PricingQuoteAppsListKind | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        quote_workspace (UUID | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1PricingQuoteAppsListScope | Unset):
        search (str | Unset):
        state (ApiV1PricingQuoteAppsListState | Unset):
        updated_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPricingQuoteAppListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        debug_mode=debug_mode,
        kind=kind,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        quote_workspace=quote_workspace,
        reconciliation_running=reconciliation_running,
        scope=scope,
        search=search,
        state=state,
        updated_at=updated_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1PricingQuoteAppsListCreatedByComponent | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    kind: ApiV1PricingQuoteAppsListKind | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    quote_workspace: UUID | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1PricingQuoteAppsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1PricingQuoteAppsListState | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
) -> PaginatedPricingQuoteAppListList | None:
    """App bookings within a quote workspace. Staff-only.
    Spec: .specs/0.13.0/pricing-business-layer.md

    Args:
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1PricingQuoteAppsListCreatedByComponent | Unset):
        debug_mode (bool | Unset):
        kind (ApiV1PricingQuoteAppsListKind | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        quote_workspace (UUID | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1PricingQuoteAppsListScope | Unset):
        search (str | Unset):
        state (ApiV1PricingQuoteAppsListState | Unset):
        updated_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPricingQuoteAppListList
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            created_at=created_at,
            created_by_component=created_by_component,
            debug_mode=debug_mode,
            kind=kind,
            name=name,
            ordering=ordering,
            page=page,
            page_size=page_size,
            quote_workspace=quote_workspace,
            reconciliation_running=reconciliation_running,
            scope=scope,
            search=search,
            state=state,
            updated_at=updated_at,
        )
    ).parsed
