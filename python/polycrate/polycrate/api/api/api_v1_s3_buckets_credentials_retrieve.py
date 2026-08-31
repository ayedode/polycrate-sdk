from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_409 import ErrorResponse409
from ...models.error_response_410 import ErrorResponse410
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.error_response_502 import ErrorResponse502
from ...models.parse_error_response import ParseErrorResponse
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
) -> (
    Any
    | ErrorResponse401
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | ParseErrorResponse
    | S3CredentialListResponse
    | None
):
    if response.status_code == 200:
        response_200 = S3CredentialListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ParseErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 405:
        response_405 = ErrorResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = ErrorResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = ErrorResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = ErrorResponse410.from_dict(response.json())

        return response_410

    if response.status_code == 415:
        response_415 = ErrorResponse415.from_dict(response.json())

        return response_415

    if response.status_code == 500:
        response_500 = ErrorResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ErrorResponse502.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ErrorResponse401
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | ParseErrorResponse
    | S3CredentialListResponse
]:
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
) -> Response[
    Any
    | ErrorResponse401
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | ParseErrorResponse
    | S3CredentialListResponse
]:
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
        Response[Any | ErrorResponse401 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | ParseErrorResponse | S3CredentialListResponse]
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
) -> (
    Any
    | ErrorResponse401
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | ParseErrorResponse
    | S3CredentialListResponse
    | None
):
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
        Any | ErrorResponse401 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | ParseErrorResponse | S3CredentialListResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | ErrorResponse401
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | ParseErrorResponse
    | S3CredentialListResponse
]:
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
        Response[Any | ErrorResponse401 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | ParseErrorResponse | S3CredentialListResponse]
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
) -> (
    Any
    | ErrorResponse401
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | ParseErrorResponse
    | S3CredentialListResponse
    | None
):
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
        Any | ErrorResponse401 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | ParseErrorResponse | S3CredentialListResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
