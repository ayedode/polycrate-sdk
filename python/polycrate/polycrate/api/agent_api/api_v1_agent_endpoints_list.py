from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_endpoint import AgentEndpoint
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_409 import ErrorResponse409
from ...models.error_response_410 import ErrorResponse410
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.error_response_502 import ErrorResponse502
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
) -> (
    Any
    | ErrorResponse401
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | list[AgentEndpoint]
    | None
):
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

    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 405:
        response_405 = ErrorResponse405.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = ErrorResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = ErrorResponse409.from_dict(response.json())

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
    | ErrorResponse401
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | list[AgentEndpoint]
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
    x_agent_id: str,
) -> Response[
    Any
    | ErrorResponse401
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | list[AgentEndpoint]
]:
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
        Response[Any | ErrorResponse401 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | list[AgentEndpoint]]
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
) -> (
    Any
    | ErrorResponse401
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | list[AgentEndpoint]
    | None
):
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
        Any | ErrorResponse401 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | list[AgentEndpoint]
    """

    return sync_detailed(
        client=client,
        x_agent_id=x_agent_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    x_agent_id: str,
) -> Response[
    Any
    | ErrorResponse401
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | list[AgentEndpoint]
]:
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
        Response[Any | ErrorResponse401 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | list[AgentEndpoint]]
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
) -> (
    Any
    | ErrorResponse401
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | list[AgentEndpoint]
    | None
):
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
        Any | ErrorResponse401 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | list[AgentEndpoint]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_agent_id=x_agent_id,
        )
    ).parsed
