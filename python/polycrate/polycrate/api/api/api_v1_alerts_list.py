import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_category_slug import AlertCategorySlug
from ...models.api_v1_alerts_list_status import ApiV1AlertsListStatus
from ...models.paginated_alert_list_list import PaginatedAlertListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    alert_router: UUID | Unset = UNSET,
    category: list[AlertCategorySlug] | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
    external_url: str | Unset = UNSET,
    fingerprint: str | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    original_alert_identifier: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    status: ApiV1AlertsListStatus | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    workspace: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_alert_router: str | Unset = UNSET
    if not isinstance(alert_router, Unset):
        json_alert_router = str(alert_router)
    params["alert_router"] = json_alert_router

    json_category: list[str] | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = []
        for category_item_data in category:
            category_item: str = category_item_data
            json_category.append(category_item)

    params["category"] = json_category

    json_created_after: str | Unset = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat()
    params["created_after"] = json_created_after

    json_created_before: str | Unset = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat()
    params["created_before"] = json_created_before

    params["external_url"] = external_url

    params["fingerprint"] = fingerprint

    params["name"] = name

    params["ordering"] = ordering

    json_organization: str | Unset = UNSET
    if not isinstance(organization, Unset):
        json_organization = str(organization)
    params["organization"] = json_organization

    params["original_alert_identifier"] = original_alert_identifier

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_until: str | Unset = UNSET
    if not isinstance(until, Unset):
        json_until = until.isoformat()
    params["until"] = json_until

    json_workspace: str | Unset = UNSET
    if not isinstance(workspace, Unset):
        json_workspace = str(workspace)
    params["workspace"] = json_workspace

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/alerts/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedAlertListList | None:
    if response.status_code == 200:
        response_200 = PaginatedAlertListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedAlertListList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    alert_router: UUID | Unset = UNSET,
    category: list[AlertCategorySlug] | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
    external_url: str | Unset = UNSET,
    fingerprint: str | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    original_alert_identifier: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    status: ApiV1AlertsListStatus | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    workspace: UUID | Unset = UNSET,
) -> Response[PaginatedAlertListList]:
    """API endpoint that allows endpoints to be viewed or edited.

    Args:
        alert_router (UUID | Unset):
        category (list[AlertCategorySlug] | Unset):
        created_after (datetime.datetime | Unset):
        created_before (datetime.datetime | Unset):
        external_url (str | Unset):
        fingerprint (str | Unset):
        name (str | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        original_alert_identifier (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        since (datetime.datetime | Unset):
        status (ApiV1AlertsListStatus | Unset):
        until (datetime.datetime | Unset):
        workspace (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAlertListList]
    """

    kwargs = _get_kwargs(
        alert_router=alert_router,
        category=category,
        created_after=created_after,
        created_before=created_before,
        external_url=external_url,
        fingerprint=fingerprint,
        name=name,
        ordering=ordering,
        organization=organization,
        original_alert_identifier=original_alert_identifier,
        page=page,
        page_size=page_size,
        search=search,
        since=since,
        status=status,
        until=until,
        workspace=workspace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    alert_router: UUID | Unset = UNSET,
    category: list[AlertCategorySlug] | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
    external_url: str | Unset = UNSET,
    fingerprint: str | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    original_alert_identifier: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    status: ApiV1AlertsListStatus | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    workspace: UUID | Unset = UNSET,
) -> PaginatedAlertListList | None:
    """API endpoint that allows endpoints to be viewed or edited.

    Args:
        alert_router (UUID | Unset):
        category (list[AlertCategorySlug] | Unset):
        created_after (datetime.datetime | Unset):
        created_before (datetime.datetime | Unset):
        external_url (str | Unset):
        fingerprint (str | Unset):
        name (str | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        original_alert_identifier (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        since (datetime.datetime | Unset):
        status (ApiV1AlertsListStatus | Unset):
        until (datetime.datetime | Unset):
        workspace (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAlertListList
    """

    return sync_detailed(
        client=client,
        alert_router=alert_router,
        category=category,
        created_after=created_after,
        created_before=created_before,
        external_url=external_url,
        fingerprint=fingerprint,
        name=name,
        ordering=ordering,
        organization=organization,
        original_alert_identifier=original_alert_identifier,
        page=page,
        page_size=page_size,
        search=search,
        since=since,
        status=status,
        until=until,
        workspace=workspace,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    alert_router: UUID | Unset = UNSET,
    category: list[AlertCategorySlug] | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
    external_url: str | Unset = UNSET,
    fingerprint: str | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    original_alert_identifier: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    status: ApiV1AlertsListStatus | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    workspace: UUID | Unset = UNSET,
) -> Response[PaginatedAlertListList]:
    """API endpoint that allows endpoints to be viewed or edited.

    Args:
        alert_router (UUID | Unset):
        category (list[AlertCategorySlug] | Unset):
        created_after (datetime.datetime | Unset):
        created_before (datetime.datetime | Unset):
        external_url (str | Unset):
        fingerprint (str | Unset):
        name (str | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        original_alert_identifier (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        since (datetime.datetime | Unset):
        status (ApiV1AlertsListStatus | Unset):
        until (datetime.datetime | Unset):
        workspace (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAlertListList]
    """

    kwargs = _get_kwargs(
        alert_router=alert_router,
        category=category,
        created_after=created_after,
        created_before=created_before,
        external_url=external_url,
        fingerprint=fingerprint,
        name=name,
        ordering=ordering,
        organization=organization,
        original_alert_identifier=original_alert_identifier,
        page=page,
        page_size=page_size,
        search=search,
        since=since,
        status=status,
        until=until,
        workspace=workspace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    alert_router: UUID | Unset = UNSET,
    category: list[AlertCategorySlug] | Unset = UNSET,
    created_after: datetime.datetime | Unset = UNSET,
    created_before: datetime.datetime | Unset = UNSET,
    external_url: str | Unset = UNSET,
    fingerprint: str | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    original_alert_identifier: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    status: ApiV1AlertsListStatus | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    workspace: UUID | Unset = UNSET,
) -> PaginatedAlertListList | None:
    """API endpoint that allows endpoints to be viewed or edited.

    Args:
        alert_router (UUID | Unset):
        category (list[AlertCategorySlug] | Unset):
        created_after (datetime.datetime | Unset):
        created_before (datetime.datetime | Unset):
        external_url (str | Unset):
        fingerprint (str | Unset):
        name (str | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        original_alert_identifier (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        since (datetime.datetime | Unset):
        status (ApiV1AlertsListStatus | Unset):
        until (datetime.datetime | Unset):
        workspace (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAlertListList
    """

    return (
        await asyncio_detailed(
            client=client,
            alert_router=alert_router,
            category=category,
            created_after=created_after,
            created_before=created_before,
            external_url=external_url,
            fingerprint=fingerprint,
            name=name,
            ordering=ordering,
            organization=organization,
            original_alert_identifier=original_alert_identifier,
            page=page,
            page_size=page_size,
            search=search,
            since=since,
            status=status,
            until=until,
            workspace=workspace,
        )
    ).parsed
