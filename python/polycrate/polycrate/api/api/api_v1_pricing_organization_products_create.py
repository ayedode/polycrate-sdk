from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organization_product_detail import OrganizationProductDetail
from ...models.organization_product_detail_request import OrganizationProductDetailRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: OrganizationProductDetailRequest
    | OrganizationProductDetailRequest
    | OrganizationProductDetailRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/pricing/organization-products/",
    }

    if isinstance(body, OrganizationProductDetailRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, OrganizationProductDetailRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, OrganizationProductDetailRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OrganizationProductDetail | None:
    if response.status_code == 201:
        response_201 = OrganizationProductDetail.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OrganizationProductDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OrganizationProductDetailRequest
    | OrganizationProductDetailRequest
    | OrganizationProductDetailRequest
    | Unset = UNSET,
) -> Response[OrganizationProductDetail]:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (OrganizationProductDetailRequest): Full detail serializer.
        body (OrganizationProductDetailRequest): Full detail serializer.
        body (OrganizationProductDetailRequest): Full detail serializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationProductDetail]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: OrganizationProductDetailRequest
    | OrganizationProductDetailRequest
    | OrganizationProductDetailRequest
    | Unset = UNSET,
) -> OrganizationProductDetail | None:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (OrganizationProductDetailRequest): Full detail serializer.
        body (OrganizationProductDetailRequest): Full detail serializer.
        body (OrganizationProductDetailRequest): Full detail serializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrganizationProductDetail
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OrganizationProductDetailRequest
    | OrganizationProductDetailRequest
    | OrganizationProductDetailRequest
    | Unset = UNSET,
) -> Response[OrganizationProductDetail]:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (OrganizationProductDetailRequest): Full detail serializer.
        body (OrganizationProductDetailRequest): Full detail serializer.
        body (OrganizationProductDetailRequest): Full detail serializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationProductDetail]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: OrganizationProductDetailRequest
    | OrganizationProductDetailRequest
    | OrganizationProductDetailRequest
    | Unset = UNSET,
) -> OrganizationProductDetail | None:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (OrganizationProductDetailRequest): Full detail serializer.
        body (OrganizationProductDetailRequest): Full detail serializer.
        body (OrganizationProductDetailRequest): Full detail serializer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrganizationProductDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
