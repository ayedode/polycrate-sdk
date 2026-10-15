from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.policy_binding import PolicyBinding
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/policy-bindings/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PolicyBinding | None:
    if response.status_code == 200:
        response_200 = PolicyBinding.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PolicyBinding]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[PolicyBinding]:
    """API ViewSet for PolicyBinding management.

    NEW in v4.0 - CRUD endpoints for policy bindings.

    Features:
    - List bindings (filter by policy or target object)
    - Create binding (assign policy to object)
    - Update binding (enable/disable)
    - Delete binding (unassign policy)

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PolicyBinding]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
) -> PolicyBinding | None:
    """API ViewSet for PolicyBinding management.

    NEW in v4.0 - CRUD endpoints for policy bindings.

    Features:
    - List bindings (filter by policy or target object)
    - Create binding (assign policy to object)
    - Update binding (enable/disable)
    - Delete binding (unassign policy)

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PolicyBinding
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[PolicyBinding]:
    """API ViewSet for PolicyBinding management.

    NEW in v4.0 - CRUD endpoints for policy bindings.

    Features:
    - List bindings (filter by policy or target object)
    - Create binding (assign policy to object)
    - Update binding (enable/disable)
    - Delete binding (unassign policy)

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PolicyBinding]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
) -> PolicyBinding | None:
    """API ViewSet for PolicyBinding management.

    NEW in v4.0 - CRUD endpoints for policy bindings.

    Features:
    - List bindings (filter by policy or target object)
    - Create binding (assign policy to object)
    - Update binding (enable/disable)
    - Delete binding (unassign policy)

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PolicyBinding
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
