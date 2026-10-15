from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dns_provider_catalog_response import DNSProviderCatalogResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/dns/providers/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DNSProviderCatalogResponse | None:
    if response.status_code == 200:
        response_200 = DNSProviderCatalogResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DNSProviderCatalogResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[DNSProviderCatalogResponse]:
    """List supported DNS providers

     Returns the list of DNS providers enabled on this system (configured via
    SystemConfig.dns_supported_providers). Each provider entry includes the Lexicon slug, a human-
    readable label, and a credential_schema that documents which Credential fields (api_key, api_user,
    metadata) are required or optional for that provider.

    To associate a Credential with a DNS provider, set Credential.metadata.dns_provider to the provider
    slug. Example: {"dns_provider": "cloudflare"}.

    Spec 490: DNS Provider Catalog

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSProviderCatalogResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> DNSProviderCatalogResponse | None:
    """List supported DNS providers

     Returns the list of DNS providers enabled on this system (configured via
    SystemConfig.dns_supported_providers). Each provider entry includes the Lexicon slug, a human-
    readable label, and a credential_schema that documents which Credential fields (api_key, api_user,
    metadata) are required or optional for that provider.

    To associate a Credential with a DNS provider, set Credential.metadata.dns_provider to the provider
    slug. Example: {"dns_provider": "cloudflare"}.

    Spec 490: DNS Provider Catalog

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSProviderCatalogResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[DNSProviderCatalogResponse]:
    """List supported DNS providers

     Returns the list of DNS providers enabled on this system (configured via
    SystemConfig.dns_supported_providers). Each provider entry includes the Lexicon slug, a human-
    readable label, and a credential_schema that documents which Credential fields (api_key, api_user,
    metadata) are required or optional for that provider.

    To associate a Credential with a DNS provider, set Credential.metadata.dns_provider to the provider
    slug. Example: {"dns_provider": "cloudflare"}.

    Spec 490: DNS Provider Catalog

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSProviderCatalogResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> DNSProviderCatalogResponse | None:
    """List supported DNS providers

     Returns the list of DNS providers enabled on this system (configured via
    SystemConfig.dns_supported_providers). Each provider entry includes the Lexicon slug, a human-
    readable label, and a credential_schema that documents which Credential fields (api_key, api_user,
    metadata) are required or optional for that provider.

    To associate a Credential with a DNS provider, set Credential.metadata.dns_provider to the provider
    slug. Example: {"dns_provider": "cloudflare"}.

    Spec 490: DNS Provider Catalog

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSProviderCatalogResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
