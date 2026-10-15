from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.k8s_addon import K8SAddon
from ...models.patched_k8s_addon_request import PatchedK8SAddonRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedK8SAddonRequest | PatchedK8SAddonRequest | PatchedK8SAddonRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/kubernetes/addons/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedK8SAddonRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedK8SAddonRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedK8SAddonRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> K8SAddon | None:
    if response.status_code == 200:
        response_200 = K8SAddon.from_dict(response.json())

        return response_200

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
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedK8SAddonRequest | PatchedK8SAddonRequest | PatchedK8SAddonRequest | Unset = UNSET,
) -> Response[K8SAddon]:
    """API endpoint for K8sAddon catalog.
    Mutate: admin via PERMISSION_CONFIG. Spec: polycrate spec inspect 695

    Args:
        id (UUID):
        body (PatchedK8SAddonRequest | Unset): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (PatchedK8SAddonRequest | Unset): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (PatchedK8SAddonRequest | Unset): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SAddon]
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
    body: PatchedK8SAddonRequest | PatchedK8SAddonRequest | PatchedK8SAddonRequest | Unset = UNSET,
) -> K8SAddon | None:
    """API endpoint for K8sAddon catalog.
    Mutate: admin via PERMISSION_CONFIG. Spec: polycrate spec inspect 695

    Args:
        id (UUID):
        body (PatchedK8SAddonRequest | Unset): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (PatchedK8SAddonRequest | Unset): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (PatchedK8SAddonRequest | Unset): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SAddon
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
    body: PatchedK8SAddonRequest | PatchedK8SAddonRequest | PatchedK8SAddonRequest | Unset = UNSET,
) -> Response[K8SAddon]:
    """API endpoint for K8sAddon catalog.
    Mutate: admin via PERMISSION_CONFIG. Spec: polycrate spec inspect 695

    Args:
        id (UUID):
        body (PatchedK8SAddonRequest | Unset): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (PatchedK8SAddonRequest | Unset): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (PatchedK8SAddonRequest | Unset): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SAddon]
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
    body: PatchedK8SAddonRequest | PatchedK8SAddonRequest | PatchedK8SAddonRequest | Unset = UNSET,
) -> K8SAddon | None:
    """API endpoint for K8sAddon catalog.
    Mutate: admin via PERMISSION_CONFIG. Spec: polycrate spec inspect 695

    Args:
        id (UUID):
        body (PatchedK8SAddonRequest | Unset): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (PatchedK8SAddonRequest | Unset): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695
        body (PatchedK8SAddonRequest | Unset): Detail serializer for K8sAddon catalog entries.
            catalogue_app is a writable FK (UUID). Spec: polycrate spec inspect 695

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SAddon
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
