from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_create_request import UserCreateRequest
from ...models.user_detail import UserDetail
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: UserCreateRequest | UserCreateRequest | UserCreateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/users/",
    }

    if isinstance(body, UserCreateRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UserCreateRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UserCreateRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | UserDetail | None:
    if response.status_code == 201:
        response_201 = UserDetail.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | UserDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UserCreateRequest | UserCreateRequest | UserCreateRequest | Unset = UNSET,
) -> Response[Any | UserDetail]:
    """Create user (blocking Keycloak provision)

     Create a Polycrate user with an organization membership and provision the Keycloak user + org
    membership + org role group atomically. On Keycloak failure the Django user is rolled back.
    Duplicate email returns HTTP 409. Spec 525.

    Args:
        body (UserCreateRequest): Create a user with organization membership and blocking Keycloak
            provision.

            Spec: polycrate spec inspect 525
        body (UserCreateRequest): Create a user with organization membership and blocking Keycloak
            provision.

            Spec: polycrate spec inspect 525
        body (UserCreateRequest): Create a user with organization membership and blocking Keycloak
            provision.

            Spec: polycrate spec inspect 525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UserDetail]
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
    body: UserCreateRequest | UserCreateRequest | UserCreateRequest | Unset = UNSET,
) -> Any | UserDetail | None:
    """Create user (blocking Keycloak provision)

     Create a Polycrate user with an organization membership and provision the Keycloak user + org
    membership + org role group atomically. On Keycloak failure the Django user is rolled back.
    Duplicate email returns HTTP 409. Spec 525.

    Args:
        body (UserCreateRequest): Create a user with organization membership and blocking Keycloak
            provision.

            Spec: polycrate spec inspect 525
        body (UserCreateRequest): Create a user with organization membership and blocking Keycloak
            provision.

            Spec: polycrate spec inspect 525
        body (UserCreateRequest): Create a user with organization membership and blocking Keycloak
            provision.

            Spec: polycrate spec inspect 525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UserDetail
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UserCreateRequest | UserCreateRequest | UserCreateRequest | Unset = UNSET,
) -> Response[Any | UserDetail]:
    """Create user (blocking Keycloak provision)

     Create a Polycrate user with an organization membership and provision the Keycloak user + org
    membership + org role group atomically. On Keycloak failure the Django user is rolled back.
    Duplicate email returns HTTP 409. Spec 525.

    Args:
        body (UserCreateRequest): Create a user with organization membership and blocking Keycloak
            provision.

            Spec: polycrate spec inspect 525
        body (UserCreateRequest): Create a user with organization membership and blocking Keycloak
            provision.

            Spec: polycrate spec inspect 525
        body (UserCreateRequest): Create a user with organization membership and blocking Keycloak
            provision.

            Spec: polycrate spec inspect 525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UserDetail]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UserCreateRequest | UserCreateRequest | UserCreateRequest | Unset = UNSET,
) -> Any | UserDetail | None:
    """Create user (blocking Keycloak provision)

     Create a Polycrate user with an organization membership and provision the Keycloak user + org
    membership + org role group atomically. On Keycloak failure the Django user is rolled back.
    Duplicate email returns HTTP 409. Spec 525.

    Args:
        body (UserCreateRequest): Create a user with organization membership and blocking Keycloak
            provision.

            Spec: polycrate spec inspect 525
        body (UserCreateRequest): Create a user with organization membership and blocking Keycloak
            provision.

            Spec: polycrate spec inspect 525
        body (UserCreateRequest): Create a user with organization membership and blocking Keycloak
            provision.

            Spec: polycrate spec inspect 525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UserDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
