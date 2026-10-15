from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_org_api_key_list import PaginatedOrgAPIKeyList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org_name: str,
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
        "url": "/api/v1/organizations/{org_name}/api-keys/".format(
            org_name=quote(str(org_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedOrgAPIKeyList | None:
    if response.status_code == 200:
        response_200 = PaginatedOrgAPIKeyList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedOrgAPIKeyList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org_name: str,
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedOrgAPIKeyList]:
    """CRUD for Organization API Keys (kind='org_api_key') scoped to one org.
    Create/Delete: superuser only.  List: superuser OR OrgAPIUser of this org.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        org_name (str):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrgAPIKeyList]
    """

    kwargs = _get_kwargs(
        org_name=org_name,
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
    org_name: str,
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedOrgAPIKeyList | None:
    """CRUD for Organization API Keys (kind='org_api_key') scoped to one org.
    Create/Delete: superuser only.  List: superuser OR OrgAPIUser of this org.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        org_name (str):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOrgAPIKeyList
    """

    return sync_detailed(
        org_name=org_name,
        client=client,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
    ).parsed


async def asyncio_detailed(
    org_name: str,
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedOrgAPIKeyList]:
    """CRUD for Organization API Keys (kind='org_api_key') scoped to one org.
    Create/Delete: superuser only.  List: superuser OR OrgAPIUser of this org.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        org_name (str):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOrgAPIKeyList]
    """

    kwargs = _get_kwargs(
        org_name=org_name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org_name: str,
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedOrgAPIKeyList | None:
    """CRUD for Organization API Keys (kind='org_api_key') scoped to one org.
    Create/Delete: superuser only.  List: superuser OR OrgAPIUser of this org.
    The raw token is returned only on create and never again.
    Spec 488: System and Organization API Keys

    Args:
        org_name (str):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOrgAPIKeyList
    """

    return (
        await asyncio_detailed(
            org_name=org_name,
            client=client,
            ordering=ordering,
            page=page,
            page_size=page_size,
            search=search,
        )
    ).parsed
