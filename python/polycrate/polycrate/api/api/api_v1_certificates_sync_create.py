from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.certificate_sync import CertificateSync
from ...models.certificate_sync_request import CertificateSyncRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CertificateSyncRequest | CertificateSyncRequest | CertificateSyncRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/certificates/sync/",
    }

    if isinstance(body, CertificateSyncRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CertificateSyncRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CertificateSyncRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CertificateSync | None:
    if response.status_code == 200:
        response_200 = CertificateSync.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CertificateSync]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CertificateSyncRequest | CertificateSyncRequest | CertificateSyncRequest | Unset = UNSET,
) -> Response[CertificateSync]:
    """Sync a certificate from Polycrate Operator.

    Accepts raw cert-manager Certificate CR data and creates/updates
    the Certificate model instance.

    Args:
        body (CertificateSyncRequest): Serializer for syncing certificates from Polycrate
            Operator.
        body (CertificateSyncRequest): Serializer for syncing certificates from Polycrate
            Operator.
        body (CertificateSyncRequest): Serializer for syncing certificates from Polycrate
            Operator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CertificateSync]
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
    body: CertificateSyncRequest | CertificateSyncRequest | CertificateSyncRequest | Unset = UNSET,
) -> CertificateSync | None:
    """Sync a certificate from Polycrate Operator.

    Accepts raw cert-manager Certificate CR data and creates/updates
    the Certificate model instance.

    Args:
        body (CertificateSyncRequest): Serializer for syncing certificates from Polycrate
            Operator.
        body (CertificateSyncRequest): Serializer for syncing certificates from Polycrate
            Operator.
        body (CertificateSyncRequest): Serializer for syncing certificates from Polycrate
            Operator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CertificateSync
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CertificateSyncRequest | CertificateSyncRequest | CertificateSyncRequest | Unset = UNSET,
) -> Response[CertificateSync]:
    """Sync a certificate from Polycrate Operator.

    Accepts raw cert-manager Certificate CR data and creates/updates
    the Certificate model instance.

    Args:
        body (CertificateSyncRequest): Serializer for syncing certificates from Polycrate
            Operator.
        body (CertificateSyncRequest): Serializer for syncing certificates from Polycrate
            Operator.
        body (CertificateSyncRequest): Serializer for syncing certificates from Polycrate
            Operator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CertificateSync]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CertificateSyncRequest | CertificateSyncRequest | CertificateSyncRequest | Unset = UNSET,
) -> CertificateSync | None:
    """Sync a certificate from Polycrate Operator.

    Accepts raw cert-manager Certificate CR data and creates/updates
    the Certificate model instance.

    Args:
        body (CertificateSyncRequest): Serializer for syncing certificates from Polycrate
            Operator.
        body (CertificateSyncRequest): Serializer for syncing certificates from Polycrate
            Operator.
        body (CertificateSyncRequest): Serializer for syncing certificates from Polycrate
            Operator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CertificateSync
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
