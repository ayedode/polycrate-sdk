from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_alertcategory_mappings_list_match_type import (
    ApiV1AlertcategoryMappingsListMatchType,
)
from ...models.api_v1_alertcategory_mappings_list_validation_error import ApiV1AlertcategoryMappingsListValidationError
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_404 import ErrorResponse404
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_409 import ErrorResponse409
from ...models.error_response_410 import ErrorResponse410
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.error_response_502 import ErrorResponse502
from ...models.paginated_alert_category_mapping_list import PaginatedAlertCategoryMappingList
from ...models.parse_error_response import ParseErrorResponse
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
) -> (
    ApiV1AlertcategoryMappingsListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedAlertCategoryMappingList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedAlertCategoryMappingList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1AlertcategoryMappingsListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alertcategory_mappings_list_error_response_400_type_0 = (
                    ApiV1AlertcategoryMappingsListValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_alertcategory_mappings_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_alertcategory_mappings_list_error_response_400_type_1 = (
                ParseErrorResponse.from_dict(data)
            )

            return componentsschemas_api_v1_alertcategory_mappings_list_error_response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401

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
    ApiV1AlertcategoryMappingsListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedAlertCategoryMappingList
]:
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
) -> Response[
    ApiV1AlertcategoryMappingsListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedAlertCategoryMappingList
]:
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
        Response[ApiV1AlertcategoryMappingsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedAlertCategoryMappingList]
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
) -> (
    ApiV1AlertcategoryMappingsListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedAlertCategoryMappingList
    | None
):
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
        ApiV1AlertcategoryMappingsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedAlertCategoryMappingList
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
) -> Response[
    ApiV1AlertcategoryMappingsListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedAlertCategoryMappingList
]:
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
        Response[ApiV1AlertcategoryMappingsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedAlertCategoryMappingList]
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
) -> (
    ApiV1AlertcategoryMappingsListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedAlertCategoryMappingList
    | None
):
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
        ApiV1AlertcategoryMappingsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedAlertCategoryMappingList
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
