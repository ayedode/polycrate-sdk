from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.k8s_addon_config_revision import K8SAddonConfigRevision
from ...models.patched_k8s_addon_config_revision_request import PatchedK8SAddonConfigRevisionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedK8SAddonConfigRevisionRequest
    | PatchedK8SAddonConfigRevisionRequest
    | PatchedK8SAddonConfigRevisionRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/kubernetes/addon-config-revisions/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedK8SAddonConfigRevisionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedK8SAddonConfigRevisionRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedK8SAddonConfigRevisionRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> K8SAddonConfigRevision | None:
    if response.status_code == 200:
        response_200 = K8SAddonConfigRevision.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[K8SAddonConfigRevision]:
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
    body: PatchedK8SAddonConfigRevisionRequest
    | PatchedK8SAddonConfigRevisionRequest
    | PatchedK8SAddonConfigRevisionRequest
    | Unset = UNSET,
) -> Response[K8SAddonConfigRevision]:
    """API endpoint for K8sAddonConfigRevision.
    Mutate: admin via PERMISSION_CONFIG. Spec: polycrate spec inspect 745

    Args:
        id (UUID):
        body (PatchedK8SAddonConfigRevisionRequest | Unset): Basis-Serializer für alle
            ManagedObject Detail-Endpoints.

            Enthält alle generischen Felder eines ManagedObjects.
            Subclasses erweitern diese Liste mit model-spezifischen Feldern.

            Inkludiert:
            - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
            - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
            - organization/workspace als generische ManagedObject-Referenzen (mit URL)
            - created: Kombifeld (created_at, created_at_humanized, created_by)
            - url: Absolute URL zum Object (via get_absolute_url())

            Usage:
                class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
                    class Meta(ManagedObjectDetailSerializer.Meta):
                        model = K8sCluster
                        fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']
        body (PatchedK8SAddonConfigRevisionRequest | Unset): Basis-Serializer für alle
            ManagedObject Detail-Endpoints.

            Enthält alle generischen Felder eines ManagedObjects.
            Subclasses erweitern diese Liste mit model-spezifischen Feldern.

            Inkludiert:
            - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
            - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
            - organization/workspace als generische ManagedObject-Referenzen (mit URL)
            - created: Kombifeld (created_at, created_at_humanized, created_by)
            - url: Absolute URL zum Object (via get_absolute_url())

            Usage:
                class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
                    class Meta(ManagedObjectDetailSerializer.Meta):
                        model = K8sCluster
                        fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']
        body (PatchedK8SAddonConfigRevisionRequest | Unset): Basis-Serializer für alle
            ManagedObject Detail-Endpoints.

            Enthält alle generischen Felder eines ManagedObjects.
            Subclasses erweitern diese Liste mit model-spezifischen Feldern.

            Inkludiert:
            - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
            - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
            - organization/workspace als generische ManagedObject-Referenzen (mit URL)
            - created: Kombifeld (created_at, created_at_humanized, created_by)
            - url: Absolute URL zum Object (via get_absolute_url())

            Usage:
                class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
                    class Meta(ManagedObjectDetailSerializer.Meta):
                        model = K8sCluster
                        fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SAddonConfigRevision]
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
    body: PatchedK8SAddonConfigRevisionRequest
    | PatchedK8SAddonConfigRevisionRequest
    | PatchedK8SAddonConfigRevisionRequest
    | Unset = UNSET,
) -> K8SAddonConfigRevision | None:
    """API endpoint for K8sAddonConfigRevision.
    Mutate: admin via PERMISSION_CONFIG. Spec: polycrate spec inspect 745

    Args:
        id (UUID):
        body (PatchedK8SAddonConfigRevisionRequest | Unset): Basis-Serializer für alle
            ManagedObject Detail-Endpoints.

            Enthält alle generischen Felder eines ManagedObjects.
            Subclasses erweitern diese Liste mit model-spezifischen Feldern.

            Inkludiert:
            - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
            - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
            - organization/workspace als generische ManagedObject-Referenzen (mit URL)
            - created: Kombifeld (created_at, created_at_humanized, created_by)
            - url: Absolute URL zum Object (via get_absolute_url())

            Usage:
                class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
                    class Meta(ManagedObjectDetailSerializer.Meta):
                        model = K8sCluster
                        fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']
        body (PatchedK8SAddonConfigRevisionRequest | Unset): Basis-Serializer für alle
            ManagedObject Detail-Endpoints.

            Enthält alle generischen Felder eines ManagedObjects.
            Subclasses erweitern diese Liste mit model-spezifischen Feldern.

            Inkludiert:
            - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
            - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
            - organization/workspace als generische ManagedObject-Referenzen (mit URL)
            - created: Kombifeld (created_at, created_at_humanized, created_by)
            - url: Absolute URL zum Object (via get_absolute_url())

            Usage:
                class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
                    class Meta(ManagedObjectDetailSerializer.Meta):
                        model = K8sCluster
                        fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']
        body (PatchedK8SAddonConfigRevisionRequest | Unset): Basis-Serializer für alle
            ManagedObject Detail-Endpoints.

            Enthält alle generischen Felder eines ManagedObjects.
            Subclasses erweitern diese Liste mit model-spezifischen Feldern.

            Inkludiert:
            - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
            - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
            - organization/workspace als generische ManagedObject-Referenzen (mit URL)
            - created: Kombifeld (created_at, created_at_humanized, created_by)
            - url: Absolute URL zum Object (via get_absolute_url())

            Usage:
                class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
                    class Meta(ManagedObjectDetailSerializer.Meta):
                        model = K8sCluster
                        fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SAddonConfigRevision
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
    body: PatchedK8SAddonConfigRevisionRequest
    | PatchedK8SAddonConfigRevisionRequest
    | PatchedK8SAddonConfigRevisionRequest
    | Unset = UNSET,
) -> Response[K8SAddonConfigRevision]:
    """API endpoint for K8sAddonConfigRevision.
    Mutate: admin via PERMISSION_CONFIG. Spec: polycrate spec inspect 745

    Args:
        id (UUID):
        body (PatchedK8SAddonConfigRevisionRequest | Unset): Basis-Serializer für alle
            ManagedObject Detail-Endpoints.

            Enthält alle generischen Felder eines ManagedObjects.
            Subclasses erweitern diese Liste mit model-spezifischen Feldern.

            Inkludiert:
            - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
            - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
            - organization/workspace als generische ManagedObject-Referenzen (mit URL)
            - created: Kombifeld (created_at, created_at_humanized, created_by)
            - url: Absolute URL zum Object (via get_absolute_url())

            Usage:
                class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
                    class Meta(ManagedObjectDetailSerializer.Meta):
                        model = K8sCluster
                        fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']
        body (PatchedK8SAddonConfigRevisionRequest | Unset): Basis-Serializer für alle
            ManagedObject Detail-Endpoints.

            Enthält alle generischen Felder eines ManagedObjects.
            Subclasses erweitern diese Liste mit model-spezifischen Feldern.

            Inkludiert:
            - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
            - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
            - organization/workspace als generische ManagedObject-Referenzen (mit URL)
            - created: Kombifeld (created_at, created_at_humanized, created_by)
            - url: Absolute URL zum Object (via get_absolute_url())

            Usage:
                class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
                    class Meta(ManagedObjectDetailSerializer.Meta):
                        model = K8sCluster
                        fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']
        body (PatchedK8SAddonConfigRevisionRequest | Unset): Basis-Serializer für alle
            ManagedObject Detail-Endpoints.

            Enthält alle generischen Felder eines ManagedObjects.
            Subclasses erweitern diese Liste mit model-spezifischen Feldern.

            Inkludiert:
            - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
            - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
            - organization/workspace als generische ManagedObject-Referenzen (mit URL)
            - created: Kombifeld (created_at, created_at_humanized, created_by)
            - url: Absolute URL zum Object (via get_absolute_url())

            Usage:
                class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
                    class Meta(ManagedObjectDetailSerializer.Meta):
                        model = K8sCluster
                        fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SAddonConfigRevision]
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
    body: PatchedK8SAddonConfigRevisionRequest
    | PatchedK8SAddonConfigRevisionRequest
    | PatchedK8SAddonConfigRevisionRequest
    | Unset = UNSET,
) -> K8SAddonConfigRevision | None:
    """API endpoint for K8sAddonConfigRevision.
    Mutate: admin via PERMISSION_CONFIG. Spec: polycrate spec inspect 745

    Args:
        id (UUID):
        body (PatchedK8SAddonConfigRevisionRequest | Unset): Basis-Serializer für alle
            ManagedObject Detail-Endpoints.

            Enthält alle generischen Felder eines ManagedObjects.
            Subclasses erweitern diese Liste mit model-spezifischen Feldern.

            Inkludiert:
            - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
            - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
            - organization/workspace als generische ManagedObject-Referenzen (mit URL)
            - created: Kombifeld (created_at, created_at_humanized, created_by)
            - url: Absolute URL zum Object (via get_absolute_url())

            Usage:
                class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
                    class Meta(ManagedObjectDetailSerializer.Meta):
                        model = K8sCluster
                        fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']
        body (PatchedK8SAddonConfigRevisionRequest | Unset): Basis-Serializer für alle
            ManagedObject Detail-Endpoints.

            Enthält alle generischen Felder eines ManagedObjects.
            Subclasses erweitern diese Liste mit model-spezifischen Feldern.

            Inkludiert:
            - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
            - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
            - organization/workspace als generische ManagedObject-Referenzen (mit URL)
            - created: Kombifeld (created_at, created_at_humanized, created_by)
            - url: Absolute URL zum Object (via get_absolute_url())

            Usage:
                class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
                    class Meta(ManagedObjectDetailSerializer.Meta):
                        model = K8sCluster
                        fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']
        body (PatchedK8SAddonConfigRevisionRequest | Unset): Basis-Serializer für alle
            ManagedObject Detail-Endpoints.

            Enthält alle generischen Felder eines ManagedObjects.
            Subclasses erweitern diese Liste mit model-spezifischen Feldern.

            Inkludiert:
            - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
            - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
            - organization/workspace als generische ManagedObject-Referenzen (mit URL)
            - created: Kombifeld (created_at, created_at_humanized, created_by)
            - url: Absolute URL zum Object (via get_absolute_url())

            Usage:
                class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
                    class Meta(ManagedObjectDetailSerializer.Meta):
                        model = K8sCluster
                        fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SAddonConfigRevision
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
