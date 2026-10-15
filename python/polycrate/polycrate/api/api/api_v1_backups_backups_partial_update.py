from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backup import Backup
from ...models.patched_backup_request import PatchedBackupRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedBackupRequest | PatchedBackupRequest | PatchedBackupRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/backups/backups/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedBackupRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedBackupRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedBackupRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Backup | None:
    if response.status_code == 200:
        response_200 = Backup.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Backup]:
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
    body: PatchedBackupRequest | PatchedBackupRequest | PatchedBackupRequest | Unset = UNSET,
) -> Response[Backup]:
    """API ViewSet for Backups (all providers).

    Architecture (Operator-Driven Discovery):
        Backups werden vom Polycrate Operator im Kubernetes Cluster discovered
        und via API (Create/Update/Delete) synchronisiert. Das entlastet die K8sCluster
        Reconciliation der API erheblich.

        Wenn ein Velero Backup im Cluster gelöscht wird, löscht der Operator
        auch das entsprechende API-Objekt via Finalizer-Cleanup.

    Supported Providers:
        - Velero (cluster, app backups)
        - CloudnativePG (database backups)
        - Custom providers

    Agent Token Support:
        Supports Agent Token authentication with workspace isolation.
        Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅
        Workspace/Organization auto-assigned from Agent Token via ManagedObjectBaseViewset.

        See: .specs/operator-command.md

    Args:
        id (UUID):
        body (PatchedBackupRequest | Unset): Full serializer for Backup - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Der Operator sendet k8s_cluster UUID, aber SerializerMethodField ist read-only.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Das OpenAPI-Schema erwartet UUID, aber to_representation gab Objekt zurück.
            Führte zu Go SDK Unmarshal-Fehler:
                "json: cannot unmarshal object into Go struct field Backup.k8s_cluster of type
            uuid.UUID"
            Jetzt: UUID rein, UUID raus. Konsistent mit Schema.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.11.16): Name-Validierung hinzugefügt.
            Backups wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Siehe: .specs/0.11.16/backup-name-validation.md
        body (PatchedBackupRequest | Unset): Full serializer for Backup - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Der Operator sendet k8s_cluster UUID, aber SerializerMethodField ist read-only.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Das OpenAPI-Schema erwartet UUID, aber to_representation gab Objekt zurück.
            Führte zu Go SDK Unmarshal-Fehler:
                "json: cannot unmarshal object into Go struct field Backup.k8s_cluster of type
            uuid.UUID"
            Jetzt: UUID rein, UUID raus. Konsistent mit Schema.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.11.16): Name-Validierung hinzugefügt.
            Backups wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Siehe: .specs/0.11.16/backup-name-validation.md
        body (PatchedBackupRequest | Unset): Full serializer for Backup - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Der Operator sendet k8s_cluster UUID, aber SerializerMethodField ist read-only.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Das OpenAPI-Schema erwartet UUID, aber to_representation gab Objekt zurück.
            Führte zu Go SDK Unmarshal-Fehler:
                "json: cannot unmarshal object into Go struct field Backup.k8s_cluster of type
            uuid.UUID"
            Jetzt: UUID rein, UUID raus. Konsistent mit Schema.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.11.16): Name-Validierung hinzugefügt.
            Backups wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Siehe: .specs/0.11.16/backup-name-validation.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Backup]
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
    body: PatchedBackupRequest | PatchedBackupRequest | PatchedBackupRequest | Unset = UNSET,
) -> Backup | None:
    """API ViewSet for Backups (all providers).

    Architecture (Operator-Driven Discovery):
        Backups werden vom Polycrate Operator im Kubernetes Cluster discovered
        und via API (Create/Update/Delete) synchronisiert. Das entlastet die K8sCluster
        Reconciliation der API erheblich.

        Wenn ein Velero Backup im Cluster gelöscht wird, löscht der Operator
        auch das entsprechende API-Objekt via Finalizer-Cleanup.

    Supported Providers:
        - Velero (cluster, app backups)
        - CloudnativePG (database backups)
        - Custom providers

    Agent Token Support:
        Supports Agent Token authentication with workspace isolation.
        Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅
        Workspace/Organization auto-assigned from Agent Token via ManagedObjectBaseViewset.

        See: .specs/operator-command.md

    Args:
        id (UUID):
        body (PatchedBackupRequest | Unset): Full serializer for Backup - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Der Operator sendet k8s_cluster UUID, aber SerializerMethodField ist read-only.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Das OpenAPI-Schema erwartet UUID, aber to_representation gab Objekt zurück.
            Führte zu Go SDK Unmarshal-Fehler:
                "json: cannot unmarshal object into Go struct field Backup.k8s_cluster of type
            uuid.UUID"
            Jetzt: UUID rein, UUID raus. Konsistent mit Schema.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.11.16): Name-Validierung hinzugefügt.
            Backups wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Siehe: .specs/0.11.16/backup-name-validation.md
        body (PatchedBackupRequest | Unset): Full serializer for Backup - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Der Operator sendet k8s_cluster UUID, aber SerializerMethodField ist read-only.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Das OpenAPI-Schema erwartet UUID, aber to_representation gab Objekt zurück.
            Führte zu Go SDK Unmarshal-Fehler:
                "json: cannot unmarshal object into Go struct field Backup.k8s_cluster of type
            uuid.UUID"
            Jetzt: UUID rein, UUID raus. Konsistent mit Schema.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.11.16): Name-Validierung hinzugefügt.
            Backups wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Siehe: .specs/0.11.16/backup-name-validation.md
        body (PatchedBackupRequest | Unset): Full serializer for Backup - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Der Operator sendet k8s_cluster UUID, aber SerializerMethodField ist read-only.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Das OpenAPI-Schema erwartet UUID, aber to_representation gab Objekt zurück.
            Führte zu Go SDK Unmarshal-Fehler:
                "json: cannot unmarshal object into Go struct field Backup.k8s_cluster of type
            uuid.UUID"
            Jetzt: UUID rein, UUID raus. Konsistent mit Schema.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.11.16): Name-Validierung hinzugefügt.
            Backups wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Siehe: .specs/0.11.16/backup-name-validation.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Backup
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
    body: PatchedBackupRequest | PatchedBackupRequest | PatchedBackupRequest | Unset = UNSET,
) -> Response[Backup]:
    """API ViewSet for Backups (all providers).

    Architecture (Operator-Driven Discovery):
        Backups werden vom Polycrate Operator im Kubernetes Cluster discovered
        und via API (Create/Update/Delete) synchronisiert. Das entlastet die K8sCluster
        Reconciliation der API erheblich.

        Wenn ein Velero Backup im Cluster gelöscht wird, löscht der Operator
        auch das entsprechende API-Objekt via Finalizer-Cleanup.

    Supported Providers:
        - Velero (cluster, app backups)
        - CloudnativePG (database backups)
        - Custom providers

    Agent Token Support:
        Supports Agent Token authentication with workspace isolation.
        Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅
        Workspace/Organization auto-assigned from Agent Token via ManagedObjectBaseViewset.

        See: .specs/operator-command.md

    Args:
        id (UUID):
        body (PatchedBackupRequest | Unset): Full serializer for Backup - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Der Operator sendet k8s_cluster UUID, aber SerializerMethodField ist read-only.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Das OpenAPI-Schema erwartet UUID, aber to_representation gab Objekt zurück.
            Führte zu Go SDK Unmarshal-Fehler:
                "json: cannot unmarshal object into Go struct field Backup.k8s_cluster of type
            uuid.UUID"
            Jetzt: UUID rein, UUID raus. Konsistent mit Schema.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.11.16): Name-Validierung hinzugefügt.
            Backups wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Siehe: .specs/0.11.16/backup-name-validation.md
        body (PatchedBackupRequest | Unset): Full serializer for Backup - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Der Operator sendet k8s_cluster UUID, aber SerializerMethodField ist read-only.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Das OpenAPI-Schema erwartet UUID, aber to_representation gab Objekt zurück.
            Führte zu Go SDK Unmarshal-Fehler:
                "json: cannot unmarshal object into Go struct field Backup.k8s_cluster of type
            uuid.UUID"
            Jetzt: UUID rein, UUID raus. Konsistent mit Schema.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.11.16): Name-Validierung hinzugefügt.
            Backups wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Siehe: .specs/0.11.16/backup-name-validation.md
        body (PatchedBackupRequest | Unset): Full serializer for Backup - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Der Operator sendet k8s_cluster UUID, aber SerializerMethodField ist read-only.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Das OpenAPI-Schema erwartet UUID, aber to_representation gab Objekt zurück.
            Führte zu Go SDK Unmarshal-Fehler:
                "json: cannot unmarshal object into Go struct field Backup.k8s_cluster of type
            uuid.UUID"
            Jetzt: UUID rein, UUID raus. Konsistent mit Schema.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.11.16): Name-Validierung hinzugefügt.
            Backups wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Siehe: .specs/0.11.16/backup-name-validation.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Backup]
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
    body: PatchedBackupRequest | PatchedBackupRequest | PatchedBackupRequest | Unset = UNSET,
) -> Backup | None:
    """API ViewSet for Backups (all providers).

    Architecture (Operator-Driven Discovery):
        Backups werden vom Polycrate Operator im Kubernetes Cluster discovered
        und via API (Create/Update/Delete) synchronisiert. Das entlastet die K8sCluster
        Reconciliation der API erheblich.

        Wenn ein Velero Backup im Cluster gelöscht wird, löscht der Operator
        auch das entsprechende API-Objekt via Finalizer-Cleanup.

    Supported Providers:
        - Velero (cluster, app backups)
        - CloudnativePG (database backups)
        - Custom providers

    Agent Token Support:
        Supports Agent Token authentication with workspace isolation.
        Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅
        Workspace/Organization auto-assigned from Agent Token via ManagedObjectBaseViewset.

        See: .specs/operator-command.md

    Args:
        id (UUID):
        body (PatchedBackupRequest | Unset): Full serializer for Backup - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Der Operator sendet k8s_cluster UUID, aber SerializerMethodField ist read-only.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Das OpenAPI-Schema erwartet UUID, aber to_representation gab Objekt zurück.
            Führte zu Go SDK Unmarshal-Fehler:
                "json: cannot unmarshal object into Go struct field Backup.k8s_cluster of type
            uuid.UUID"
            Jetzt: UUID rein, UUID raus. Konsistent mit Schema.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.11.16): Name-Validierung hinzugefügt.
            Backups wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Siehe: .specs/0.11.16/backup-name-validation.md
        body (PatchedBackupRequest | Unset): Full serializer for Backup - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Der Operator sendet k8s_cluster UUID, aber SerializerMethodField ist read-only.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Das OpenAPI-Schema erwartet UUID, aber to_representation gab Objekt zurück.
            Führte zu Go SDK Unmarshal-Fehler:
                "json: cannot unmarshal object into Go struct field Backup.k8s_cluster of type
            uuid.UUID"
            Jetzt: UUID rein, UUID raus. Konsistent mit Schema.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.11.16): Name-Validierung hinzugefügt.
            Backups wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Siehe: .specs/0.11.16/backup-name-validation.md
        body (PatchedBackupRequest | Unset): Full serializer for Backup - used for all CRUD
            operations.

            FIX (0.11.8): k8s_cluster als PrimaryKeyRelatedField für write-Operationen.
            Der Operator sendet k8s_cluster UUID, aber SerializerMethodField ist read-only.
            Siehe: .specs/0.11.8/index.md

            FIX (0.11.9): to_representation für k8s_cluster ENTFERNT.
            Das OpenAPI-Schema erwartet UUID, aber to_representation gab Objekt zurück.
            Führte zu Go SDK Unmarshal-Fehler:
                "json: cannot unmarshal object into Go struct field Backup.k8s_cluster of type
            uuid.UUID"
            Jetzt: UUID rein, UUID raus. Konsistent mit Schema.
            Siehe: .specs/0.11.9/backup-k8s-cluster-schema-fix.md

            FIX (0.11.16): Name-Validierung hinzugefügt.
            Backups wurden mit leerem Namen erstellt ("Unnamed" im UI).
            Siehe: .specs/0.11.16/backup-name-validation.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Backup
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
