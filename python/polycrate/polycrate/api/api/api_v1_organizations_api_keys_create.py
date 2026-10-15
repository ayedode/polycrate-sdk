from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.org_api_key import OrgAPIKey
from ...models.org_api_key_request import OrgAPIKeyRequest
from ...types import UNSET, Response


def _get_kwargs(
    org_name: str,
    *,
    body: OrgAPIKeyRequest | OrgAPIKeyRequest | OrgAPIKeyRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/organizations/{org_name}/api-keys/".format(
            org_name=quote(str(org_name), safe=""),
        ),
    }

    if isinstance(body, OrgAPIKeyRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, OrgAPIKeyRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, OrgAPIKeyRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OrgAPIKey | None:
    if response.status_code == 201:
        response_201 = OrgAPIKey.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OrgAPIKey]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_name: str,
    *,
    client: AuthenticatedClient,
    body: OrgAPIKeyRequest | OrgAPIKeyRequest | OrgAPIKeyRequest | Unset = UNSET,
) -> Response[OrgAPIKey]:
    """CRUD for Organization API Keys (kind='org_api_key') scoped to one org.
    Create/Delete: superuser only.  List: superuser OR OrgAPIUser of this org.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        org_name (str):
        body (OrgAPIKeyRequest): Serializer for Organization API Keys (kind='org_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (OrgAPIKeyRequest): Serializer for Organization API Keys (kind='org_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (OrgAPIKeyRequest): Serializer for Organization API Keys (kind='org_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrgAPIKey]
    """

    kwargs = _get_kwargs(
        org_name=org_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_name: str,
    *,
    client: AuthenticatedClient,
    body: OrgAPIKeyRequest | OrgAPIKeyRequest | OrgAPIKeyRequest | Unset = UNSET,
) -> OrgAPIKey | None:
    """CRUD for Organization API Keys (kind='org_api_key') scoped to one org.
    Create/Delete: superuser only.  List: superuser OR OrgAPIUser of this org.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        org_name (str):
        body (OrgAPIKeyRequest): Serializer for Organization API Keys (kind='org_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (OrgAPIKeyRequest): Serializer for Organization API Keys (kind='org_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (OrgAPIKeyRequest): Serializer for Organization API Keys (kind='org_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrgAPIKey
    """

    return sync_detailed(
        org_name=org_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    org_name: str,
    *,
    client: AuthenticatedClient,
    body: OrgAPIKeyRequest | OrgAPIKeyRequest | OrgAPIKeyRequest | Unset = UNSET,
) -> Response[OrgAPIKey]:
    """CRUD for Organization API Keys (kind='org_api_key') scoped to one org.
    Create/Delete: superuser only.  List: superuser OR OrgAPIUser of this org.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        org_name (str):
        body (OrgAPIKeyRequest): Serializer for Organization API Keys (kind='org_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (OrgAPIKeyRequest): Serializer for Organization API Keys (kind='org_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (OrgAPIKeyRequest): Serializer for Organization API Keys (kind='org_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrgAPIKey]
    """

    kwargs = _get_kwargs(
        org_name=org_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_name: str,
    *,
    client: AuthenticatedClient,
    body: OrgAPIKeyRequest | OrgAPIKeyRequest | OrgAPIKeyRequest | Unset = UNSET,
) -> OrgAPIKey | None:
    """CRUD for Organization API Keys (kind='org_api_key') scoped to one org.
    Create/Delete: superuser only.  List: superuser OR OrgAPIUser of this org.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        org_name (str):
        body (OrgAPIKeyRequest): Serializer for Organization API Keys (kind='org_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (OrgAPIKeyRequest): Serializer for Organization API Keys (kind='org_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys
        body (OrgAPIKeyRequest): Serializer for Organization API Keys (kind='org_api_key').
            token is only included on create (write-once).
            Spec 488: System and Organization API Keys

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrgAPIKey
    """

    return (
        await asyncio_detailed(
            org_name=org_name,
            client=client,
            body=body,
        )
    ).parsed
