from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dashboard_operations_response import DashboardOperationsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fresh: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fresh"] = fresh

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/dashboard/operations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DashboardOperationsResponse | None:
    if response.status_code == 200:
        response_200 = DashboardOperationsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DashboardOperationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    fresh: bool | Unset = UNSET,
) -> Response[DashboardOperationsResponse]:
    """Dashboard operations overview (list sections)

     Operations cockpit list sections for the dashboard Overview tab.

    Spec: polycrate spec inspect 412
    Spec 515: Redis-cached lists only; S3/LB via DashboardOperationsWidgetsView.

    Args:
        fresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DashboardOperationsResponse]
    """

    kwargs = _get_kwargs(
        fresh=fresh,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    fresh: bool | Unset = UNSET,
) -> DashboardOperationsResponse | None:
    """Dashboard operations overview (list sections)

     Operations cockpit list sections for the dashboard Overview tab.

    Spec: polycrate spec inspect 412
    Spec 515: Redis-cached lists only; S3/LB via DashboardOperationsWidgetsView.

    Args:
        fresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DashboardOperationsResponse
    """

    return sync_detailed(
        client=client,
        fresh=fresh,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    fresh: bool | Unset = UNSET,
) -> Response[DashboardOperationsResponse]:
    """Dashboard operations overview (list sections)

     Operations cockpit list sections for the dashboard Overview tab.

    Spec: polycrate spec inspect 412
    Spec 515: Redis-cached lists only; S3/LB via DashboardOperationsWidgetsView.

    Args:
        fresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DashboardOperationsResponse]
    """

    kwargs = _get_kwargs(
        fresh=fresh,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    fresh: bool | Unset = UNSET,
) -> DashboardOperationsResponse | None:
    """Dashboard operations overview (list sections)

     Operations cockpit list sections for the dashboard Overview tab.

    Spec: polycrate spec inspect 412
    Spec 515: Redis-cached lists only; S3/LB via DashboardOperationsWidgetsView.

    Args:
        fresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DashboardOperationsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            fresh=fresh,
        )
    ).parsed
