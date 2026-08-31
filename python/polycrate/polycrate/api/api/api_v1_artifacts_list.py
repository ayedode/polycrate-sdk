from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_artifacts_list_kind import ApiV1ArtifactsListKind
from ...models.api_v1_artifacts_list_validation_error import ApiV1ArtifactsListValidationError
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
from ...models.paginated_artifact_list_list import PaginatedArtifactListList
from ...models.parse_error_response import ParseErrorResponse
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
) -> (
    ApiV1ArtifactsListValidationError
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
    | PaginatedArtifactListList
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedArtifactListList.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1ArtifactsListValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifacts_list_error_response_400_type_0 = (
                    ApiV1ArtifactsListValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_artifacts_list_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_artifacts_list_error_response_400_type_1 = ParseErrorResponse.from_dict(data)

            return componentsschemas_api_v1_artifacts_list_error_response_400_type_1

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
    ApiV1ArtifactsListValidationError
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
    | PaginatedArtifactListList
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
) -> Response[
    ApiV1ArtifactsListValidationError
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
    | PaginatedArtifactListList
]:
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
        Response[ApiV1ArtifactsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedArtifactListList]
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
) -> (
    ApiV1ArtifactsListValidationError
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
    | PaginatedArtifactListList
    | None
):
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
        ApiV1ArtifactsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedArtifactListList
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
) -> Response[
    ApiV1ArtifactsListValidationError
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
    | PaginatedArtifactListList
]:
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
        Response[ApiV1ArtifactsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedArtifactListList]
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
) -> (
    ApiV1ArtifactsListValidationError
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
    | PaginatedArtifactListList
    | None
):
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
        ApiV1ArtifactsListValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | PaginatedArtifactListList
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
