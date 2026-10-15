from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.membership_create_request import MembershipCreateRequest
from ...models.user_admin import UserAdmin
from ...types import UNSET, Response


def _get_kwargs(
    id: int,
    *,
    body: MembershipCreateRequest | MembershipCreateRequest | MembershipCreateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/admin/users/{id}/memberships/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, MembershipCreateRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MembershipCreateRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, MembershipCreateRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UserAdmin | None:
    if response.status_code == 200:
        response_200 = UserAdmin.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UserAdmin]:
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
    body: MembershipCreateRequest | MembershipCreateRequest | MembershipCreateRequest | Unset = UNSET,
) -> Response[UserAdmin]:
    """Manage admin user memberships

     GET/POST organization memberships. POST accepts role and syncs Keycloak org membership + role group
    (blocking). DELETE uses path .../memberships/{organization_id}/. Spec 525 / 561.

    Args:
        id (int):
        body (MembershipCreateRequest): Add user to another organization with role. Spec 525
        body (MembershipCreateRequest): Add user to another organization with role. Spec 525
        body (MembershipCreateRequest): Add user to another organization with role. Spec 525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserAdmin]
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
    body: MembershipCreateRequest | MembershipCreateRequest | MembershipCreateRequest | Unset = UNSET,
) -> UserAdmin | None:
    """Manage admin user memberships

     GET/POST organization memberships. POST accepts role and syncs Keycloak org membership + role group
    (blocking). DELETE uses path .../memberships/{organization_id}/. Spec 525 / 561.

    Args:
        id (int):
        body (MembershipCreateRequest): Add user to another organization with role. Spec 525
        body (MembershipCreateRequest): Add user to another organization with role. Spec 525
        body (MembershipCreateRequest): Add user to another organization with role. Spec 525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserAdmin
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
    body: MembershipCreateRequest | MembershipCreateRequest | MembershipCreateRequest | Unset = UNSET,
) -> Response[UserAdmin]:
    """Manage admin user memberships

     GET/POST organization memberships. POST accepts role and syncs Keycloak org membership + role group
    (blocking). DELETE uses path .../memberships/{organization_id}/. Spec 525 / 561.

    Args:
        id (int):
        body (MembershipCreateRequest): Add user to another organization with role. Spec 525
        body (MembershipCreateRequest): Add user to another organization with role. Spec 525
        body (MembershipCreateRequest): Add user to another organization with role. Spec 525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserAdmin]
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
    body: MembershipCreateRequest | MembershipCreateRequest | MembershipCreateRequest | Unset = UNSET,
) -> UserAdmin | None:
    """Manage admin user memberships

     GET/POST organization memberships. POST accepts role and syncs Keycloak org membership + role group
    (blocking). DELETE uses path .../memberships/{organization_id}/. Spec 525 / 561.

    Args:
        id (int):
        body (MembershipCreateRequest): Add user to another organization with role. Spec 525
        body (MembershipCreateRequest): Add user to another organization with role. Spec 525
        body (MembershipCreateRequest): Add user to another organization with role. Spec 525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserAdmin
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
