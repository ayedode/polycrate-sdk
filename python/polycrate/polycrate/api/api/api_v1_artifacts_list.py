from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_artifacts_list_kind import ApiV1ArtifactsListKind
from ...models.paginated_artifact_list_list import PaginatedArtifactListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    app_version: str | Unset = UNSET,
    artifact_package: UUID | Unset = UNSET,
    artifact_package_name: str | Unset = UNSET,
    content_url: str | Unset = UNSET,
    deprecated: bool | Unset = UNSET,
    kind: ApiV1ArtifactsListKind | Unset = UNSET,
    mirrored: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["app_version"] = app_version

    json_artifact_package: str | Unset = UNSET
    if not isinstance(artifact_package, Unset):
        json_artifact_package = str(artifact_package)
    params["artifact_package"] = json_artifact_package

    params["artifact_package_name"] = artifact_package_name

    params["content_url"] = content_url

    params["deprecated"] = deprecated

    json_kind: str | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind

    params["kind"] = json_kind

    params["mirrored"] = mirrored

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/artifacts/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedArtifactListList | None:
    if response.status_code == 200:
        response_200 = PaginatedArtifactListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedArtifactListList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    app_version: str | Unset = UNSET,
    artifact_package: UUID | Unset = UNSET,
    artifact_package_name: str | Unset = UNSET,
    content_url: str | Unset = UNSET,
    deprecated: bool | Unset = UNSET,
    kind: ApiV1ArtifactsListKind | Unset = UNSET,
    mirrored: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[PaginatedArtifactListList]:
    """API endpoint for Artifacts (CLI binaries, Docker images, etc.).

    Artifacts are global resources (not workspace-scoped) used by the CLI
    for version checks and downloads.

    Supports Agent Token authentication (READ-ONLY for agents).
    Agent Permissions: Read ✅, Write ❌, Create ❌, Delete ❌

    See: .specs/agent-token-extended-api-access.md

    Args:
        app_version (str | Unset):
        artifact_package (UUID | Unset):
        artifact_package_name (str | Unset):
        content_url (str | Unset):
        deprecated (bool | Unset):
        kind (ApiV1ArtifactsListKind | Unset):
        mirrored (bool | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedArtifactListList]
    """

    kwargs = _get_kwargs(
        app_version=app_version,
        artifact_package=artifact_package,
        artifact_package_name=artifact_package_name,
        content_url=content_url,
        deprecated=deprecated,
        kind=kind,
        mirrored=mirrored,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    app_version: str | Unset = UNSET,
    artifact_package: UUID | Unset = UNSET,
    artifact_package_name: str | Unset = UNSET,
    content_url: str | Unset = UNSET,
    deprecated: bool | Unset = UNSET,
    kind: ApiV1ArtifactsListKind | Unset = UNSET,
    mirrored: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> PaginatedArtifactListList | None:
    """API endpoint for Artifacts (CLI binaries, Docker images, etc.).

    Artifacts are global resources (not workspace-scoped) used by the CLI
    for version checks and downloads.

    Supports Agent Token authentication (READ-ONLY for agents).
    Agent Permissions: Read ✅, Write ❌, Create ❌, Delete ❌

    See: .specs/agent-token-extended-api-access.md

    Args:
        app_version (str | Unset):
        artifact_package (UUID | Unset):
        artifact_package_name (str | Unset):
        content_url (str | Unset):
        deprecated (bool | Unset):
        kind (ApiV1ArtifactsListKind | Unset):
        mirrored (bool | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedArtifactListList
    """

    return sync_detailed(
        client=client,
        app_version=app_version,
        artifact_package=artifact_package,
        artifact_package_name=artifact_package_name,
        content_url=content_url,
        deprecated=deprecated,
        kind=kind,
        mirrored=mirrored,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    app_version: str | Unset = UNSET,
    artifact_package: UUID | Unset = UNSET,
    artifact_package_name: str | Unset = UNSET,
    content_url: str | Unset = UNSET,
    deprecated: bool | Unset = UNSET,
    kind: ApiV1ArtifactsListKind | Unset = UNSET,
    mirrored: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> Response[PaginatedArtifactListList]:
    """API endpoint for Artifacts (CLI binaries, Docker images, etc.).

    Artifacts are global resources (not workspace-scoped) used by the CLI
    for version checks and downloads.

    Supports Agent Token authentication (READ-ONLY for agents).
    Agent Permissions: Read ✅, Write ❌, Create ❌, Delete ❌

    See: .specs/agent-token-extended-api-access.md

    Args:
        app_version (str | Unset):
        artifact_package (UUID | Unset):
        artifact_package_name (str | Unset):
        content_url (str | Unset):
        deprecated (bool | Unset):
        kind (ApiV1ArtifactsListKind | Unset):
        mirrored (bool | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedArtifactListList]
    """

    kwargs = _get_kwargs(
        app_version=app_version,
        artifact_package=artifact_package,
        artifact_package_name=artifact_package_name,
        content_url=content_url,
        deprecated=deprecated,
        kind=kind,
        mirrored=mirrored,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    app_version: str | Unset = UNSET,
    artifact_package: UUID | Unset = UNSET,
    artifact_package_name: str | Unset = UNSET,
    content_url: str | Unset = UNSET,
    deprecated: bool | Unset = UNSET,
    kind: ApiV1ArtifactsListKind | Unset = UNSET,
    mirrored: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
    version: str | Unset = UNSET,
) -> PaginatedArtifactListList | None:
    """API endpoint for Artifacts (CLI binaries, Docker images, etc.).

    Artifacts are global resources (not workspace-scoped) used by the CLI
    for version checks and downloads.

    Supports Agent Token authentication (READ-ONLY for agents).
    Agent Permissions: Read ✅, Write ❌, Create ❌, Delete ❌

    See: .specs/agent-token-extended-api-access.md

    Args:
        app_version (str | Unset):
        artifact_package (UUID | Unset):
        artifact_package_name (str | Unset):
        content_url (str | Unset):
        deprecated (bool | Unset):
        kind (ApiV1ArtifactsListKind | Unset):
        mirrored (bool | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):
        version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedArtifactListList
    """

    return (
        await asyncio_detailed(
            client=client,
            app_version=app_version,
            artifact_package=artifact_package,
            artifact_package_name=artifact_package_name,
            content_url=content_url,
            deprecated=deprecated,
            kind=kind,
            mirrored=mirrored,
            ordering=ordering,
            page=page,
            page_size=page_size,
            search=search,
            version=version,
        )
    ).parsed
