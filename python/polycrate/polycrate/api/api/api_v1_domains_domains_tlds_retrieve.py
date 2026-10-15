from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_public_detail import DomainPublicDetail
from ...types import Response


def _get_kwargs(
    tld: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/domains/domains/tlds/{tld}/".format(
            tld=quote(str(tld), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DomainPublicDetail | None:
    if response.status_code == 200:
        response_200 = DomainPublicDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DomainPublicDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tld: str,
    *,
    client: AuthenticatedClient,
) -> Response[DomainPublicDetail]:
    """TLD domicile price fallback. Spec: polycrate spec inspect 891

    Args:
        tld (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainPublicDetail]
    """

    kwargs = _get_kwargs(
        tld=tld,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tld: str,
    *,
    client: AuthenticatedClient,
) -> DomainPublicDetail | None:
    """TLD domicile price fallback. Spec: polycrate spec inspect 891

    Args:
        tld (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainPublicDetail
    """

    return sync_detailed(
        tld=tld,
        client=client,
    ).parsed


async def asyncio_detailed(
    tld: str,
    *,
    client: AuthenticatedClient,
) -> Response[DomainPublicDetail]:
    """TLD domicile price fallback. Spec: polycrate spec inspect 891

    Args:
        tld (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainPublicDetail]
    """

    kwargs = _get_kwargs(
        tld=tld,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tld: str,
    *,
    client: AuthenticatedClient,
) -> DomainPublicDetail | None:
    """TLD domicile price fallback. Spec: polycrate spec inspect 891

    Args:
        tld (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainPublicDetail
    """

    return (
        await asyncio_detailed(
            tld=tld,
            client=client,
        )
    ).parsed
