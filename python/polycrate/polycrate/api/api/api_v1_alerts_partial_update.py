from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert import Alert
from ...models.patched_alert_request import PatchedAlertRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedAlertRequest | PatchedAlertRequest | PatchedAlertRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/alerts/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedAlertRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedAlertRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedAlertRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Alert | None:
    if response.status_code == 200:
        response_200 = Alert.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Alert]:
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
    body: PatchedAlertRequest | PatchedAlertRequest | PatchedAlertRequest | Unset = UNSET,
) -> Response[Alert]:
    """API endpoint that allows endpoints to be viewed or edited.

    Args:
        id (UUID):
        body (PatchedAlertRequest | Unset): Detail serializer for Alert.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (PatchedAlertRequest | Unset): Detail serializer for Alert.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (PatchedAlertRequest | Unset): Detail serializer for Alert.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Alert]
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
    body: PatchedAlertRequest | PatchedAlertRequest | PatchedAlertRequest | Unset = UNSET,
) -> Alert | None:
    """API endpoint that allows endpoints to be viewed or edited.

    Args:
        id (UUID):
        body (PatchedAlertRequest | Unset): Detail serializer for Alert.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (PatchedAlertRequest | Unset): Detail serializer for Alert.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (PatchedAlertRequest | Unset): Detail serializer for Alert.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Alert
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
    body: PatchedAlertRequest | PatchedAlertRequest | PatchedAlertRequest | Unset = UNSET,
) -> Response[Alert]:
    """API endpoint that allows endpoints to be viewed or edited.

    Args:
        id (UUID):
        body (PatchedAlertRequest | Unset): Detail serializer for Alert.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (PatchedAlertRequest | Unset): Detail serializer for Alert.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (PatchedAlertRequest | Unset): Detail serializer for Alert.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Alert]
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
    body: PatchedAlertRequest | PatchedAlertRequest | PatchedAlertRequest | Unset = UNSET,
) -> Alert | None:
    """API endpoint that allows endpoints to be viewed or edited.

    Args:
        id (UUID):
        body (PatchedAlertRequest | Unset): Detail serializer for Alert.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (PatchedAlertRequest | Unset): Detail serializer for Alert.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.
        body (PatchedAlertRequest | Unset): Detail serializer for Alert.
            Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
            organization and workspace are provided as serialize_managed_object_simple dicts by the
            base class.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Alert
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
