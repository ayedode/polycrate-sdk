from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.maintenance_window_status import MaintenanceWindowStatus
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workspaces/{id}/maintenance-window-status/".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MaintenanceWindowStatus | None:
    if response.status_code == 200:
        response_200 = MaintenanceWindowStatus.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MaintenanceWindowStatus]:
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
) -> Response[MaintenanceWindowStatus]:
    """Check if workspace is currently within an active maintenance window

     Returns whether the workspace is currently within an active maintenance window. Effective windows
    are resolved via inheritance: workspace-level → org-level → system default. Spec 220.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaintenanceWindowStatus]
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
) -> MaintenanceWindowStatus | None:
    """Check if workspace is currently within an active maintenance window

     Returns whether the workspace is currently within an active maintenance window. Effective windows
    are resolved via inheritance: workspace-level → org-level → system default. Spec 220.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaintenanceWindowStatus
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[MaintenanceWindowStatus]:
    """Check if workspace is currently within an active maintenance window

     Returns whether the workspace is currently within an active maintenance window. Effective windows
    are resolved via inheritance: workspace-level → org-level → system default. Spec 220.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaintenanceWindowStatus]
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
) -> MaintenanceWindowStatus | None:
    """Check if workspace is currently within an active maintenance window

     Returns whether the workspace is currently within an active maintenance window. Effective windows
    are resolved via inheritance: workspace-level → org-level → system default. Spec 220.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaintenanceWindowStatus
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
