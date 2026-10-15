from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notification_sink import NotificationSink
from ...models.notification_sink_request import NotificationSinkRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: NotificationSinkRequest | NotificationSinkRequest | NotificationSinkRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/notifications/sinks/{id}/test/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, NotificationSinkRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, NotificationSinkRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, NotificationSinkRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> NotificationSink | None:
    if response.status_code == 200:
        response_200 = NotificationSink.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[NotificationSink]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: NotificationSinkRequest | NotificationSinkRequest | NotificationSinkRequest | Unset = UNSET,
) -> Response[NotificationSink]:
    """Send a test notification to verify sink configuration.

    Args:
        id (UUID):
        body (NotificationSinkRequest): Full serializer for NotificationSink.
        body (NotificationSinkRequest): Full serializer for NotificationSink.
        body (NotificationSinkRequest): Full serializer for NotificationSink.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationSink]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: NotificationSinkRequest | NotificationSinkRequest | NotificationSinkRequest | Unset = UNSET,
) -> NotificationSink | None:
    """Send a test notification to verify sink configuration.

    Args:
        id (UUID):
        body (NotificationSinkRequest): Full serializer for NotificationSink.
        body (NotificationSinkRequest): Full serializer for NotificationSink.
        body (NotificationSinkRequest): Full serializer for NotificationSink.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationSink
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: NotificationSinkRequest | NotificationSinkRequest | NotificationSinkRequest | Unset = UNSET,
) -> Response[NotificationSink]:
    """Send a test notification to verify sink configuration.

    Args:
        id (UUID):
        body (NotificationSinkRequest): Full serializer for NotificationSink.
        body (NotificationSinkRequest): Full serializer for NotificationSink.
        body (NotificationSinkRequest): Full serializer for NotificationSink.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationSink]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: NotificationSinkRequest | NotificationSinkRequest | NotificationSinkRequest | Unset = UNSET,
) -> NotificationSink | None:
    """Send a test notification to verify sink configuration.

    Args:
        id (UUID):
        body (NotificationSinkRequest): Full serializer for NotificationSink.
        body (NotificationSinkRequest): Full serializer for NotificationSink.
        body (NotificationSinkRequest): Full serializer for NotificationSink.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationSink
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
