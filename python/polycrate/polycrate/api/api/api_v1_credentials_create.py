from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credential_create import CredentialCreate
from ...models.credential_create_request import CredentialCreateRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CredentialCreateRequest | CredentialCreateRequest | CredentialCreateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/credentials/",
    }

    if isinstance(body, CredentialCreateRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CredentialCreateRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CredentialCreateRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CredentialCreate | None:
    if response.status_code == 201:
        response_201 = CredentialCreate.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CredentialCreate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CredentialCreateRequest | CredentialCreateRequest | CredentialCreateRequest | Unset = UNSET,
) -> Response[CredentialCreate]:
    """Create credential via API - enabled for microservice integration

    Args:
        body (CredentialCreateRequest): Serializer for creating credentials via API (microservice
            integration).
            Allows setting all necessary fields for credential creation.
        body (CredentialCreateRequest): Serializer for creating credentials via API (microservice
            integration).
            Allows setting all necessary fields for credential creation.
        body (CredentialCreateRequest): Serializer for creating credentials via API (microservice
            integration).
            Allows setting all necessary fields for credential creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialCreate]
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
    body: CredentialCreateRequest | CredentialCreateRequest | CredentialCreateRequest | Unset = UNSET,
) -> CredentialCreate | None:
    """Create credential via API - enabled for microservice integration

    Args:
        body (CredentialCreateRequest): Serializer for creating credentials via API (microservice
            integration).
            Allows setting all necessary fields for credential creation.
        body (CredentialCreateRequest): Serializer for creating credentials via API (microservice
            integration).
            Allows setting all necessary fields for credential creation.
        body (CredentialCreateRequest): Serializer for creating credentials via API (microservice
            integration).
            Allows setting all necessary fields for credential creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialCreate
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CredentialCreateRequest | CredentialCreateRequest | CredentialCreateRequest | Unset = UNSET,
) -> Response[CredentialCreate]:
    """Create credential via API - enabled for microservice integration

    Args:
        body (CredentialCreateRequest): Serializer for creating credentials via API (microservice
            integration).
            Allows setting all necessary fields for credential creation.
        body (CredentialCreateRequest): Serializer for creating credentials via API (microservice
            integration).
            Allows setting all necessary fields for credential creation.
        body (CredentialCreateRequest): Serializer for creating credentials via API (microservice
            integration).
            Allows setting all necessary fields for credential creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialCreate]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CredentialCreateRequest | CredentialCreateRequest | CredentialCreateRequest | Unset = UNSET,
) -> CredentialCreate | None:
    """Create credential via API - enabled for microservice integration

    Args:
        body (CredentialCreateRequest): Serializer for creating credentials via API (microservice
            integration).
            Allows setting all necessary fields for credential creation.
        body (CredentialCreateRequest): Serializer for creating credentials via API (microservice
            integration).
            Allows setting all necessary fields for credential creation.
        body (CredentialCreateRequest): Serializer for creating credentials via API (microservice
            integration).
            Allows setting all necessary fields for credential creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialCreate
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
