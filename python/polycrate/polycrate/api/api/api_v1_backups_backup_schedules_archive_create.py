from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archive_response import ArchiveResponse
from ...models.backup_schedule_request import BackupScheduleRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: BackupScheduleRequest | BackupScheduleRequest | BackupScheduleRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/backups/backup-schedules/{id}/archive/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, BackupScheduleRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, BackupScheduleRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, BackupScheduleRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ArchiveResponse | None:
    if response.status_code == 200:
        response_200 = ArchiveResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ArchiveResponse]:
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
    body: BackupScheduleRequest | BackupScheduleRequest | BackupScheduleRequest | Unset = UNSET,
) -> Response[ArchiveResponse]:
    """Toggle archive state

     POST with {"archive_reason": "..."} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

    Args:
        id (UUID):
        body (BackupScheduleRequest): Full serializer for BackupSchedule - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Konsistent mit BackupSerializer - UUID rein, UUID raus.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.13.0): Name-Validierung hinzugefügt.
            BackupSchedules wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Ursache: Operator sendete Name nur in metadata-Map.
            Operator-Fix: polycrate-cli 0.30.0.
            Siehe: .specs/0.13.0/backupschedule-name-fix.md
        body (BackupScheduleRequest): Full serializer for BackupSchedule - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Konsistent mit BackupSerializer - UUID rein, UUID raus.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.13.0): Name-Validierung hinzugefügt.
            BackupSchedules wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Ursache: Operator sendete Name nur in metadata-Map.
            Operator-Fix: polycrate-cli 0.30.0.
            Siehe: .specs/0.13.0/backupschedule-name-fix.md
        body (BackupScheduleRequest): Full serializer for BackupSchedule - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Konsistent mit BackupSerializer - UUID rein, UUID raus.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.13.0): Name-Validierung hinzugefügt.
            BackupSchedules wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Ursache: Operator sendete Name nur in metadata-Map.
            Operator-Fix: polycrate-cli 0.30.0.
            Siehe: .specs/0.13.0/backupschedule-name-fix.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveResponse]
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
    body: BackupScheduleRequest | BackupScheduleRequest | BackupScheduleRequest | Unset = UNSET,
) -> ArchiveResponse | None:
    """Toggle archive state

     POST with {"archive_reason": "..."} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

    Args:
        id (UUID):
        body (BackupScheduleRequest): Full serializer for BackupSchedule - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Konsistent mit BackupSerializer - UUID rein, UUID raus.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.13.0): Name-Validierung hinzugefügt.
            BackupSchedules wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Ursache: Operator sendete Name nur in metadata-Map.
            Operator-Fix: polycrate-cli 0.30.0.
            Siehe: .specs/0.13.0/backupschedule-name-fix.md
        body (BackupScheduleRequest): Full serializer for BackupSchedule - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Konsistent mit BackupSerializer - UUID rein, UUID raus.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.13.0): Name-Validierung hinzugefügt.
            BackupSchedules wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Ursache: Operator sendete Name nur in metadata-Map.
            Operator-Fix: polycrate-cli 0.30.0.
            Siehe: .specs/0.13.0/backupschedule-name-fix.md
        body (BackupScheduleRequest): Full serializer for BackupSchedule - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Konsistent mit BackupSerializer - UUID rein, UUID raus.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.13.0): Name-Validierung hinzugefügt.
            BackupSchedules wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Ursache: Operator sendete Name nur in metadata-Map.
            Operator-Fix: polycrate-cli 0.30.0.
            Siehe: .specs/0.13.0/backupschedule-name-fix.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveResponse
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
    body: BackupScheduleRequest | BackupScheduleRequest | BackupScheduleRequest | Unset = UNSET,
) -> Response[ArchiveResponse]:
    """Toggle archive state

     POST with {"archive_reason": "..."} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

    Args:
        id (UUID):
        body (BackupScheduleRequest): Full serializer for BackupSchedule - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Konsistent mit BackupSerializer - UUID rein, UUID raus.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.13.0): Name-Validierung hinzugefügt.
            BackupSchedules wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Ursache: Operator sendete Name nur in metadata-Map.
            Operator-Fix: polycrate-cli 0.30.0.
            Siehe: .specs/0.13.0/backupschedule-name-fix.md
        body (BackupScheduleRequest): Full serializer for BackupSchedule - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Konsistent mit BackupSerializer - UUID rein, UUID raus.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.13.0): Name-Validierung hinzugefügt.
            BackupSchedules wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Ursache: Operator sendete Name nur in metadata-Map.
            Operator-Fix: polycrate-cli 0.30.0.
            Siehe: .specs/0.13.0/backupschedule-name-fix.md
        body (BackupScheduleRequest): Full serializer for BackupSchedule - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Konsistent mit BackupSerializer - UUID rein, UUID raus.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.13.0): Name-Validierung hinzugefügt.
            BackupSchedules wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Ursache: Operator sendete Name nur in metadata-Map.
            Operator-Fix: polycrate-cli 0.30.0.
            Siehe: .specs/0.13.0/backupschedule-name-fix.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveResponse]
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
    body: BackupScheduleRequest | BackupScheduleRequest | BackupScheduleRequest | Unset = UNSET,
) -> ArchiveResponse | None:
    """Toggle archive state

     POST with {"archive_reason": "..."} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

    Args:
        id (UUID):
        body (BackupScheduleRequest): Full serializer for BackupSchedule - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Konsistent mit BackupSerializer - UUID rein, UUID raus.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.13.0): Name-Validierung hinzugefügt.
            BackupSchedules wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Ursache: Operator sendete Name nur in metadata-Map.
            Operator-Fix: polycrate-cli 0.30.0.
            Siehe: .specs/0.13.0/backupschedule-name-fix.md
        body (BackupScheduleRequest): Full serializer for BackupSchedule - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Konsistent mit BackupSerializer - UUID rein, UUID raus.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.13.0): Name-Validierung hinzugefügt.
            BackupSchedules wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Ursache: Operator sendete Name nur in metadata-Map.
            Operator-Fix: polycrate-cli 0.30.0.
            Siehe: .specs/0.13.0/backupschedule-name-fix.md
        body (BackupScheduleRequest): Full serializer for BackupSchedule - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Konsistent mit BackupSerializer - UUID rein, UUID raus.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.13.0): Name-Validierung hinzugefügt.
            BackupSchedules wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Ursache: Operator sendete Name nur in metadata-Map.
            Operator-Fix: polycrate-cli 0.30.0.
            Siehe: .specs/0.13.0/backupschedule-name-fix.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
