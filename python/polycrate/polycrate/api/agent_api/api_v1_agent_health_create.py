from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_health_data_request import AgentHealthDataRequest
from ...models.agent_health_submission_response import AgentHealthSubmissionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AgentHealthDataRequest | AgentHealthDataRequest | AgentHealthDataRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/agent/health/",
    }

    if isinstance(body, AgentHealthDataRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, AgentHealthDataRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AgentHealthDataRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentHealthSubmissionResponse | Any | None:
    if response.status_code == 201:
        response_201 = AgentHealthSubmissionResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentHealthSubmissionResponse | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AgentHealthDataRequest | AgentHealthDataRequest | AgentHealthDataRequest | Unset = UNSET,
) -> Response[AgentHealthSubmissionResponse | Any]:
    """Submit agent health data


        Accepts and stores agent health and performance data.

        This endpoint also handles agent registration:
        - If agent does not exist, it will be created
        - Agent's source_pop is derived from workspace.pop
        - Updates agent activity timestamp on each call
        - Returns workspace and organization context for automatic operator configuration

        Health data includes:
        - System metrics (CPU, memory, disk)
        - Network metrics
        - Check execution statistics
        - Error counts and warnings

        The response includes workspace_id, workspace_name, organization_id, and organization_name
        to enable automatic workspace resolution in the Polycrate Operator.
        See: .specs/0.11.0/agent-workspace-response.md


    Args:
        body (AgentHealthDataRequest | Unset): Serializer for agents to submit health data.

            Extended in 0.11.9 to accept check_summary and check_results.
            Now writes directly to Agent model instead of creating AgentHealthData.

            Per .specs/0.11.9/index.md - Sektion 4
        body (AgentHealthDataRequest | Unset): Serializer for agents to submit health data.

            Extended in 0.11.9 to accept check_summary and check_results.
            Now writes directly to Agent model instead of creating AgentHealthData.

            Per .specs/0.11.9/index.md - Sektion 4
        body (AgentHealthDataRequest | Unset): Serializer for agents to submit health data.

            Extended in 0.11.9 to accept check_summary and check_results.
            Now writes directly to Agent model instead of creating AgentHealthData.

            Per .specs/0.11.9/index.md - Sektion 4

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentHealthSubmissionResponse | Any]
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
    body: AgentHealthDataRequest | AgentHealthDataRequest | AgentHealthDataRequest | Unset = UNSET,
) -> AgentHealthSubmissionResponse | Any | None:
    """Submit agent health data


        Accepts and stores agent health and performance data.

        This endpoint also handles agent registration:
        - If agent does not exist, it will be created
        - Agent's source_pop is derived from workspace.pop
        - Updates agent activity timestamp on each call
        - Returns workspace and organization context for automatic operator configuration

        Health data includes:
        - System metrics (CPU, memory, disk)
        - Network metrics
        - Check execution statistics
        - Error counts and warnings

        The response includes workspace_id, workspace_name, organization_id, and organization_name
        to enable automatic workspace resolution in the Polycrate Operator.
        See: .specs/0.11.0/agent-workspace-response.md


    Args:
        body (AgentHealthDataRequest | Unset): Serializer for agents to submit health data.

            Extended in 0.11.9 to accept check_summary and check_results.
            Now writes directly to Agent model instead of creating AgentHealthData.

            Per .specs/0.11.9/index.md - Sektion 4
        body (AgentHealthDataRequest | Unset): Serializer for agents to submit health data.

            Extended in 0.11.9 to accept check_summary and check_results.
            Now writes directly to Agent model instead of creating AgentHealthData.

            Per .specs/0.11.9/index.md - Sektion 4
        body (AgentHealthDataRequest | Unset): Serializer for agents to submit health data.

            Extended in 0.11.9 to accept check_summary and check_results.
            Now writes directly to Agent model instead of creating AgentHealthData.

            Per .specs/0.11.9/index.md - Sektion 4

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentHealthSubmissionResponse | Any
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AgentHealthDataRequest | AgentHealthDataRequest | AgentHealthDataRequest | Unset = UNSET,
) -> Response[AgentHealthSubmissionResponse | Any]:
    """Submit agent health data


        Accepts and stores agent health and performance data.

        This endpoint also handles agent registration:
        - If agent does not exist, it will be created
        - Agent's source_pop is derived from workspace.pop
        - Updates agent activity timestamp on each call
        - Returns workspace and organization context for automatic operator configuration

        Health data includes:
        - System metrics (CPU, memory, disk)
        - Network metrics
        - Check execution statistics
        - Error counts and warnings

        The response includes workspace_id, workspace_name, organization_id, and organization_name
        to enable automatic workspace resolution in the Polycrate Operator.
        See: .specs/0.11.0/agent-workspace-response.md


    Args:
        body (AgentHealthDataRequest | Unset): Serializer for agents to submit health data.

            Extended in 0.11.9 to accept check_summary and check_results.
            Now writes directly to Agent model instead of creating AgentHealthData.

            Per .specs/0.11.9/index.md - Sektion 4
        body (AgentHealthDataRequest | Unset): Serializer for agents to submit health data.

            Extended in 0.11.9 to accept check_summary and check_results.
            Now writes directly to Agent model instead of creating AgentHealthData.

            Per .specs/0.11.9/index.md - Sektion 4
        body (AgentHealthDataRequest | Unset): Serializer for agents to submit health data.

            Extended in 0.11.9 to accept check_summary and check_results.
            Now writes directly to Agent model instead of creating AgentHealthData.

            Per .specs/0.11.9/index.md - Sektion 4

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentHealthSubmissionResponse | Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AgentHealthDataRequest | AgentHealthDataRequest | AgentHealthDataRequest | Unset = UNSET,
) -> AgentHealthSubmissionResponse | Any | None:
    """Submit agent health data


        Accepts and stores agent health and performance data.

        This endpoint also handles agent registration:
        - If agent does not exist, it will be created
        - Agent's source_pop is derived from workspace.pop
        - Updates agent activity timestamp on each call
        - Returns workspace and organization context for automatic operator configuration

        Health data includes:
        - System metrics (CPU, memory, disk)
        - Network metrics
        - Check execution statistics
        - Error counts and warnings

        The response includes workspace_id, workspace_name, organization_id, and organization_name
        to enable automatic workspace resolution in the Polycrate Operator.
        See: .specs/0.11.0/agent-workspace-response.md


    Args:
        body (AgentHealthDataRequest | Unset): Serializer for agents to submit health data.

            Extended in 0.11.9 to accept check_summary and check_results.
            Now writes directly to Agent model instead of creating AgentHealthData.

            Per .specs/0.11.9/index.md - Sektion 4
        body (AgentHealthDataRequest | Unset): Serializer for agents to submit health data.

            Extended in 0.11.9 to accept check_summary and check_results.
            Now writes directly to Agent model instead of creating AgentHealthData.

            Per .specs/0.11.9/index.md - Sektion 4
        body (AgentHealthDataRequest | Unset): Serializer for agents to submit health data.

            Extended in 0.11.9 to accept check_summary and check_results.
            Now writes directly to Agent model instead of creating AgentHealthData.

            Per .specs/0.11.9/index.md - Sektion 4

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentHealthSubmissionResponse | Any
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
