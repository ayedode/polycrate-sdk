from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.k8s_app import K8SApp
from ...models.k8s_app_request import K8SAppRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: K8SAppRequest | K8SAppRequest | K8SAppRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/kubernetes/apps/{id}/install/".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, K8SAppRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, K8SAppRequest):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, K8SAppRequest):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> K8SApp | None:
    if response.status_code == 200:
        response_200 = K8SApp.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[K8SApp]:
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
    body: K8SAppRequest | K8SAppRequest | K8SAppRequest | Unset = UNSET,
) -> Response[K8SApp]:
    """Install the K8s App via its associated block

    Args:
        id (UUID):
        body (K8SAppRequest | Unset): Full serializer for K8sApp detail view.
        body (K8SAppRequest | Unset): Full serializer for K8sApp detail view.
        body (K8SAppRequest | Unset): Full serializer for K8sApp detail view.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SApp]
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
    body: K8SAppRequest | K8SAppRequest | K8SAppRequest | Unset = UNSET,
) -> K8SApp | None:
    """Install the K8s App via its associated block

    Args:
        id (UUID):
        body (K8SAppRequest | Unset): Full serializer for K8sApp detail view.
        body (K8SAppRequest | Unset): Full serializer for K8sApp detail view.
        body (K8SAppRequest | Unset): Full serializer for K8sApp detail view.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SApp
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
    body: K8SAppRequest | K8SAppRequest | K8SAppRequest | Unset = UNSET,
) -> Response[K8SApp]:
    """Install the K8s App via its associated block

    Args:
        id (UUID):
        body (K8SAppRequest | Unset): Full serializer for K8sApp detail view.
        body (K8SAppRequest | Unset): Full serializer for K8sApp detail view.
        body (K8SAppRequest | Unset): Full serializer for K8sApp detail view.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[K8SApp]
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
    body: K8SAppRequest | K8SAppRequest | K8SAppRequest | Unset = UNSET,
) -> K8SApp | None:
    """Install the K8s App via its associated block

    Args:
        id (UUID):
        body (K8SAppRequest | Unset): Full serializer for K8sApp detail view.
        body (K8SAppRequest | Unset): Full serializer for K8sApp detail view.
        body (K8SAppRequest | Unset): Full serializer for K8sApp detail view.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        K8SApp
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
