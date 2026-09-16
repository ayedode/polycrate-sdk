from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_incidents_archive_create_validation_error import ApiV1IncidentsArchiveCreateValidationError
from ...models.archive_response import ArchiveResponse
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
from ...models.incident_request import IncidentRequest
from ...models.parse_error_response import ParseErrorResponse
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: IncidentRequest | IncidentRequest | IncidentRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/incidents/{id}/archive/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, IncidentRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, IncidentRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, IncidentRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiV1IncidentsArchiveCreateValidationError
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

        def _parse_response_400(data: object) -> ApiV1IncidentsArchiveCreateValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_incidents_archive_create_error_response_400_type_0 = (
                    ApiV1IncidentsArchiveCreateValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_incidents_archive_create_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_incidents_archive_create_error_response_400_type_1 = ParseErrorResponse.from_dict(
                data
            )

            return componentsschemas_api_v1_incidents_archive_create_error_response_400_type_1

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
    ApiV1IncidentsArchiveCreateValidationError
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
    body: IncidentRequest | IncidentRequest | IncidentRequest | Unset = UNSET,
) -> Response[
    ApiV1IncidentsArchiveCreateValidationError
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
    """Toggle archive state

     POST with {"archive_reason": "..."} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

    Args:
        id (UUID):
        body (IncidentRequest): Full serializer for Incident detail view.

            organization nullable (system-wide). Write via organization_id.
            downtimes is exposed read-only via DowntimeSimpleSerializer; write via downtime_ids.
        body (IncidentRequest): Full serializer for Incident detail view.

            organization nullable (system-wide). Write via organization_id.
            downtimes is exposed read-only via DowntimeSimpleSerializer; write via downtime_ids.
        body (IncidentRequest): Full serializer for Incident detail view.

            organization nullable (system-wide). Write via organization_id.
            downtimes is exposed read-only via DowntimeSimpleSerializer; write via downtime_ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1IncidentsArchiveCreateValidationError | ParseErrorResponse | ArchiveResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502]
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
    body: IncidentRequest | IncidentRequest | IncidentRequest | Unset = UNSET,
) -> (
    ApiV1IncidentsArchiveCreateValidationError
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
    """Toggle archive state

     POST with {"archive_reason": "..."} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

    Args:
        id (UUID):
        body (IncidentRequest): Full serializer for Incident detail view.

            organization nullable (system-wide). Write via organization_id.
            downtimes is exposed read-only via DowntimeSimpleSerializer; write via downtime_ids.
        body (IncidentRequest): Full serializer for Incident detail view.

            organization nullable (system-wide). Write via organization_id.
            downtimes is exposed read-only via DowntimeSimpleSerializer; write via downtime_ids.
        body (IncidentRequest): Full serializer for Incident detail view.

            organization nullable (system-wide). Write via organization_id.
            downtimes is exposed read-only via DowntimeSimpleSerializer; write via downtime_ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1IncidentsArchiveCreateValidationError | ParseErrorResponse | ArchiveResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502
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
    body: IncidentRequest | IncidentRequest | IncidentRequest | Unset = UNSET,
) -> Response[
    ApiV1IncidentsArchiveCreateValidationError
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
    """Toggle archive state

     POST with {"archive_reason": "..."} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

    Args:
        id (UUID):
        body (IncidentRequest): Full serializer for Incident detail view.

            organization nullable (system-wide). Write via organization_id.
            downtimes is exposed read-only via DowntimeSimpleSerializer; write via downtime_ids.
        body (IncidentRequest): Full serializer for Incident detail view.

            organization nullable (system-wide). Write via organization_id.
            downtimes is exposed read-only via DowntimeSimpleSerializer; write via downtime_ids.
        body (IncidentRequest): Full serializer for Incident detail view.

            organization nullable (system-wide). Write via organization_id.
            downtimes is exposed read-only via DowntimeSimpleSerializer; write via downtime_ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1IncidentsArchiveCreateValidationError | ParseErrorResponse | ArchiveResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502]
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
    body: IncidentRequest | IncidentRequest | IncidentRequest | Unset = UNSET,
) -> (
    ApiV1IncidentsArchiveCreateValidationError
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
    """Toggle archive state

     POST with {"archive_reason": "..."} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

    Args:
        id (UUID):
        body (IncidentRequest): Full serializer for Incident detail view.

            organization nullable (system-wide). Write via organization_id.
            downtimes is exposed read-only via DowntimeSimpleSerializer; write via downtime_ids.
        body (IncidentRequest): Full serializer for Incident detail view.

            organization nullable (system-wide). Write via organization_id.
            downtimes is exposed read-only via DowntimeSimpleSerializer; write via downtime_ids.
        body (IncidentRequest): Full serializer for Incident detail view.

            organization nullable (system-wide). Write via organization_id.
            downtimes is exposed read-only via DowntimeSimpleSerializer; write via downtime_ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1IncidentsArchiveCreateValidationError | ParseErrorResponse | ArchiveResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
