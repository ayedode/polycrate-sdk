from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_conversations_conversations_list_kind_item import (
    ApiV1ConversationsConversationsListKindItem,
)
from ...models.api_v1_conversations_conversations_list_status_item import (
    ApiV1ConversationsConversationsListStatusItem,
)
from ...models.paginated_conversation_list_list import PaginatedConversationListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    conversation_provider: UUID | Unset = UNSET,
    kind: list[ApiV1ConversationsConversationsListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    provider_id: str | Unset = UNSET,
    provider_id_contains: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: list[ApiV1ConversationsConversationsListStatusItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_conversation_provider: str | Unset = UNSET
    if not isinstance(conversation_provider, Unset):
        json_conversation_provider = str(conversation_provider)
    params["conversation_provider"] = json_conversation_provider

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

    params["provider_id"] = provider_id

    params["provider_id_contains"] = provider_id_contains

    params["search"] = search

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item: str = status_item_data
            json_status.append(status_item)

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/conversations/conversations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedConversationListList | None:
    if response.status_code == 200:
        response_200 = PaginatedConversationListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedConversationListList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    conversation_provider: UUID | Unset = UNSET,
    kind: list[ApiV1ConversationsConversationsListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    provider_id: str | Unset = UNSET,
    provider_id_contains: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: list[ApiV1ConversationsConversationsListStatusItem] | Unset = UNSET,
) -> Response[PaginatedConversationListList]:
    """API ViewSet for Conversations Conversations.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        conversation_provider (UUID | Unset):
        kind (list[ApiV1ConversationsConversationsListKindItem] | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        provider_id (str | Unset):
        provider_id_contains (str | Unset):
        search (str | Unset):
        status (list[ApiV1ConversationsConversationsListStatusItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConversationListList]
    """

    kwargs = _get_kwargs(
        conversation_provider=conversation_provider,
        kind=kind,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        provider_id=provider_id,
        provider_id_contains=provider_id_contains,
        search=search,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    conversation_provider: UUID | Unset = UNSET,
    kind: list[ApiV1ConversationsConversationsListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    provider_id: str | Unset = UNSET,
    provider_id_contains: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: list[ApiV1ConversationsConversationsListStatusItem] | Unset = UNSET,
) -> PaginatedConversationListList | None:
    """API ViewSet for Conversations Conversations.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        conversation_provider (UUID | Unset):
        kind (list[ApiV1ConversationsConversationsListKindItem] | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        provider_id (str | Unset):
        provider_id_contains (str | Unset):
        search (str | Unset):
        status (list[ApiV1ConversationsConversationsListStatusItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConversationListList
    """

    return sync_detailed(
        client=client,
        conversation_provider=conversation_provider,
        kind=kind,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        provider_id=provider_id,
        provider_id_contains=provider_id_contains,
        search=search,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    conversation_provider: UUID | Unset = UNSET,
    kind: list[ApiV1ConversationsConversationsListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    provider_id: str | Unset = UNSET,
    provider_id_contains: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: list[ApiV1ConversationsConversationsListStatusItem] | Unset = UNSET,
) -> Response[PaginatedConversationListList]:
    """API ViewSet for Conversations Conversations.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        conversation_provider (UUID | Unset):
        kind (list[ApiV1ConversationsConversationsListKindItem] | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        provider_id (str | Unset):
        provider_id_contains (str | Unset):
        search (str | Unset):
        status (list[ApiV1ConversationsConversationsListStatusItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConversationListList]
    """

    kwargs = _get_kwargs(
        conversation_provider=conversation_provider,
        kind=kind,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        provider_id=provider_id,
        provider_id_contains=provider_id_contains,
        search=search,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    conversation_provider: UUID | Unset = UNSET,
    kind: list[ApiV1ConversationsConversationsListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    provider_id: str | Unset = UNSET,
    provider_id_contains: str | Unset = UNSET,
    search: str | Unset = UNSET,
    status: list[ApiV1ConversationsConversationsListStatusItem] | Unset = UNSET,
) -> PaginatedConversationListList | None:
    """API ViewSet for Conversations Conversations.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        conversation_provider (UUID | Unset):
        kind (list[ApiV1ConversationsConversationsListKindItem] | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        provider_id (str | Unset):
        provider_id_contains (str | Unset):
        search (str | Unset):
        status (list[ApiV1ConversationsConversationsListStatusItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConversationListList
    """

    return (
        await asyncio_detailed(
            client=client,
            conversation_provider=conversation_provider,
            kind=kind,
            ordering=ordering,
            organization=organization,
            page=page,
            page_size=page_size,
            provider_id=provider_id,
            provider_id_contains=provider_id_contains,
            search=search,
            status=status,
        )
    ).parsed
