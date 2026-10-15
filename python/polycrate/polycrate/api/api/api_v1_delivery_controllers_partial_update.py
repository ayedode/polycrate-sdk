from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delivery_controller import DeliveryController
from ...models.patched_delivery_controller_request import PatchedDeliveryControllerRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedDeliveryControllerRequest
    | PatchedDeliveryControllerRequest
    | PatchedDeliveryControllerRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/delivery/controllers/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedDeliveryControllerRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedDeliveryControllerRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedDeliveryControllerRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeliveryController | None:
    if response.status_code == 200:
        response_200 = DeliveryController.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeliveryController]:
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
    body: PatchedDeliveryControllerRequest
    | PatchedDeliveryControllerRequest
    | PatchedDeliveryControllerRequest
    | Unset = UNSET,
) -> Response[DeliveryController]:
    """API endpoint that allows Delivery Controllers to be viewed or edited.

    Provides standard CRUD operations via REST API with proper permissions,
    filtering, and serialization. Includes custom actions for logs, reconcile, and discover.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (PatchedDeliveryControllerRequest | Unset): Full serializer for DeliveryController
            detail views.
        body (PatchedDeliveryControllerRequest | Unset): Full serializer for DeliveryController
            detail views.
        body (PatchedDeliveryControllerRequest | Unset): Full serializer for DeliveryController
            detail views.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliveryController]
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
    body: PatchedDeliveryControllerRequest
    | PatchedDeliveryControllerRequest
    | PatchedDeliveryControllerRequest
    | Unset = UNSET,
) -> DeliveryController | None:
    """API endpoint that allows Delivery Controllers to be viewed or edited.

    Provides standard CRUD operations via REST API with proper permissions,
    filtering, and serialization. Includes custom actions for logs, reconcile, and discover.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (PatchedDeliveryControllerRequest | Unset): Full serializer for DeliveryController
            detail views.
        body (PatchedDeliveryControllerRequest | Unset): Full serializer for DeliveryController
            detail views.
        body (PatchedDeliveryControllerRequest | Unset): Full serializer for DeliveryController
            detail views.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliveryController
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
    body: PatchedDeliveryControllerRequest
    | PatchedDeliveryControllerRequest
    | PatchedDeliveryControllerRequest
    | Unset = UNSET,
) -> Response[DeliveryController]:
    """API endpoint that allows Delivery Controllers to be viewed or edited.

    Provides standard CRUD operations via REST API with proper permissions,
    filtering, and serialization. Includes custom actions for logs, reconcile, and discover.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (PatchedDeliveryControllerRequest | Unset): Full serializer for DeliveryController
            detail views.
        body (PatchedDeliveryControllerRequest | Unset): Full serializer for DeliveryController
            detail views.
        body (PatchedDeliveryControllerRequest | Unset): Full serializer for DeliveryController
            detail views.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliveryController]
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
    body: PatchedDeliveryControllerRequest
    | PatchedDeliveryControllerRequest
    | PatchedDeliveryControllerRequest
    | Unset = UNSET,
) -> DeliveryController | None:
    """API endpoint that allows Delivery Controllers to be viewed or edited.

    Provides standard CRUD operations via REST API with proper permissions,
    filtering, and serialization. Includes custom actions for logs, reconcile, and discover.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (PatchedDeliveryControllerRequest | Unset): Full serializer for DeliveryController
            detail views.
        body (PatchedDeliveryControllerRequest | Unset): Full serializer for DeliveryController
            detail views.
        body (PatchedDeliveryControllerRequest | Unset): Full serializer for DeliveryController
            detail views.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliveryController
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
