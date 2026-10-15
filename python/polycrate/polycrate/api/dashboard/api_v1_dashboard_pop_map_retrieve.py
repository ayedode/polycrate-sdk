from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pop_map_response import PopMapResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_organization: str | Unset = UNSET
    if not isinstance(organization, Unset):
        json_organization = str(organization)
    params["organization"] = json_organization

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/dashboard/pop-map/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PopMapResponse | None:
    if response.status_code == 200:
        response_200 = PopMapResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PopMapResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    organization: UUID | Unset = UNSET,
) -> Response[PopMapResponse]:
    """Active PoPs with workspaces

     Returns PoPs that have at least one workspace assigned within the user's scope.

    Spec: .specs/0.13.0/dashboard-pop-map-widget.md

    Args:
        organization (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PopMapResponse]
    """

    kwargs = _get_kwargs(
        organization=organization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    organization: UUID | Unset = UNSET,
) -> PopMapResponse | None:
    """Active PoPs with workspaces

     Returns PoPs that have at least one workspace assigned within the user's scope.

    Spec: .specs/0.13.0/dashboard-pop-map-widget.md

    Args:
        organization (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PopMapResponse
    """

    return sync_detailed(
        client=client,
        organization=organization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    organization: UUID | Unset = UNSET,
) -> Response[PopMapResponse]:
    """Active PoPs with workspaces

     Returns PoPs that have at least one workspace assigned within the user's scope.

    Spec: .specs/0.13.0/dashboard-pop-map-widget.md

    Args:
        organization (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PopMapResponse]
    """

    kwargs = _get_kwargs(
        organization=organization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    organization: UUID | Unset = UNSET,
) -> PopMapResponse | None:
    """Active PoPs with workspaces

     Returns PoPs that have at least one workspace assigned within the user's scope.

    Spec: .specs/0.13.0/dashboard-pop-map-widget.md

    Args:
        organization (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PopMapResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            organization=organization,
        )
    ).parsed
