from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_policy_binding_list_list import PaginatedPolicyBindingListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/policy-bindings/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedPolicyBindingListList | None:
    if response.status_code == 200:
        response_200 = PaginatedPolicyBindingListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedPolicyBindingListList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedPolicyBindingListList]:
    """API ViewSet for PolicyBinding management.

    NEW in v4.0 - CRUD endpoints for policy bindings.

    Features:
    - List bindings (filter by policy or target object)
    - Create binding (assign policy to object)
    - Update binding (enable/disable)
    - Delete binding (unassign policy)

    Args:
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPolicyBindingListList]
    """

    kwargs = _get_kwargs(
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
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedPolicyBindingListList | None:
    """API ViewSet for PolicyBinding management.

    NEW in v4.0 - CRUD endpoints for policy bindings.

    Features:
    - List bindings (filter by policy or target object)
    - Create binding (assign policy to object)
    - Update binding (enable/disable)
    - Delete binding (unassign policy)

    Args:
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPolicyBindingListList
    """

    return sync_detailed(
        client=client,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedPolicyBindingListList]:
    """API ViewSet for PolicyBinding management.

    NEW in v4.0 - CRUD endpoints for policy bindings.

    Features:
    - List bindings (filter by policy or target object)
    - Create binding (assign policy to object)
    - Update binding (enable/disable)
    - Delete binding (unassign policy)

    Args:
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPolicyBindingListList]
    """

    kwargs = _get_kwargs(
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
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedPolicyBindingListList | None:
    """API ViewSet for PolicyBinding management.

    NEW in v4.0 - CRUD endpoints for policy bindings.

    Features:
    - List bindings (filter by policy or target object)
    - Create binding (assign policy to object)
    - Update binding (enable/disable)
    - Delete binding (unassign policy)

    Args:
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPolicyBindingListList
    """

    return (
        await asyncio_detailed(
            client=client,
            ordering=ordering,
            page=page,
            page_size=page_size,
            search=search,
        )
    ).parsed
