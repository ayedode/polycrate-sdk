from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.s3_bucket_policy_request import S3BucketPolicyRequest
from ...models.s3_bucket_policy_response import S3BucketPolicyResponse
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: S3BucketPolicyRequest | S3BucketPolicyRequest | S3BucketPolicyRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/s3/buckets/{id}/policy/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, S3BucketPolicyRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, S3BucketPolicyRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, S3BucketPolicyRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> S3BucketPolicyResponse | None:
    if response.status_code == 200:
        response_200 = S3BucketPolicyResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[S3BucketPolicyResponse]:
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
    body: S3BucketPolicyRequest | S3BucketPolicyRequest | S3BucketPolicyRequest | Unset = UNSET,
) -> Response[S3BucketPolicyResponse]:
    """Get bucket policy

     API endpoint that allows S3 Buckets to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (S3BucketPolicyRequest):
        body (S3BucketPolicyRequest):
        body (S3BucketPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3BucketPolicyResponse]
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
    body: S3BucketPolicyRequest | S3BucketPolicyRequest | S3BucketPolicyRequest | Unset = UNSET,
) -> S3BucketPolicyResponse | None:
    """Get bucket policy

     API endpoint that allows S3 Buckets to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (S3BucketPolicyRequest):
        body (S3BucketPolicyRequest):
        body (S3BucketPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3BucketPolicyResponse
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
    body: S3BucketPolicyRequest | S3BucketPolicyRequest | S3BucketPolicyRequest | Unset = UNSET,
) -> Response[S3BucketPolicyResponse]:
    """Get bucket policy

     API endpoint that allows S3 Buckets to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (S3BucketPolicyRequest):
        body (S3BucketPolicyRequest):
        body (S3BucketPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3BucketPolicyResponse]
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
    body: S3BucketPolicyRequest | S3BucketPolicyRequest | S3BucketPolicyRequest | Unset = UNSET,
) -> S3BucketPolicyResponse | None:
    """Get bucket policy

     API endpoint that allows S3 Buckets to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (S3BucketPolicyRequest):
        body (S3BucketPolicyRequest):
        body (S3BucketPolicyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3BucketPolicyResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
