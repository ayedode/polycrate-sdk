from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cli_action_run_finish_request_request import CLIActionRunFinishRequestRequest
from ...models.cli_action_run_finish_response import CLIActionRunFinishResponse
from ...types import UNSET, Response


def _get_kwargs(
    action_run_id: UUID,
    *,
    body: CLIActionRunFinishRequestRequest
    | CLIActionRunFinishRequestRequest
    | CLIActionRunFinishRequestRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/cli/action-runs/{action_run_id}/finish/".format(
            action_run_id=quote(str(action_run_id), safe=""),
        ),
    }

    if isinstance(body, CLIActionRunFinishRequestRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CLIActionRunFinishRequestRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CLIActionRunFinishRequestRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CLIActionRunFinishResponse | None:
    if response.status_code == 200:
        response_200 = CLIActionRunFinishResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CLIActionRunFinishResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    action_run_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CLIActionRunFinishRequestRequest
    | CLIActionRunFinishRequestRequest
    | CLIActionRunFinishRequestRequest
    | Unset = UNSET,
) -> Response[Any | CLIActionRunFinishResponse]:
    """Finish CLI action run (phase 2)

     Updates an existing ActionRun with execution results. Maps exit_code 0 to success, non-zero to
    failed.

    Args:
        action_run_id (UUID):
        body (CLIActionRunFinishRequestRequest):
        body (CLIActionRunFinishRequestRequest):
        body (CLIActionRunFinishRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CLIActionRunFinishResponse]
    """

    kwargs = _get_kwargs(
        action_run_id=action_run_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    action_run_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CLIActionRunFinishRequestRequest
    | CLIActionRunFinishRequestRequest
    | CLIActionRunFinishRequestRequest
    | Unset = UNSET,
) -> Any | CLIActionRunFinishResponse | None:
    """Finish CLI action run (phase 2)

     Updates an existing ActionRun with execution results. Maps exit_code 0 to success, non-zero to
    failed.

    Args:
        action_run_id (UUID):
        body (CLIActionRunFinishRequestRequest):
        body (CLIActionRunFinishRequestRequest):
        body (CLIActionRunFinishRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CLIActionRunFinishResponse
    """

    return sync_detailed(
        action_run_id=action_run_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    action_run_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CLIActionRunFinishRequestRequest
    | CLIActionRunFinishRequestRequest
    | CLIActionRunFinishRequestRequest
    | Unset = UNSET,
) -> Response[Any | CLIActionRunFinishResponse]:
    """Finish CLI action run (phase 2)

     Updates an existing ActionRun with execution results. Maps exit_code 0 to success, non-zero to
    failed.

    Args:
        action_run_id (UUID):
        body (CLIActionRunFinishRequestRequest):
        body (CLIActionRunFinishRequestRequest):
        body (CLIActionRunFinishRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CLIActionRunFinishResponse]
    """

    kwargs = _get_kwargs(
        action_run_id=action_run_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    action_run_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CLIActionRunFinishRequestRequest
    | CLIActionRunFinishRequestRequest
    | CLIActionRunFinishRequestRequest
    | Unset = UNSET,
) -> Any | CLIActionRunFinishResponse | None:
    """Finish CLI action run (phase 2)

     Updates an existing ActionRun with execution results. Maps exit_code 0 to success, non-zero to
    failed.

    Args:
        action_run_id (UUID):
        body (CLIActionRunFinishRequestRequest):
        body (CLIActionRunFinishRequestRequest):
        body (CLIActionRunFinishRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CLIActionRunFinishResponse
    """

    return (
        await asyncio_detailed(
            action_run_id=action_run_id,
            client=client,
            body=body,
        )
    ).parsed
