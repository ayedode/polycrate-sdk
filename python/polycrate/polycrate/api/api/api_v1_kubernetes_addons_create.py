from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.k8s_addon import K8SAddon
from ...models.k8s_addon_request import K8SAddonRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: K8SAddonRequest | K8SAddonRequest | K8SAddonRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/kubernetes/addons/",
    }

    if isinstance(body, K8SAddonRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, K8SAddonRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, K8SAddonRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> K8SAddon | None:
    if response.status_code == 201:
        response_201 = K8SAddon.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[K8SAddon]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: K8SAddonRequest | K8SAddonRequest | K8SAddonRequest | Unset = UNSET,
) -> Response[K8SAddon]:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (K8SAddonRequest): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (K8SAddonRequest): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (K8SAddonRequest): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SAddon]
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
    body: K8SAddonRequest | K8SAddonRequest | K8SAddonRequest | Unset = UNSET,
) -> K8SAddon | None:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (K8SAddonRequest): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (K8SAddonRequest): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (K8SAddonRequest): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SAddon
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: K8SAddonRequest | K8SAddonRequest | K8SAddonRequest | Unset = UNSET,
) -> Response[K8SAddon]:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (K8SAddonRequest): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (K8SAddonRequest): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (K8SAddonRequest): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SAddon]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: K8SAddonRequest | K8SAddonRequest | K8SAddonRequest | Unset = UNSET,
) -> K8SAddon | None:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (K8SAddonRequest): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (K8SAddonRequest): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (K8SAddonRequest): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SAddon
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
