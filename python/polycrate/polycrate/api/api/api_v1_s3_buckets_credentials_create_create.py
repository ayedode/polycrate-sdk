from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1s3_buckets_credentials_create_create_response_201 import (
    ApiV1S3BucketsCredentialsCreateCreateResponse201,
)
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_404 import ErrorResponse404
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_409 import ErrorResponse409
from ...models.error_response_410 import ErrorResponse410
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.error_response_502 import ErrorResponse502
from ...models.s3_credential_create_request import S3CredentialCreateRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: S3CredentialCreateRequest | S3CredentialCreateRequest | S3CredentialCreateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/s3/buckets/{id}/credentials/create/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, S3CredentialCreateRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, S3CredentialCreateRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, S3CredentialCreateRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ApiV1S3BucketsCredentialsCreateCreateResponse201
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | None
):
    if response.status_code == 201:
        response_201 = ApiV1S3BucketsCredentialsCreateCreateResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse404.from_dict(response.json())

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
    | ApiV1S3BucketsCredentialsCreateCreateResponse201
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
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
    body: S3CredentialCreateRequest | S3CredentialCreateRequest | S3CredentialCreateRequest | Unset = UNSET,
) -> Response[
    Any
    | ApiV1S3BucketsCredentialsCreateCreateResponse201
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
]:
    """Create bucket access key


            Creates a new access key for a specific S3 bucket using RadosGW sub-users.

            **Only available for rook-ceph (RadosGW) clusters. MinIO clusters do not support
            sub-user management and will return 400.**

            Response uses the legacy StandardAPIResponseMixin envelope
            (`success` / `data` / `message`). `data` includes `access_key` and `secret_key`
            (Spec 508 — restore pre-0.23.0 contract).


    Args:
        id (UUID):
        body (S3CredentialCreateRequest): Serializer für Access Key Erstellung
        body (S3CredentialCreateRequest): Serializer für Access Key Erstellung
        body (S3CredentialCreateRequest): Serializer für Access Key Erstellung

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1S3BucketsCredentialsCreateCreateResponse201 | ErrorResponse401 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502]
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
    body: S3CredentialCreateRequest | S3CredentialCreateRequest | S3CredentialCreateRequest | Unset = UNSET,
) -> (
    Any
    | ApiV1S3BucketsCredentialsCreateCreateResponse201
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | None
):
    """Create bucket access key


            Creates a new access key for a specific S3 bucket using RadosGW sub-users.

            **Only available for rook-ceph (RadosGW) clusters. MinIO clusters do not support
            sub-user management and will return 400.**

            Response uses the legacy StandardAPIResponseMixin envelope
            (`success` / `data` / `message`). `data` includes `access_key` and `secret_key`
            (Spec 508 — restore pre-0.23.0 contract).


    Args:
        id (UUID):
        body (S3CredentialCreateRequest): Serializer für Access Key Erstellung
        body (S3CredentialCreateRequest): Serializer für Access Key Erstellung
        body (S3CredentialCreateRequest): Serializer für Access Key Erstellung

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1S3BucketsCredentialsCreateCreateResponse201 | ErrorResponse401 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502
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
    body: S3CredentialCreateRequest | S3CredentialCreateRequest | S3CredentialCreateRequest | Unset = UNSET,
) -> Response[
    Any
    | ApiV1S3BucketsCredentialsCreateCreateResponse201
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
]:
    """Create bucket access key


            Creates a new access key for a specific S3 bucket using RadosGW sub-users.

            **Only available for rook-ceph (RadosGW) clusters. MinIO clusters do not support
            sub-user management and will return 400.**

            Response uses the legacy StandardAPIResponseMixin envelope
            (`success` / `data` / `message`). `data` includes `access_key` and `secret_key`
            (Spec 508 — restore pre-0.23.0 contract).


    Args:
        id (UUID):
        body (S3CredentialCreateRequest): Serializer für Access Key Erstellung
        body (S3CredentialCreateRequest): Serializer für Access Key Erstellung
        body (S3CredentialCreateRequest): Serializer für Access Key Erstellung

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1S3BucketsCredentialsCreateCreateResponse201 | ErrorResponse401 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502]
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
    body: S3CredentialCreateRequest | S3CredentialCreateRequest | S3CredentialCreateRequest | Unset = UNSET,
) -> (
    Any
    | ApiV1S3BucketsCredentialsCreateCreateResponse201
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | None
):
    """Create bucket access key


            Creates a new access key for a specific S3 bucket using RadosGW sub-users.

            **Only available for rook-ceph (RadosGW) clusters. MinIO clusters do not support
            sub-user management and will return 400.**

            Response uses the legacy StandardAPIResponseMixin envelope
            (`success` / `data` / `message`). `data` includes `access_key` and `secret_key`
            (Spec 508 — restore pre-0.23.0 contract).


    Args:
        id (UUID):
        body (S3CredentialCreateRequest): Serializer für Access Key Erstellung
        body (S3CredentialCreateRequest): Serializer für Access Key Erstellung
        body (S3CredentialCreateRequest): Serializer für Access Key Erstellung

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1S3BucketsCredentialsCreateCreateResponse201 | ErrorResponse401 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
