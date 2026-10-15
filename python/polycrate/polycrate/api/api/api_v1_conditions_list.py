from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_conditions_list_severity import ApiV1ConditionsListSeverity
from ...models.paginated_condition_catalog_list_list import PaginatedConditionCatalogListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_system: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    severity: ApiV1ConditionsListSeverity | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["is_system"] = is_system

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    json_severity: str | Unset = UNSET
    if not isinstance(severity, Unset):
        json_severity = severity

    params["severity"] = json_severity

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/conditions/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedConditionCatalogListList | None:
    if response.status_code == 200:
        response_200 = PaginatedConditionCatalogListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedConditionCatalogListList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_system: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    severity: ApiV1ConditionsListSeverity | Unset = UNSET,
) -> Response[PaginatedConditionCatalogListList]:
    """Read-only API for the Condition catalog.
    System conditions cannot be modified or deleted.
    Spec: polycrate spec inspect 419

    Args:
        is_system (bool | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        severity (ApiV1ConditionsListSeverity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConditionCatalogListList]
    """

    kwargs = _get_kwargs(
        is_system=is_system,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
        severity=severity,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    is_system: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    severity: ApiV1ConditionsListSeverity | Unset = UNSET,
) -> PaginatedConditionCatalogListList | None:
    """Read-only API for the Condition catalog.
    System conditions cannot be modified or deleted.
    Spec: polycrate spec inspect 419

    Args:
        is_system (bool | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        severity (ApiV1ConditionsListSeverity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConditionCatalogListList
    """

    return sync_detailed(
        client=client,
        is_system=is_system,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
        severity=severity,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_system: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    severity: ApiV1ConditionsListSeverity | Unset = UNSET,
) -> Response[PaginatedConditionCatalogListList]:
    """Read-only API for the Condition catalog.
    System conditions cannot be modified or deleted.
    Spec: polycrate spec inspect 419

    Args:
        is_system (bool | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        severity (ApiV1ConditionsListSeverity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConditionCatalogListList]
    """

    kwargs = _get_kwargs(
        is_system=is_system,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
        severity=severity,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_system: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    severity: ApiV1ConditionsListSeverity | Unset = UNSET,
) -> PaginatedConditionCatalogListList | None:
    """Read-only API for the Condition catalog.
    System conditions cannot be modified or deleted.
    Spec: polycrate spec inspect 419

    Args:
        is_system (bool | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        severity (ApiV1ConditionsListSeverity | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConditionCatalogListList
    """

    return (
        await asyncio_detailed(
            client=client,
            is_system=is_system,
            ordering=ordering,
            page=page,
            page_size=page_size,
            search=search,
            severity=severity,
        )
    ).parsed
