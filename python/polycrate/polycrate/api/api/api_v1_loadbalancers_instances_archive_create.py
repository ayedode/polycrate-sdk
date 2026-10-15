from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archive_response import ArchiveResponse
from ...models.loadbalancer_instance_request import LoadbalancerInstanceRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: LoadbalancerInstanceRequest | LoadbalancerInstanceRequest | LoadbalancerInstanceRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/loadbalancers/instances/{id}/archive/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, LoadbalancerInstanceRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, LoadbalancerInstanceRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, LoadbalancerInstanceRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ArchiveResponse | None:
    if response.status_code == 200:
        response_200 = ArchiveResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ArchiveResponse]:
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
    body: LoadbalancerInstanceRequest | LoadbalancerInstanceRequest | LoadbalancerInstanceRequest | Unset = UNSET,
) -> Response[ArchiveResponse]:
    """Toggle archive state

     POST with {"archive_reason": "..."} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

    Args:
        id (UUID):
        body (LoadbalancerInstanceRequest | Unset): Detail serializer for LoadbalancerInstance —
            erbt von ManagedObjectDetailSerializer.
            Spec: polycrate spec inspect 70
        body (LoadbalancerInstanceRequest | Unset): Detail serializer for LoadbalancerInstance —
            erbt von ManagedObjectDetailSerializer.
            Spec: polycrate spec inspect 70
        body (LoadbalancerInstanceRequest | Unset): Detail serializer for LoadbalancerInstance —
            erbt von ManagedObjectDetailSerializer.
            Spec: polycrate spec inspect 70

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveResponse]
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
    body: LoadbalancerInstanceRequest | LoadbalancerInstanceRequest | LoadbalancerInstanceRequest | Unset = UNSET,
) -> ArchiveResponse | None:
    """Toggle archive state

     POST with {"archive_reason": "..."} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

    Args:
        id (UUID):
        body (LoadbalancerInstanceRequest | Unset): Detail serializer for LoadbalancerInstance —
            erbt von ManagedObjectDetailSerializer.
            Spec: polycrate spec inspect 70
        body (LoadbalancerInstanceRequest | Unset): Detail serializer for LoadbalancerInstance —
            erbt von ManagedObjectDetailSerializer.
            Spec: polycrate spec inspect 70
        body (LoadbalancerInstanceRequest | Unset): Detail serializer for LoadbalancerInstance —
            erbt von ManagedObjectDetailSerializer.
            Spec: polycrate spec inspect 70

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveResponse
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
    body: LoadbalancerInstanceRequest | LoadbalancerInstanceRequest | LoadbalancerInstanceRequest | Unset = UNSET,
) -> Response[ArchiveResponse]:
    """Toggle archive state

     POST with {"archive_reason": "..."} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

    Args:
        id (UUID):
        body (LoadbalancerInstanceRequest | Unset): Detail serializer for LoadbalancerInstance —
            erbt von ManagedObjectDetailSerializer.
            Spec: polycrate spec inspect 70
        body (LoadbalancerInstanceRequest | Unset): Detail serializer for LoadbalancerInstance —
            erbt von ManagedObjectDetailSerializer.
            Spec: polycrate spec inspect 70
        body (LoadbalancerInstanceRequest | Unset): Detail serializer for LoadbalancerInstance —
            erbt von ManagedObjectDetailSerializer.
            Spec: polycrate spec inspect 70

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveResponse]
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
    body: LoadbalancerInstanceRequest | LoadbalancerInstanceRequest | LoadbalancerInstanceRequest | Unset = UNSET,
) -> ArchiveResponse | None:
    """Toggle archive state

     POST with {"archive_reason": "..."} to archive. POST without body to unarchive. Per
    .specs/.next/29-managed-object-dashboard-component.md

    Args:
        id (UUID):
        body (LoadbalancerInstanceRequest | Unset): Detail serializer for LoadbalancerInstance —
            erbt von ManagedObjectDetailSerializer.
            Spec: polycrate spec inspect 70
        body (LoadbalancerInstanceRequest | Unset): Detail serializer for LoadbalancerInstance —
            erbt von ManagedObjectDetailSerializer.
            Spec: polycrate spec inspect 70
        body (LoadbalancerInstanceRequest | Unset): Detail serializer for LoadbalancerInstance —
            erbt von ManagedObjectDetailSerializer.
            Spec: polycrate spec inspect 70

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
