from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_run_submission_request_request import ActionRunSubmissionRequestRequest
from ...models.action_run_submission_response import ActionRunSubmissionResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: ActionRunSubmissionRequestRequest
    | ActionRunSubmissionRequestRequest
    | ActionRunSubmissionRequestRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/cli/action-runs/",
    }

    if isinstance(body, ActionRunSubmissionRequestRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ActionRunSubmissionRequestRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ActionRunSubmissionRequestRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActionRunSubmissionResponse | Any | None:
    if response.status_code == 201:
        response_201 = ActionRunSubmissionResponse.from_dict(response.json())

        return response_201

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
) -> Response[ActionRunSubmissionResponse | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ActionRunSubmissionRequestRequest
    | ActionRunSubmissionRequestRequest
    | ActionRunSubmissionRequestRequest
    | Unset = UNSET,
) -> Response[ActionRunSubmissionResponse | Any]:
    """Submit CLI action run results


        Accepts action run results from Polycrate CLI and creates ActionRun objects.

        Used by `polycrate run` command to report action execution results including:
        - Exit code, stdout, stderr
        - Timing information (started_at, finished_at)
        - Block configuration snapshot
        - Optional metadata


    Args:
        body (ActionRunSubmissionRequestRequest):
        body (ActionRunSubmissionRequestRequest):
        body (ActionRunSubmissionRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionRunSubmissionResponse | Any]
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
    body: ActionRunSubmissionRequestRequest
    | ActionRunSubmissionRequestRequest
    | ActionRunSubmissionRequestRequest
    | Unset = UNSET,
) -> ActionRunSubmissionResponse | Any | None:
    """Submit CLI action run results


        Accepts action run results from Polycrate CLI and creates ActionRun objects.

        Used by `polycrate run` command to report action execution results including:
        - Exit code, stdout, stderr
        - Timing information (started_at, finished_at)
        - Block configuration snapshot
        - Optional metadata


    Args:
        body (ActionRunSubmissionRequestRequest):
        body (ActionRunSubmissionRequestRequest):
        body (ActionRunSubmissionRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionRunSubmissionResponse | Any
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ActionRunSubmissionRequestRequest
    | ActionRunSubmissionRequestRequest
    | ActionRunSubmissionRequestRequest
    | Unset = UNSET,
) -> Response[ActionRunSubmissionResponse | Any]:
    """Submit CLI action run results


        Accepts action run results from Polycrate CLI and creates ActionRun objects.

        Used by `polycrate run` command to report action execution results including:
        - Exit code, stdout, stderr
        - Timing information (started_at, finished_at)
        - Block configuration snapshot
        - Optional metadata


    Args:
        body (ActionRunSubmissionRequestRequest):
        body (ActionRunSubmissionRequestRequest):
        body (ActionRunSubmissionRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionRunSubmissionResponse | Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ActionRunSubmissionRequestRequest
    | ActionRunSubmissionRequestRequest
    | ActionRunSubmissionRequestRequest
    | Unset = UNSET,
) -> ActionRunSubmissionResponse | Any | None:
    """Submit CLI action run results


        Accepts action run results from Polycrate CLI and creates ActionRun objects.

        Used by `polycrate run` command to report action execution results including:
        - Exit code, stdout, stderr
        - Timing information (started_at, finished_at)
        - Block configuration snapshot
        - Optional metadata


    Args:
        body (ActionRunSubmissionRequestRequest):
        body (ActionRunSubmissionRequestRequest):
        body (ActionRunSubmissionRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionRunSubmissionResponse | Any
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
