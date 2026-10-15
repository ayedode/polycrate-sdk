from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dns_record_detail import DNSRecordDetail
from ...models.patched_dns_record_detail_request import PatchedDNSRecordDetailRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: PatchedDNSRecordDetailRequest | PatchedDNSRecordDetailRequest | PatchedDNSRecordDetailRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/domains/dnsrecords/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedDNSRecordDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedDNSRecordDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedDNSRecordDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DNSRecordDetail | None:
    if response.status_code == 200:
        response_200 = DNSRecordDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DNSRecordDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedDNSRecordDetailRequest | PatchedDNSRecordDetailRequest | PatchedDNSRecordDetailRequest | Unset = UNSET,
) -> Response[DNSRecordDetail]:
    """CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind="internal"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind="external"`: records live only at the provider; the API passes
      operations straight through to python-lexicon.

    For external zones, `?dns_zone=<uuid>` is REQUIRED on list, and
    provider-assigned record IDs are used as the detail PK.

    Spec: polycrate spec inspect 137
    Spec 492: Composite ID fix for external records.

    Args:
        id (str):
        body (PatchedDNSRecordDetailRequest | Unset): Basis-Serializer für alle ManagedObject
            Detail-Endpoints.

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
        body (PatchedDNSRecordDetailRequest | Unset): Basis-Serializer für alle ManagedObject
            Detail-Endpoints.

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
        body (PatchedDNSRecordDetailRequest | Unset): Basis-Serializer für alle ManagedObject
            Detail-Endpoints.

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
        Response[DNSRecordDetail]
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedDNSRecordDetailRequest | PatchedDNSRecordDetailRequest | PatchedDNSRecordDetailRequest | Unset = UNSET,
) -> DNSRecordDetail | None:
    """CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind="internal"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind="external"`: records live only at the provider; the API passes
      operations straight through to python-lexicon.

    For external zones, `?dns_zone=<uuid>` is REQUIRED on list, and
    provider-assigned record IDs are used as the detail PK.

    Spec: polycrate spec inspect 137
    Spec 492: Composite ID fix for external records.

    Args:
        id (str):
        body (PatchedDNSRecordDetailRequest | Unset): Basis-Serializer für alle ManagedObject
            Detail-Endpoints.

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
        body (PatchedDNSRecordDetailRequest | Unset): Basis-Serializer für alle ManagedObject
            Detail-Endpoints.

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
        body (PatchedDNSRecordDetailRequest | Unset): Basis-Serializer für alle ManagedObject
            Detail-Endpoints.

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
        DNSRecordDetail
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedDNSRecordDetailRequest | PatchedDNSRecordDetailRequest | PatchedDNSRecordDetailRequest | Unset = UNSET,
) -> Response[DNSRecordDetail]:
    """CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind="internal"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind="external"`: records live only at the provider; the API passes
      operations straight through to python-lexicon.

    For external zones, `?dns_zone=<uuid>` is REQUIRED on list, and
    provider-assigned record IDs are used as the detail PK.

    Spec: polycrate spec inspect 137
    Spec 492: Composite ID fix for external records.

    Args:
        id (str):
        body (PatchedDNSRecordDetailRequest | Unset): Basis-Serializer für alle ManagedObject
            Detail-Endpoints.

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
        body (PatchedDNSRecordDetailRequest | Unset): Basis-Serializer für alle ManagedObject
            Detail-Endpoints.

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
        body (PatchedDNSRecordDetailRequest | Unset): Basis-Serializer für alle ManagedObject
            Detail-Endpoints.

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
        Response[DNSRecordDetail]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedDNSRecordDetailRequest | PatchedDNSRecordDetailRequest | PatchedDNSRecordDetailRequest | Unset = UNSET,
) -> DNSRecordDetail | None:
    """CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind="internal"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind="external"`: records live only at the provider; the API passes
      operations straight through to python-lexicon.

    For external zones, `?dns_zone=<uuid>` is REQUIRED on list, and
    provider-assigned record IDs are used as the detail PK.

    Spec: polycrate spec inspect 137
    Spec 492: Composite ID fix for external records.

    Args:
        id (str):
        body (PatchedDNSRecordDetailRequest | Unset): Basis-Serializer für alle ManagedObject
            Detail-Endpoints.

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
        body (PatchedDNSRecordDetailRequest | Unset): Basis-Serializer für alle ManagedObject
            Detail-Endpoints.

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
        body (PatchedDNSRecordDetailRequest | Unset): Basis-Serializer für alle ManagedObject
            Detail-Endpoints.

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
        DNSRecordDetail
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
