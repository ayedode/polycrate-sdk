from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_search_retrieve_state import ApiV1SearchRetrieveState
from ...models.global_search_response import GlobalSearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    facets: bool | Unset = UNSET,
    kind: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    object_type: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    q: str,
    state: ApiV1SearchRetrieveState | Unset = UNSET,
    workspace_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["facets"] = facets

    params["kind"] = kind

    params["limit"] = limit

    json_object_type: list[str] | Unset = UNSET
    if not isinstance(object_type, Unset):
        json_object_type = object_type

    params["object_type"] = json_object_type

    params["offset"] = offset

    params["organization_id"] = organization_id

    params["q"] = q

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    params["workspace_id"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/search/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GlobalSearchResponse | None:
    if response.status_code == 200:
        response_200 = GlobalSearchResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GlobalSearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    facets: bool | Unset = UNSET,
    kind: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    object_type: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    q: str,
    state: ApiV1SearchRetrieveState | Unset = UNSET,
    workspace_id: str | Unset = UNSET,
) -> Response[GlobalSearchResponse]:
    """Global full-text search across all ManagedObjects

     GET /api/v1/search/?q=<query>

    Performs PostgreSQL full-text + trigram search across the SearchIndex.
    Rate-limited per user via SearchRateThrottle.

    Args:
        facets (bool | Unset):
        kind (str | Unset):
        limit (int | Unset):
        object_type (list[str] | Unset):
        offset (int | Unset):
        organization_id (str | Unset):
        q (str):
        state (ApiV1SearchRetrieveState | Unset):
        workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GlobalSearchResponse]
    """

    kwargs = _get_kwargs(
        facets=facets,
        kind=kind,
        limit=limit,
        object_type=object_type,
        offset=offset,
        organization_id=organization_id,
        q=q,
        state=state,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    facets: bool | Unset = UNSET,
    kind: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    object_type: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    q: str,
    state: ApiV1SearchRetrieveState | Unset = UNSET,
    workspace_id: str | Unset = UNSET,
) -> GlobalSearchResponse | None:
    """Global full-text search across all ManagedObjects

     GET /api/v1/search/?q=<query>

    Performs PostgreSQL full-text + trigram search across the SearchIndex.
    Rate-limited per user via SearchRateThrottle.

    Args:
        facets (bool | Unset):
        kind (str | Unset):
        limit (int | Unset):
        object_type (list[str] | Unset):
        offset (int | Unset):
        organization_id (str | Unset):
        q (str):
        state (ApiV1SearchRetrieveState | Unset):
        workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GlobalSearchResponse
    """

    return sync_detailed(
        client=client,
        facets=facets,
        kind=kind,
        limit=limit,
        object_type=object_type,
        offset=offset,
        organization_id=organization_id,
        q=q,
        state=state,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    facets: bool | Unset = UNSET,
    kind: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    object_type: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    q: str,
    state: ApiV1SearchRetrieveState | Unset = UNSET,
    workspace_id: str | Unset = UNSET,
) -> Response[GlobalSearchResponse]:
    """Global full-text search across all ManagedObjects

     GET /api/v1/search/?q=<query>

    Performs PostgreSQL full-text + trigram search across the SearchIndex.
    Rate-limited per user via SearchRateThrottle.

    Args:
        facets (bool | Unset):
        kind (str | Unset):
        limit (int | Unset):
        object_type (list[str] | Unset):
        offset (int | Unset):
        organization_id (str | Unset):
        q (str):
        state (ApiV1SearchRetrieveState | Unset):
        workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GlobalSearchResponse]
    """

    kwargs = _get_kwargs(
        facets=facets,
        kind=kind,
        limit=limit,
        object_type=object_type,
        offset=offset,
        organization_id=organization_id,
        q=q,
        state=state,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    facets: bool | Unset = UNSET,
    kind: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    object_type: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    organization_id: str | Unset = UNSET,
    q: str,
    state: ApiV1SearchRetrieveState | Unset = UNSET,
    workspace_id: str | Unset = UNSET,
) -> GlobalSearchResponse | None:
    """Global full-text search across all ManagedObjects

     GET /api/v1/search/?q=<query>

    Performs PostgreSQL full-text + trigram search across the SearchIndex.
    Rate-limited per user via SearchRateThrottle.

    Args:
        facets (bool | Unset):
        kind (str | Unset):
        limit (int | Unset):
        object_type (list[str] | Unset):
        offset (int | Unset):
        organization_id (str | Unset):
        q (str):
        state (ApiV1SearchRetrieveState | Unset):
        workspace_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GlobalSearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            facets=facets,
            kind=kind,
            limit=limit,
            object_type=object_type,
            offset=offset,
            organization_id=organization_id,
            q=q,
            state=state,
            workspace_id=workspace_id,
        )
    ).parsed
