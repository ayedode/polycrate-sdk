from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_router import AlertRouter
from ...models.alert_router_request import AlertRouterRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: AlertRouterRequest | AlertRouterRequest | AlertRouterRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/alertrouters/{id}/ingest/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, AlertRouterRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, AlertRouterRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AlertRouterRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AlertRouter | None:
    if response.status_code == 200:
        response_200 = AlertRouter.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AlertRouter]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: AlertRouterRequest | AlertRouterRequest | AlertRouterRequest | Unset = UNSET,
) -> Response[AlertRouter]:
    """Ingest Grafana webhook and create/update Alerts.

    This endpoint accepts direct Grafana webhook payloads (native format).
    Processes all alerts in the payload, qualifies them, and applies router policy.

    No authentication required for external systems (Grafana).
    Auth/permission short-circuit: get_permissions / get_authenticators (Spec 632).

    Args:
        id (UUID):
        body (AlertRouterRequest | Unset): Detail serializer for AlertRouter.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (AlertRouterRequest | Unset): Detail serializer for AlertRouter.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (AlertRouterRequest | Unset): Detail serializer for AlertRouter.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertRouter]
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
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: AlertRouterRequest | AlertRouterRequest | AlertRouterRequest | Unset = UNSET,
) -> AlertRouter | None:
    """Ingest Grafana webhook and create/update Alerts.

    This endpoint accepts direct Grafana webhook payloads (native format).
    Processes all alerts in the payload, qualifies them, and applies router policy.

    No authentication required for external systems (Grafana).
    Auth/permission short-circuit: get_permissions / get_authenticators (Spec 632).

    Args:
        id (UUID):
        body (AlertRouterRequest | Unset): Detail serializer for AlertRouter.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (AlertRouterRequest | Unset): Detail serializer for AlertRouter.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (AlertRouterRequest | Unset): Detail serializer for AlertRouter.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertRouter
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: AlertRouterRequest | AlertRouterRequest | AlertRouterRequest | Unset = UNSET,
) -> Response[AlertRouter]:
    """Ingest Grafana webhook and create/update Alerts.

    This endpoint accepts direct Grafana webhook payloads (native format).
    Processes all alerts in the payload, qualifies them, and applies router policy.

    No authentication required for external systems (Grafana).
    Auth/permission short-circuit: get_permissions / get_authenticators (Spec 632).

    Args:
        id (UUID):
        body (AlertRouterRequest | Unset): Detail serializer for AlertRouter.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (AlertRouterRequest | Unset): Detail serializer for AlertRouter.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (AlertRouterRequest | Unset): Detail serializer for AlertRouter.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertRouter]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: AlertRouterRequest | AlertRouterRequest | AlertRouterRequest | Unset = UNSET,
) -> AlertRouter | None:
    """Ingest Grafana webhook and create/update Alerts.

    This endpoint accepts direct Grafana webhook payloads (native format).
    Processes all alerts in the payload, qualifies them, and applies router policy.

    No authentication required for external systems (Grafana).
    Auth/permission short-circuit: get_permissions / get_authenticators (Spec 632).

    Args:
        id (UUID):
        body (AlertRouterRequest | Unset): Detail serializer for AlertRouter.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (AlertRouterRequest | Unset): Detail serializer for AlertRouter.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (AlertRouterRequest | Unset): Detail serializer for AlertRouter.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertRouter
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
