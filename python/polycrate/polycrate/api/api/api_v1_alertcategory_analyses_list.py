from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_alert_category_analysis_list import PaginatedAlertCategoryAnalysisList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    alertname: str | Unset = UNSET,
    category: UUID | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    signal_class: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["alertname"] = alertname

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = str(category)
    params["category"] = json_category

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    params["signal_class"] = signal_class

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/alertcategory-analyses/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedAlertCategoryAnalysisList | None:
    if response.status_code == 200:
        response_200 = PaginatedAlertCategoryAnalysisList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedAlertCategoryAnalysisList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    alertname: str | Unset = UNSET,
    category: UUID | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    signal_class: str | Unset = UNSET,
) -> Response[PaginatedAlertCategoryAnalysisList]:
    """Read + delete persisted LLM analyses (Spec 674).

    Args:
        alertname (str | Unset):
        category (UUID | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        signal_class (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAlertCategoryAnalysisList]
    """

    kwargs = _get_kwargs(
        alertname=alertname,
        category=category,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
        signal_class=signal_class,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    alertname: str | Unset = UNSET,
    category: UUID | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    signal_class: str | Unset = UNSET,
) -> PaginatedAlertCategoryAnalysisList | None:
    """Read + delete persisted LLM analyses (Spec 674).

    Args:
        alertname (str | Unset):
        category (UUID | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        signal_class (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAlertCategoryAnalysisList
    """

    return sync_detailed(
        client=client,
        alertname=alertname,
        category=category,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
        signal_class=signal_class,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    alertname: str | Unset = UNSET,
    category: UUID | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    signal_class: str | Unset = UNSET,
) -> Response[PaginatedAlertCategoryAnalysisList]:
    """Read + delete persisted LLM analyses (Spec 674).

    Args:
        alertname (str | Unset):
        category (UUID | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        signal_class (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedAlertCategoryAnalysisList]
    """

    kwargs = _get_kwargs(
        alertname=alertname,
        category=category,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
        signal_class=signal_class,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    alertname: str | Unset = UNSET,
    category: UUID | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    signal_class: str | Unset = UNSET,
) -> PaginatedAlertCategoryAnalysisList | None:
    """Read + delete persisted LLM analyses (Spec 674).

    Args:
        alertname (str | Unset):
        category (UUID | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        signal_class (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedAlertCategoryAnalysisList
    """

    return (
        await asyncio_detailed(
            client=client,
            alertname=alertname,
            category=category,
            ordering=ordering,
            page=page,
            page_size=page_size,
            search=search,
            signal_class=signal_class,
        )
    ).parsed
