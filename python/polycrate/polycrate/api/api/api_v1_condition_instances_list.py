from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_condition_instances_list_condition_severity import (
    ApiV1ConditionInstancesListConditionSeverity,
)
from ...models.api_v1_condition_instances_list_validation_error import ApiV1ConditionInstancesListValidationError
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_403 import ErrorResponse403
from ...models.error_response_404 import ErrorResponse404
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_409 import ErrorResponse409
from ...models.error_response_410 import ErrorResponse410
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.error_response_502 import ErrorResponse502
from ...models.paginated_condition_instance_list_list import PaginatedConditionInstanceListList
from ...models.parse_error_response import ParseErrorResponse
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
) -> (
    ApiV1ConditionInstancesListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedConditionInstanceListList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedConditionInstanceListList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1ConditionInstancesListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_condition_instances_list_error_response_400_type_0 = (
                    ApiV1ConditionInstancesListValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_condition_instances_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_condition_instances_list_error_response_400_type_1 = ParseErrorResponse.from_dict(
                data
            )

            return componentsschemas_api_v1_condition_instances_list_error_response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse404.from_dict(response.json())

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
    ApiV1ConditionInstancesListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedConditionInstanceListList
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
    active: bool | Unset = UNSET,
    condition: UUID | Unset = UNSET,
    condition_severity: ApiV1ConditionInstancesListConditionSeverity | Unset = UNSET,
    ordering: str | Unset = UNSET,
    organization: UUID | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    workspace: UUID | Unset = UNSET,
) -> Response[
    ApiV1ConditionInstancesListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedConditionInstanceListList
]:
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
        Response[ApiV1ConditionInstancesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedConditionInstanceListList]
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
) -> (
    ApiV1ConditionInstancesListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedConditionInstanceListList
    | None
):
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
        ApiV1ConditionInstancesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedConditionInstanceListList
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
) -> Response[
    ApiV1ConditionInstancesListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedConditionInstanceListList
]:
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
        Response[ApiV1ConditionInstancesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedConditionInstanceListList]
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
) -> (
    ApiV1ConditionInstancesListValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse404
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | ErrorResponse502
    | PaginatedConditionInstanceListList
    | None
):
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
        ApiV1ConditionInstancesListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedConditionInstanceListList
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
