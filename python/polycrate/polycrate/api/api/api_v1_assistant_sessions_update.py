from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assistant_session import AssistantSession
from ...models.assistant_session_request import AssistantSessionRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: AssistantSessionRequest | AssistantSessionRequest | AssistantSessionRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/assistant-sessions/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, AssistantSessionRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, AssistantSessionRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AssistantSessionRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AssistantSession | None:
    if response.status_code == 200:
        response_200 = AssistantSession.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AssistantSession]:
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
    body: AssistantSessionRequest | AssistantSessionRequest | AssistantSessionRequest | Unset = UNSET,
) -> Response[AssistantSession]:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (AssistantSessionRequest): Detail/create/partial serializer. Spec: polycrate spec
            inspect 738
        body (AssistantSessionRequest): Detail/create/partial serializer. Spec: polycrate spec
            inspect 738
        body (AssistantSessionRequest): Detail/create/partial serializer. Spec: polycrate spec
            inspect 738

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssistantSession]
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
    body: AssistantSessionRequest | AssistantSessionRequest | AssistantSessionRequest | Unset = UNSET,
) -> AssistantSession | None:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (AssistantSessionRequest): Detail/create/partial serializer. Spec: polycrate spec
            inspect 738
        body (AssistantSessionRequest): Detail/create/partial serializer. Spec: polycrate spec
            inspect 738
        body (AssistantSessionRequest): Detail/create/partial serializer. Spec: polycrate spec
            inspect 738

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssistantSession
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
    body: AssistantSessionRequest | AssistantSessionRequest | AssistantSessionRequest | Unset = UNSET,
) -> Response[AssistantSession]:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (AssistantSessionRequest): Detail/create/partial serializer. Spec: polycrate spec
            inspect 738
        body (AssistantSessionRequest): Detail/create/partial serializer. Spec: polycrate spec
            inspect 738
        body (AssistantSessionRequest): Detail/create/partial serializer. Spec: polycrate spec
            inspect 738

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssistantSession]
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
    body: AssistantSessionRequest | AssistantSessionRequest | AssistantSessionRequest | Unset = UNSET,
) -> AssistantSession | None:
    """Apply the same IntegrityError → 409 mapping to updates (Spec 159 F2).

    Args:
        id (UUID):
        body (AssistantSessionRequest): Detail/create/partial serializer. Spec: polycrate spec
            inspect 738
        body (AssistantSessionRequest): Detail/create/partial serializer. Spec: polycrate spec
            inspect 738
        body (AssistantSessionRequest): Detail/create/partial serializer. Spec: polycrate spec
            inspect 738

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssistantSession
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
