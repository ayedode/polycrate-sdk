from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_users_memberships_partial_update_validation_error import (
    ApiV1UsersMembershipsPartialUpdateValidationError,
)
from ...models.error_response_401 import ErrorResponse401
from ...models.error_response_403 import ErrorResponse403
from ...models.error_response_405 import ErrorResponse405
from ...models.error_response_406 import ErrorResponse406
from ...models.error_response_409 import ErrorResponse409
from ...models.error_response_410 import ErrorResponse410
from ...models.error_response_415 import ErrorResponse415
from ...models.error_response_500 import ErrorResponse500
from ...models.membership_role_update import MembershipRoleUpdate
from ...models.parse_error_response import ParseErrorResponse
from ...models.patched_membership_role_update_request import PatchedMembershipRoleUpdateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: PatchedMembershipRoleUpdateRequest
    | PatchedMembershipRoleUpdateRequest
    | PatchedMembershipRoleUpdateRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/users/{id}/memberships/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PatchedMembershipRoleUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedMembershipRoleUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedMembershipRoleUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ApiV1UsersMembershipsPartialUpdateValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | MembershipRoleUpdate
    | None
):
    if response.status_code == 200:
        response_200 = MembershipRoleUpdate.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(data: object) -> ApiV1UsersMembershipsPartialUpdateValidationError | ParseErrorResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_users_memberships_partial_update_error_response_400_type_0 = (
                    ApiV1UsersMembershipsPartialUpdateValidationError.from_dict(data)
                )

                return componentsschemas_api_v1_users_memberships_partial_update_error_response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_api_v1_users_memberships_partial_update_error_response_400_type_1 = (
                ParseErrorResponse.from_dict(data)
            )

            return componentsschemas_api_v1_users_memberships_partial_update_error_response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
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
        response_502 = cast(Any, None)
        return response_502

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ApiV1UsersMembershipsPartialUpdateValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | MembershipRoleUpdate
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMembershipRoleUpdateRequest
    | PatchedMembershipRoleUpdateRequest
    | PatchedMembershipRoleUpdateRequest
    | Unset = UNSET,
) -> Response[
    Any
    | ApiV1UsersMembershipsPartialUpdateValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | MembershipRoleUpdate
]:
    """Update membership role

     Update OrganizationMembership.role and sync Keycloak Organization Group membership (leave previous
    role group, join new). Spec 525.

    Args:
        id (int):
        body (PatchedMembershipRoleUpdateRequest | Unset): Update org-scoped membership role. Spec
            525
        body (PatchedMembershipRoleUpdateRequest | Unset): Update org-scoped membership role. Spec
            525
        body (PatchedMembershipRoleUpdateRequest | Unset): Update org-scoped membership role. Spec
            525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1UsersMembershipsPartialUpdateValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | MembershipRoleUpdate]
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
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMembershipRoleUpdateRequest
    | PatchedMembershipRoleUpdateRequest
    | PatchedMembershipRoleUpdateRequest
    | Unset = UNSET,
) -> (
    Any
    | ApiV1UsersMembershipsPartialUpdateValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | MembershipRoleUpdate
    | None
):
    """Update membership role

     Update OrganizationMembership.role and sync Keycloak Organization Group membership (leave previous
    role group, join new). Spec 525.

    Args:
        id (int):
        body (PatchedMembershipRoleUpdateRequest | Unset): Update org-scoped membership role. Spec
            525
        body (PatchedMembershipRoleUpdateRequest | Unset): Update org-scoped membership role. Spec
            525
        body (PatchedMembershipRoleUpdateRequest | Unset): Update org-scoped membership role. Spec
            525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1UsersMembershipsPartialUpdateValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | MembershipRoleUpdate
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMembershipRoleUpdateRequest
    | PatchedMembershipRoleUpdateRequest
    | PatchedMembershipRoleUpdateRequest
    | Unset = UNSET,
) -> Response[
    Any
    | ApiV1UsersMembershipsPartialUpdateValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | MembershipRoleUpdate
]:
    """Update membership role

     Update OrganizationMembership.role and sync Keycloak Organization Group membership (leave previous
    role group, join new). Spec 525.

    Args:
        id (int):
        body (PatchedMembershipRoleUpdateRequest | Unset): Update org-scoped membership role. Spec
            525
        body (PatchedMembershipRoleUpdateRequest | Unset): Update org-scoped membership role. Spec
            525
        body (PatchedMembershipRoleUpdateRequest | Unset): Update org-scoped membership role. Spec
            525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiV1UsersMembershipsPartialUpdateValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | MembershipRoleUpdate]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedMembershipRoleUpdateRequest
    | PatchedMembershipRoleUpdateRequest
    | PatchedMembershipRoleUpdateRequest
    | Unset = UNSET,
) -> (
    Any
    | ApiV1UsersMembershipsPartialUpdateValidationError
    | ParseErrorResponse
    | ErrorResponse401
    | ErrorResponse403
    | ErrorResponse405
    | ErrorResponse406
    | ErrorResponse409
    | ErrorResponse410
    | ErrorResponse415
    | ErrorResponse500
    | MembershipRoleUpdate
    | None
):
    """Update membership role

     Update OrganizationMembership.role and sync Keycloak Organization Group membership (leave previous
    role group, join new). Spec 525.

    Args:
        id (int):
        body (PatchedMembershipRoleUpdateRequest | Unset): Update org-scoped membership role. Spec
            525
        body (PatchedMembershipRoleUpdateRequest | Unset): Update org-scoped membership role. Spec
            525
        body (PatchedMembershipRoleUpdateRequest | Unset): Update org-scoped membership role. Spec
            525

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiV1UsersMembershipsPartialUpdateValidationError | ParseErrorResponse | ErrorResponse401 | ErrorResponse403 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | MembershipRoleUpdate
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
