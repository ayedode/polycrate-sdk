from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.external_credential import ExternalCredential
from ...models.external_credential_request import ExternalCredentialRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: ExternalCredentialRequest | ExternalCredentialRequest | ExternalCredentialRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/external-credentials/",
    }

    if isinstance(body, ExternalCredentialRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ExternalCredentialRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ExternalCredentialRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExternalCredential | None:
    if response.status_code == 201:
        response_201 = ExternalCredential.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ExternalCredential]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ExternalCredentialRequest | ExternalCredentialRequest | ExternalCredentialRequest | Unset = UNSET,
) -> Response[ExternalCredential]:
    """Create a credential

     Create a new Credential accessible to the authenticated API key.

    For dns-provider credentials, set `metadata.dns_provider` to the Lexicon provider slug (e.g.
    'cloudflare'). See GET /api/v1/dns/providers/ for the list of supported providers and the required
    fields per provider.

    **Access:** System API Key (read-write) or Org API Key (read-write, own organization only). Read-
    only API keys receive 403. Regular users receive 403.

    Spec 491: Credential API Endpoint

    Args:
        body (ExternalCredentialRequest): Serializer for creating/retrieving Credentials via the
            external API endpoint.

            Intended for System API Keys and Org API Keys to manage dns-provider
            credentials. Sensitive fields (api_key) are write-only — never returned.

            Spec 491: Credential API Endpoint
        body (ExternalCredentialRequest): Serializer for creating/retrieving Credentials via the
            external API endpoint.

            Intended for System API Keys and Org API Keys to manage dns-provider
            credentials. Sensitive fields (api_key) are write-only — never returned.

            Spec 491: Credential API Endpoint
        body (ExternalCredentialRequest): Serializer for creating/retrieving Credentials via the
            external API endpoint.

            Intended for System API Keys and Org API Keys to manage dns-provider
            credentials. Sensitive fields (api_key) are write-only — never returned.

            Spec 491: Credential API Endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExternalCredential]
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
    body: ExternalCredentialRequest | ExternalCredentialRequest | ExternalCredentialRequest | Unset = UNSET,
) -> ExternalCredential | None:
    """Create a credential

     Create a new Credential accessible to the authenticated API key.

    For dns-provider credentials, set `metadata.dns_provider` to the Lexicon provider slug (e.g.
    'cloudflare'). See GET /api/v1/dns/providers/ for the list of supported providers and the required
    fields per provider.

    **Access:** System API Key (read-write) or Org API Key (read-write, own organization only). Read-
    only API keys receive 403. Regular users receive 403.

    Spec 491: Credential API Endpoint

    Args:
        body (ExternalCredentialRequest): Serializer for creating/retrieving Credentials via the
            external API endpoint.

            Intended for System API Keys and Org API Keys to manage dns-provider
            credentials. Sensitive fields (api_key) are write-only — never returned.

            Spec 491: Credential API Endpoint
        body (ExternalCredentialRequest): Serializer for creating/retrieving Credentials via the
            external API endpoint.

            Intended for System API Keys and Org API Keys to manage dns-provider
            credentials. Sensitive fields (api_key) are write-only — never returned.

            Spec 491: Credential API Endpoint
        body (ExternalCredentialRequest): Serializer for creating/retrieving Credentials via the
            external API endpoint.

            Intended for System API Keys and Org API Keys to manage dns-provider
            credentials. Sensitive fields (api_key) are write-only — never returned.

            Spec 491: Credential API Endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExternalCredential
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ExternalCredentialRequest | ExternalCredentialRequest | ExternalCredentialRequest | Unset = UNSET,
) -> Response[ExternalCredential]:
    """Create a credential

     Create a new Credential accessible to the authenticated API key.

    For dns-provider credentials, set `metadata.dns_provider` to the Lexicon provider slug (e.g.
    'cloudflare'). See GET /api/v1/dns/providers/ for the list of supported providers and the required
    fields per provider.

    **Access:** System API Key (read-write) or Org API Key (read-write, own organization only). Read-
    only API keys receive 403. Regular users receive 403.

    Spec 491: Credential API Endpoint

    Args:
        body (ExternalCredentialRequest): Serializer for creating/retrieving Credentials via the
            external API endpoint.

            Intended for System API Keys and Org API Keys to manage dns-provider
            credentials. Sensitive fields (api_key) are write-only — never returned.

            Spec 491: Credential API Endpoint
        body (ExternalCredentialRequest): Serializer for creating/retrieving Credentials via the
            external API endpoint.

            Intended for System API Keys and Org API Keys to manage dns-provider
            credentials. Sensitive fields (api_key) are write-only — never returned.

            Spec 491: Credential API Endpoint
        body (ExternalCredentialRequest): Serializer for creating/retrieving Credentials via the
            external API endpoint.

            Intended for System API Keys and Org API Keys to manage dns-provider
            credentials. Sensitive fields (api_key) are write-only — never returned.

            Spec 491: Credential API Endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExternalCredential]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ExternalCredentialRequest | ExternalCredentialRequest | ExternalCredentialRequest | Unset = UNSET,
) -> ExternalCredential | None:
    """Create a credential

     Create a new Credential accessible to the authenticated API key.

    For dns-provider credentials, set `metadata.dns_provider` to the Lexicon provider slug (e.g.
    'cloudflare'). See GET /api/v1/dns/providers/ for the list of supported providers and the required
    fields per provider.

    **Access:** System API Key (read-write) or Org API Key (read-write, own organization only). Read-
    only API keys receive 403. Regular users receive 403.

    Spec 491: Credential API Endpoint

    Args:
        body (ExternalCredentialRequest): Serializer for creating/retrieving Credentials via the
            external API endpoint.

            Intended for System API Keys and Org API Keys to manage dns-provider
            credentials. Sensitive fields (api_key) are write-only — never returned.

            Spec 491: Credential API Endpoint
        body (ExternalCredentialRequest): Serializer for creating/retrieving Credentials via the
            external API endpoint.

            Intended for System API Keys and Org API Keys to manage dns-provider
            credentials. Sensitive fields (api_key) are write-only — never returned.

            Spec 491: Credential API Endpoint
        body (ExternalCredentialRequest): Serializer for creating/retrieving Credentials via the
            external API endpoint.

            Intended for System API Keys and Org API Keys to manage dns-provider
            credentials. Sensitive fields (api_key) are write-only — never returned.

            Spec 491: Credential API Endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExternalCredential
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
