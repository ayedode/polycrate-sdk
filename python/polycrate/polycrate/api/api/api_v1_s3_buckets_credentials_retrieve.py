from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.s3_credential_list_response import S3CredentialListResponse
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/s3/buckets/{id}/credentials/".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | S3CredentialListResponse | None:
    if response.status_code == 200:
        response_200 = S3CredentialListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | S3CredentialListResponse]:
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
) -> Response[Any | S3CredentialListResponse]:
    """List bucket access keys


            Returns all access keys (primary and additional) for a specific S3 bucket.

            Response uses the legacy StandardAPIResponseMixin envelope
            (`success` / `data.credentials` / `meta`). Credentials include
            `access_key` and `secret_key` (Spec 508 — restore pre-0.23.0 contract).

            Additional access keys via RadosGW sub-users are only available for
            rook-ceph clusters. MinIO clusters do not support sub-user management.


    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | S3CredentialListResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | S3CredentialListResponse | None:
    """List bucket access keys


            Returns all access keys (primary and additional) for a specific S3 bucket.

            Response uses the legacy StandardAPIResponseMixin envelope
            (`success` / `data.credentials` / `meta`). Credentials include
            `access_key` and `secret_key` (Spec 508 — restore pre-0.23.0 contract).

            Additional access keys via RadosGW sub-users are only available for
            rook-ceph clusters. MinIO clusters do not support sub-user management.


    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | S3CredentialListResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | S3CredentialListResponse]:
    """List bucket access keys


            Returns all access keys (primary and additional) for a specific S3 bucket.

            Response uses the legacy StandardAPIResponseMixin envelope
            (`success` / `data.credentials` / `meta`). Credentials include
            `access_key` and `secret_key` (Spec 508 — restore pre-0.23.0 contract).

            Additional access keys via RadosGW sub-users are only available for
            rook-ceph clusters. MinIO clusters do not support sub-user management.


    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | S3CredentialListResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | S3CredentialListResponse | None:
    """List bucket access keys


            Returns all access keys (primary and additional) for a specific S3 bucket.

            Response uses the legacy StandardAPIResponseMixin envelope
            (`success` / `data.credentials` / `meta`). Credentials include
            `access_key` and `secret_key` (Spec 508 — restore pre-0.23.0 contract).

            Additional access keys via RadosGW sub-users are only available for
            rook-ceph clusters. MinIO clusters do not support sub-user management.


    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | S3CredentialListResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
