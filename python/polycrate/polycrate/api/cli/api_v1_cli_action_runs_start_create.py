from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cli_action_run_start_conflict_response import CLIActionRunStartConflictResponse
from ...models.cli_action_run_start_request_request import CLIActionRunStartRequestRequest
from ...models.cli_action_run_start_response import CLIActionRunStartResponse
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_404 import ErrorResponse404
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_410 import ErrorResponse410
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.error_response_502 import ErrorResponse502
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CLIActionRunStartRequestRequest
    | CLIActionRunStartRequestRequest
    | CLIActionRunStartRequestRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/cli/action-runs/start/",
    }

    if isinstance(body, CLIActionRunStartRequestRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CLIActionRunStartRequestRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CLIActionRunStartRequestRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | CLIActionRunStartConflictResponse
    | CLIActionRunStartResponse
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | None
):
    if response.status_code == 201:
        response_201 = CLIActionRunStartResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
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
        response_409 = CLIActionRunStartConflictResponse.from_dict(response.json())

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
    Any
    | CLIActionRunStartConflictResponse
    | CLIActionRunStartResponse
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
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
    body: CLIActionRunStartRequestRequest
    | CLIActionRunStartRequestRequest
    | CLIActionRunStartRequestRequest
    | Unset = UNSET,
) -> Response[
    Any
    | CLIActionRunStartConflictResponse
    | CLIActionRunStartResponse
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
]:
    """Register CLI action run start (phase 1)

     Registers a new ActionRun before the CLI action executes. Returns an ID the CLI sets as
    polycrate_actionrun_id block label. Returns 409 if a running/pending ActionRun already exists for
    the same block+workspace (unless force=true).

    Args:
        body (CLIActionRunStartRequestRequest):
        body (CLIActionRunStartRequestRequest):
        body (CLIActionRunStartRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CLIActionRunStartConflictResponse | CLIActionRunStartResponse | ErrorResponse401 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502]
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
    body: CLIActionRunStartRequestRequest
    | CLIActionRunStartRequestRequest
    | CLIActionRunStartRequestRequest
    | Unset = UNSET,
) -> (
    Any
    | CLIActionRunStartConflictResponse
    | CLIActionRunStartResponse
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | None
):
    """Register CLI action run start (phase 1)

     Registers a new ActionRun before the CLI action executes. Returns an ID the CLI sets as
    polycrate_actionrun_id block label. Returns 409 if a running/pending ActionRun already exists for
    the same block+workspace (unless force=true).

    Args:
        body (CLIActionRunStartRequestRequest):
        body (CLIActionRunStartRequestRequest):
        body (CLIActionRunStartRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CLIActionRunStartConflictResponse | CLIActionRunStartResponse | ErrorResponse401 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CLIActionRunStartRequestRequest
    | CLIActionRunStartRequestRequest
    | CLIActionRunStartRequestRequest
    | Unset = UNSET,
) -> Response[
    Any
    | CLIActionRunStartConflictResponse
    | CLIActionRunStartResponse
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
]:
    """Register CLI action run start (phase 1)

     Registers a new ActionRun before the CLI action executes. Returns an ID the CLI sets as
    polycrate_actionrun_id block label. Returns 409 if a running/pending ActionRun already exists for
    the same block+workspace (unless force=true).

    Args:
        body (CLIActionRunStartRequestRequest):
        body (CLIActionRunStartRequestRequest):
        body (CLIActionRunStartRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CLIActionRunStartConflictResponse | CLIActionRunStartResponse | ErrorResponse401 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CLIActionRunStartRequestRequest
    | CLIActionRunStartRequestRequest
    | CLIActionRunStartRequestRequest
    | Unset = UNSET,
) -> (
    Any
    | CLIActionRunStartConflictResponse
    | CLIActionRunStartResponse
    | ErrorResponse401
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | None
):
    """Register CLI action run start (phase 1)

     Registers a new ActionRun before the CLI action executes. Returns an ID the CLI sets as
    polycrate_actionrun_id block label. Returns 409 if a running/pending ActionRun already exists for
    the same block+workspace (unless force=true).

    Args:
        body (CLIActionRunStartRequestRequest):
        body (CLIActionRunStartRequestRequest):
        body (CLIActionRunStartRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CLIActionRunStartConflictResponse | CLIActionRunStartResponse | ErrorResponse401 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
