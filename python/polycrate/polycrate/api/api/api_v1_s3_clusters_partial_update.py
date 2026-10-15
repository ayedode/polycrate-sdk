from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_s3_cluster_request import PatchedS3ClusterRequest
from ...models.s3_cluster import S3Cluster
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedS3ClusterRequest | PatchedS3ClusterRequest | PatchedS3ClusterRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/s3/clusters/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedS3ClusterRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedS3ClusterRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedS3ClusterRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> S3Cluster | None:
    if response.status_code == 200:
        response_200 = S3Cluster.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[S3Cluster]:
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
    body: PatchedS3ClusterRequest | PatchedS3ClusterRequest | PatchedS3ClusterRequest | Unset = UNSET,
) -> Response[S3Cluster]:
    """API endpoint that allows S3 Clusters to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (PatchedS3ClusterRequest | Unset): S3Cluster detail — ManagedObjectDetailSerializer
            like K8sApp; workspace resolved via k8s_cluster FK.
        body (PatchedS3ClusterRequest | Unset): S3Cluster detail — ManagedObjectDetailSerializer
            like K8sApp; workspace resolved via k8s_cluster FK.
        body (PatchedS3ClusterRequest | Unset): S3Cluster detail — ManagedObjectDetailSerializer
            like K8sApp; workspace resolved via k8s_cluster FK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3Cluster]
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
    body: PatchedS3ClusterRequest | PatchedS3ClusterRequest | PatchedS3ClusterRequest | Unset = UNSET,
) -> S3Cluster | None:
    """API endpoint that allows S3 Clusters to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (PatchedS3ClusterRequest | Unset): S3Cluster detail — ManagedObjectDetailSerializer
            like K8sApp; workspace resolved via k8s_cluster FK.
        body (PatchedS3ClusterRequest | Unset): S3Cluster detail — ManagedObjectDetailSerializer
            like K8sApp; workspace resolved via k8s_cluster FK.
        body (PatchedS3ClusterRequest | Unset): S3Cluster detail — ManagedObjectDetailSerializer
            like K8sApp; workspace resolved via k8s_cluster FK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3Cluster
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
    body: PatchedS3ClusterRequest | PatchedS3ClusterRequest | PatchedS3ClusterRequest | Unset = UNSET,
) -> Response[S3Cluster]:
    """API endpoint that allows S3 Clusters to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (PatchedS3ClusterRequest | Unset): S3Cluster detail — ManagedObjectDetailSerializer
            like K8sApp; workspace resolved via k8s_cluster FK.
        body (PatchedS3ClusterRequest | Unset): S3Cluster detail — ManagedObjectDetailSerializer
            like K8sApp; workspace resolved via k8s_cluster FK.
        body (PatchedS3ClusterRequest | Unset): S3Cluster detail — ManagedObjectDetailSerializer
            like K8sApp; workspace resolved via k8s_cluster FK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3Cluster]
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
    body: PatchedS3ClusterRequest | PatchedS3ClusterRequest | PatchedS3ClusterRequest | Unset = UNSET,
) -> S3Cluster | None:
    """API endpoint that allows S3 Clusters to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (PatchedS3ClusterRequest | Unset): S3Cluster detail — ManagedObjectDetailSerializer
            like K8sApp; workspace resolved via k8s_cluster FK.
        body (PatchedS3ClusterRequest | Unset): S3Cluster detail — ManagedObjectDetailSerializer
            like K8sApp; workspace resolved via k8s_cluster FK.
        body (PatchedS3ClusterRequest | Unset): S3Cluster detail — ManagedObjectDetailSerializer
            like K8sApp; workspace resolved via k8s_cluster FK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3Cluster
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
