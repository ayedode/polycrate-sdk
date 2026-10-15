from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.certificate import Certificate
from ...models.patched_certificate_request import PatchedCertificateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedCertificateRequest | PatchedCertificateRequest | PatchedCertificateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/certificates/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedCertificateRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedCertificateRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedCertificateRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Certificate | None:
    if response.status_code == 200:
        response_200 = Certificate.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Certificate]:
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
    body: PatchedCertificateRequest | PatchedCertificateRequest | PatchedCertificateRequest | Unset = UNSET,
) -> Response[Certificate]:
    """API ViewSet for Certificates (from cert-manager).

    Architecture (Operator-Driven Discovery):
        Certificates are discovered from cert-manager by the Polycrate Operator
        and synced via API (Create/Update/Delete). When a cert-manager Certificate
        is deleted in the cluster, the Operator also deletes the API object via
        Finalizer-Cleanup.

    Agent Token Support:
        Supports Agent Token authentication with workspace isolation.
        Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅
        Workspace/Organization auto-assigned from Agent Token via ManagedObjectBaseViewset.

        See: polycrate-cli/.specs/certificate-discovery.md

    Args:
        id (UUID):
        body (PatchedCertificateRequest | Unset): Full serializer for Certificate detail views.

            Name validation per .specs/0.11.16/certificate-name-validation.md
        body (PatchedCertificateRequest | Unset): Full serializer for Certificate detail views.

            Name validation per .specs/0.11.16/certificate-name-validation.md
        body (PatchedCertificateRequest | Unset): Full serializer for Certificate detail views.

            Name validation per .specs/0.11.16/certificate-name-validation.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Certificate]
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
    body: PatchedCertificateRequest | PatchedCertificateRequest | PatchedCertificateRequest | Unset = UNSET,
) -> Certificate | None:
    """API ViewSet for Certificates (from cert-manager).

    Architecture (Operator-Driven Discovery):
        Certificates are discovered from cert-manager by the Polycrate Operator
        and synced via API (Create/Update/Delete). When a cert-manager Certificate
        is deleted in the cluster, the Operator also deletes the API object via
        Finalizer-Cleanup.

    Agent Token Support:
        Supports Agent Token authentication with workspace isolation.
        Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅
        Workspace/Organization auto-assigned from Agent Token via ManagedObjectBaseViewset.

        See: polycrate-cli/.specs/certificate-discovery.md

    Args:
        id (UUID):
        body (PatchedCertificateRequest | Unset): Full serializer for Certificate detail views.

            Name validation per .specs/0.11.16/certificate-name-validation.md
        body (PatchedCertificateRequest | Unset): Full serializer for Certificate detail views.

            Name validation per .specs/0.11.16/certificate-name-validation.md
        body (PatchedCertificateRequest | Unset): Full serializer for Certificate detail views.

            Name validation per .specs/0.11.16/certificate-name-validation.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Certificate
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
    body: PatchedCertificateRequest | PatchedCertificateRequest | PatchedCertificateRequest | Unset = UNSET,
) -> Response[Certificate]:
    """API ViewSet for Certificates (from cert-manager).

    Architecture (Operator-Driven Discovery):
        Certificates are discovered from cert-manager by the Polycrate Operator
        and synced via API (Create/Update/Delete). When a cert-manager Certificate
        is deleted in the cluster, the Operator also deletes the API object via
        Finalizer-Cleanup.

    Agent Token Support:
        Supports Agent Token authentication with workspace isolation.
        Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅
        Workspace/Organization auto-assigned from Agent Token via ManagedObjectBaseViewset.

        See: polycrate-cli/.specs/certificate-discovery.md

    Args:
        id (UUID):
        body (PatchedCertificateRequest | Unset): Full serializer for Certificate detail views.

            Name validation per .specs/0.11.16/certificate-name-validation.md
        body (PatchedCertificateRequest | Unset): Full serializer for Certificate detail views.

            Name validation per .specs/0.11.16/certificate-name-validation.md
        body (PatchedCertificateRequest | Unset): Full serializer for Certificate detail views.

            Name validation per .specs/0.11.16/certificate-name-validation.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Certificate]
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
    body: PatchedCertificateRequest | PatchedCertificateRequest | PatchedCertificateRequest | Unset = UNSET,
) -> Certificate | None:
    """API ViewSet for Certificates (from cert-manager).

    Architecture (Operator-Driven Discovery):
        Certificates are discovered from cert-manager by the Polycrate Operator
        and synced via API (Create/Update/Delete). When a cert-manager Certificate
        is deleted in the cluster, the Operator also deletes the API object via
        Finalizer-Cleanup.

    Agent Token Support:
        Supports Agent Token authentication with workspace isolation.
        Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅
        Workspace/Organization auto-assigned from Agent Token via ManagedObjectBaseViewset.

        See: polycrate-cli/.specs/certificate-discovery.md

    Args:
        id (UUID):
        body (PatchedCertificateRequest | Unset): Full serializer for Certificate detail views.

            Name validation per .specs/0.11.16/certificate-name-validation.md
        body (PatchedCertificateRequest | Unset): Full serializer for Certificate detail views.

            Name validation per .specs/0.11.16/certificate-name-validation.md
        body (PatchedCertificateRequest | Unset): Full serializer for Certificate detail views.

            Name validation per .specs/0.11.16/certificate-name-validation.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Certificate
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
