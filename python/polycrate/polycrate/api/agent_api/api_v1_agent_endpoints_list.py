from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_endpoint import AgentEndpoint
from ...types import Response


def _get_kwargs(
    *,
    x_agent_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Agent-ID"] = x_agent_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/agent/endpoints/",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[AgentEndpoint] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AgentEndpoint.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | list[AgentEndpoint]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    x_agent_id: str,
) -> Response[Any | list[AgentEndpoint]]:
    """List endpoints for agent monitoring


        Returns the list of endpoints that this agent should monitor.

        Uses static agent-endpoint assignment via M2M relations:
        - Endpoints are pre-assigned to agents via Celery task
        - Returns statically assigned endpoints for optimal performance
        - Assignment respects agent capacity and monitoring modes


    Args:
        x_agent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[AgentEndpoint]]
    """

    kwargs = _get_kwargs(
        x_agent_id=x_agent_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    x_agent_id: str,
) -> Any | list[AgentEndpoint] | None:
    """List endpoints for agent monitoring


        Returns the list of endpoints that this agent should monitor.

        Uses static agent-endpoint assignment via M2M relations:
        - Endpoints are pre-assigned to agents via Celery task
        - Returns statically assigned endpoints for optimal performance
        - Assignment respects agent capacity and monitoring modes


    Args:
        x_agent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[AgentEndpoint]
    """

    return sync_detailed(
        client=client,
        x_agent_id=x_agent_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    x_agent_id: str,
) -> Response[Any | list[AgentEndpoint]]:
    """List endpoints for agent monitoring


        Returns the list of endpoints that this agent should monitor.

        Uses static agent-endpoint assignment via M2M relations:
        - Endpoints are pre-assigned to agents via Celery task
        - Returns statically assigned endpoints for optimal performance
        - Assignment respects agent capacity and monitoring modes


    Args:
        x_agent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[AgentEndpoint]]
    """

    kwargs = _get_kwargs(
        x_agent_id=x_agent_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    x_agent_id: str,
) -> Any | list[AgentEndpoint] | None:
    """List endpoints for agent monitoring


        Returns the list of endpoints that this agent should monitor.

        Uses static agent-endpoint assignment via M2M relations:
        - Endpoints are pre-assigned to agents via Celery task
        - Returns statically assigned endpoints for optimal performance
        - Assignment respects agent capacity and monitoring modes


    Args:
        x_agent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[AgentEndpoint]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_agent_id=x_agent_id,
        )
    ).parsed
