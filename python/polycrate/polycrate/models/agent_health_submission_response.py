from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentHealthSubmissionResponse")


@_attrs_define
class AgentHealthSubmissionResponse:
    """
    Attributes:
        status (str): Always "success"
        agent_id (UUID): Platform agent ID
        reported_agent_id (str): Agent-reported ID
        health_data_id (None | UUID): Stored health data ID
        pop_name (str): PoP name for this agent
        pop_id (None | UUID): PoP ID
        endpoint_monitoring_mode (str): Monitoring mode configured for workspace
        operator_global_endpoint_monitor (bool): Whether this operator monitors endpoints from other workspaces
        workspace_id (UUID): Workspace UUID for automatic operator configuration
        workspace_name (str): Human-readable workspace name
        organization_id (None | UUID): Organization UUID for automatic operator configuration
        organization_name (None | str): Human-readable organization name
    """

    status: str
    agent_id: UUID
    reported_agent_id: str
    health_data_id: None | UUID
    pop_name: str
    pop_id: None | UUID
    endpoint_monitoring_mode: str
    operator_global_endpoint_monitor: bool
    workspace_id: UUID
    workspace_name: str
    organization_id: None | UUID
    organization_name: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        agent_id = str(self.agent_id)

        reported_agent_id = self.reported_agent_id

        health_data_id: None | str
        if isinstance(self.health_data_id, UUID):
            health_data_id = str(self.health_data_id)
        else:
            health_data_id = self.health_data_id

        pop_name = self.pop_name

        pop_id: None | str
        if isinstance(self.pop_id, UUID):
            pop_id = str(self.pop_id)
        else:
            pop_id = self.pop_id

        endpoint_monitoring_mode = self.endpoint_monitoring_mode

        operator_global_endpoint_monitor = self.operator_global_endpoint_monitor

        workspace_id = str(self.workspace_id)

        workspace_name = self.workspace_name

        organization_id: None | str
        if isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        organization_name: None | str
        organization_name = self.organization_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "agent_id": agent_id,
                "reported_agent_id": reported_agent_id,
                "health_data_id": health_data_id,
                "pop_name": pop_name,
                "pop_id": pop_id,
                "endpoint_monitoring_mode": endpoint_monitoring_mode,
                "operator_global_endpoint_monitor": operator_global_endpoint_monitor,
                "workspace_id": workspace_id,
                "workspace_name": workspace_name,
                "organization_id": organization_id,
                "organization_name": organization_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        agent_id = UUID(d.pop("agent_id"))

        reported_agent_id = d.pop("reported_agent_id")

        def _parse_health_data_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                health_data_id_type_0 = UUID(data)

                return health_data_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        health_data_id = _parse_health_data_id(d.pop("health_data_id"))

        pop_name = d.pop("pop_name")

        def _parse_pop_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pop_id_type_0 = UUID(data)

                return pop_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        pop_id = _parse_pop_id(d.pop("pop_id"))

        endpoint_monitoring_mode = d.pop("endpoint_monitoring_mode")

        operator_global_endpoint_monitor = d.pop("operator_global_endpoint_monitor")

        workspace_id = UUID(d.pop("workspace_id"))

        workspace_name = d.pop("workspace_name")

        def _parse_organization_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)

                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        organization_id = _parse_organization_id(d.pop("organization_id"))

        def _parse_organization_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        organization_name = _parse_organization_name(d.pop("organization_name"))

        agent_health_submission_response = cls(
            status=status,
            agent_id=agent_id,
            reported_agent_id=reported_agent_id,
            health_data_id=health_data_id,
            pop_name=pop_name,
            pop_id=pop_id,
            endpoint_monitoring_mode=endpoint_monitoring_mode,
            operator_global_endpoint_monitor=operator_global_endpoint_monitor,
            workspace_id=workspace_id,
            workspace_name=workspace_name,
            organization_id=organization_id,
            organization_name=organization_name,
        )

        agent_health_submission_response.additional_properties = d
        return agent_health_submission_response

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
