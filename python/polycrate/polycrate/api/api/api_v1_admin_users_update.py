from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_admin_write import UserAdminWrite
from ...models.user_admin_write_request import UserAdminWriteRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: UserAdminWriteRequest | UserAdminWriteRequest | UserAdminWriteRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/admin/users/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, UserAdminWriteRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UserAdminWriteRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UserAdminWriteRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UserAdminWrite | None:
    if response.status_code == 200:
        response_200 = UserAdminWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UserAdminWrite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UserAdminWriteRequest | UserAdminWriteRequest | UserAdminWriteRequest | Unset = UNSET,
) -> Response[UserAdminWrite]:
    """Admin-only API endpoint with full CRUD for user management.
    Spec: polycrate spec inspect 131 / 525 / 561

    Args:
        id (int):
        body (UserAdminWriteRequest): Writable serializer for admin user CRUD.

            keycloak_user_id is intentionally omitted (read-only / provision-managed).
            Spec: polycrate spec inspect 131 / 525
        body (UserAdminWriteRequest): Writable serializer for admin user CRUD.

            keycloak_user_id is intentionally omitted (read-only / provision-managed).
            Spec: polycrate spec inspect 131 / 525
        body (UserAdminWriteRequest): Writable serializer for admin user CRUD.

            keycloak_user_id is intentionally omitted (read-only / provision-managed).
            Spec: polycrate spec inspect 131 / 525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserAdminWrite]
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
    id: int,
    *,
    client: AuthenticatedClient,
    body: UserAdminWriteRequest | UserAdminWriteRequest | UserAdminWriteRequest | Unset = UNSET,
) -> UserAdminWrite | None:
    """Admin-only API endpoint with full CRUD for user management.
    Spec: polycrate spec inspect 131 / 525 / 561

    Args:
        id (int):
        body (UserAdminWriteRequest): Writable serializer for admin user CRUD.

            keycloak_user_id is intentionally omitted (read-only / provision-managed).
            Spec: polycrate spec inspect 131 / 525
        body (UserAdminWriteRequest): Writable serializer for admin user CRUD.

            keycloak_user_id is intentionally omitted (read-only / provision-managed).
            Spec: polycrate spec inspect 131 / 525
        body (UserAdminWriteRequest): Writable serializer for admin user CRUD.

            keycloak_user_id is intentionally omitted (read-only / provision-managed).
            Spec: polycrate spec inspect 131 / 525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserAdminWrite
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UserAdminWriteRequest | UserAdminWriteRequest | UserAdminWriteRequest | Unset = UNSET,
) -> Response[UserAdminWrite]:
    """Admin-only API endpoint with full CRUD for user management.
    Spec: polycrate spec inspect 131 / 525 / 561

    Args:
        id (int):
        body (UserAdminWriteRequest): Writable serializer for admin user CRUD.

            keycloak_user_id is intentionally omitted (read-only / provision-managed).
            Spec: polycrate spec inspect 131 / 525
        body (UserAdminWriteRequest): Writable serializer for admin user CRUD.

            keycloak_user_id is intentionally omitted (read-only / provision-managed).
            Spec: polycrate spec inspect 131 / 525
        body (UserAdminWriteRequest): Writable serializer for admin user CRUD.

            keycloak_user_id is intentionally omitted (read-only / provision-managed).
            Spec: polycrate spec inspect 131 / 525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserAdminWrite]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UserAdminWriteRequest | UserAdminWriteRequest | UserAdminWriteRequest | Unset = UNSET,
) -> UserAdminWrite | None:
    """Admin-only API endpoint with full CRUD for user management.
    Spec: polycrate spec inspect 131 / 525 / 561

    Args:
        id (int):
        body (UserAdminWriteRequest): Writable serializer for admin user CRUD.

            keycloak_user_id is intentionally omitted (read-only / provision-managed).
            Spec: polycrate spec inspect 131 / 525
        body (UserAdminWriteRequest): Writable serializer for admin user CRUD.

            keycloak_user_id is intentionally omitted (read-only / provision-managed).
            Spec: polycrate spec inspect 131 / 525
        body (UserAdminWriteRequest): Writable serializer for admin user CRUD.

            keycloak_user_id is intentionally omitted (read-only / provision-managed).
            Spec: polycrate spec inspect 131 / 525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserAdminWrite
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
