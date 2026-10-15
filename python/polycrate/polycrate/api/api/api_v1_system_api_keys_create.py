from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.system_api_key import SystemAPIKey
from ...models.system_api_key_request import SystemAPIKeyRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: SystemAPIKeyRequest | SystemAPIKeyRequest | SystemAPIKeyRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/system-api-keys/",
    }

    if isinstance(body, SystemAPIKeyRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, SystemAPIKeyRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, SystemAPIKeyRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SystemAPIKey | None:
    if response.status_code == 201:
        response_201 = SystemAPIKey.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SystemAPIKey]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SystemAPIKeyRequest | SystemAPIKeyRequest | SystemAPIKeyRequest | Unset = UNSET,
) -> Response[SystemAPIKey]:
    """CRUD for System API Keys (kind='system_api_key').
    Only superusers (Admin users and SystemAPIUser with is_superuser=True) may access.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        body (SystemAPIKeyRequest): Serializer for System API Keys (kind='system_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (SystemAPIKeyRequest): Serializer for System API Keys (kind='system_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (SystemAPIKeyRequest): Serializer for System API Keys (kind='system_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemAPIKey]
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
    body: SystemAPIKeyRequest | SystemAPIKeyRequest | SystemAPIKeyRequest | Unset = UNSET,
) -> SystemAPIKey | None:
    """CRUD for System API Keys (kind='system_api_key').
    Only superusers (Admin users and SystemAPIUser with is_superuser=True) may access.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        body (SystemAPIKeyRequest): Serializer for System API Keys (kind='system_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (SystemAPIKeyRequest): Serializer for System API Keys (kind='system_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (SystemAPIKeyRequest): Serializer for System API Keys (kind='system_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SystemAPIKey
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SystemAPIKeyRequest | SystemAPIKeyRequest | SystemAPIKeyRequest | Unset = UNSET,
) -> Response[SystemAPIKey]:
    """CRUD for System API Keys (kind='system_api_key').
    Only superusers (Admin users and SystemAPIUser with is_superuser=True) may access.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        body (SystemAPIKeyRequest): Serializer for System API Keys (kind='system_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (SystemAPIKeyRequest): Serializer for System API Keys (kind='system_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (SystemAPIKeyRequest): Serializer for System API Keys (kind='system_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemAPIKey]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SystemAPIKeyRequest | SystemAPIKeyRequest | SystemAPIKeyRequest | Unset = UNSET,
) -> SystemAPIKey | None:
    """CRUD for System API Keys (kind='system_api_key').
    Only superusers (Admin users and SystemAPIUser with is_superuser=True) may access.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        body (SystemAPIKeyRequest): Serializer for System API Keys (kind='system_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (SystemAPIKeyRequest): Serializer for System API Keys (kind='system_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (SystemAPIKeyRequest): Serializer for System API Keys (kind='system_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SystemAPIKey
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
