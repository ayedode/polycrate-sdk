from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_workspace_template_request import PatchedWorkspaceTemplateRequest
from ...models.workspace_template import WorkspaceTemplate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedWorkspaceTemplateRequest
    | PatchedWorkspaceTemplateRequest
    | PatchedWorkspaceTemplateRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/workspace-templates/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedWorkspaceTemplateRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedWorkspaceTemplateRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedWorkspaceTemplateRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WorkspaceTemplate | None:
    if response.status_code == 200:
        response_200 = WorkspaceTemplate.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WorkspaceTemplate]:
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
    body: PatchedWorkspaceTemplateRequest
    | PatchedWorkspaceTemplateRequest
    | PatchedWorkspaceTemplateRequest
    | Unset = UNSET,
) -> Response[WorkspaceTemplate]:
    """API endpoint for WorkspaceTemplate CRUD operations.

    Provides:
    - List/Create/Retrieve/Update/Delete
    - Template rendering endpoint
    - Organization-scoped filtering
    - Name-based lookup for CLI template selection

    Args:
        id (UUID):
        body (PatchedWorkspaceTemplateRequest | Unset): Full serializer for WorkspaceTemplate -
            includes template content.
        body (PatchedWorkspaceTemplateRequest | Unset): Full serializer for WorkspaceTemplate -
            includes template content.
        body (PatchedWorkspaceTemplateRequest | Unset): Full serializer for WorkspaceTemplate -
            includes template content.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkspaceTemplate]
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
    body: PatchedWorkspaceTemplateRequest
    | PatchedWorkspaceTemplateRequest
    | PatchedWorkspaceTemplateRequest
    | Unset = UNSET,
) -> WorkspaceTemplate | None:
    """API endpoint for WorkspaceTemplate CRUD operations.

    Provides:
    - List/Create/Retrieve/Update/Delete
    - Template rendering endpoint
    - Organization-scoped filtering
    - Name-based lookup for CLI template selection

    Args:
        id (UUID):
        body (PatchedWorkspaceTemplateRequest | Unset): Full serializer for WorkspaceTemplate -
            includes template content.
        body (PatchedWorkspaceTemplateRequest | Unset): Full serializer for WorkspaceTemplate -
            includes template content.
        body (PatchedWorkspaceTemplateRequest | Unset): Full serializer for WorkspaceTemplate -
            includes template content.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkspaceTemplate
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
    body: PatchedWorkspaceTemplateRequest
    | PatchedWorkspaceTemplateRequest
    | PatchedWorkspaceTemplateRequest
    | Unset = UNSET,
) -> Response[WorkspaceTemplate]:
    """API endpoint for WorkspaceTemplate CRUD operations.

    Provides:
    - List/Create/Retrieve/Update/Delete
    - Template rendering endpoint
    - Organization-scoped filtering
    - Name-based lookup for CLI template selection

    Args:
        id (UUID):
        body (PatchedWorkspaceTemplateRequest | Unset): Full serializer for WorkspaceTemplate -
            includes template content.
        body (PatchedWorkspaceTemplateRequest | Unset): Full serializer for WorkspaceTemplate -
            includes template content.
        body (PatchedWorkspaceTemplateRequest | Unset): Full serializer for WorkspaceTemplate -
            includes template content.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkspaceTemplate]
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
    body: PatchedWorkspaceTemplateRequest
    | PatchedWorkspaceTemplateRequest
    | PatchedWorkspaceTemplateRequest
    | Unset = UNSET,
) -> WorkspaceTemplate | None:
    """API endpoint for WorkspaceTemplate CRUD operations.

    Provides:
    - List/Create/Retrieve/Update/Delete
    - Template rendering endpoint
    - Organization-scoped filtering
    - Name-based lookup for CLI template selection

    Args:
        id (UUID):
        body (PatchedWorkspaceTemplateRequest | Unset): Full serializer for WorkspaceTemplate -
            includes template content.
        body (PatchedWorkspaceTemplateRequest | Unset): Full serializer for WorkspaceTemplate -
            includes template content.
        body (PatchedWorkspaceTemplateRequest | Unset): Full serializer for WorkspaceTemplate -
            includes template content.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkspaceTemplate
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
