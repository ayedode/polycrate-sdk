from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backup import Backup
from ...models.backup_request import BackupRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: BackupRequest | BackupRequest | BackupRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/backups/backups/",
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
    if response.status_code == 201:
        response_201 = Backup.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: BackupRequest | BackupRequest | BackupRequest | Unset = UNSET,
) -> Response[Backup]:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
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
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BackupRequest | BackupRequest | BackupRequest | Unset = UNSET,
) -> Backup | None:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
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
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BackupRequest | BackupRequest | BackupRequest | Unset = UNSET,
) -> Response[Backup]:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
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
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BackupRequest | BackupRequest | BackupRequest | Unset = UNSET,
) -> Backup | None:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
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
            client=client,
            body=body,
        )
    ).parsed
