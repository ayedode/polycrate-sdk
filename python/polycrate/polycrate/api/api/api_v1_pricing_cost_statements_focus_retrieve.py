from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_v1_pricing_cost_statements_focus_retrieve_format import (
    ApiV1PricingCostStatementsFocusRetrieveFormat,
)
from ...models.cost_statement_detail import CostStatementDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    format_: ApiV1PricingCostStatementsFocusRetrieveFormat | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/pricing/cost-statements/{id}/focus/".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CostStatementDetail | None:
    if response.status_code == 200:
        response_200 = CostStatementDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CostStatementDetail]:
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
    format_: ApiV1PricingCostStatementsFocusRetrieveFormat | Unset = UNSET,
) -> Response[CostStatementDetail]:
    """FOCUS 1.2 projection of this CostStatement. Query ?format=json|csv.
    Spec: polycrate spec inspect 860

    Args:
        id (UUID):
        format_ (ApiV1PricingCostStatementsFocusRetrieveFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostStatementDetail]
    """

    kwargs = _get_kwargs(
        id=id,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    format_: ApiV1PricingCostStatementsFocusRetrieveFormat | Unset = UNSET,
) -> CostStatementDetail | None:
    """FOCUS 1.2 projection of this CostStatement. Query ?format=json|csv.
    Spec: polycrate spec inspect 860

    Args:
        id (UUID):
        format_ (ApiV1PricingCostStatementsFocusRetrieveFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostStatementDetail
    """

    return sync_detailed(
        id=id,
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    format_: ApiV1PricingCostStatementsFocusRetrieveFormat | Unset = UNSET,
) -> Response[CostStatementDetail]:
    """FOCUS 1.2 projection of this CostStatement. Query ?format=json|csv.
    Spec: polycrate spec inspect 860

    Args:
        id (UUID):
        format_ (ApiV1PricingCostStatementsFocusRetrieveFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostStatementDetail]
    """

    kwargs = _get_kwargs(
        id=id,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    format_: ApiV1PricingCostStatementsFocusRetrieveFormat | Unset = UNSET,
) -> CostStatementDetail | None:
    """FOCUS 1.2 projection of this CostStatement. Query ?format=json|csv.
    Spec: polycrate spec inspect 860

    Args:
        id (UUID):
        format_ (ApiV1PricingCostStatementsFocusRetrieveFormat | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostStatementDetail
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            format_=format_,
        )
    ).parsed
