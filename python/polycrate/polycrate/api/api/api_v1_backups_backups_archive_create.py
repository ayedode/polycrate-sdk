from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_backups_backups_archive_create_validation_error import (
    ApiV1BackupsBackupsArchiveCreateValidationError,
)
from ...models.archive_response import ArchiveResponse
from ...models.backup_request import BackupRequest
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
from ...models.parse_error_response import ParseErrorResponse
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: BackupRequest | BackupRequest | BackupRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/backups/backups/{id}/archive/".format(
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


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiV1BackupsBackupsArchiveCreateValidationError
    | ParseErrorResponse
    | ArchiveResponse
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
    | None
):
    if response.status_code == 200:
        response_200 = ArchiveResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1BackupsBackupsArchiveCreateValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_backups_backups_archive_create_error_response_400_type_0 = (
                    ApiV1BackupsBackupsArchiveCreateValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_backups_backups_archive_create_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_backups_backups_archive_create_error_response_400_type_1 = (
                ParseErrorResponse.from_dict(data)
            )

            return componentsschemas_api_v1_backups_backups_archive_create_error_response_400_type_1

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
    ApiV1BackupsBackupsArchiveCreateValidationError
    | ParseErrorResponse
    | ArchiveResponse
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
]:
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
) -> Response[
    ApiV1BackupsBackupsArchiveCreateValidationError
    | ParseErrorResponse
    | ArchiveResponse
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
]:
    r"""Toggle archive state

     POST with {\"archive_reason\": \"...\"} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

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
        Response[ApiV1BackupsBackupsArchiveCreateValidationError | ParseErrorResponse | ArchiveResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502]
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
) -> (
    ApiV1BackupsBackupsArchiveCreateValidationError
    | ParseErrorResponse
    | ArchiveResponse
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
    | None
):
    r"""Toggle archive state

     POST with {\"archive_reason\": \"...\"} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

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
        ApiV1BackupsBackupsArchiveCreateValidationError | ParseErrorResponse | ArchiveResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502
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
) -> Response[
    ApiV1BackupsBackupsArchiveCreateValidationError
    | ParseErrorResponse
    | ArchiveResponse
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
]:
    r"""Toggle archive state

     POST with {\"archive_reason\": \"...\"} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

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
        Response[ApiV1BackupsBackupsArchiveCreateValidationError | ParseErrorResponse | ArchiveResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502]
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
) -> (
    ApiV1BackupsBackupsArchiveCreateValidationError
    | ParseErrorResponse
    | ArchiveResponse
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
    | None
):
    r"""Toggle archive state

     POST with {\"archive_reason\": \"...\"} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

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
        ApiV1BackupsBackupsArchiveCreateValidationError | ParseErrorResponse | ArchiveResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
