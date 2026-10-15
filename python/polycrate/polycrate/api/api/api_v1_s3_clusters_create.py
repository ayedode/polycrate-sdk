from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.s3_cluster import S3Cluster
from ...models.s3_cluster_request import S3ClusterRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: S3ClusterRequest | S3ClusterRequest | S3ClusterRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/s3/clusters/",
    }

    if isinstance(body, S3ClusterRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, S3ClusterRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, S3ClusterRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> S3Cluster | None:
    if response.status_code == 201:
        response_201 = S3Cluster.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: S3ClusterRequest | S3ClusterRequest | S3ClusterRequest | Unset = UNSET,
) -> Response[S3Cluster]:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (S3ClusterRequest): S3Cluster detail — ManagedObjectDetailSerializer like K8sApp;
            workspace resolved via k8s_cluster FK.
        body (S3ClusterRequest): S3Cluster detail — ManagedObjectDetailSerializer like K8sApp;
            workspace resolved via k8s_cluster FK.
        body (S3ClusterRequest): S3Cluster detail — ManagedObjectDetailSerializer like K8sApp;
            workspace resolved via k8s_cluster FK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3Cluster]
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
    body: S3ClusterRequest | S3ClusterRequest | S3ClusterRequest | Unset = UNSET,
) -> S3Cluster | None:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (S3ClusterRequest): S3Cluster detail — ManagedObjectDetailSerializer like K8sApp;
            workspace resolved via k8s_cluster FK.
        body (S3ClusterRequest): S3Cluster detail — ManagedObjectDetailSerializer like K8sApp;
            workspace resolved via k8s_cluster FK.
        body (S3ClusterRequest): S3Cluster detail — ManagedObjectDetailSerializer like K8sApp;
            workspace resolved via k8s_cluster FK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3Cluster
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: S3ClusterRequest | S3ClusterRequest | S3ClusterRequest | Unset = UNSET,
) -> Response[S3Cluster]:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (S3ClusterRequest): S3Cluster detail — ManagedObjectDetailSerializer like K8sApp;
            workspace resolved via k8s_cluster FK.
        body (S3ClusterRequest): S3Cluster detail — ManagedObjectDetailSerializer like K8sApp;
            workspace resolved via k8s_cluster FK.
        body (S3ClusterRequest): S3Cluster detail — ManagedObjectDetailSerializer like K8sApp;
            workspace resolved via k8s_cluster FK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3Cluster]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: S3ClusterRequest | S3ClusterRequest | S3ClusterRequest | Unset = UNSET,
) -> S3Cluster | None:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (S3ClusterRequest): S3Cluster detail — ManagedObjectDetailSerializer like K8sApp;
            workspace resolved via k8s_cluster FK.
        body (S3ClusterRequest): S3Cluster detail — ManagedObjectDetailSerializer like K8sApp;
            workspace resolved via k8s_cluster FK.
        body (S3ClusterRequest): S3Cluster detail — ManagedObjectDetailSerializer like K8sApp;
            workspace resolved via k8s_cluster FK.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3Cluster
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
