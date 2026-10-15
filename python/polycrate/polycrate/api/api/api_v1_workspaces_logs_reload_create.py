from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.workspace import Workspace
from ...models.workspace_request import WorkspaceRequest
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: WorkspaceRequest | WorkspaceRequest | WorkspaceRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/workspaces/{id}/logs_reload/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, WorkspaceRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, WorkspaceRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, WorkspaceRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Workspace | None:
    if response.status_code == 200:
        response_200 = Workspace.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Workspace]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: WorkspaceRequest | WorkspaceRequest | WorkspaceRequest | Unset = UNSET,
) -> Response[Workspace]:
    """API endpoint that allows workspaces to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (WorkspaceRequest): Full Workspace serializer for CRUD operations.

            Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
            per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

            Supports template-based creation using template name (slug).
            Template can be org-specific or system-wide (organization=null).
        body (WorkspaceRequest): Full Workspace serializer for CRUD operations.

            Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
            per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

            Supports template-based creation using template name (slug).
            Template can be org-specific or system-wide (organization=null).
        body (WorkspaceRequest): Full Workspace serializer for CRUD operations.

            Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
            per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

            Supports template-based creation using template name (slug).
            Template can be org-specific or system-wide (organization=null).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Workspace]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: WorkspaceRequest | WorkspaceRequest | WorkspaceRequest | Unset = UNSET,
) -> Workspace | None:
    """API endpoint that allows workspaces to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (WorkspaceRequest): Full Workspace serializer for CRUD operations.

            Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
            per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

            Supports template-based creation using template name (slug).
            Template can be org-specific or system-wide (organization=null).
        body (WorkspaceRequest): Full Workspace serializer for CRUD operations.

            Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
            per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

            Supports template-based creation using template name (slug).
            Template can be org-specific or system-wide (organization=null).
        body (WorkspaceRequest): Full Workspace serializer for CRUD operations.

            Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
            per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

            Supports template-based creation using template name (slug).
            Template can be org-specific or system-wide (organization=null).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Workspace
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: WorkspaceRequest | WorkspaceRequest | WorkspaceRequest | Unset = UNSET,
) -> Response[Workspace]:
    """API endpoint that allows workspaces to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (WorkspaceRequest): Full Workspace serializer for CRUD operations.

            Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
            per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

            Supports template-based creation using template name (slug).
            Template can be org-specific or system-wide (organization=null).
        body (WorkspaceRequest): Full Workspace serializer for CRUD operations.

            Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
            per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

            Supports template-based creation using template name (slug).
            Template can be org-specific or system-wide (organization=null).
        body (WorkspaceRequest): Full Workspace serializer for CRUD operations.

            Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
            per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

            Supports template-based creation using template name (slug).
            Template can be org-specific or system-wide (organization=null).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Workspace]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: WorkspaceRequest | WorkspaceRequest | WorkspaceRequest | Unset = UNSET,
) -> Workspace | None:
    """API endpoint that allows workspaces to be viewed or edited.

    Archived filter, user permissions, and query optimizations
    are handled by ManagedObjectBaseViewset.

    Args:
        id (UUID):
        body (WorkspaceRequest): Full Workspace serializer for CRUD operations.

            Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
            per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

            Supports template-based creation using template name (slug).
            Template can be org-specific or system-wide (organization=null).
        body (WorkspaceRequest): Full Workspace serializer for CRUD operations.

            Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
            per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

            Supports template-based creation using template name (slug).
            Template can be org-specific or system-wide (organization=null).
        body (WorkspaceRequest): Full Workspace serializer for CRUD operations.

            Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
            per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

            Supports template-based creation using template name (slug).
            Template can be org-specific or system-wide (organization=null).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Workspace
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
