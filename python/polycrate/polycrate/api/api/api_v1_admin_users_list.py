from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_admin_users_list_role import ApiV1AdminUsersListRole
from ...models.paginated_user_admin_list import PaginatedUserAdminList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_active: bool | Unset = UNSET,
    is_staff: bool | Unset = UNSET,
    is_superuser: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    role: ApiV1AdminUsersListRole | Unset = UNSET,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["is_active"] = is_active

    params["is_staff"] = is_staff

    params["is_superuser"] = is_superuser

    params["ordering"] = ordering

    json_organization: str | Unset = UNSET
    if not isinstance(organization, Unset):
        json_organization = str(organization)
    params["organization"] = json_organization

    params["page"] = page

    params["page_size"] = page_size

    json_role: str | Unset = UNSET
    if not isinstance(role, Unset):
        json_role = role

    params["role"] = json_role

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/admin/users/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedUserAdminList | None:
    if response.status_code == 200:
        response_200 = PaginatedUserAdminList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedUserAdminList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_active: bool | Unset = UNSET,
    is_staff: bool | Unset = UNSET,
    is_superuser: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    role: ApiV1AdminUsersListRole | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedUserAdminList]:
    """Admin-only API endpoint with full CRUD for user management.
    Spec: polycrate spec inspect 131 / 525 / 561

    Args:
        is_active (bool | Unset):
        is_staff (bool | Unset):
        is_superuser (bool | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        role (ApiV1AdminUsersListRole | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserAdminList]
    """

    kwargs = _get_kwargs(
        is_active=is_active,
        is_staff=is_staff,
        is_superuser=is_superuser,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        role=role,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    is_active: bool | Unset = UNSET,
    is_staff: bool | Unset = UNSET,
    is_superuser: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    role: ApiV1AdminUsersListRole | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedUserAdminList | None:
    """Admin-only API endpoint with full CRUD for user management.
    Spec: polycrate spec inspect 131 / 525 / 561

    Args:
        is_active (bool | Unset):
        is_staff (bool | Unset):
        is_superuser (bool | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        role (ApiV1AdminUsersListRole | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserAdminList
    """

    return sync_detailed(
        client=client,
        is_active=is_active,
        is_staff=is_staff,
        is_superuser=is_superuser,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        role=role,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_active: bool | Unset = UNSET,
    is_staff: bool | Unset = UNSET,
    is_superuser: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    role: ApiV1AdminUsersListRole | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedUserAdminList]:
    """Admin-only API endpoint with full CRUD for user management.
    Spec: polycrate spec inspect 131 / 525 / 561

    Args:
        is_active (bool | Unset):
        is_staff (bool | Unset):
        is_superuser (bool | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        role (ApiV1AdminUsersListRole | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserAdminList]
    """

    kwargs = _get_kwargs(
        is_active=is_active,
        is_staff=is_staff,
        is_superuser=is_superuser,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        role=role,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_active: bool | Unset = UNSET,
    is_staff: bool | Unset = UNSET,
    is_superuser: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    role: ApiV1AdminUsersListRole | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedUserAdminList | None:
    """Admin-only API endpoint with full CRUD for user management.
    Spec: polycrate spec inspect 131 / 525 / 561

    Args:
        is_active (bool | Unset):
        is_staff (bool | Unset):
        is_superuser (bool | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        role (ApiV1AdminUsersListRole | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserAdminList
    """

    return (
        await asyncio_detailed(
            client=client,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            ordering=ordering,
            organization=organization,
            page=page,
            page_size=page_size,
            role=role,
            search=search,
        )
    ).parsed
