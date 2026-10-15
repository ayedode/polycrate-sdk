from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_error_report_request_request import AgentErrorReportRequestRequest
from ...models.agent_error_submission_response import AgentErrorSubmissionResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: AgentErrorReportRequestRequest
    | AgentErrorReportRequestRequest
    | AgentErrorReportRequestRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/agent/errors/",
    }

    if isinstance(body, AgentErrorReportRequestRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, AgentErrorReportRequestRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AgentErrorReportRequestRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentErrorSubmissionResponse | Any | None:
    if response.status_code == 201:
        response_201 = AgentErrorSubmissionResponse.from_dict(response.json())

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
) -> Response[AgentErrorSubmissionResponse | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AgentErrorReportRequestRequest
    | AgentErrorReportRequestRequest
    | AgentErrorReportRequestRequest
    | Unset = UNSET,
) -> Response[AgentErrorSubmissionResponse | Any]:
    """Submit agent error reports


        Accepts and stores agent error reports.

        Error reports include:
        - Total error count
        - Error counts by category
        - Critical errors list
        - Recent errors with timestamps
        - System info at time of errors

        Critical errors will trigger condition updates on the agent.


    Args:
        body (AgentErrorReportRequestRequest):
        body (AgentErrorReportRequestRequest):
        body (AgentErrorReportRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentErrorSubmissionResponse | Any]
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
    body: AgentErrorReportRequestRequest
    | AgentErrorReportRequestRequest
    | AgentErrorReportRequestRequest
    | Unset = UNSET,
) -> AgentErrorSubmissionResponse | Any | None:
    """Submit agent error reports


        Accepts and stores agent error reports.

        Error reports include:
        - Total error count
        - Error counts by category
        - Critical errors list
        - Recent errors with timestamps
        - System info at time of errors

        Critical errors will trigger condition updates on the agent.


    Args:
        body (AgentErrorReportRequestRequest):
        body (AgentErrorReportRequestRequest):
        body (AgentErrorReportRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentErrorSubmissionResponse | Any
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AgentErrorReportRequestRequest
    | AgentErrorReportRequestRequest
    | AgentErrorReportRequestRequest
    | Unset = UNSET,
) -> Response[AgentErrorSubmissionResponse | Any]:
    """Submit agent error reports


        Accepts and stores agent error reports.

        Error reports include:
        - Total error count
        - Error counts by category
        - Critical errors list
        - Recent errors with timestamps
        - System info at time of errors

        Critical errors will trigger condition updates on the agent.


    Args:
        body (AgentErrorReportRequestRequest):
        body (AgentErrorReportRequestRequest):
        body (AgentErrorReportRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentErrorSubmissionResponse | Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AgentErrorReportRequestRequest
    | AgentErrorReportRequestRequest
    | AgentErrorReportRequestRequest
    | Unset = UNSET,
) -> AgentErrorSubmissionResponse | Any | None:
    """Submit agent error reports


        Accepts and stores agent error reports.

        Error reports include:
        - Total error count
        - Error counts by category
        - Critical errors list
        - Recent errors with timestamps
        - System info at time of errors

        Critical errors will trigger condition updates on the agent.


    Args:
        body (AgentErrorReportRequestRequest):
        body (AgentErrorReportRequestRequest):
        body (AgentErrorReportRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentErrorSubmissionResponse | Any
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
