from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_condition_instances_list_condition_severity import (
    ApiV1ConditionInstancesListConditionSeverity,
)
from ...models.paginated_condition_instance_list_list import PaginatedConditionInstanceListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: bool | Unset = UNSET,
    condition: UUID | Unset = UNSET,
    condition_severity: ApiV1ConditionInstancesListConditionSeverity | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    workspace: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["active"] = active

    json_condition: str | Unset = UNSET
    if not isinstance(condition, Unset):
        json_condition = str(condition)
    params["condition"] = json_condition

    json_condition_severity: str | Unset = UNSET
    if not isinstance(condition_severity, Unset):
        json_condition_severity = condition_severity

    params["condition__severity"] = json_condition_severity

    params["ordering"] = ordering

    json_organization: str | Unset = UNSET
    if not isinstance(organization, Unset):
        json_organization = str(organization)
    params["organization"] = json_organization

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    json_workspace: str | Unset = UNSET
    if not isinstance(workspace, Unset):
        json_workspace = str(workspace)
    params["workspace"] = json_workspace

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/condition-instances/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedConditionInstanceListList | None:
    if response.status_code == 200:
        response_200 = PaginatedConditionInstanceListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedConditionInstanceListList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    condition: UUID | Unset = UNSET,
    condition_severity: ApiV1ConditionInstancesListConditionSeverity | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    workspace: UUID | Unset = UNSET,
) -> Response[PaginatedConditionInstanceListList]:
    """Read API for ConditionInstance objects.
    Instances are managed exclusively by the system (add/remove_condition).
    Spec: polycrate spec inspect 419
    Spec: polycrate spec inspect 587

    Args:
        active (bool | Unset):
        condition (UUID | Unset):
        condition_severity (ApiV1ConditionInstancesListConditionSeverity | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        workspace (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConditionInstanceListList]
    """

    kwargs = _get_kwargs(
        active=active,
        condition=condition,
        condition_severity=condition_severity,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        search=search,
        workspace=workspace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    condition: UUID | Unset = UNSET,
    condition_severity: ApiV1ConditionInstancesListConditionSeverity | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    workspace: UUID | Unset = UNSET,
) -> PaginatedConditionInstanceListList | None:
    """Read API for ConditionInstance objects.
    Instances are managed exclusively by the system (add/remove_condition).
    Spec: polycrate spec inspect 419
    Spec: polycrate spec inspect 587

    Args:
        active (bool | Unset):
        condition (UUID | Unset):
        condition_severity (ApiV1ConditionInstancesListConditionSeverity | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        workspace (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConditionInstanceListList
    """

    return sync_detailed(
        client=client,
        active=active,
        condition=condition,
        condition_severity=condition_severity,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        search=search,
        workspace=workspace,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    condition: UUID | Unset = UNSET,
    condition_severity: ApiV1ConditionInstancesListConditionSeverity | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    workspace: UUID | Unset = UNSET,
) -> Response[PaginatedConditionInstanceListList]:
    """Read API for ConditionInstance objects.
    Instances are managed exclusively by the system (add/remove_condition).
    Spec: polycrate spec inspect 419
    Spec: polycrate spec inspect 587

    Args:
        active (bool | Unset):
        condition (UUID | Unset):
        condition_severity (ApiV1ConditionInstancesListConditionSeverity | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        workspace (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConditionInstanceListList]
    """

    kwargs = _get_kwargs(
        active=active,
        condition=condition,
        condition_severity=condition_severity,
        ordering=ordering,
        organization=organization,
        page=page,
        page_size=page_size,
        search=search,
        workspace=workspace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    active: bool | Unset = UNSET,
    condition: UUID | Unset = UNSET,
    condition_severity: ApiV1ConditionInstancesListConditionSeverity | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    workspace: UUID | Unset = UNSET,
) -> PaginatedConditionInstanceListList | None:
    """Read API for ConditionInstance objects.
    Instances are managed exclusively by the system (add/remove_condition).
    Spec: polycrate spec inspect 419
    Spec: polycrate spec inspect 587

    Args:
        active (bool | Unset):
        condition (UUID | Unset):
        condition_severity (ApiV1ConditionInstancesListConditionSeverity | Unset):
        ordering (str | Unset):
        organization (UUID | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        workspace (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConditionInstanceListList
    """

    return (
        await asyncio_detailed(
            client=client,
            active=active,
            condition=condition,
            condition_severity=condition_severity,
            ordering=ordering,
            organization=organization,
            page=page,
            page_size=page_size,
            search=search,
            workspace=workspace,
        )
    ).parsed
