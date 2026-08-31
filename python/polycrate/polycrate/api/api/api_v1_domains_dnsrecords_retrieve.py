from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dns_record_detail import DNSRecordDetail
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
from ...models.parse_error_response import ParseErrorResponse
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/domains/dnsrecords/{id}/".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DNSRecordDetail
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
    | ParseErrorResponse
    | None
):
    if response.status_code == 200:
        response_200 = DNSRecordDetail.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ParseErrorResponse.from_dict(response.json())

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
    DNSRecordDetail
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
    | ParseErrorResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    DNSRecordDetail
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
    | ParseErrorResponse
]:
    r"""CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind=\"internal\"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind=\"external\"`: records live only at the provider; the API passes
      operations straight through to python-lexicon.

    For external zones, `?dns_zone=<uuid>` is REQUIRED on list, and
    provider-assigned record IDs are used as the detail PK.

    Spec: polycrate spec inspect 137
    Spec 492: Composite ID fix for external records.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSRecordDetail | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | ParseErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> (
    DNSRecordDetail
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
    | ParseErrorResponse
    | None
):
    r"""CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind=\"internal\"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind=\"external\"`: records live only at the provider; the API passes
      operations straight through to python-lexicon.

    For external zones, `?dns_zone=<uuid>` is REQUIRED on list, and
    provider-assigned record IDs are used as the detail PK.

    Spec: polycrate spec inspect 137
    Spec 492: Composite ID fix for external records.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSRecordDetail | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | ParseErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    DNSRecordDetail
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
    | ParseErrorResponse
]:
    r"""CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind=\"internal\"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind=\"external\"`: records live only at the provider; the API passes
      operations straight through to python-lexicon.

    For external zones, `?dns_zone=<uuid>` is REQUIRED on list, and
    provider-assigned record IDs are used as the detail PK.

    Spec: polycrate spec inspect 137
    Spec 492: Composite ID fix for external records.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSRecordDetail | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | ParseErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> (
    DNSRecordDetail
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
    | ParseErrorResponse
    | None
):
    r"""CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind=\"internal\"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind=\"external\"`: records live only at the provider; the API passes
      operations straight through to python-lexicon.

    For external zones, `?dns_zone=<uuid>` is REQUIRED on list, and
    provider-assigned record IDs are used as the detail PK.

    Spec: polycrate spec inspect 137
    Spec 492: Composite ID fix for external records.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSRecordDetail | ErrorResponse401 | ErrorResponse403 | ErrorResponse404 | ErrorResponse405 | ErrorResponse406 | ErrorResponse409 | ErrorResponse410 | ErrorResponse415 | ErrorResponse500 | ErrorResponse502 | ParseErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
