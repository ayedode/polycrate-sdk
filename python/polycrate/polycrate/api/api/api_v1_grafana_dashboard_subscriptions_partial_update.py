from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organization_grafana_dashboard_subscription import OrganizationGrafanaDashboardSubscription
from ...models.patched_organization_grafana_dashboard_subscription_request import (
    PatchedOrganizationGrafanaDashboardSubscriptionRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/grafana-dashboard-subscriptions/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedOrganizationGrafanaDashboardSubscriptionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedOrganizationGrafanaDashboardSubscriptionRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedOrganizationGrafanaDashboardSubscriptionRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OrganizationGrafanaDashboardSubscription | None:
    if response.status_code == 200:
        response_200 = OrganizationGrafanaDashboardSubscription.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OrganizationGrafanaDashboardSubscription]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | Unset = UNSET,
) -> Response[OrganizationGrafanaDashboardSubscription]:
    """API ViewSet for managing GrafanaDashboard subscriptions per Organization.

    - GET  /api/v1/organizations/{org_pk}/grafana-dashboard-subscriptions/
    - POST /api/v1/organizations/{org_pk}/grafana-dashboard-subscriptions/
    - PATCH/DELETE /{id}/

    Filtering: ?organization=<id>&dashboard=<id>&enabled=<bool>

    Args:
        id (int):
        body (PatchedOrganizationGrafanaDashboardSubscriptionRequest | Unset): Serializer for
            reading/writing GrafanaDashboard subscriptions of an Organization.

            Create: POST with dashboard (id). revision is optional (null = track latest).
            Update: PATCH enabled / revision only.
        body (PatchedOrganizationGrafanaDashboardSubscriptionRequest | Unset): Serializer for
            reading/writing GrafanaDashboard subscriptions of an Organization.

            Create: POST with dashboard (id). revision is optional (null = track latest).
            Update: PATCH enabled / revision only.
        body (PatchedOrganizationGrafanaDashboardSubscriptionRequest | Unset): Serializer for
            reading/writing GrafanaDashboard subscriptions of an Organization.

            Create: POST with dashboard (id). revision is optional (null = track latest).
            Update: PATCH enabled / revision only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationGrafanaDashboardSubscription]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | Unset = UNSET,
) -> OrganizationGrafanaDashboardSubscription | None:
    """API ViewSet for managing GrafanaDashboard subscriptions per Organization.

    - GET  /api/v1/organizations/{org_pk}/grafana-dashboard-subscriptions/
    - POST /api/v1/organizations/{org_pk}/grafana-dashboard-subscriptions/
    - PATCH/DELETE /{id}/

    Filtering: ?organization=<id>&dashboard=<id>&enabled=<bool>

    Args:
        id (int):
        body (PatchedOrganizationGrafanaDashboardSubscriptionRequest | Unset): Serializer for
            reading/writing GrafanaDashboard subscriptions of an Organization.

            Create: POST with dashboard (id). revision is optional (null = track latest).
            Update: PATCH enabled / revision only.
        body (PatchedOrganizationGrafanaDashboardSubscriptionRequest | Unset): Serializer for
            reading/writing GrafanaDashboard subscriptions of an Organization.

            Create: POST with dashboard (id). revision is optional (null = track latest).
            Update: PATCH enabled / revision only.
        body (PatchedOrganizationGrafanaDashboardSubscriptionRequest | Unset): Serializer for
            reading/writing GrafanaDashboard subscriptions of an Organization.

            Create: POST with dashboard (id). revision is optional (null = track latest).
            Update: PATCH enabled / revision only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrganizationGrafanaDashboardSubscription
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | Unset = UNSET,
) -> Response[OrganizationGrafanaDashboardSubscription]:
    """API ViewSet for managing GrafanaDashboard subscriptions per Organization.

    - GET  /api/v1/organizations/{org_pk}/grafana-dashboard-subscriptions/
    - POST /api/v1/organizations/{org_pk}/grafana-dashboard-subscriptions/
    - PATCH/DELETE /{id}/

    Filtering: ?organization=<id>&dashboard=<id>&enabled=<bool>

    Args:
        id (int):
        body (PatchedOrganizationGrafanaDashboardSubscriptionRequest | Unset): Serializer for
            reading/writing GrafanaDashboard subscriptions of an Organization.

            Create: POST with dashboard (id). revision is optional (null = track latest).
            Update: PATCH enabled / revision only.
        body (PatchedOrganizationGrafanaDashboardSubscriptionRequest | Unset): Serializer for
            reading/writing GrafanaDashboard subscriptions of an Organization.

            Create: POST with dashboard (id). revision is optional (null = track latest).
            Update: PATCH enabled / revision only.
        body (PatchedOrganizationGrafanaDashboardSubscriptionRequest | Unset): Serializer for
            reading/writing GrafanaDashboard subscriptions of an Organization.

            Create: POST with dashboard (id). revision is optional (null = track latest).
            Update: PATCH enabled / revision only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationGrafanaDashboardSubscription]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | PatchedOrganizationGrafanaDashboardSubscriptionRequest
    | Unset = UNSET,
) -> OrganizationGrafanaDashboardSubscription | None:
    """API ViewSet for managing GrafanaDashboard subscriptions per Organization.

    - GET  /api/v1/organizations/{org_pk}/grafana-dashboard-subscriptions/
    - POST /api/v1/organizations/{org_pk}/grafana-dashboard-subscriptions/
    - PATCH/DELETE /{id}/

    Filtering: ?organization=<id>&dashboard=<id>&enabled=<bool>

    Args:
        id (int):
        body (PatchedOrganizationGrafanaDashboardSubscriptionRequest | Unset): Serializer for
            reading/writing GrafanaDashboard subscriptions of an Organization.

            Create: POST with dashboard (id). revision is optional (null = track latest).
            Update: PATCH enabled / revision only.
        body (PatchedOrganizationGrafanaDashboardSubscriptionRequest | Unset): Serializer for
            reading/writing GrafanaDashboard subscriptions of an Organization.

            Create: POST with dashboard (id). revision is optional (null = track latest).
            Update: PATCH enabled / revision only.
        body (PatchedOrganizationGrafanaDashboardSubscriptionRequest | Unset): Serializer for
            reading/writing GrafanaDashboard subscriptions of an Organization.

            Create: POST with dashboard (id). revision is optional (null = track latest).
            Update: PATCH enabled / revision only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrganizationGrafanaDashboardSubscription
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
