from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_product_detail_request import PatchedProductDetailRequest
from ...models.product_detail import ProductDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedProductDetailRequest | PatchedProductDetailRequest | PatchedProductDetailRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/pricing/products/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedProductDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedProductDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedProductDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProductDetail | None:
    if response.status_code == 200:
        response_200 = ProductDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProductDetail]:
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
    body: PatchedProductDetailRequest | PatchedProductDetailRequest | PatchedProductDetailRequest | Unset = UNSET,
) -> Response[ProductDetail]:
    """Product catalogue.
    Public read (list/retrieve) for pricing calculator – spec: .specs/0.13.0/pricing-business-layer.md
    Admin-only for write operations.

    Args:
        id (UUID):
        body (PatchedProductDetailRequest | Unset): Full detail serializer.
        body (PatchedProductDetailRequest | Unset): Full detail serializer.
        body (PatchedProductDetailRequest | Unset): Full detail serializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductDetail]
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
    body: PatchedProductDetailRequest | PatchedProductDetailRequest | PatchedProductDetailRequest | Unset = UNSET,
) -> ProductDetail | None:
    """Product catalogue.
    Public read (list/retrieve) for pricing calculator – spec: .specs/0.13.0/pricing-business-layer.md
    Admin-only for write operations.

    Args:
        id (UUID):
        body (PatchedProductDetailRequest | Unset): Full detail serializer.
        body (PatchedProductDetailRequest | Unset): Full detail serializer.
        body (PatchedProductDetailRequest | Unset): Full detail serializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductDetail
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
    body: PatchedProductDetailRequest | PatchedProductDetailRequest | PatchedProductDetailRequest | Unset = UNSET,
) -> Response[ProductDetail]:
    """Product catalogue.
    Public read (list/retrieve) for pricing calculator – spec: .specs/0.13.0/pricing-business-layer.md
    Admin-only for write operations.

    Args:
        id (UUID):
        body (PatchedProductDetailRequest | Unset): Full detail serializer.
        body (PatchedProductDetailRequest | Unset): Full detail serializer.
        body (PatchedProductDetailRequest | Unset): Full detail serializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductDetail]
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
    body: PatchedProductDetailRequest | PatchedProductDetailRequest | PatchedProductDetailRequest | Unset = UNSET,
) -> ProductDetail | None:
    """Product catalogue.
    Public read (list/retrieve) for pricing calculator – spec: .specs/0.13.0/pricing-business-layer.md
    Admin-only for write operations.

    Args:
        id (UUID):
        body (PatchedProductDetailRequest | Unset): Full detail serializer.
        body (PatchedProductDetailRequest | Unset): Full detail serializer.
        body (PatchedProductDetailRequest | Unset): Full detail serializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductDetail
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
