from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.host import Host
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/hosts/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Host | None:
    if response.status_code == 200:
        response_200 = Host.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Host]:
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
) -> Response[Host]:
    """API endpoint that allows hosts to be viewed or edited.

    Supports Agent Token authentication with workspace isolation.
    Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅

    See: .specs/agent-token-extended-api-access.md

    Archived filter, user permissions (workspace-based), and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Host]
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
) -> Host | None:
    """API endpoint that allows hosts to be viewed or edited.

    Supports Agent Token authentication with workspace isolation.
    Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅

    See: .specs/agent-token-extended-api-access.md

    Archived filter, user permissions (workspace-based), and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Host
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Host]:
    """API endpoint that allows hosts to be viewed or edited.

    Supports Agent Token authentication with workspace isolation.
    Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅

    See: .specs/agent-token-extended-api-access.md

    Archived filter, user permissions (workspace-based), and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Host]
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
) -> Host | None:
    """API endpoint that allows hosts to be viewed or edited.

    Supports Agent Token authentication with workspace isolation.
    Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ✅

    See: .specs/agent-token-extended-api-access.md

    Archived filter, user permissions (workspace-based), and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Host
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
