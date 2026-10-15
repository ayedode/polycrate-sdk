from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.conversation_provider_post import ConversationProviderPost
from ...models.conversation_provider_post_request import ConversationProviderPostRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: ConversationProviderPostRequest
    | ConversationProviderPostRequest
    | ConversationProviderPostRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/conversations/providers/",
    }

    if isinstance(body, ConversationProviderPostRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ConversationProviderPostRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ConversationProviderPostRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConversationProviderPost | None:
    if response.status_code == 201:
        response_201 = ConversationProviderPost.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConversationProviderPost]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ConversationProviderPostRequest
    | ConversationProviderPostRequest
    | ConversationProviderPostRequest
    | Unset = UNSET,
) -> Response[ConversationProviderPost]:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (ConversationProviderPostRequest): Serializer for ConversationProvider creation.
            Following S3 pattern with validation and create logic.
        body (ConversationProviderPostRequest): Serializer for ConversationProvider creation.
            Following S3 pattern with validation and create logic.
        body (ConversationProviderPostRequest): Serializer for ConversationProvider creation.
            Following S3 pattern with validation and create logic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationProviderPost]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ConversationProviderPostRequest
    | ConversationProviderPostRequest
    | ConversationProviderPostRequest
    | Unset = UNSET,
) -> ConversationProviderPost | None:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (ConversationProviderPostRequest): Serializer for ConversationProvider creation.
            Following S3 pattern with validation and create logic.
        body (ConversationProviderPostRequest): Serializer for ConversationProvider creation.
            Following S3 pattern with validation and create logic.
        body (ConversationProviderPostRequest): Serializer for ConversationProvider creation.
            Following S3 pattern with validation and create logic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationProviderPost
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ConversationProviderPostRequest
    | ConversationProviderPostRequest
    | ConversationProviderPostRequest
    | Unset = UNSET,
) -> Response[ConversationProviderPost]:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (ConversationProviderPostRequest): Serializer for ConversationProvider creation.
            Following S3 pattern with validation and create logic.
        body (ConversationProviderPostRequest): Serializer for ConversationProvider creation.
            Following S3 pattern with validation and create logic.
        body (ConversationProviderPostRequest): Serializer for ConversationProvider creation.
            Following S3 pattern with validation and create logic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationProviderPost]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ConversationProviderPostRequest
    | ConversationProviderPostRequest
    | ConversationProviderPostRequest
    | Unset = UNSET,
) -> ConversationProviderPost | None:
    """Translate DB unique-constraint violations into HTTP 409 Conflict.

    Spec 159 F2: ``POST`` on ManagedObject endpoints previously returned 500
    when the underlying ``INSERT`` violated a unique constraint (e.g.
    ``unique_k8s_cluster_per_workspace``) because ``IntegrityError`` bubbled
    up to the default exception handler. Clients — especially the Polycrate
    Operator — need a deterministic 409 signal so they can treat
    "already exists" as a legitimate case instead of a transport error.

    Args:
        body (ConversationProviderPostRequest): Serializer for ConversationProvider creation.
            Following S3 pattern with validation and create logic.
        body (ConversationProviderPostRequest): Serializer for ConversationProvider creation.
            Following S3 pattern with validation and create logic.
        body (ConversationProviderPostRequest): Serializer for ConversationProvider creation.
            Following S3 pattern with validation and create logic.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationProviderPost
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
