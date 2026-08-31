import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_alerts_list_category_item import (
    ApiV1AlertsListCategoryItem,
)
from ...models.api_v1_alerts_list_status import ApiV1AlertsListStatus
from ...models.api_v1_alerts_list_validation_error import ApiV1AlertsListValidationError
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
from ...models.paginated_alert_list_list import PaginatedAlertListList
from ...models.parse_error_response import ParseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    alert_router: UUID | Unset = UNSET,
    category: list[ApiV1AlertsListCategoryItem] | Unset = UNSET,
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


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiV1AlertsListValidationError
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
    | PaginatedAlertListList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedAlertListList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1AlertsListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alerts_list_error_response_400_type_0 = (
                    ApiV1AlertsListValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_alerts_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_alerts_list_error_response_400_type_1 = ParseErrorResponse.from_dict(data)

            return componentsschemas_api_v1_alerts_list_error_response_400_type_1

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
    ApiV1AlertsListValidationError
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
    | PaginatedAlertListList
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
    alert_router: UUID | Unset = UNSET,
    category: list[ApiV1AlertsListCategoryItem] | Unset = UNSET,
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
) -> Response[
    ApiV1AlertsListValidationError
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
    | PaginatedAlertListList
]:
    """API endpoint that allows endpoints to be viewed or edited.

    Args:
        alert_router (UUID | Unset):
        category (list[ApiV1AlertsListCategoryItem] | Unset):
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
        Response[ApiV1AlertsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedAlertListList]
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
    category: list[ApiV1AlertsListCategoryItem] | Unset = UNSET,
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
) -> (
    ApiV1AlertsListValidationError
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
    | PaginatedAlertListList
    | None
):
    """API endpoint that allows endpoints to be viewed or edited.

    Args:
        alert_router (UUID | Unset):
        category (list[ApiV1AlertsListCategoryItem] | Unset):
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
        ApiV1AlertsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedAlertListList
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
    category: list[ApiV1AlertsListCategoryItem] | Unset = UNSET,
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
) -> Response[
    ApiV1AlertsListValidationError
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
    | PaginatedAlertListList
]:
    """API endpoint that allows endpoints to be viewed or edited.

    Args:
        alert_router (UUID | Unset):
        category (list[ApiV1AlertsListCategoryItem] | Unset):
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
        Response[ApiV1AlertsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedAlertListList]
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
    category: list[ApiV1AlertsListCategoryItem] | Unset = UNSET,
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
) -> (
    ApiV1AlertsListValidationError
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
    | PaginatedAlertListList
    | None
):
    """API endpoint that allows endpoints to be viewed or edited.

    Args:
        alert_router (UUID | Unset):
        category (list[ApiV1AlertsListCategoryItem] | Unset):
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
        ApiV1AlertsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedAlertListList
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
