from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.slo_overview_response import SloOverviewResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization: str | Unset = UNSET,
    workspace: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["organization"] = organization

    params["workspace"] = workspace

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/slo-overview/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SloOverviewResponse | None:
    if response.status_code == 200:
        response_200 = SloOverviewResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SloOverviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    organization: str | Unset = UNSET,
    workspace: str | Unset = UNSET,
) -> Response[SloOverviewResponse]:
    """Get SLO/SLA overview


        Returns SLO/SLA status data for Endpoints and K8sClusters with optional
        organization and workspace filtering.

        Uses pre-computed ServiceLevelBreach records for breach/at_risk classification
        (created during object reconciliation) and bulk downtime queries for performance.

        **Statistics**:
        - `tracked`: Total number of monitored objects
        - `ok`: Objects with no active breach or warning
        - `at_risk`: Objects with active SLO/SLA warning (error budget running low)
        - `breached`: Objects with active SLO/SLA breach (error budget exhausted)
        - `in_downtime`: Objects currently in active downtime

        **Filtering**:
        - Filter by organization to see org-specific SLO status
        - Filter by workspace for workspace-level overview
        - Non-superusers only see data for their assigned organizations

        **Use Cases**:
        - Controlling/Reporting: Export SLO compliance data
        - Dashboard integration: Real-time SLO monitoring
        - Alerting: Identify objects requiring attention


    Args:
        organization (str | Unset):
        workspace (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SloOverviewResponse]
    """

    kwargs = _get_kwargs(
        organization=organization,
        workspace=workspace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    organization: str | Unset = UNSET,
    workspace: str | Unset = UNSET,
) -> SloOverviewResponse | None:
    """Get SLO/SLA overview


        Returns SLO/SLA status data for Endpoints and K8sClusters with optional
        organization and workspace filtering.

        Uses pre-computed ServiceLevelBreach records for breach/at_risk classification
        (created during object reconciliation) and bulk downtime queries for performance.

        **Statistics**:
        - `tracked`: Total number of monitored objects
        - `ok`: Objects with no active breach or warning
        - `at_risk`: Objects with active SLO/SLA warning (error budget running low)
        - `breached`: Objects with active SLO/SLA breach (error budget exhausted)
        - `in_downtime`: Objects currently in active downtime

        **Filtering**:
        - Filter by organization to see org-specific SLO status
        - Filter by workspace for workspace-level overview
        - Non-superusers only see data for their assigned organizations

        **Use Cases**:
        - Controlling/Reporting: Export SLO compliance data
        - Dashboard integration: Real-time SLO monitoring
        - Alerting: Identify objects requiring attention


    Args:
        organization (str | Unset):
        workspace (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SloOverviewResponse
    """

    return sync_detailed(
        client=client,
        organization=organization,
        workspace=workspace,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    organization: str | Unset = UNSET,
    workspace: str | Unset = UNSET,
) -> Response[SloOverviewResponse]:
    """Get SLO/SLA overview


        Returns SLO/SLA status data for Endpoints and K8sClusters with optional
        organization and workspace filtering.

        Uses pre-computed ServiceLevelBreach records for breach/at_risk classification
        (created during object reconciliation) and bulk downtime queries for performance.

        **Statistics**:
        - `tracked`: Total number of monitored objects
        - `ok`: Objects with no active breach or warning
        - `at_risk`: Objects with active SLO/SLA warning (error budget running low)
        - `breached`: Objects with active SLO/SLA breach (error budget exhausted)
        - `in_downtime`: Objects currently in active downtime

        **Filtering**:
        - Filter by organization to see org-specific SLO status
        - Filter by workspace for workspace-level overview
        - Non-superusers only see data for their assigned organizations

        **Use Cases**:
        - Controlling/Reporting: Export SLO compliance data
        - Dashboard integration: Real-time SLO monitoring
        - Alerting: Identify objects requiring attention


    Args:
        organization (str | Unset):
        workspace (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SloOverviewResponse]
    """

    kwargs = _get_kwargs(
        organization=organization,
        workspace=workspace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    organization: str | Unset = UNSET,
    workspace: str | Unset = UNSET,
) -> SloOverviewResponse | None:
    """Get SLO/SLA overview


        Returns SLO/SLA status data for Endpoints and K8sClusters with optional
        organization and workspace filtering.

        Uses pre-computed ServiceLevelBreach records for breach/at_risk classification
        (created during object reconciliation) and bulk downtime queries for performance.

        **Statistics**:
        - `tracked`: Total number of monitored objects
        - `ok`: Objects with no active breach or warning
        - `at_risk`: Objects with active SLO/SLA warning (error budget running low)
        - `breached`: Objects with active SLO/SLA breach (error budget exhausted)
        - `in_downtime`: Objects currently in active downtime

        **Filtering**:
        - Filter by organization to see org-specific SLO status
        - Filter by workspace for workspace-level overview
        - Non-superusers only see data for their assigned organizations

        **Use Cases**:
        - Controlling/Reporting: Export SLO compliance data
        - Dashboard integration: Real-time SLO monitoring
        - Alerting: Identify objects requiring attention


    Args:
        organization (str | Unset):
        workspace (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SloOverviewResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            organization=organization,
            workspace=workspace,
        )
    ).parsed
