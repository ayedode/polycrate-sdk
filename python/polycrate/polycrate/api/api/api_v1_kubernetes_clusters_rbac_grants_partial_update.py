from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.k8s_cluster import K8SCluster
from ...models.patched_k8s_cluster_request import PatchedK8SClusterRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    cred_id: str,
    *,
    body: PatchedK8SClusterRequest | PatchedK8SClusterRequest | PatchedK8SClusterRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/kubernetes/clusters/{id}/rbac/grants/{cred_id}/".format(
            id=quote(str(id), safe=""),
            cred_id=quote(str(cred_id), safe=""),
        ),
    }

    if isinstance(body, PatchedK8SClusterRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedK8SClusterRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedK8SClusterRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> K8SCluster | None:
    if response.status_code == 200:
        response_200 = K8SCluster.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[K8SCluster]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    cred_id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedK8SClusterRequest | PatchedK8SClusterRequest | PatchedK8SClusterRequest | Unset = UNSET,
) -> Response[K8SCluster]:
    """API endpoint that allows K8s clusters to be viewed or edited.

    Supports Agent Token authentication with workspace isolation.
    Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ❌

    See: .specs/agent-token-extended-api-access.md

    Archived filter, user permissions (workspace-based), and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        cred_id (str):
        body (PatchedK8SClusterRequest | Unset): K8sCluster Detail Serializer - erbt von
            ManagedObjectDetailSerializer.

            Generische Felder (von ManagedObjectDetailSerializer):
            - Alle BaseObject Felder (id, name, display_name, labels, etc.)
            - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
            - organization, workspace als generische Referenzen (mit URL)
            - created (Kombifeld), url

            K8sCluster-spezifische Felder:
            - kubernetes_version, block, kubernetes_apps, etc.

            Per .specs/0.11.4/dynamic-table-v2.md
        body (PatchedK8SClusterRequest | Unset): K8sCluster Detail Serializer - erbt von
            ManagedObjectDetailSerializer.

            Generische Felder (von ManagedObjectDetailSerializer):
            - Alle BaseObject Felder (id, name, display_name, labels, etc.)
            - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
            - organization, workspace als generische Referenzen (mit URL)
            - created (Kombifeld), url

            K8sCluster-spezifische Felder:
            - kubernetes_version, block, kubernetes_apps, etc.

            Per .specs/0.11.4/dynamic-table-v2.md
        body (PatchedK8SClusterRequest | Unset): K8sCluster Detail Serializer - erbt von
            ManagedObjectDetailSerializer.

            Generische Felder (von ManagedObjectDetailSerializer):
            - Alle BaseObject Felder (id, name, display_name, labels, etc.)
            - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
            - organization, workspace als generische Referenzen (mit URL)
            - created (Kombifeld), url

            K8sCluster-spezifische Felder:
            - kubernetes_version, block, kubernetes_apps, etc.

            Per .specs/0.11.4/dynamic-table-v2.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SCluster]
    """

    kwargs = _get_kwargs(
        id=id,
        cred_id=cred_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    cred_id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedK8SClusterRequest | PatchedK8SClusterRequest | PatchedK8SClusterRequest | Unset = UNSET,
) -> K8SCluster | None:
    """API endpoint that allows K8s clusters to be viewed or edited.

    Supports Agent Token authentication with workspace isolation.
    Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ❌

    See: .specs/agent-token-extended-api-access.md

    Archived filter, user permissions (workspace-based), and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        cred_id (str):
        body (PatchedK8SClusterRequest | Unset): K8sCluster Detail Serializer - erbt von
            ManagedObjectDetailSerializer.

            Generische Felder (von ManagedObjectDetailSerializer):
            - Alle BaseObject Felder (id, name, display_name, labels, etc.)
            - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
            - organization, workspace als generische Referenzen (mit URL)
            - created (Kombifeld), url

            K8sCluster-spezifische Felder:
            - kubernetes_version, block, kubernetes_apps, etc.

            Per .specs/0.11.4/dynamic-table-v2.md
        body (PatchedK8SClusterRequest | Unset): K8sCluster Detail Serializer - erbt von
            ManagedObjectDetailSerializer.

            Generische Felder (von ManagedObjectDetailSerializer):
            - Alle BaseObject Felder (id, name, display_name, labels, etc.)
            - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
            - organization, workspace als generische Referenzen (mit URL)
            - created (Kombifeld), url

            K8sCluster-spezifische Felder:
            - kubernetes_version, block, kubernetes_apps, etc.

            Per .specs/0.11.4/dynamic-table-v2.md
        body (PatchedK8SClusterRequest | Unset): K8sCluster Detail Serializer - erbt von
            ManagedObjectDetailSerializer.

            Generische Felder (von ManagedObjectDetailSerializer):
            - Alle BaseObject Felder (id, name, display_name, labels, etc.)
            - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
            - organization, workspace als generische Referenzen (mit URL)
            - created (Kombifeld), url

            K8sCluster-spezifische Felder:
            - kubernetes_version, block, kubernetes_apps, etc.

            Per .specs/0.11.4/dynamic-table-v2.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SCluster
    """

    return sync_detailed(
        id=id,
        cred_id=cred_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    cred_id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedK8SClusterRequest | PatchedK8SClusterRequest | PatchedK8SClusterRequest | Unset = UNSET,
) -> Response[K8SCluster]:
    """API endpoint that allows K8s clusters to be viewed or edited.

    Supports Agent Token authentication with workspace isolation.
    Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ❌

    See: .specs/agent-token-extended-api-access.md

    Archived filter, user permissions (workspace-based), and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        cred_id (str):
        body (PatchedK8SClusterRequest | Unset): K8sCluster Detail Serializer - erbt von
            ManagedObjectDetailSerializer.

            Generische Felder (von ManagedObjectDetailSerializer):
            - Alle BaseObject Felder (id, name, display_name, labels, etc.)
            - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
            - organization, workspace als generische Referenzen (mit URL)
            - created (Kombifeld), url

            K8sCluster-spezifische Felder:
            - kubernetes_version, block, kubernetes_apps, etc.

            Per .specs/0.11.4/dynamic-table-v2.md
        body (PatchedK8SClusterRequest | Unset): K8sCluster Detail Serializer - erbt von
            ManagedObjectDetailSerializer.

            Generische Felder (von ManagedObjectDetailSerializer):
            - Alle BaseObject Felder (id, name, display_name, labels, etc.)
            - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
            - organization, workspace als generische Referenzen (mit URL)
            - created (Kombifeld), url

            K8sCluster-spezifische Felder:
            - kubernetes_version, block, kubernetes_apps, etc.

            Per .specs/0.11.4/dynamic-table-v2.md
        body (PatchedK8SClusterRequest | Unset): K8sCluster Detail Serializer - erbt von
            ManagedObjectDetailSerializer.

            Generische Felder (von ManagedObjectDetailSerializer):
            - Alle BaseObject Felder (id, name, display_name, labels, etc.)
            - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
            - organization, workspace als generische Referenzen (mit URL)
            - created (Kombifeld), url

            K8sCluster-spezifische Felder:
            - kubernetes_version, block, kubernetes_apps, etc.

            Per .specs/0.11.4/dynamic-table-v2.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SCluster]
    """

    kwargs = _get_kwargs(
        id=id,
        cred_id=cred_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    cred_id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedK8SClusterRequest | PatchedK8SClusterRequest | PatchedK8SClusterRequest | Unset = UNSET,
) -> K8SCluster | None:
    """API endpoint that allows K8s clusters to be viewed or edited.

    Supports Agent Token authentication with workspace isolation.
    Agent Permissions: Read ✅, Write ✅, Create ✅, Delete ❌

    See: .specs/agent-token-extended-api-access.md

    Archived filter, user permissions (workspace-based), and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        cred_id (str):
        body (PatchedK8SClusterRequest | Unset): K8sCluster Detail Serializer - erbt von
            ManagedObjectDetailSerializer.

            Generische Felder (von ManagedObjectDetailSerializer):
            - Alle BaseObject Felder (id, name, display_name, labels, etc.)
            - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
            - organization, workspace als generische Referenzen (mit URL)
            - created (Kombifeld), url

            K8sCluster-spezifische Felder:
            - kubernetes_version, block, kubernetes_apps, etc.

            Per .specs/0.11.4/dynamic-table-v2.md
        body (PatchedK8SClusterRequest | Unset): K8sCluster Detail Serializer - erbt von
            ManagedObjectDetailSerializer.

            Generische Felder (von ManagedObjectDetailSerializer):
            - Alle BaseObject Felder (id, name, display_name, labels, etc.)
            - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
            - organization, workspace als generische Referenzen (mit URL)
            - created (Kombifeld), url

            K8sCluster-spezifische Felder:
            - kubernetes_version, block, kubernetes_apps, etc.

            Per .specs/0.11.4/dynamic-table-v2.md
        body (PatchedK8SClusterRequest | Unset): K8sCluster Detail Serializer - erbt von
            ManagedObjectDetailSerializer.

            Generische Felder (von ManagedObjectDetailSerializer):
            - Alle BaseObject Felder (id, name, display_name, labels, etc.)
            - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
            - organization, workspace als generische Referenzen (mit URL)
            - created (Kombifeld), url

            K8sCluster-spezifische Felder:
            - kubernetes_version, block, kubernetes_apps, etc.

            Per .specs/0.11.4/dynamic-table-v2.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SCluster
    """

    return (
        await asyncio_detailed(
            id=id,
            cred_id=cred_id,
            client=client,
            body=body,
        )
    ).parsed
