from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalogue_app_detail import CatalogueAppDetail
from ...models.patched_catalogue_app_detail_request import PatchedCatalogueAppDetailRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: PatchedCatalogueAppDetailRequest
    | PatchedCatalogueAppDetailRequest
    | PatchedCatalogueAppDetailRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/catalogue-apps/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedCatalogueAppDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedCatalogueAppDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedCatalogueAppDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CatalogueAppDetail | None:
    if response.status_code == 200:
        response_200 = CatalogueAppDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CatalogueAppDetail]:
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
    body: PatchedCatalogueAppDetailRequest
    | PatchedCatalogueAppDetailRequest
    | PatchedCatalogueAppDetailRequest
    | Unset = UNSET,
) -> Response[CatalogueAppDetail]:
    """API endpoint for CatalogueApps.
    Per .specs/0.12.0/catalogue-app.md

    CatalogueApps are global resources (not workspace-scoped).
    Read access (GET/HEAD/OPTIONS) for all authenticated users.
    Write access (POST/PUT/PATCH/DELETE) only for superusers.

    Optional query parameter ``artifact_version`` (on retrieve):
        When set, the nested ``artifact_package_detail`` serializer exposes
        metadata (version, changelog, readme …) from the Artifact matching
        that version instead of the latest one.

    Args:
        id (UUID):
        body (PatchedCatalogueAppDetailRequest | Unset): Detail serializer for CatalogueApp with
            full data + validation.
            Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md
        body (PatchedCatalogueAppDetailRequest | Unset): Detail serializer for CatalogueApp with
            full data + validation.
            Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md
        body (PatchedCatalogueAppDetailRequest | Unset): Detail serializer for CatalogueApp with
            full data + validation.
            Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogueAppDetail]
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
    body: PatchedCatalogueAppDetailRequest
    | PatchedCatalogueAppDetailRequest
    | PatchedCatalogueAppDetailRequest
    | Unset = UNSET,
) -> CatalogueAppDetail | None:
    """API endpoint for CatalogueApps.
    Per .specs/0.12.0/catalogue-app.md

    CatalogueApps are global resources (not workspace-scoped).
    Read access (GET/HEAD/OPTIONS) for all authenticated users.
    Write access (POST/PUT/PATCH/DELETE) only for superusers.

    Optional query parameter ``artifact_version`` (on retrieve):
        When set, the nested ``artifact_package_detail`` serializer exposes
        metadata (version, changelog, readme …) from the Artifact matching
        that version instead of the latest one.

    Args:
        id (UUID):
        body (PatchedCatalogueAppDetailRequest | Unset): Detail serializer for CatalogueApp with
            full data + validation.
            Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md
        body (PatchedCatalogueAppDetailRequest | Unset): Detail serializer for CatalogueApp with
            full data + validation.
            Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md
        body (PatchedCatalogueAppDetailRequest | Unset): Detail serializer for CatalogueApp with
            full data + validation.
            Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogueAppDetail
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
    body: PatchedCatalogueAppDetailRequest
    | PatchedCatalogueAppDetailRequest
    | PatchedCatalogueAppDetailRequest
    | Unset = UNSET,
) -> Response[CatalogueAppDetail]:
    """API endpoint for CatalogueApps.
    Per .specs/0.12.0/catalogue-app.md

    CatalogueApps are global resources (not workspace-scoped).
    Read access (GET/HEAD/OPTIONS) for all authenticated users.
    Write access (POST/PUT/PATCH/DELETE) only for superusers.

    Optional query parameter ``artifact_version`` (on retrieve):
        When set, the nested ``artifact_package_detail`` serializer exposes
        metadata (version, changelog, readme …) from the Artifact matching
        that version instead of the latest one.

    Args:
        id (UUID):
        body (PatchedCatalogueAppDetailRequest | Unset): Detail serializer for CatalogueApp with
            full data + validation.
            Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md
        body (PatchedCatalogueAppDetailRequest | Unset): Detail serializer for CatalogueApp with
            full data + validation.
            Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md
        body (PatchedCatalogueAppDetailRequest | Unset): Detail serializer for CatalogueApp with
            full data + validation.
            Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogueAppDetail]
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
    body: PatchedCatalogueAppDetailRequest
    | PatchedCatalogueAppDetailRequest
    | PatchedCatalogueAppDetailRequest
    | Unset = UNSET,
) -> CatalogueAppDetail | None:
    """API endpoint for CatalogueApps.
    Per .specs/0.12.0/catalogue-app.md

    CatalogueApps are global resources (not workspace-scoped).
    Read access (GET/HEAD/OPTIONS) for all authenticated users.
    Write access (POST/PUT/PATCH/DELETE) only for superusers.

    Optional query parameter ``artifact_version`` (on retrieve):
        When set, the nested ``artifact_package_detail`` serializer exposes
        metadata (version, changelog, readme …) from the Artifact matching
        that version instead of the latest one.

    Args:
        id (UUID):
        body (PatchedCatalogueAppDetailRequest | Unset): Detail serializer for CatalogueApp with
            full data + validation.
            Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md
        body (PatchedCatalogueAppDetailRequest | Unset): Detail serializer for CatalogueApp with
            full data + validation.
            Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md
        body (PatchedCatalogueAppDetailRequest | Unset): Detail serializer for CatalogueApp with
            full data + validation.
            Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogueAppDetail
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
