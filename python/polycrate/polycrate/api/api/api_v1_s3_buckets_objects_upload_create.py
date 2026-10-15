from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.s3_object_upload_request_request import S3ObjectUploadRequestRequest
from ...models.s3_object_upload_response import S3ObjectUploadResponse
from ...types import Response


def _get_kwargs(
    id: UUID,
    *,
    body: S3ObjectUploadRequestRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/s3/buckets/{id}/objects/upload/".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> S3ObjectUploadResponse | None:
    if response.status_code == 201:
        response_201 = S3ObjectUploadResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[S3ObjectUploadResponse]:
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
    body: S3ObjectUploadRequestRequest,
) -> Response[S3ObjectUploadResponse]:
    """Upload an object to the bucket

     API endpoint that allows S3 Buckets to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (S3ObjectUploadRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3ObjectUploadResponse]
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
    body: S3ObjectUploadRequestRequest,
) -> S3ObjectUploadResponse | None:
    """Upload an object to the bucket

     API endpoint that allows S3 Buckets to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (S3ObjectUploadRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3ObjectUploadResponse
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
    body: S3ObjectUploadRequestRequest,
) -> Response[S3ObjectUploadResponse]:
    """Upload an object to the bucket

     API endpoint that allows S3 Buckets to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (S3ObjectUploadRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3ObjectUploadResponse]
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
    body: S3ObjectUploadRequestRequest,
) -> S3ObjectUploadResponse | None:
    """Upload an object to the bucket

     API endpoint that allows S3 Buckets to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (S3ObjectUploadRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3ObjectUploadResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
