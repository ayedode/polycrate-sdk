from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backup import Backup
from ...models.backup_request import BackupRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: BackupRequest | BackupRequest | BackupRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/backups/backups/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, BackupRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, BackupRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, BackupRequest):
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
    body: BackupRequest | BackupRequest | BackupRequest | Unset = UNSET,
) -> Response[Backup]:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (BackupRequest): Full serializer for Backup - used for all CRUD operations.

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
        body (BackupRequest): Full serializer for Backup - used for all CRUD operations.

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
        body (BackupRequest): Full serializer for Backup - used for all CRUD operations.

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
    body: BackupRequest | BackupRequest | BackupRequest | Unset = UNSET,
) -> Backup | None:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (BackupRequest): Full serializer for Backup - used for all CRUD operations.

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
        body (BackupRequest): Full serializer for Backup - used for all CRUD operations.

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
        body (BackupRequest): Full serializer for Backup - used for all CRUD operations.

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
    body: BackupRequest | BackupRequest | BackupRequest | Unset = UNSET,
) -> Response[Backup]:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (BackupRequest): Full serializer for Backup - used for all CRUD operations.

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
        body (BackupRequest): Full serializer for Backup - used for all CRUD operations.

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
        body (BackupRequest): Full serializer for Backup - used for all CRUD operations.

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
    body: BackupRequest | BackupRequest | BackupRequest | Unset = UNSET,
) -> Backup | None:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (BackupRequest): Full serializer for Backup - used for all CRUD operations.

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
        body (BackupRequest): Full serializer for Backup - used for all CRUD operations.

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
        body (BackupRequest): Full serializer for Backup - used for all CRUD operations.

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
