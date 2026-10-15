from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.k8s_volume import K8SVolume
from ...models.patched_k8s_volume_request import PatchedK8SVolumeRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedK8SVolumeRequest | PatchedK8SVolumeRequest | PatchedK8SVolumeRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/kubernetes/volumes/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedK8SVolumeRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedK8SVolumeRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedK8SVolumeRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> K8SVolume | None:
    if response.status_code == 200:
        response_200 = K8SVolume.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[K8SVolume]:
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
    body: PatchedK8SVolumeRequest | PatchedK8SVolumeRequest | PatchedK8SVolumeRequest | Unset = UNSET,
) -> Response[K8SVolume]:
    """API endpoint for K8sVolume — PersistentVolume tracking.

    Read/Write via Operator Agent Token. No user-facing Create/Delete in UI.
    Spec: polycrate spec inspect 31

    Args:
        id (UUID):
        body (PatchedK8SVolumeRequest | Unset): K8sVolume Detail Serializer — used by the operator
            and API clients.
            Spec: polycrate spec inspect 31
            Pricing: polycrate spec inspect 155

            k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
            so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
            The operator must be able to set k8s_cluster on create/update.
            organization and workspace are handled by ManagedObjectBaseViewset.perform_create.
        body (PatchedK8SVolumeRequest | Unset): K8sVolume Detail Serializer — used by the operator
            and API clients.
            Spec: polycrate spec inspect 31
            Pricing: polycrate spec inspect 155

            k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
            so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
            The operator must be able to set k8s_cluster on create/update.
            organization and workspace are handled by ManagedObjectBaseViewset.perform_create.
        body (PatchedK8SVolumeRequest | Unset): K8sVolume Detail Serializer — used by the operator
            and API clients.
            Spec: polycrate spec inspect 31
            Pricing: polycrate spec inspect 155

            k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
            so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
            The operator must be able to set k8s_cluster on create/update.
            organization and workspace are handled by ManagedObjectBaseViewset.perform_create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SVolume]
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
    body: PatchedK8SVolumeRequest | PatchedK8SVolumeRequest | PatchedK8SVolumeRequest | Unset = UNSET,
) -> K8SVolume | None:
    """API endpoint for K8sVolume — PersistentVolume tracking.

    Read/Write via Operator Agent Token. No user-facing Create/Delete in UI.
    Spec: polycrate spec inspect 31

    Args:
        id (UUID):
        body (PatchedK8SVolumeRequest | Unset): K8sVolume Detail Serializer — used by the operator
            and API clients.
            Spec: polycrate spec inspect 31
            Pricing: polycrate spec inspect 155

            k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
            so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
            The operator must be able to set k8s_cluster on create/update.
            organization and workspace are handled by ManagedObjectBaseViewset.perform_create.
        body (PatchedK8SVolumeRequest | Unset): K8sVolume Detail Serializer — used by the operator
            and API clients.
            Spec: polycrate spec inspect 31
            Pricing: polycrate spec inspect 155

            k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
            so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
            The operator must be able to set k8s_cluster on create/update.
            organization and workspace are handled by ManagedObjectBaseViewset.perform_create.
        body (PatchedK8SVolumeRequest | Unset): K8sVolume Detail Serializer — used by the operator
            and API clients.
            Spec: polycrate spec inspect 31
            Pricing: polycrate spec inspect 155

            k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
            so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
            The operator must be able to set k8s_cluster on create/update.
            organization and workspace are handled by ManagedObjectBaseViewset.perform_create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SVolume
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
    body: PatchedK8SVolumeRequest | PatchedK8SVolumeRequest | PatchedK8SVolumeRequest | Unset = UNSET,
) -> Response[K8SVolume]:
    """API endpoint for K8sVolume — PersistentVolume tracking.

    Read/Write via Operator Agent Token. No user-facing Create/Delete in UI.
    Spec: polycrate spec inspect 31

    Args:
        id (UUID):
        body (PatchedK8SVolumeRequest | Unset): K8sVolume Detail Serializer — used by the operator
            and API clients.
            Spec: polycrate spec inspect 31
            Pricing: polycrate spec inspect 155

            k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
            so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
            The operator must be able to set k8s_cluster on create/update.
            organization and workspace are handled by ManagedObjectBaseViewset.perform_create.
        body (PatchedK8SVolumeRequest | Unset): K8sVolume Detail Serializer — used by the operator
            and API clients.
            Spec: polycrate spec inspect 31
            Pricing: polycrate spec inspect 155

            k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
            so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
            The operator must be able to set k8s_cluster on create/update.
            organization and workspace are handled by ManagedObjectBaseViewset.perform_create.
        body (PatchedK8SVolumeRequest | Unset): K8sVolume Detail Serializer — used by the operator
            and API clients.
            Spec: polycrate spec inspect 31
            Pricing: polycrate spec inspect 155

            k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
            so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
            The operator must be able to set k8s_cluster on create/update.
            organization and workspace are handled by ManagedObjectBaseViewset.perform_create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SVolume]
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
    body: PatchedK8SVolumeRequest | PatchedK8SVolumeRequest | PatchedK8SVolumeRequest | Unset = UNSET,
) -> K8SVolume | None:
    """API endpoint for K8sVolume — PersistentVolume tracking.

    Read/Write via Operator Agent Token. No user-facing Create/Delete in UI.
    Spec: polycrate spec inspect 31

    Args:
        id (UUID):
        body (PatchedK8SVolumeRequest | Unset): K8sVolume Detail Serializer — used by the operator
            and API clients.
            Spec: polycrate spec inspect 31
            Pricing: polycrate spec inspect 155

            k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
            so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
            The operator must be able to set k8s_cluster on create/update.
            organization and workspace are handled by ManagedObjectBaseViewset.perform_create.
        body (PatchedK8SVolumeRequest | Unset): K8sVolume Detail Serializer — used by the operator
            and API clients.
            Spec: polycrate spec inspect 31
            Pricing: polycrate spec inspect 155

            k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
            so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
            The operator must be able to set k8s_cluster on create/update.
            organization and workspace are handled by ManagedObjectBaseViewset.perform_create.
        body (PatchedK8SVolumeRequest | Unset): K8sVolume Detail Serializer — used by the operator
            and API clients.
            Spec: polycrate spec inspect 31
            Pricing: polycrate spec inspect 155

            k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
            so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
            The operator must be able to set k8s_cluster on create/update.
            organization and workspace are handled by ManagedObjectBaseViewset.perform_create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SVolume
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
