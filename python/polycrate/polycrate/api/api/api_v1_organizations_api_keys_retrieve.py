from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.org_api_key import OrgAPIKey
from ...types import Response


def _get_kwargs(
    org_name: str,
    id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/organizations/{org_name}/api-keys/{id}/".format(
            org_name=quote(str(org_name), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OrgAPIKey | None:
    if response.status_code == 200:
        response_200 = OrgAPIKey.from_dict(response.json())

        return response_200

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
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[OrgAPIKey]:
    """CRUD for Organization API Keys (kind='org_api_key') scoped to one org.
    Create/Delete: superuser only.  List: superuser OR OrgAPIUser of this org.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        org_name (str):
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrgAPIKey]
    """

    kwargs = _get_kwargs(
        org_name=org_name,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org_name: str,
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> OrgAPIKey | None:
    """CRUD for Organization API Keys (kind='org_api_key') scoped to one org.
    Create/Delete: superuser only.  List: superuser OR OrgAPIUser of this org.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        org_name (str):
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrgAPIKey
    """

    return sync_detailed(
        org_name=org_name,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    org_name: str,
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[OrgAPIKey]:
    """CRUD for Organization API Keys (kind='org_api_key') scoped to one org.
    Create/Delete: superuser only.  List: superuser OR OrgAPIUser of this org.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        org_name (str):
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrgAPIKey]
    """

    kwargs = _get_kwargs(
        org_name=org_name,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_name: str,
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> OrgAPIKey | None:
    """CRUD for Organization API Keys (kind='org_api_key') scoped to one org.
    Create/Delete: superuser only.  List: superuser OR OrgAPIUser of this org.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        org_name (str):
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrgAPIKey
    """

    return (
        await asyncio_detailed(
            org_name=org_name,
            id=id,
            client=client,
        )
    ).parsed
