from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_conversations_messages_list_content_kind import (
    ApiV1ConversationsMessagesListContentKind,
)
from ...models.api_v1_conversations_messages_list_kind_item import (
    ApiV1ConversationsMessagesListKindItem,
)
from ...models.api_v1_conversations_messages_list_sender import (
    ApiV1ConversationsMessagesListSender,
)
from ...models.api_v1_conversations_messages_list_status_item import (
    ApiV1ConversationsMessagesListStatusItem,
)
from ...models.api_v1_conversations_messages_list_validation_error import ApiV1ConversationsMessagesListValidationError
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
from ...models.paginated_message_list_list import PaginatedMessageListList
from ...models.parse_error_response import ParseErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    content_kind: ApiV1ConversationsMessagesListContentKind | Unset = UNSET,
    conversation: UUID | Unset = UNSET,
    kind: list[ApiV1ConversationsMessagesListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    sender: ApiV1ConversationsMessagesListSender | Unset = UNSET,
    status: list[ApiV1ConversationsMessagesListStatusItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_content_kind: str | Unset = UNSET
    if not isinstance(content_kind, Unset):
        json_content_kind = content_kind

    params["content_kind"] = json_content_kind

    json_conversation: str | Unset = UNSET
    if not isinstance(conversation, Unset):
        json_conversation = str(conversation)
    params["conversation"] = json_conversation

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

    params["search"] = search

    json_sender: str | Unset = UNSET
    if not isinstance(sender, Unset):
        json_sender = sender

    params["sender"] = json_sender

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
        "url": "/api/v1/conversations/messages/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ApiV1ConversationsMessagesListValidationError
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
    | PaginatedMessageListList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedMessageListList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1ConversationsMessagesListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_conversations_messages_list_error_response_400_type_0 = (
                    ApiV1ConversationsMessagesListValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_conversations_messages_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_conversations_messages_list_error_response_400_type_1 = (
                ParseErrorResponse.from_dict(data)
            )

            return componentsschemas_api_v1_conversations_messages_list_error_response_400_type_1

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
    ApiV1ConversationsMessagesListValidationError
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
    | PaginatedMessageListList
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
    content_kind: ApiV1ConversationsMessagesListContentKind | Unset = UNSET,
    conversation: UUID | Unset = UNSET,
    kind: list[ApiV1ConversationsMessagesListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    sender: ApiV1ConversationsMessagesListSender | Unset = UNSET,
    status: list[ApiV1ConversationsMessagesListStatusItem] | Unset = UNSET,
) -> Response[
    ApiV1ConversationsMessagesListValidationError
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
    | PaginatedMessageListList
]:
    """API ViewSet for Conversations Messages.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        content_kind (ApiV1ConversationsMessagesListContentKind | Unset):
        conversation (UUID | Unset):
        kind (list[ApiV1ConversationsMessagesListKindItem] | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        sender (ApiV1ConversationsMessagesListSender | Unset):
        status (list[ApiV1ConversationsMessagesListStatusItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1ConversationsMessagesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedMessageListList]
    """

    kwargs = _get_kwargs(
        content_kind=content_kind,
        conversation=conversation,
        kind=kind,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        search=search,
        sender=sender,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    content_kind: ApiV1ConversationsMessagesListContentKind | Unset = UNSET,
    conversation: UUID | Unset = UNSET,
    kind: list[ApiV1ConversationsMessagesListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    sender: ApiV1ConversationsMessagesListSender | Unset = UNSET,
    status: list[ApiV1ConversationsMessagesListStatusItem] | Unset = UNSET,
) -> (
    ApiV1ConversationsMessagesListValidationError
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
    | PaginatedMessageListList
    | None
):
    """API ViewSet for Conversations Messages.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        content_kind (ApiV1ConversationsMessagesListContentKind | Unset):
        conversation (UUID | Unset):
        kind (list[ApiV1ConversationsMessagesListKindItem] | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        sender (ApiV1ConversationsMessagesListSender | Unset):
        status (list[ApiV1ConversationsMessagesListStatusItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1ConversationsMessagesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedMessageListList
    """

    return sync_detailed(
        client=client,
        content_kind=content_kind,
        conversation=conversation,
        kind=kind,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        search=search,
        sender=sender,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    content_kind: ApiV1ConversationsMessagesListContentKind | Unset = UNSET,
    conversation: UUID | Unset = UNSET,
    kind: list[ApiV1ConversationsMessagesListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    sender: ApiV1ConversationsMessagesListSender | Unset = UNSET,
    status: list[ApiV1ConversationsMessagesListStatusItem] | Unset = UNSET,
) -> Response[
    ApiV1ConversationsMessagesListValidationError
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
    | PaginatedMessageListList
]:
    """API ViewSet for Conversations Messages.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        content_kind (ApiV1ConversationsMessagesListContentKind | Unset):
        conversation (UUID | Unset):
        kind (list[ApiV1ConversationsMessagesListKindItem] | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        sender (ApiV1ConversationsMessagesListSender | Unset):
        status (list[ApiV1ConversationsMessagesListStatusItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiV1ConversationsMessagesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedMessageListList]
    """

    kwargs = _get_kwargs(
        content_kind=content_kind,
        conversation=conversation,
        kind=kind,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        search=search,
        sender=sender,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    content_kind: ApiV1ConversationsMessagesListContentKind | Unset = UNSET,
    conversation: UUID | Unset = UNSET,
    kind: list[ApiV1ConversationsMessagesListKindItem] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    sender: ApiV1ConversationsMessagesListSender | Unset = UNSET,
    status: list[ApiV1ConversationsMessagesListStatusItem] | Unset = UNSET,
) -> (
    ApiV1ConversationsMessagesListValidationError
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
    | PaginatedMessageListList
    | None
):
    """API ViewSet for Conversations Messages.

    Provides CRUD operations via REST API with proper permissions,
    filtering, and serialization.

    Args:
        content_kind (ApiV1ConversationsMessagesListContentKind | Unset):
        conversation (UUID | Unset):
        kind (list[ApiV1ConversationsMessagesListKindItem] | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        sender (ApiV1ConversationsMessagesListSender | Unset):
        status (list[ApiV1ConversationsMessagesListStatusItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiV1ConversationsMessagesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedMessageListList
    """

    return (
        await asyncio_detailed(
            client=client,
            content_kind=content_kind,
            conversation=conversation,
            kind=kind,
            ordering=ordering,
            organization=organization,
            page=page,
            page_size=page_size,
            search=search,
            sender=sender,
            status=status,
        )
    ).parsed
