from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dns_import_records_request_request import DNSImportRecordsRequestRequest
from ...models.dns_import_records_response import DNSImportRecordsResponse
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    *,
    body: DNSImportRecordsRequestRequest
    | DNSImportRecordsRequestRequest
    | DNSImportRecordsRequestRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/domains/dnszones/{id}/import-records/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, DNSImportRecordsRequestRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, DNSImportRecordsRequestRequest):
        _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, DNSImportRecordsRequestRequest):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DNSImportRecordsResponse | None:
    if response.status_code == 200:
        response_200 = DNSImportRecordsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DNSImportRecordsResponse]:
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
    body: DNSImportRecordsRequestRequest
    | DNSImportRecordsRequestRequest
    | DNSImportRecordsRequestRequest
    | Unset = UNSET,
) -> Response[DNSImportRecordsResponse]:
    """Import DNS records from BIND zone file

     Bulk-import DNS records from a BIND zone file (internal zones only). Each record is attempted
    independently — partial success is possible. System record types (SOA, NSEC, NSEC3, RRSIG, DNSKEY)
    are skipped. Spec 492: DNS Zone Fixes.

    Args:
        id (UUID):
        body (DNSImportRecordsRequestRequest):
        body (DNSImportRecordsRequestRequest):
        body (DNSImportRecordsRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSImportRecordsResponse]
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
    body: DNSImportRecordsRequestRequest
    | DNSImportRecordsRequestRequest
    | DNSImportRecordsRequestRequest
    | Unset = UNSET,
) -> DNSImportRecordsResponse | None:
    """Import DNS records from BIND zone file

     Bulk-import DNS records from a BIND zone file (internal zones only). Each record is attempted
    independently — partial success is possible. System record types (SOA, NSEC, NSEC3, RRSIG, DNSKEY)
    are skipped. Spec 492: DNS Zone Fixes.

    Args:
        id (UUID):
        body (DNSImportRecordsRequestRequest):
        body (DNSImportRecordsRequestRequest):
        body (DNSImportRecordsRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSImportRecordsResponse
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
    body: DNSImportRecordsRequestRequest
    | DNSImportRecordsRequestRequest
    | DNSImportRecordsRequestRequest
    | Unset = UNSET,
) -> Response[DNSImportRecordsResponse]:
    """Import DNS records from BIND zone file

     Bulk-import DNS records from a BIND zone file (internal zones only). Each record is attempted
    independently — partial success is possible. System record types (SOA, NSEC, NSEC3, RRSIG, DNSKEY)
    are skipped. Spec 492: DNS Zone Fixes.

    Args:
        id (UUID):
        body (DNSImportRecordsRequestRequest):
        body (DNSImportRecordsRequestRequest):
        body (DNSImportRecordsRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DNSImportRecordsResponse]
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
    body: DNSImportRecordsRequestRequest
    | DNSImportRecordsRequestRequest
    | DNSImportRecordsRequestRequest
    | Unset = UNSET,
) -> DNSImportRecordsResponse | None:
    """Import DNS records from BIND zone file

     Bulk-import DNS records from a BIND zone file (internal zones only). Each record is attempted
    independently — partial success is possible. System record types (SOA, NSEC, NSEC3, RRSIG, DNSKEY)
    are skipped. Spec 492: DNS Zone Fixes.

    Args:
        id (UUID):
        body (DNSImportRecordsRequestRequest):
        body (DNSImportRecordsRequestRequest):
        body (DNSImportRecordsRequestRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DNSImportRecordsResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
