from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.s3_bucket_update import S3BucketUpdate
from ...models.s3_bucket_update_request import S3BucketUpdateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: S3BucketUpdateRequest | S3BucketUpdateRequest | S3BucketUpdateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/s3/buckets/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, S3BucketUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, S3BucketUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, S3BucketUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> S3BucketUpdate | None:
    if response.status_code == 200:
        response_200 = S3BucketUpdate.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[S3BucketUpdate]:
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
    body: S3BucketUpdateRequest | S3BucketUpdateRequest | S3BucketUpdateRequest | Unset = UNSET,
) -> Response[S3BucketUpdate]:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (S3BucketUpdateRequest | Unset):
        body (S3BucketUpdateRequest | Unset):
        body (S3BucketUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3BucketUpdate]
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
    body: S3BucketUpdateRequest | S3BucketUpdateRequest | S3BucketUpdateRequest | Unset = UNSET,
) -> S3BucketUpdate | None:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (S3BucketUpdateRequest | Unset):
        body (S3BucketUpdateRequest | Unset):
        body (S3BucketUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3BucketUpdate
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
    body: S3BucketUpdateRequest | S3BucketUpdateRequest | S3BucketUpdateRequest | Unset = UNSET,
) -> Response[S3BucketUpdate]:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (S3BucketUpdateRequest | Unset):
        body (S3BucketUpdateRequest | Unset):
        body (S3BucketUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3BucketUpdate]
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
    body: S3BucketUpdateRequest | S3BucketUpdateRequest | S3BucketUpdateRequest | Unset = UNSET,
) -> S3BucketUpdate | None:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (S3BucketUpdateRequest | Unset):
        body (S3BucketUpdateRequest | Unset):
        body (S3BucketUpdateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3BucketUpdate
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
