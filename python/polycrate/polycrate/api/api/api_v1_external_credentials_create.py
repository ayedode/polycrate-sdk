from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_external_credentials_create_validation_error import ApiV1ExternalCredentialsCreateValidationError
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
from ...models.external_credential import ExternalCredential
from ...models.external_credential_request import ExternalCredentialRequest
from ...models.parse_error_response import ParseErrorResponse
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


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiV1ExternalCredentialsCreateValidationError
    | ParseErrorResponse
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
    | ExternalCredential
    | None
):
    if response.status_code == 201:
        response_201 = ExternalCredential.from_dict(response.json())

        return response_201

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1ExternalCredentialsCreateValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_external_credentials_create_error_response_400_type_0 = (
                    ApiV1ExternalCredentialsCreateValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_external_credentials_create_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_external_credentials_create_error_response_400_type_1 = (
                ParseErrorResponse.from_dict(data)
            )

            return componentsschemas_api_v1_external_credentials_create_error_response_400_type_1

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
    ApiV1ExternalCredentialsCreateValidationError
    | ParseErrorResponse
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
    | ExternalCredential
]:
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
) -> Response[
    ApiV1ExternalCredentialsCreateValidationError
    | ParseErrorResponse
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
    | ExternalCredential
]:
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
        Response[ApiV1ExternalCredentialsCreateValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | ExternalCredential]
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
) -> (
    ApiV1ExternalCredentialsCreateValidationError
    | ParseErrorResponse
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
    | ExternalCredential
    | None
):
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
        ApiV1ExternalCredentialsCreateValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | ExternalCredential
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ExternalCredentialRequest | ExternalCredentialRequest | ExternalCredentialRequest | Unset = UNSET,
) -> Response[
    ApiV1ExternalCredentialsCreateValidationError
    | ParseErrorResponse
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
    | ExternalCredential
]:
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
        Response[ApiV1ExternalCredentialsCreateValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | ExternalCredential]
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
) -> (
    ApiV1ExternalCredentialsCreateValidationError
    | ParseErrorResponse
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
    | ExternalCredential
    | None
):
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
        ApiV1ExternalCredentialsCreateValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | ExternalCredential
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
