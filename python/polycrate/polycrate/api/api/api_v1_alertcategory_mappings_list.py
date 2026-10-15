from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_alertcategory_mappings_list_match_type import (
    ApiV1AlertcategoryMappingsListMatchType,
)
from ...models.paginated_alert_category_mapping_list import PaginatedAlertCategoryMappingList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: UUID | Unset = UNSET,
    is_system: bool | Unset = UNSET,
    match_type: ApiV1AlertcategoryMappingsListMatchType | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = str(category)
    params["category"] = json_category

    params["is_system"] = is_system

    json_match_type: str | Unset = UNSET
    if not isinstance(match_type, Unset):
        json_match_type = match_type

    params["match_type"] = json_match_type

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/alertcategory-mappings/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedAlertCategoryMappingList | None:
    if response.status_code == 200:
        response_200 = PaginatedAlertCategoryMappingList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedAlertCategoryMappingList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    category: UUID | Unset = UNSET,
    is_system: bool | Unset = UNSET,
    match_type: ApiV1AlertcategoryMappingsListMatchType | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedAlertCategoryMappingList]:
    """CRUD for alertname → category mapping rules (Spec 674).

    Args:
        category (UUID | Unset):
        is_system (bool | Unset):
        match_type (ApiV1AlertcategoryMappingsListMatchType | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAlertCategoryMappingList]
    """

    kwargs = _get_kwargs(
        category=category,
        is_system=is_system,
        match_type=match_type,
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
    category: UUID | Unset = UNSET,
    is_system: bool | Unset = UNSET,
    match_type: ApiV1AlertcategoryMappingsListMatchType | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedAlertCategoryMappingList | None:
    """CRUD for alertname → category mapping rules (Spec 674).

    Args:
        category (UUID | Unset):
        is_system (bool | Unset):
        match_type (ApiV1AlertcategoryMappingsListMatchType | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAlertCategoryMappingList
    """

    return sync_detailed(
        client=client,
        category=category,
        is_system=is_system,
        match_type=match_type,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category: UUID | Unset = UNSET,
    is_system: bool | Unset = UNSET,
    match_type: ApiV1AlertcategoryMappingsListMatchType | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedAlertCategoryMappingList]:
    """CRUD for alertname → category mapping rules (Spec 674).

    Args:
        category (UUID | Unset):
        is_system (bool | Unset):
        match_type (ApiV1AlertcategoryMappingsListMatchType | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAlertCategoryMappingList]
    """

    kwargs = _get_kwargs(
        category=category,
        is_system=is_system,
        match_type=match_type,
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
    category: UUID | Unset = UNSET,
    is_system: bool | Unset = UNSET,
    match_type: ApiV1AlertcategoryMappingsListMatchType | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedAlertCategoryMappingList | None:
    """CRUD for alertname → category mapping rules (Spec 674).

    Args:
        category (UUID | Unset):
        is_system (bool | Unset):
        match_type (ApiV1AlertcategoryMappingsListMatchType | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAlertCategoryMappingList
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            is_system=is_system,
            match_type=match_type,
            ordering=ordering,
            page=page,
            page_size=page_size,
            search=search,
        )
    ).parsed
