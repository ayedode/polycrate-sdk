from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_user_api_key_list import PaginatedUserAPIKeyList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
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
        "url": "/api/v1/users/{user_id}/api-keys/".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedUserAPIKeyList | None:
    if response.status_code == 200:
        response_200 = PaginatedUserAPIKeyList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedUserAPIKeyList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedUserAPIKeyList]:
    """List user API keys

     List Knox user API keys (tokens with APIKeyMetadata) for the given user. Web-login Knox tokens
    without metadata are never returned. The raw token is never included. Spec 868.

    Args:
        user_id (int):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserAPIKeyList]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
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
    user_id: int,
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedUserAPIKeyList | None:
    """List user API keys

     List Knox user API keys (tokens with APIKeyMetadata) for the given user. Web-login Knox tokens
    without metadata are never returned. The raw token is never included. Spec 868.

    Args:
        user_id (int):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserAPIKeyList
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedUserAPIKeyList]:
    """List user API keys

     List Knox user API keys (tokens with APIKeyMetadata) for the given user. Web-login Knox tokens
    without metadata are never returned. The raw token is never included. Spec 868.

    Args:
        user_id (int):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserAPIKeyList]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedUserAPIKeyList | None:
    """List user API keys

     List Knox user API keys (tokens with APIKeyMetadata) for the given user. Web-login Knox tokens
    without metadata are never returned. The raw token is never included. Spec 868.

    Args:
        user_id (int):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserAPIKeyList
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            ordering=ordering,
            page=page,
            page_size=page_size,
            search=search,
        )
    ).parsed
