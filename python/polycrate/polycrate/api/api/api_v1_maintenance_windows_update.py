from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.maintenance_window import MaintenanceWindow
from ...models.maintenance_window_request import MaintenanceWindowRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: MaintenanceWindowRequest | MaintenanceWindowRequest | MaintenanceWindowRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/maintenance-windows/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, MaintenanceWindowRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MaintenanceWindowRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, MaintenanceWindowRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MaintenanceWindow | None:
    if response.status_code == 200:
        response_200 = MaintenanceWindow.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MaintenanceWindow]:
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
    body: MaintenanceWindowRequest | MaintenanceWindowRequest | MaintenanceWindowRequest | Unset = UNSET,
) -> Response[MaintenanceWindow]:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (MaintenanceWindowRequest | Unset): Full serializer for MaintenanceWindow detail
            view.
            organization/workspace automatisch von ManagedObjectDetailSerializer.
        body (MaintenanceWindowRequest | Unset): Full serializer for MaintenanceWindow detail
            view.
            organization/workspace automatisch von ManagedObjectDetailSerializer.
        body (MaintenanceWindowRequest | Unset): Full serializer for MaintenanceWindow detail
            view.
            organization/workspace automatisch von ManagedObjectDetailSerializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaintenanceWindow]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: MaintenanceWindowRequest | MaintenanceWindowRequest | MaintenanceWindowRequest | Unset = UNSET,
) -> MaintenanceWindow | None:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (MaintenanceWindowRequest | Unset): Full serializer for MaintenanceWindow detail
            view.
            organization/workspace automatisch von ManagedObjectDetailSerializer.
        body (MaintenanceWindowRequest | Unset): Full serializer for MaintenanceWindow detail
            view.
            organization/workspace automatisch von ManagedObjectDetailSerializer.
        body (MaintenanceWindowRequest | Unset): Full serializer for MaintenanceWindow detail
            view.
            organization/workspace automatisch von ManagedObjectDetailSerializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaintenanceWindow
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: MaintenanceWindowRequest | MaintenanceWindowRequest | MaintenanceWindowRequest | Unset = UNSET,
) -> Response[MaintenanceWindow]:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (MaintenanceWindowRequest | Unset): Full serializer for MaintenanceWindow detail
            view.
            organization/workspace automatisch von ManagedObjectDetailSerializer.
        body (MaintenanceWindowRequest | Unset): Full serializer for MaintenanceWindow detail
            view.
            organization/workspace automatisch von ManagedObjectDetailSerializer.
        body (MaintenanceWindowRequest | Unset): Full serializer for MaintenanceWindow detail
            view.
            organization/workspace automatisch von ManagedObjectDetailSerializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MaintenanceWindow]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: MaintenanceWindowRequest | MaintenanceWindowRequest | MaintenanceWindowRequest | Unset = UNSET,
) -> MaintenanceWindow | None:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (MaintenanceWindowRequest | Unset): Full serializer for MaintenanceWindow detail
            view.
            organization/workspace automatisch von ManagedObjectDetailSerializer.
        body (MaintenanceWindowRequest | Unset): Full serializer for MaintenanceWindow detail
            view.
            organization/workspace automatisch von ManagedObjectDetailSerializer.
        body (MaintenanceWindowRequest | Unset): Full serializer for MaintenanceWindow detail
            view.
            organization/workspace automatisch von ManagedObjectDetailSerializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MaintenanceWindow
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
