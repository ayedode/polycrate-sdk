import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_domains_dnsrecords_list_created_by_component import (
    ApiV1DomainsDnsrecordsListCreatedByComponent,
)
from ...models.api_v1_domains_dnsrecords_list_kind_item import (
    ApiV1DomainsDnsrecordsListKindItem,
)
from ...models.api_v1_domains_dnsrecords_list_scope import (
    ApiV1DomainsDnsrecordsListScope,
)
from ...models.api_v1_domains_dnsrecords_list_state import (
    ApiV1DomainsDnsrecordsListState,
)
from ...models.api_v1_domains_dnsrecords_list_state_not import (
    ApiV1DomainsDnsrecordsListStateNot,
)
from ...models.api_v1_domains_dnsrecords_list_time_range import (
    ApiV1DomainsDnsrecordsListTimeRange,
)
from ...models.api_v1_domains_dnsrecords_list_validation_error import ApiV1DomainsDnsrecordsListValidationError
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
from ...models.paginated_dns_record_list_list import PaginatedDNSRecordListList
from ...models.parse_error_response import ParseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1DomainsDnsrecordsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    dns_zone: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1DomainsDnsrecordsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1DomainsDnsrecordsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1DomainsDnsrecordsListState | Unset = UNSET,
    state_not: ApiV1DomainsDnsrecordsListStateNot | Unset = UNSET,
    time_range: ApiV1DomainsDnsrecordsListTimeRange | Unset = UNSET,
    type_: str | Unset = UNSET,
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

    json_dns_zone: str | Unset = UNSET
    if not isinstance(dns_zone, Unset):
        json_dns_zone = str(dns_zone)
    params["dns_zone"] = json_dns_zone

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

    params["type"] = type_

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
        "url": "/api/v1/domains/dnsrecords/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiV1DomainsDnsrecordsListValidationError
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
    | PaginatedDNSRecordListList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedDNSRecordListList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1DomainsDnsrecordsListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnsrecords_list_error_response_400_type_0 = (
                    ApiV1DomainsDnsrecordsListValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnsrecords_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_domains_dnsrecords_list_error_response_400_type_1 = ParseErrorResponse.from_dict(
                data
            )

            return componentsschemas_api_v1_domains_dnsrecords_list_error_response_400_type_1

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
    ApiV1DomainsDnsrecordsListValidationError
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
    | PaginatedDNSRecordListList
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
    created_by_component: ApiV1DomainsDnsrecordsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    dns_zone: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1DomainsDnsrecordsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1DomainsDnsrecordsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1DomainsDnsrecordsListState | Unset = UNSET,
    state_not: ApiV1DomainsDnsrecordsListStateNot | Unset = UNSET,
    time_range: ApiV1DomainsDnsrecordsListTimeRange | Unset = UNSET,
    type_: str | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[
    ApiV1DomainsDnsrecordsListValidationError
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
    | PaginatedDNSRecordListList
]:
    r"""CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind=\"internal\"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind=\"external\"`: records live only at the provider; the API passes
      operations straight through to python-lexicon.

    For external zones, `?dns_zone=<uuid>` is REQUIRED on list, and
    provider-assigned record IDs are used as the detail PK.

    Spec: polycrate spec inspect 137
    Spec 492: Composite ID fix for external records.

    Args:
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1DomainsDnsrecordsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        dns_zone (UUID | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1DomainsDnsrecordsListKindItem] | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1DomainsDnsrecordsListScope | Unset):
        search (str | Unset):
        state (ApiV1DomainsDnsrecordsListState | Unset):
        state_not (ApiV1DomainsDnsrecordsListStateNot | Unset):
        time_range (ApiV1DomainsDnsrecordsListTimeRange | Unset):
        type_ (str | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1DomainsDnsrecordsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedDNSRecordListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        dns_zone=dns_zone,
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
        type_=type_,
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
    created_by_component: ApiV1DomainsDnsrecordsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    dns_zone: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1DomainsDnsrecordsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1DomainsDnsrecordsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1DomainsDnsrecordsListState | Unset = UNSET,
    state_not: ApiV1DomainsDnsrecordsListStateNot | Unset = UNSET,
    time_range: ApiV1DomainsDnsrecordsListTimeRange | Unset = UNSET,
    type_: str | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> (
    ApiV1DomainsDnsrecordsListValidationError
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
    | PaginatedDNSRecordListList
    | None
):
    r"""CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind=\"internal\"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind=\"external\"`: records live only at the provider; the API passes
      operations straight through to python-lexicon.

    For external zones, `?dns_zone=<uuid>` is REQUIRED on list, and
    provider-assigned record IDs are used as the detail PK.

    Spec: polycrate spec inspect 137
    Spec 492: Composite ID fix for external records.

    Args:
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1DomainsDnsrecordsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        dns_zone (UUID | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1DomainsDnsrecordsListKindItem] | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1DomainsDnsrecordsListScope | Unset):
        search (str | Unset):
        state (ApiV1DomainsDnsrecordsListState | Unset):
        state_not (ApiV1DomainsDnsrecordsListStateNot | Unset):
        time_range (ApiV1DomainsDnsrecordsListTimeRange | Unset):
        type_ (str | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1DomainsDnsrecordsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedDNSRecordListList
    """

    return sync_detailed(
        client=client,
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        dns_zone=dns_zone,
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
        type_=type_,
        updated_at=updated_at,
        workspaces=workspaces,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    archived: bool | Unset = UNSET,
    created_at: datetime.datetime | Unset = UNSET,
    created_by_component: ApiV1DomainsDnsrecordsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    dns_zone: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1DomainsDnsrecordsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1DomainsDnsrecordsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1DomainsDnsrecordsListState | Unset = UNSET,
    state_not: ApiV1DomainsDnsrecordsListStateNot | Unset = UNSET,
    time_range: ApiV1DomainsDnsrecordsListTimeRange | Unset = UNSET,
    type_: str | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> Response[
    ApiV1DomainsDnsrecordsListValidationError
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
    | PaginatedDNSRecordListList
]:
    r"""CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind=\"internal\"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind=\"external\"`: records live only at the provider; the API passes
      operations straight through to python-lexicon.

    For external zones, `?dns_zone=<uuid>` is REQUIRED on list, and
    provider-assigned record IDs are used as the detail PK.

    Spec: polycrate spec inspect 137
    Spec 492: Composite ID fix for external records.

    Args:
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1DomainsDnsrecordsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        dns_zone (UUID | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1DomainsDnsrecordsListKindItem] | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1DomainsDnsrecordsListScope | Unset):
        search (str | Unset):
        state (ApiV1DomainsDnsrecordsListState | Unset):
        state_not (ApiV1DomainsDnsrecordsListStateNot | Unset):
        time_range (ApiV1DomainsDnsrecordsListTimeRange | Unset):
        type_ (str | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1DomainsDnsrecordsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedDNSRecordListList]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_at=created_at,
        created_by_component=created_by_component,
        created_by_users=created_by_users,
        debug_mode=debug_mode,
        dns_zone=dns_zone,
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
        type_=type_,
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
    created_by_component: ApiV1DomainsDnsrecordsListCreatedByComponent | Unset = UNSET,
    created_by_users: list[list[int]] | Unset = UNSET,
    debug_mode: bool | Unset = UNSET,
    dns_zone: UUID | Unset = UNSET,
    has_conditions: bool | Unset = UNSET,
    kind: list[ApiV1DomainsDnsrecordsListKindItem] | Unset = UNSET,
    name: str | Unset = UNSET,
    name_exact: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organizations: list[list[UUID]] | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    reconciliation_running: bool | Unset = UNSET,
    scope: ApiV1DomainsDnsrecordsListScope | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1DomainsDnsrecordsListState | Unset = UNSET,
    state_not: ApiV1DomainsDnsrecordsListStateNot | Unset = UNSET,
    time_range: ApiV1DomainsDnsrecordsListTimeRange | Unset = UNSET,
    type_: str | Unset = UNSET,
    updated_at: datetime.datetime | Unset = UNSET,
    workspaces: list[list[UUID]] | Unset = UNSET,
) -> (
    ApiV1DomainsDnsrecordsListValidationError
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
    | PaginatedDNSRecordListList
    | None
):
    r"""CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind=\"internal\"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind=\"external\"`: records live only at the provider; the API passes
      operations straight through to python-lexicon.

    For external zones, `?dns_zone=<uuid>` is REQUIRED on list, and
    provider-assigned record IDs are used as the detail PK.

    Spec: polycrate spec inspect 137
    Spec 492: Composite ID fix for external records.

    Args:
        archived (bool | Unset):
        created_at (datetime.datetime | Unset):
        created_by_component (ApiV1DomainsDnsrecordsListCreatedByComponent | Unset):
        created_by_users (list[list[int]] | Unset):
        debug_mode (bool | Unset):
        dns_zone (UUID | Unset):
        has_conditions (bool | Unset):
        kind (list[ApiV1DomainsDnsrecordsListKindItem] | Unset):
        name (str | Unset):
        name_exact (str | Unset):
        ordering (str | Unset):
        organizations (list[list[UUID]] | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        reconciliation_running (bool | Unset):
        scope (ApiV1DomainsDnsrecordsListScope | Unset):
        search (str | Unset):
        state (ApiV1DomainsDnsrecordsListState | Unset):
        state_not (ApiV1DomainsDnsrecordsListStateNot | Unset):
        time_range (ApiV1DomainsDnsrecordsListTimeRange | Unset):
        type_ (str | Unset):
        updated_at (datetime.datetime | Unset):
        workspaces (list[list[UUID]] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1DomainsDnsrecordsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedDNSRecordListList
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            created_at=created_at,
            created_by_component=created_by_component,
            created_by_users=created_by_users,
            debug_mode=debug_mode,
            dns_zone=dns_zone,
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
            type_=type_,
            updated_at=updated_at,
            workspaces=workspaces,
        )
    ).parsed
