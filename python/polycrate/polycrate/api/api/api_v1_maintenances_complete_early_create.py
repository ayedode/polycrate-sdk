from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.maintenance import Maintenance
from ...models.maintenance_request import MaintenanceRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: MaintenanceRequest | MaintenanceRequest | MaintenanceRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/maintenances/{id}/complete_early/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, MaintenanceRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MaintenanceRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, MaintenanceRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Maintenance | None:
    if response.status_code == 200:
        response_200 = Maintenance.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Maintenance]:
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
    body: MaintenanceRequest | MaintenanceRequest | MaintenanceRequest | Unset = UNSET,
) -> Response[Maintenance]:
    """Spec 542: End an in-progress, published maintenance immediately (end=now).

    Args:
        id (UUID):
        body (MaintenanceRequest): Full serializer for Maintenance detail view.

            Spec 532: organization nullable (system-wide). Write via organization_id.
            Per .specs/0.12.0/ai-maintenance-detection.md: pop, source_note, source_datasource added
            Per .specs/.next/482-maintenance-embedded-note-content-project-time-tracking.md:
            embedded_note (description, replaces removed `message`) and project (optional,
            propagated to embedded_note.project for time tracking/billing) added.
        body (MaintenanceRequest): Full serializer for Maintenance detail view.

            Spec 532: organization nullable (system-wide). Write via organization_id.
            Per .specs/0.12.0/ai-maintenance-detection.md: pop, source_note, source_datasource added
            Per .specs/.next/482-maintenance-embedded-note-content-project-time-tracking.md:
            embedded_note (description, replaces removed `message`) and project (optional,
            propagated to embedded_note.project for time tracking/billing) added.
        body (MaintenanceRequest): Full serializer for Maintenance detail view.

            Spec 532: organization nullable (system-wide). Write via organization_id.
            Per .specs/0.12.0/ai-maintenance-detection.md: pop, source_note, source_datasource added
            Per .specs/.next/482-maintenance-embedded-note-content-project-time-tracking.md:
            embedded_note (description, replaces removed `message`) and project (optional,
            propagated to embedded_note.project for time tracking/billing) added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Maintenance]
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
    body: MaintenanceRequest | MaintenanceRequest | MaintenanceRequest | Unset = UNSET,
) -> Maintenance | None:
    """Spec 542: End an in-progress, published maintenance immediately (end=now).

    Args:
        id (UUID):
        body (MaintenanceRequest): Full serializer for Maintenance detail view.

            Spec 532: organization nullable (system-wide). Write via organization_id.
            Per .specs/0.12.0/ai-maintenance-detection.md: pop, source_note, source_datasource added
            Per .specs/.next/482-maintenance-embedded-note-content-project-time-tracking.md:
            embedded_note (description, replaces removed `message`) and project (optional,
            propagated to embedded_note.project for time tracking/billing) added.
        body (MaintenanceRequest): Full serializer for Maintenance detail view.

            Spec 532: organization nullable (system-wide). Write via organization_id.
            Per .specs/0.12.0/ai-maintenance-detection.md: pop, source_note, source_datasource added
            Per .specs/.next/482-maintenance-embedded-note-content-project-time-tracking.md:
            embedded_note (description, replaces removed `message`) and project (optional,
            propagated to embedded_note.project for time tracking/billing) added.
        body (MaintenanceRequest): Full serializer for Maintenance detail view.

            Spec 532: organization nullable (system-wide). Write via organization_id.
            Per .specs/0.12.0/ai-maintenance-detection.md: pop, source_note, source_datasource added
            Per .specs/.next/482-maintenance-embedded-note-content-project-time-tracking.md:
            embedded_note (description, replaces removed `message`) and project (optional,
            propagated to embedded_note.project for time tracking/billing) added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Maintenance
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
    body: MaintenanceRequest | MaintenanceRequest | MaintenanceRequest | Unset = UNSET,
) -> Response[Maintenance]:
    """Spec 542: End an in-progress, published maintenance immediately (end=now).

    Args:
        id (UUID):
        body (MaintenanceRequest): Full serializer for Maintenance detail view.

            Spec 532: organization nullable (system-wide). Write via organization_id.
            Per .specs/0.12.0/ai-maintenance-detection.md: pop, source_note, source_datasource added
            Per .specs/.next/482-maintenance-embedded-note-content-project-time-tracking.md:
            embedded_note (description, replaces removed `message`) and project (optional,
            propagated to embedded_note.project for time tracking/billing) added.
        body (MaintenanceRequest): Full serializer for Maintenance detail view.

            Spec 532: organization nullable (system-wide). Write via organization_id.
            Per .specs/0.12.0/ai-maintenance-detection.md: pop, source_note, source_datasource added
            Per .specs/.next/482-maintenance-embedded-note-content-project-time-tracking.md:
            embedded_note (description, replaces removed `message`) and project (optional,
            propagated to embedded_note.project for time tracking/billing) added.
        body (MaintenanceRequest): Full serializer for Maintenance detail view.

            Spec 532: organization nullable (system-wide). Write via organization_id.
            Per .specs/0.12.0/ai-maintenance-detection.md: pop, source_note, source_datasource added
            Per .specs/.next/482-maintenance-embedded-note-content-project-time-tracking.md:
            embedded_note (description, replaces removed `message`) and project (optional,
            propagated to embedded_note.project for time tracking/billing) added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Maintenance]
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
    body: MaintenanceRequest | MaintenanceRequest | MaintenanceRequest | Unset = UNSET,
) -> Maintenance | None:
    """Spec 542: End an in-progress, published maintenance immediately (end=now).

    Args:
        id (UUID):
        body (MaintenanceRequest): Full serializer for Maintenance detail view.

            Spec 532: organization nullable (system-wide). Write via organization_id.
            Per .specs/0.12.0/ai-maintenance-detection.md: pop, source_note, source_datasource added
            Per .specs/.next/482-maintenance-embedded-note-content-project-time-tracking.md:
            embedded_note (description, replaces removed `message`) and project (optional,
            propagated to embedded_note.project for time tracking/billing) added.
        body (MaintenanceRequest): Full serializer for Maintenance detail view.

            Spec 532: organization nullable (system-wide). Write via organization_id.
            Per .specs/0.12.0/ai-maintenance-detection.md: pop, source_note, source_datasource added
            Per .specs/.next/482-maintenance-embedded-note-content-project-time-tracking.md:
            embedded_note (description, replaces removed `message`) and project (optional,
            propagated to embedded_note.project for time tracking/billing) added.
        body (MaintenanceRequest): Full serializer for Maintenance detail view.

            Spec 532: organization nullable (system-wide). Write via organization_id.
            Per .specs/0.12.0/ai-maintenance-detection.md: pop, source_note, source_datasource added
            Per .specs/.next/482-maintenance-embedded-note-content-project-time-tracking.md:
            embedded_note (description, replaces removed `message`) and project (optional,
            propagated to embedded_note.project for time tracking/billing) added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Maintenance
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
