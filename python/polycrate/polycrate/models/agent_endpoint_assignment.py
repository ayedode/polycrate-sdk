from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentEndpointAssignment")


@_attrs_define
class AgentEndpointAssignment:
    """Serializer for Agent's assigned endpoints with check status.

    Used by GET /api/v1/agents/{agent_id}/assignments/ endpoint
    for lazy-loaded table in Agent Detail UI.

        Attributes:
            endpoint_id (UUID):
            endpoint_name (str):
            endpoint_url (str):
            endpoint_kind (str):
            workspace_id (None | UUID):
            workspace_name (None | str):
            organization_name (None | str):
            assigned_at (datetime.datetime):
            last_check_at (datetime.datetime | None):
            last_check_success (bool | None):
            last_check_status_code (int | None):
            last_check_error_code (int):
            last_check_error_name (str):
            last_check_duration_ms (int | None):
            checks_executed (int):
            checks_successful (int):
            checks_failed (int):
            success_rate (int):
    """

    endpoint_id: UUID
    endpoint_name: str
    endpoint_url: str
    endpoint_kind: str
    workspace_id: None | UUID
    workspace_name: None | str
    organization_name: None | str
    assigned_at: datetime.datetime
    last_check_at: datetime.datetime | None
    last_check_success: bool | None
    last_check_status_code: int | None
    last_check_error_code: int
    last_check_error_name: str
    last_check_duration_ms: int | None
    checks_executed: int
    checks_successful: int
    checks_failed: int
    success_rate: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint_id = str(self.endpoint_id)

        endpoint_name = self.endpoint_name

        endpoint_url = self.endpoint_url

        endpoint_kind = self.endpoint_kind

        workspace_id: None | str
        if isinstance(self.workspace_id, UUID):
            workspace_id = str(self.workspace_id)
        else:
            workspace_id = self.workspace_id

        workspace_name: None | str
        workspace_name = self.workspace_name

        organization_name: None | str
        organization_name = self.organization_name

        assigned_at = self.assigned_at.isoformat()

        last_check_at: None | str
        if isinstance(self.last_check_at, datetime.datetime):
            last_check_at = self.last_check_at.isoformat()
        else:
            last_check_at = self.last_check_at

        last_check_success: bool | None
        last_check_success = self.last_check_success

        last_check_status_code: int | None
        last_check_status_code = self.last_check_status_code

        last_check_error_code = self.last_check_error_code

        last_check_error_name = self.last_check_error_name

        last_check_duration_ms: int | None
        last_check_duration_ms = self.last_check_duration_ms

        checks_executed = self.checks_executed

        checks_successful = self.checks_successful

        checks_failed = self.checks_failed

        success_rate = self.success_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpoint_id": endpoint_id,
                "endpoint_name": endpoint_name,
                "endpoint_url": endpoint_url,
                "endpoint_kind": endpoint_kind,
                "workspace_id": workspace_id,
                "workspace_name": workspace_name,
                "organization_name": organization_name,
                "assigned_at": assigned_at,
                "last_check_at": last_check_at,
                "last_check_success": last_check_success,
                "last_check_status_code": last_check_status_code,
                "last_check_error_code": last_check_error_code,
                "last_check_error_name": last_check_error_name,
                "last_check_duration_ms": last_check_duration_ms,
                "checks_executed": checks_executed,
                "checks_successful": checks_successful,
                "checks_failed": checks_failed,
                "success_rate": success_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint_id = UUID(d.pop("endpoint_id"))

        endpoint_name = d.pop("endpoint_name")

        endpoint_url = d.pop("endpoint_url")

        endpoint_kind = d.pop("endpoint_kind")

        def _parse_workspace_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                workspace_id_type_0 = UUID(data)

                return workspace_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id"))

        def _parse_workspace_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        workspace_name = _parse_workspace_name(d.pop("workspace_name"))

        def _parse_organization_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        organization_name = _parse_organization_name(d.pop("organization_name"))

        assigned_at = datetime.datetime.fromisoformat(d.pop("assigned_at"))

        def _parse_last_check_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_check_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_check_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_check_at = _parse_last_check_at(d.pop("last_check_at"))

        def _parse_last_check_success(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        last_check_success = _parse_last_check_success(d.pop("last_check_success"))

        def _parse_last_check_status_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        last_check_status_code = _parse_last_check_status_code(d.pop("last_check_status_code"))

        last_check_error_code = d.pop("last_check_error_code")

        last_check_error_name = d.pop("last_check_error_name")

        def _parse_last_check_duration_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        last_check_duration_ms = _parse_last_check_duration_ms(d.pop("last_check_duration_ms"))

        checks_executed = d.pop("checks_executed")

        checks_successful = d.pop("checks_successful")

        checks_failed = d.pop("checks_failed")

        success_rate = d.pop("success_rate")

        agent_endpoint_assignment = cls(
            endpoint_id=endpoint_id,
            endpoint_name=endpoint_name,
            endpoint_url=endpoint_url,
            endpoint_kind=endpoint_kind,
            workspace_id=workspace_id,
            workspace_name=workspace_name,
            organization_name=organization_name,
            assigned_at=assigned_at,
            last_check_at=last_check_at,
            last_check_success=last_check_success,
            last_check_status_code=last_check_status_code,
            last_check_error_code=last_check_error_code,
            last_check_error_name=last_check_error_name,
            last_check_duration_ms=last_check_duration_ms,
            checks_executed=checks_executed,
            checks_successful=checks_successful,
            checks_failed=checks_failed,
            success_rate=success_rate,
        )

        agent_endpoint_assignment.additional_properties = d
        return agent_endpoint_assignment

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
