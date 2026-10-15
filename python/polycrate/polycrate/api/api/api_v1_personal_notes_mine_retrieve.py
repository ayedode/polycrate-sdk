from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.personal_note import PersonalNote
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/personal-notes/mine/",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PersonalNote | None:
    if response.status_code == 200:
        response_200 = PersonalNote.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PersonalNote]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[PersonalNote]:
    """REST API for the current user's personal note scratch-pad.

    Per .specs/0.14.10/personal-note.md

    GET  /api/v1/personal-notes/mine/  — fetch (or lazily create) the note
    PATCH /api/v1/personal-notes/mine/ — partial update (content)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PersonalNote]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> PersonalNote | None:
    """REST API for the current user's personal note scratch-pad.

    Per .specs/0.14.10/personal-note.md

    GET  /api/v1/personal-notes/mine/  — fetch (or lazily create) the note
    PATCH /api/v1/personal-notes/mine/ — partial update (content)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PersonalNote
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[PersonalNote]:
    """REST API for the current user's personal note scratch-pad.

    Per .specs/0.14.10/personal-note.md

    GET  /api/v1/personal-notes/mine/  — fetch (or lazily create) the note
    PATCH /api/v1/personal-notes/mine/ — partial update (content)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PersonalNote]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> PersonalNote | None:
    """REST API for the current user's personal note scratch-pad.

    Per .specs/0.14.10/personal-note.md

    GET  /api/v1/personal-notes/mine/  — fetch (or lazily create) the note
    PATCH /api/v1/personal-notes/mine/ — partial update (content)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PersonalNote
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
