from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_conversations_providers_list_kind_item import (
    ApiV1ConversationsProvidersListKindItem,
)
from ...models.api_v1_conversations_providers_list_state import (
    ApiV1ConversationsProvidersListState,
)
from ...models.paginated_conversation_provider_list_list import PaginatedConversationProviderListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    has_config: bool | Unset = UNSET,
    has_credential: bool | Unset = UNSET,
    kind: list[ApiV1ConversationsProvidersListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ConversationsProvidersListState | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["has_config"] = has_config

    params["has_credential"] = has_credential

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = []
        for kind_item_data in kind:
            kind_item: str = kind_item_data
            json_kind.append(kind_item)

    params["kind"] = json_kind

    params["ordering"] = ordering

    json_organization: str | Unset = UNSET
    if not isinstance(organization, Unset):
        json_organization = str(organization)
    params["organization"] = json_organization

    params["page"] = page

    params["page_size"] = page_size

    params["platform_service"] = platform_service

    params["search"] = search

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/conversations/providers/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedConversationProviderListList | None:
    if response.status_code == 200:
        response_200 = PaginatedConversationProviderListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedConversationProviderListList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    has_config: bool | Unset = UNSET,
    has_credential: bool | Unset = UNSET,
    kind: list[ApiV1ConversationsProvidersListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ConversationsProvidersListState | Unset = UNSET,
) -> Response[PaginatedConversationProviderListList]:
    """API ViewSet for Conversation Providers.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        has_config (bool | Unset):
        has_credential (bool | Unset):
        kind (list[ApiV1ConversationsProvidersListKindItem] | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        search (str | Unset):
        state (ApiV1ConversationsProvidersListState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConversationProviderListList]
    """

    kwargs = _get_kwargs(
        has_config=has_config,
        has_credential=has_credential,
        kind=kind,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        search=search,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    has_config: bool | Unset = UNSET,
    has_credential: bool | Unset = UNSET,
    kind: list[ApiV1ConversationsProvidersListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ConversationsProvidersListState | Unset = UNSET,
) -> PaginatedConversationProviderListList | None:
    """API ViewSet for Conversation Providers.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        has_config (bool | Unset):
        has_credential (bool | Unset):
        kind (list[ApiV1ConversationsProvidersListKindItem] | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        search (str | Unset):
        state (ApiV1ConversationsProvidersListState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConversationProviderListList
    """

    return sync_detailed(
        client=client,
        has_config=has_config,
        has_credential=has_credential,
        kind=kind,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        search=search,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    has_config: bool | Unset = UNSET,
    has_credential: bool | Unset = UNSET,
    kind: list[ApiV1ConversationsProvidersListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ConversationsProvidersListState | Unset = UNSET,
) -> Response[PaginatedConversationProviderListList]:
    """API ViewSet for Conversation Providers.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        has_config (bool | Unset):
        has_credential (bool | Unset):
        kind (list[ApiV1ConversationsProvidersListKindItem] | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        search (str | Unset):
        state (ApiV1ConversationsProvidersListState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConversationProviderListList]
    """

    kwargs = _get_kwargs(
        has_config=has_config,
        has_credential=has_credential,
        kind=kind,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        platform_service=platform_service,
        search=search,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    has_config: bool | Unset = UNSET,
    has_credential: bool | Unset = UNSET,
    kind: list[ApiV1ConversationsProvidersListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    platform_service: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    state: ApiV1ConversationsProvidersListState | Unset = UNSET,
) -> PaginatedConversationProviderListList | None:
    """API ViewSet for Conversation Providers.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        has_config (bool | Unset):
        has_credential (bool | Unset):
        kind (list[ApiV1ConversationsProvidersListKindItem] | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        platform_service (bool | Unset):
        search (str | Unset):
        state (ApiV1ConversationsProvidersListState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConversationProviderListList
    """

    return (
        await asyncio_detailed(
            client=client,
            has_config=has_config,
            has_credential=has_credential,
            kind=kind,
            ordering=ordering,
            organization=organization,
            page=page,
            page_size=page_size,
            platform_service=platform_service,
            search=search,
            state=state,
        )
    ).parsed
