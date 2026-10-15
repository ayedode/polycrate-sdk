from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.provider_detail import ProviderDetail
from ...models.provider_detail_request import ProviderDetailRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: ProviderDetailRequest | ProviderDetailRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/providers/{id}/icon/upload/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, ProviderDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"
    if isinstance(body, ProviderDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProviderDetail | None:
    if response.status_code == 200:
        response_200 = ProviderDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProviderDetail]:
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
    body: ProviderDetailRequest | ProviderDetailRequest | Unset = UNSET,
) -> Response[ProviderDetail]:
    """Upload icon for provider.

    Args:
        id (UUID):
        body (ProviderDetailRequest | Unset): Full detail serializer for Provider.

            Inherits icon_url + is_class_icon from ManagedObjectDetailSerializer (both use
            resolve_managed_object_icon_url which falls back to class_icon_url). has_icon is
            Provider-specific and added here. icon_data (BinaryField) is excluded intentionally.
        body (ProviderDetailRequest | Unset): Full detail serializer for Provider.

            Inherits icon_url + is_class_icon from ManagedObjectDetailSerializer (both use
            resolve_managed_object_icon_url which falls back to class_icon_url). has_icon is
            Provider-specific and added here. icon_data (BinaryField) is excluded intentionally.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProviderDetail]
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
    body: ProviderDetailRequest | ProviderDetailRequest | Unset = UNSET,
) -> ProviderDetail | None:
    """Upload icon for provider.

    Args:
        id (UUID):
        body (ProviderDetailRequest | Unset): Full detail serializer for Provider.

            Inherits icon_url + is_class_icon from ManagedObjectDetailSerializer (both use
            resolve_managed_object_icon_url which falls back to class_icon_url). has_icon is
            Provider-specific and added here. icon_data (BinaryField) is excluded intentionally.
        body (ProviderDetailRequest | Unset): Full detail serializer for Provider.

            Inherits icon_url + is_class_icon from ManagedObjectDetailSerializer (both use
            resolve_managed_object_icon_url which falls back to class_icon_url). has_icon is
            Provider-specific and added here. icon_data (BinaryField) is excluded intentionally.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProviderDetail
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
    body: ProviderDetailRequest | ProviderDetailRequest | Unset = UNSET,
) -> Response[ProviderDetail]:
    """Upload icon for provider.

    Args:
        id (UUID):
        body (ProviderDetailRequest | Unset): Full detail serializer for Provider.

            Inherits icon_url + is_class_icon from ManagedObjectDetailSerializer (both use
            resolve_managed_object_icon_url which falls back to class_icon_url). has_icon is
            Provider-specific and added here. icon_data (BinaryField) is excluded intentionally.
        body (ProviderDetailRequest | Unset): Full detail serializer for Provider.

            Inherits icon_url + is_class_icon from ManagedObjectDetailSerializer (both use
            resolve_managed_object_icon_url which falls back to class_icon_url). has_icon is
            Provider-specific and added here. icon_data (BinaryField) is excluded intentionally.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProviderDetail]
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
    body: ProviderDetailRequest | ProviderDetailRequest | Unset = UNSET,
) -> ProviderDetail | None:
    """Upload icon for provider.

    Args:
        id (UUID):
        body (ProviderDetailRequest | Unset): Full detail serializer for Provider.

            Inherits icon_url + is_class_icon from ManagedObjectDetailSerializer (both use
            resolve_managed_object_icon_url which falls back to class_icon_url). has_icon is
            Provider-specific and added here. icon_data (BinaryField) is excluded intentionally.
        body (ProviderDetailRequest | Unset): Full detail serializer for Provider.

            Inherits icon_url + is_class_icon from ManagedObjectDetailSerializer (both use
            resolve_managed_object_icon_url which falls back to class_icon_url). has_icon is
            Provider-specific and added here. icon_data (BinaryField) is excluded intentionally.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProviderDetail
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
