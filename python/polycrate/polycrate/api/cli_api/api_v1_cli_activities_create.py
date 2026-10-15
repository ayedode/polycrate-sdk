from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cli_activity_submission_request_request import CLIActivitySubmissionRequestRequest
from ...models.cli_activity_submission_response import CLIActivitySubmissionResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CLIActivitySubmissionRequestRequest
    | CLIActivitySubmissionRequestRequest
    | CLIActivitySubmissionRequestRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/cli/activities/",
    }

    if isinstance(body, CLIActivitySubmissionRequestRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CLIActivitySubmissionRequestRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CLIActivitySubmissionRequestRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CLIActivitySubmissionResponse | None:
    if response.status_code == 201:
        response_201 = CLIActivitySubmissionResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

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
) -> Response[Any | CLIActivitySubmissionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CLIActivitySubmissionRequestRequest
    | CLIActivitySubmissionRequestRequest
    | CLIActivitySubmissionRequestRequest
    | Unset = UNSET,
) -> Response[Any | CLIActivitySubmissionResponse]:
    """Create CLI activity (ssh-session, workspace-sync)


        Accepts CLI activity data and creates Activity objects for audit/compliance.

        Used by `polycrate ssh` (ssh-session) and `polycrate workspace sync` / `polycrate git sync`
        (workspace-sync). Returns activity_id and activity_url for PATCH updates.


    Args:
        body (CLIActivitySubmissionRequestRequest):
        body (CLIActivitySubmissionRequestRequest):
        body (CLIActivitySubmissionRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CLIActivitySubmissionResponse]
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
    body: CLIActivitySubmissionRequestRequest
    | CLIActivitySubmissionRequestRequest
    | CLIActivitySubmissionRequestRequest
    | Unset = UNSET,
) -> Any | CLIActivitySubmissionResponse | None:
    """Create CLI activity (ssh-session, workspace-sync)


        Accepts CLI activity data and creates Activity objects for audit/compliance.

        Used by `polycrate ssh` (ssh-session) and `polycrate workspace sync` / `polycrate git sync`
        (workspace-sync). Returns activity_id and activity_url for PATCH updates.


    Args:
        body (CLIActivitySubmissionRequestRequest):
        body (CLIActivitySubmissionRequestRequest):
        body (CLIActivitySubmissionRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CLIActivitySubmissionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CLIActivitySubmissionRequestRequest
    | CLIActivitySubmissionRequestRequest
    | CLIActivitySubmissionRequestRequest
    | Unset = UNSET,
) -> Response[Any | CLIActivitySubmissionResponse]:
    """Create CLI activity (ssh-session, workspace-sync)


        Accepts CLI activity data and creates Activity objects for audit/compliance.

        Used by `polycrate ssh` (ssh-session) and `polycrate workspace sync` / `polycrate git sync`
        (workspace-sync). Returns activity_id and activity_url for PATCH updates.


    Args:
        body (CLIActivitySubmissionRequestRequest):
        body (CLIActivitySubmissionRequestRequest):
        body (CLIActivitySubmissionRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CLIActivitySubmissionResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CLIActivitySubmissionRequestRequest
    | CLIActivitySubmissionRequestRequest
    | CLIActivitySubmissionRequestRequest
    | Unset = UNSET,
) -> Any | CLIActivitySubmissionResponse | None:
    """Create CLI activity (ssh-session, workspace-sync)


        Accepts CLI activity data and creates Activity objects for audit/compliance.

        Used by `polycrate ssh` (ssh-session) and `polycrate workspace sync` / `polycrate git sync`
        (workspace-sync). Returns activity_id and activity_url for PATCH updates.


    Args:
        body (CLIActivitySubmissionRequestRequest):
        body (CLIActivitySubmissionRequestRequest):
        body (CLIActivitySubmissionRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CLIActivitySubmissionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
