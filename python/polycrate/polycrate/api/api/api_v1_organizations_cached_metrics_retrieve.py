from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organization_cached_metrics import OrganizationCachedMetrics
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/organizations/{id}/cached-metrics/".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | OrganizationCachedMetrics | None:
    if response.status_code == 200:
        response_200 = OrganizationCachedMetrics.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | OrganizationCachedMetrics]:
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
) -> Response[Any | OrganizationCachedMetrics]:
    """Organization cached metrics (Customer Portal dashboard)

     Org-scoped dashboard payload for the Customer Portal. Counts come from beat-written
    Organization.cached_* fields; messages are a live list (max 10) of active maintenances (org +
    system-wide), open incidents (org + system-wide), and active downtimes (org). Spec 630.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OrganizationCachedMetrics]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | OrganizationCachedMetrics | None:
    """Organization cached metrics (Customer Portal dashboard)

     Org-scoped dashboard payload for the Customer Portal. Counts come from beat-written
    Organization.cached_* fields; messages are a live list (max 10) of active maintenances (org +
    system-wide), open incidents (org + system-wide), and active downtimes (org). Spec 630.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OrganizationCachedMetrics
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | OrganizationCachedMetrics]:
    """Organization cached metrics (Customer Portal dashboard)

     Org-scoped dashboard payload for the Customer Portal. Counts come from beat-written
    Organization.cached_* fields; messages are a live list (max 10) of active maintenances (org +
    system-wide), open incidents (org + system-wide), and active downtimes (org). Spec 630.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OrganizationCachedMetrics]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | OrganizationCachedMetrics | None:
    """Organization cached metrics (Customer Portal dashboard)

     Org-scoped dashboard payload for the Customer Portal. Counts come from beat-written
    Organization.cached_* fields; messages are a live list (max 10) of active maintenances (org +
    system-wide), open incidents (org + system-wide), and active downtimes (org). Spec 630.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OrganizationCachedMetrics
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
