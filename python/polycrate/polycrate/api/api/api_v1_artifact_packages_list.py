from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_artifact_package_list_list import PaginatedArtifactPackageListList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    artifact_repository: UUID | Unset = UNSET,
    artifact_repository_name: str | Unset = UNSET,
    kind: str | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_artifact_repository: str | Unset = UNSET
    if not isinstance(artifact_repository, Unset):
        json_artifact_repository = str(artifact_repository)
    params["artifact_repository"] = json_artifact_repository

    params["artifact_repository_name"] = artifact_repository_name

    params["kind"] = kind

    params["name"] = name

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/artifact-packages/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedArtifactPackageListList | None:
    if response.status_code == 200:
        response_200 = PaginatedArtifactPackageListList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedArtifactPackageListList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    artifact_repository: UUID | Unset = UNSET,
    artifact_repository_name: str | Unset = UNSET,
    kind: str | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedArtifactPackageListList]:
    """API endpoint for ArtifactPackages.

    ArtifactPackages are global resources (not workspace-scoped).

    Optional query parameter ``artifact_version`` or ``artifact_id`` (on
    retrieve): Exposes metadata from that specific Artifact instead of the
    latest one.  Per .specs/0.12.0/catalogue-app.md

    Args:
        artifact_repository (UUID | Unset):
        artifact_repository_name (str | Unset):
        kind (str | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedArtifactPackageListList]
    """

    kwargs = _get_kwargs(
        artifact_repository=artifact_repository,
        artifact_repository_name=artifact_repository_name,
        kind=kind,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    artifact_repository: UUID | Unset = UNSET,
    artifact_repository_name: str | Unset = UNSET,
    kind: str | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedArtifactPackageListList | None:
    """API endpoint for ArtifactPackages.

    ArtifactPackages are global resources (not workspace-scoped).

    Optional query parameter ``artifact_version`` or ``artifact_id`` (on
    retrieve): Exposes metadata from that specific Artifact instead of the
    latest one.  Per .specs/0.12.0/catalogue-app.md

    Args:
        artifact_repository (UUID | Unset):
        artifact_repository_name (str | Unset):
        kind (str | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedArtifactPackageListList
    """

    return sync_detailed(
        client=client,
        artifact_repository=artifact_repository,
        artifact_repository_name=artifact_repository_name,
        kind=kind,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    artifact_repository: UUID | Unset = UNSET,
    artifact_repository_name: str | Unset = UNSET,
    kind: str | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[PaginatedArtifactPackageListList]:
    """API endpoint for ArtifactPackages.

    ArtifactPackages are global resources (not workspace-scoped).

    Optional query parameter ``artifact_version`` or ``artifact_id`` (on
    retrieve): Exposes metadata from that specific Artifact instead of the
    latest one.  Per .specs/0.12.0/catalogue-app.md

    Args:
        artifact_repository (UUID | Unset):
        artifact_repository_name (str | Unset):
        kind (str | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedArtifactPackageListList]
    """

    kwargs = _get_kwargs(
        artifact_repository=artifact_repository,
        artifact_repository_name=artifact_repository_name,
        kind=kind,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    artifact_repository: UUID | Unset = UNSET,
    artifact_repository_name: str | Unset = UNSET,
    kind: str | Unset = UNSET,
    name: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    search: str | Unset = UNSET,
) -> PaginatedArtifactPackageListList | None:
    """API endpoint for ArtifactPackages.

    ArtifactPackages are global resources (not workspace-scoped).

    Optional query parameter ``artifact_version`` or ``artifact_id`` (on
    retrieve): Exposes metadata from that specific Artifact instead of the
    latest one.  Per .specs/0.12.0/catalogue-app.md

    Args:
        artifact_repository (UUID | Unset):
        artifact_repository_name (str | Unset):
        kind (str | Unset):
        name (str | Unset):
        ordering (str | Unset):
        page (int | Unset):
        page_size (int | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedArtifactPackageListList
    """

    return (
        await asyncio_detailed(
            client=client,
            artifact_repository=artifact_repository,
            artifact_repository_name=artifact_repository_name,
            kind=kind,
            name=name,
            ordering=ordering,
            page=page,
            page_size=page_size,
            search=search,
        )
    ).parsed
