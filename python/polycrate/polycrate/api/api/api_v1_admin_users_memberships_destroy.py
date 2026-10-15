from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    id: int,
    organization_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/admin/users/{id}/memberships/{organization_id}/".format(
            id=quote(str(id), safe=""),
            organization_id=quote(str(organization_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 404:
        return None

    if response.status_code == 409:
        return None

    if response.status_code == 502:
        return None

    if response.status_code == 503:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    organization_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Remove admin user membership

     Remove OrganizationMembership for the given organization_id. Blocking Keycloak org/role-group leave
    and Platform Grafana org leave (except system-org members / Spec 494). Idempotent 204. Last owner →
    409 code=last_owner. Spec 561.

    Args:
        id (int):
        organization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        organization_id=organization_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: int,
    organization_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Remove admin user membership

     Remove OrganizationMembership for the given organization_id. Blocking Keycloak org/role-group leave
    and Platform Grafana org leave (except system-org members / Spec 494). Idempotent 204. Last owner →
    409 code=last_owner. Spec 561.

    Args:
        id (int):
        organization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        organization_id=organization_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
