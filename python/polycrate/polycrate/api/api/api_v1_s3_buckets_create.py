from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.s3_bucket_region_request import S3BucketRegionRequest
from ...models.s3_bucket_region_response import S3BucketRegionResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: S3BucketRegionRequest | S3BucketRegionRequest | S3BucketRegionRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/s3/buckets/",
    }

    if isinstance(body, S3BucketRegionRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, S3BucketRegionRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, S3BucketRegionRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> S3BucketRegionResponse | None:
    if response.status_code == 201:
        response_201 = S3BucketRegionResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[S3BucketRegionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: S3BucketRegionRequest | S3BucketRegionRequest | S3BucketRegionRequest | Unset = UNSET,
) -> Response[S3BucketRegionResponse]:
    """Create a new S3 Bucket. Agent tokens: workspace/organization auto-assigned. Regular users: provide
    workspace/organization in body.

    Args:
        body (S3BucketRegionRequest): Serializer für Bucket-Erstellung mit Region-UUID.

            Accepts `region` as a workspaces.Region UUID (write-only). Create writes
            the Region FK only — no S3Cluster resolve (Spec 896). Falls back to
            SystemConfig.default_s3_region when region is omitted.
        body (S3BucketRegionRequest): Serializer für Bucket-Erstellung mit Region-UUID.

            Accepts `region` as a workspaces.Region UUID (write-only). Create writes
            the Region FK only — no S3Cluster resolve (Spec 896). Falls back to
            SystemConfig.default_s3_region when region is omitted.
        body (S3BucketRegionRequest): Serializer für Bucket-Erstellung mit Region-UUID.

            Accepts `region` as a workspaces.Region UUID (write-only). Create writes
            the Region FK only — no S3Cluster resolve (Spec 896). Falls back to
            SystemConfig.default_s3_region when region is omitted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3BucketRegionResponse]
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
    body: S3BucketRegionRequest | S3BucketRegionRequest | S3BucketRegionRequest | Unset = UNSET,
) -> S3BucketRegionResponse | None:
    """Create a new S3 Bucket. Agent tokens: workspace/organization auto-assigned. Regular users: provide
    workspace/organization in body.

    Args:
        body (S3BucketRegionRequest): Serializer für Bucket-Erstellung mit Region-UUID.

            Accepts `region` as a workspaces.Region UUID (write-only). Create writes
            the Region FK only — no S3Cluster resolve (Spec 896). Falls back to
            SystemConfig.default_s3_region when region is omitted.
        body (S3BucketRegionRequest): Serializer für Bucket-Erstellung mit Region-UUID.

            Accepts `region` as a workspaces.Region UUID (write-only). Create writes
            the Region FK only — no S3Cluster resolve (Spec 896). Falls back to
            SystemConfig.default_s3_region when region is omitted.
        body (S3BucketRegionRequest): Serializer für Bucket-Erstellung mit Region-UUID.

            Accepts `region` as a workspaces.Region UUID (write-only). Create writes
            the Region FK only — no S3Cluster resolve (Spec 896). Falls back to
            SystemConfig.default_s3_region when region is omitted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3BucketRegionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: S3BucketRegionRequest | S3BucketRegionRequest | S3BucketRegionRequest | Unset = UNSET,
) -> Response[S3BucketRegionResponse]:
    """Create a new S3 Bucket. Agent tokens: workspace/organization auto-assigned. Regular users: provide
    workspace/organization in body.

    Args:
        body (S3BucketRegionRequest): Serializer für Bucket-Erstellung mit Region-UUID.

            Accepts `region` as a workspaces.Region UUID (write-only). Create writes
            the Region FK only — no S3Cluster resolve (Spec 896). Falls back to
            SystemConfig.default_s3_region when region is omitted.
        body (S3BucketRegionRequest): Serializer für Bucket-Erstellung mit Region-UUID.

            Accepts `region` as a workspaces.Region UUID (write-only). Create writes
            the Region FK only — no S3Cluster resolve (Spec 896). Falls back to
            SystemConfig.default_s3_region when region is omitted.
        body (S3BucketRegionRequest): Serializer für Bucket-Erstellung mit Region-UUID.

            Accepts `region` as a workspaces.Region UUID (write-only). Create writes
            the Region FK only — no S3Cluster resolve (Spec 896). Falls back to
            SystemConfig.default_s3_region when region is omitted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3BucketRegionResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: S3BucketRegionRequest | S3BucketRegionRequest | S3BucketRegionRequest | Unset = UNSET,
) -> S3BucketRegionResponse | None:
    """Create a new S3 Bucket. Agent tokens: workspace/organization auto-assigned. Regular users: provide
    workspace/organization in body.

    Args:
        body (S3BucketRegionRequest): Serializer für Bucket-Erstellung mit Region-UUID.

            Accepts `region` as a workspaces.Region UUID (write-only). Create writes
            the Region FK only — no S3Cluster resolve (Spec 896). Falls back to
            SystemConfig.default_s3_region when region is omitted.
        body (S3BucketRegionRequest): Serializer für Bucket-Erstellung mit Region-UUID.

            Accepts `region` as a workspaces.Region UUID (write-only). Create writes
            the Region FK only — no S3Cluster resolve (Spec 896). Falls back to
            SystemConfig.default_s3_region when region is omitted.
        body (S3BucketRegionRequest): Serializer für Bucket-Erstellung mit Region-UUID.

            Accepts `region` as a workspaces.Region UUID (write-only). Create writes
            the Region FK only — no S3Cluster resolve (Spec 896). Falls back to
            SystemConfig.default_s3_region when region is omitted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3BucketRegionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
