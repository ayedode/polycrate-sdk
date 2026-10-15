from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_public_detail import DomainPublicDetail
from ...models.domain_public_detail_request import DomainPublicDetailRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DomainPublicDetailRequest | DomainPublicDetailRequest | DomainPublicDetailRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/domains/domains/transfer/bulk/",
    }

    if isinstance(body, DomainPublicDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, DomainPublicDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, DomainPublicDetailRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient,
    body: DomainPublicDetailRequest | DomainPublicDetailRequest | DomainPublicDetailRequest | Unset = UNSET,
) -> Response[DomainPublicDetail]:
    """Start multiple transfer-ins. Partial success allowed.

    Spec: polycrate spec inspect 886

    Args:
        body (DomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (DomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (DomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainPublicDetail]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: DomainPublicDetailRequest | DomainPublicDetailRequest | DomainPublicDetailRequest | Unset = UNSET,
) -> DomainPublicDetail | None:
    """Start multiple transfer-ins. Partial success allowed.

    Spec: polycrate spec inspect 886

    Args:
        body (DomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (DomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (DomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainPublicDetail
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DomainPublicDetailRequest | DomainPublicDetailRequest | DomainPublicDetailRequest | Unset = UNSET,
) -> Response[DomainPublicDetail]:
    """Start multiple transfer-ins. Partial success allowed.

    Spec: polycrate spec inspect 886

    Args:
        body (DomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (DomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (DomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainPublicDetail]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DomainPublicDetailRequest | DomainPublicDetailRequest | DomainPublicDetailRequest | Unset = UNSET,
) -> DomainPublicDetail | None:
    """Start multiple transfer-ins. Partial success allowed.

    Spec: polycrate spec inspect 886

    Args:
        body (DomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (DomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.
        body (DomainPublicDetailRequest | Unset): Customer/non-staff detail. Omits internal
            renewal cost. Spec 888.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainPublicDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
