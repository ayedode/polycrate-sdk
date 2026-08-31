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
from ...models.api_v1_conversations_conversations_list_validation_error import (
    ApiV1ConversationsConversationsListValidationError,
)
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_403 import ErrorResponse403
from ...models.error_response_404 import ErrorResponse404
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_409 import ErrorResponse409
from ...models.error_response_410 import ErrorResponse410
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.error_response_502 import ErrorResponse502
from ...models.paginated_conversation_list_list import PaginatedConversationListList
from ...models.parse_error_response import ParseErrorResponse
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
) -> (
    ApiV1ConversationsConversationsListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedConversationListList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedConversationListList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(
            data: object,
        ) -> ApiV1ConversationsConversationsListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_conversations_conversations_list_error_response_400_type_0 = (
                    ApiV1ConversationsConversationsListValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_conversations_conversations_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_conversations_conversations_list_error_response_400_type_1 = (
                ParseErrorResponse.from_dict(data)
            )

            return componentsschemas_api_v1_conversations_conversations_list_error_response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse403.from_dict(response.json())

        return response_403

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
    ApiV1ConversationsConversationsListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedConversationListList
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
) -> Response[
    ApiV1ConversationsConversationsListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedConversationListList
]:
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
        Response[ApiV1ConversationsConversationsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedConversationListList]
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
) -> (
    ApiV1ConversationsConversationsListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedConversationListList
    | None
):
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
        ApiV1ConversationsConversationsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedConversationListList
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
) -> Response[
    ApiV1ConversationsConversationsListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedConversationListList
]:
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
        Response[ApiV1ConversationsConversationsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedConversationListList]
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
) -> (
    ApiV1ConversationsConversationsListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedConversationListList
    | None
):
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
        ApiV1ConversationsConversationsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedConversationListList
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
