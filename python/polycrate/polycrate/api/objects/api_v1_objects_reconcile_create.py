from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reconcile_already_running_response import ReconcileAlreadyRunningResponse
from ...models.reconcile_started_response import ReconcileStartedResponse
from ...types import Response


def _get_kwargs(
    object_type: str,
    object_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/objects/{object_type}/{object_id}/reconcile/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ReconcileAlreadyRunningResponse | ReconcileStartedResponse | None:
    if response.status_code == 200:
        response_200 = ReconcileStartedResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ReconcileAlreadyRunningResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ReconcileAlreadyRunningResponse | ReconcileStartedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    object_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ReconcileAlreadyRunningResponse | ReconcileStartedResponse]:
    """Trigger object reconciliation

     Start async reconciliation for any ManagedObject. Returns immediately with task_id.

    Args:
        object_type (str):
        object_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReconcileAlreadyRunningResponse | ReconcileStartedResponse]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    object_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | ReconcileAlreadyRunningResponse | ReconcileStartedResponse | None:
    """Trigger object reconciliation

     Start async reconciliation for any ManagedObject. Returns immediately with task_id.

    Args:
        object_type (str):
        object_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReconcileAlreadyRunningResponse | ReconcileStartedResponse
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ReconcileAlreadyRunningResponse | ReconcileStartedResponse]:
    """Trigger object reconciliation

     Start async reconciliation for any ManagedObject. Returns immediately with task_id.

    Args:
        object_type (str):
        object_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReconcileAlreadyRunningResponse | ReconcileStartedResponse]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | ReconcileAlreadyRunningResponse | ReconcileStartedResponse | None:
    """Trigger object reconciliation

     Start async reconciliation for any ManagedObject. Returns immediately with task_id.

    Args:
        object_type (str):
        object_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReconcileAlreadyRunningResponse | ReconcileStartedResponse
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            client=client,
        )
    ).parsed
