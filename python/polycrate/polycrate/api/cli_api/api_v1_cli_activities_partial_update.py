from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_cli_activity_update_request_request import PatchedCLIActivityUpdateRequestRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedCLIActivityUpdateRequestRequest
    | PatchedCLIActivityUpdateRequestRequest
    | PatchedCLIActivityUpdateRequestRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/cli/activities/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedCLIActivityUpdateRequestRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedCLIActivityUpdateRequestRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedCLIActivityUpdateRequestRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    body: PatchedCLIActivityUpdateRequestRequest
    | PatchedCLIActivityUpdateRequestRequest
    | PatchedCLIActivityUpdateRequestRequest
    | Unset = UNSET,
) -> Response[Any]:
    """Update CLI ssh-session activity


        Updates an ssh-session Activity with exit_code, finished_at, duration_seconds, status.
        Only allowed for activities created by the same user (created_by).


    Args:
        id (UUID):
        body (PatchedCLIActivityUpdateRequestRequest | Unset):
        body (PatchedCLIActivityUpdateRequestRequest | Unset):
        body (PatchedCLIActivityUpdateRequestRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: PatchedCLIActivityUpdateRequestRequest
    | PatchedCLIActivityUpdateRequestRequest
    | PatchedCLIActivityUpdateRequestRequest
    | Unset = UNSET,
) -> Response[Any]:
    """Update CLI ssh-session activity


        Updates an ssh-session Activity with exit_code, finished_at, duration_seconds, status.
        Only allowed for activities created by the same user (created_by).


    Args:
        id (UUID):
        body (PatchedCLIActivityUpdateRequestRequest | Unset):
        body (PatchedCLIActivityUpdateRequestRequest | Unset):
        body (PatchedCLIActivityUpdateRequestRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
