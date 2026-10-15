from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.s3_object_list_response import S3ObjectListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    continuation_token: str | Unset = UNSET,
    delimiter: str | Unset = "/",
    max_keys: int | Unset = 100,
    prefix: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["continuation_token"] = continuation_token

    params["delimiter"] = delimiter

    params["max_keys"] = max_keys

    params["prefix"] = prefix

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/s3/buckets/{id}/objects/".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> S3ObjectListResponse | None:
    if response.status_code == 200:
        response_200 = S3ObjectListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[S3ObjectListResponse]:
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
    continuation_token: str | Unset = UNSET,
    delimiter: str | Unset = "/",
    max_keys: int | Unset = 100,
    prefix: str | Unset = "",
) -> Response[S3ObjectListResponse]:
    """List objects in bucket

     API endpoint that allows S3 Buckets to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        continuation_token (str | Unset):
        delimiter (str | Unset):  Default: '/'.
        max_keys (int | Unset):  Default: 100.
        prefix (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3ObjectListResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        continuation_token=continuation_token,
        delimiter=delimiter,
        max_keys=max_keys,
        prefix=prefix,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    continuation_token: str | Unset = UNSET,
    delimiter: str | Unset = "/",
    max_keys: int | Unset = 100,
    prefix: str | Unset = "",
) -> S3ObjectListResponse | None:
    """List objects in bucket

     API endpoint that allows S3 Buckets to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        continuation_token (str | Unset):
        delimiter (str | Unset):  Default: '/'.
        max_keys (int | Unset):  Default: 100.
        prefix (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3ObjectListResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        continuation_token=continuation_token,
        delimiter=delimiter,
        max_keys=max_keys,
        prefix=prefix,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    continuation_token: str | Unset = UNSET,
    delimiter: str | Unset = "/",
    max_keys: int | Unset = 100,
    prefix: str | Unset = "",
) -> Response[S3ObjectListResponse]:
    """List objects in bucket

     API endpoint that allows S3 Buckets to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        continuation_token (str | Unset):
        delimiter (str | Unset):  Default: '/'.
        max_keys (int | Unset):  Default: 100.
        prefix (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[S3ObjectListResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        continuation_token=continuation_token,
        delimiter=delimiter,
        max_keys=max_keys,
        prefix=prefix,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    continuation_token: str | Unset = UNSET,
    delimiter: str | Unset = "/",
    max_keys: int | Unset = 100,
    prefix: str | Unset = "",
) -> S3ObjectListResponse | None:
    """List objects in bucket

     API endpoint that allows S3 Buckets to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        continuation_token (str | Unset):
        delimiter (str | Unset):  Default: '/'.
        max_keys (int | Unset):  Default: 100.
        prefix (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        S3ObjectListResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            continuation_token=continuation_token,
            delimiter=delimiter,
            max_keys=max_keys,
            prefix=prefix,
        )
    ).parsed
