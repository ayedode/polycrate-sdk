from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_alert_category_list_list import PaginatedAlertCategoryListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: bool | Unset = UNSET,
    is_system: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["active"] = active

    params["is_system"] = is_system

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/alertcategories/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedAlertCategoryListList | None:
    if response.status_code == 200:
        response_200 = PaginatedAlertCategoryListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedAlertCategoryListList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    is_system: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedAlertCategoryListList]:
    """CRUD for global AlertCategory catalog (Spec 674).

    Args:
        active (bool | Unset):
        is_system (bool | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAlertCategoryListList]
    """

    kwargs = _get_kwargs(
        active=active,
        is_system=is_system,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    is_system: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedAlertCategoryListList | None:
    """CRUD for global AlertCategory catalog (Spec 674).

    Args:
        active (bool | Unset):
        is_system (bool | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAlertCategoryListList
    """

    return sync_detailed(
        client=client,
        active=active,
        is_system=is_system,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    is_system: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedAlertCategoryListList]:
    """CRUD for global AlertCategory catalog (Spec 674).

    Args:
        active (bool | Unset):
        is_system (bool | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAlertCategoryListList]
    """

    kwargs = _get_kwargs(
        active=active,
        is_system=is_system,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    is_system: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedAlertCategoryListList | None:
    """CRUD for global AlertCategory catalog (Spec 674).

    Args:
        active (bool | Unset):
        is_system (bool | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAlertCategoryListList
    """

    return (
        await asyncio_detailed(
            client=client,
            active=active,
            is_system=is_system,
            ordering=ordering,
            page=page,
            page_size=page_size,
            search=search,
        )
    ).parsed
