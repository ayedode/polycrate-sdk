from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dns_record_detail import DNSRecordDetail
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


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DNSRecordDetail | None:
    if response.status_code == 200:
        response_200 = DNSRecordDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DNSRecordDetail]:
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
) -> Response[DNSRecordDetail]:
    """CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind="internal"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind="external"`: records live only at the provider; the API passes
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
        Response[DNSRecordDetail]
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
) -> DNSRecordDetail | None:
    """CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind="internal"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind="external"`: records live only at the provider; the API passes
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
        DNSRecordDetail
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DNSRecordDetail]:
    """CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind="internal"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind="external"`: records live only at the provider; the API passes
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
        Response[DNSRecordDetail]
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
) -> DNSRecordDetail | None:
    """CRUD endpoint for DNS Records.

    Supports both internal (PowerDNS-backed, DB-persisted) and external
    (Lexicon-backed, provider-only) zones. The dispatch is driven by the
    zone's `kind` attribute:

    - `kind="internal"`: records are DB rows and mutations are synchronised
      to PowerDNS within a transaction.
    - `kind="external"`: records live only at the provider; the API passes
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
        DNSRecordDetail
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
