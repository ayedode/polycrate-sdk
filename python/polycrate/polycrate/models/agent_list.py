from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_kind_enum import AgentKindEnum, check_agent_kind_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.agent_list_active_condition_instances_item import AgentListActiveConditionInstancesItem
    from ..models.agent_list_created import AgentListCreated
    from ..models.agent_list_organization_type_0 import AgentListOrganizationType0
    from ..models.agent_list_workspace_type_0 import AgentListWorkspaceType0


T = TypeVar("T", bound="AgentList")


@_attrs_define
class AgentList:
    """Agent List serializer - erbt von ManagedObjectListSerializer.

    Generische Felder (von ManagedObjectListSerializer):
    - id, name, state, organization, workspace, created, reconciliation_running, url

    Agent-spezifische Felder:
    - kind, version, is_active, last_seen, utilization

    Per .specs/0.11.4/dynamic-table-v2.md
    Per .specs/0.11.11/index.md: utilization Feld für Utilization Bar

        Attributes:
            id (UUID):
            name (str): Gibt die bevorzugte UI-Anzeige (display_name) zurück.
            state (LastStateEnum): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            labels (Any):
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            condition_instance_count (int): Number of active ConditionInstances linked to this object (Spec 419).
                Uses prefetched data (_prefetched_active_conditions) when available to avoid N+1.
            active_condition_instances (list[AgentListActiveConditionInstancesItem]):
            organization (AgentListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (AgentListWorkspaceType0 | None):
            created (AgentListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            kind (AgentKindEnum): * `agent` - Agent
                * `operator` - Operator
            version (None | str): Version of the agent software
            is_active (bool): Whether this agent is considered active
            last_seen (datetime.datetime | None): Last time this agent called the API
            utilization (float): Agent utilization as percentage.

                Berechnung: (assigned_endpoints / max_endpoints) * 100

                Per .specs/0.11.11/index.md
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[AgentListActiveConditionInstancesItem]
    organization: AgentListOrganizationType0 | None
    organization_priority: bool
    workspace: AgentListWorkspaceType0 | None
    created: AgentListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    kind: AgentKindEnum
    version: None | str
    is_active: bool
    last_seen: datetime.datetime | None
    utilization: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_list_organization_type_0 import AgentListOrganizationType0  # noqa: PLC0415
        from ..models.agent_list_workspace_type_0 import AgentListWorkspaceType0  # noqa: PLC0415

        id = str(self.id)

        name = self.name

        state: str = self.state

        labels = self.labels

        conditions = self.conditions

        condition_instance_count = self.condition_instance_count

        active_condition_instances = []
        for active_condition_instances_item_data in self.active_condition_instances:
            active_condition_instances_item = active_condition_instances_item_data.to_dict()
            active_condition_instances.append(active_condition_instances_item)

        organization: dict[str, Any] | None
        if isinstance(self.organization, AgentListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, AgentListWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        kind: str = self.kind

        version: None | str
        version = self.version

        is_active = self.is_active

        last_seen: None | str
        if isinstance(self.last_seen, datetime.datetime):
            last_seen = self.last_seen.isoformat()
        else:
            last_seen = self.last_seen

        utilization = self.utilization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "labels": labels,
                "conditions": conditions,
                "condition_instance_count": condition_instance_count,
                "active_condition_instances": active_condition_instances,
                "organization": organization,
                "organization_priority": organization_priority,
                "workspace": workspace,
                "created": created,
                "archived": archived,
                "reconciliation_running": reconciliation_running,
                "effective_criticality": effective_criticality,
                "url": url,
                "kind": kind,
                "version": version,
                "is_active": is_active,
                "last_seen": last_seen,
                "utilization": utilization,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_list_active_condition_instances_item import (
            AgentListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.agent_list_created import AgentListCreated  # noqa: PLC0415
        from ..models.agent_list_organization_type_0 import AgentListOrganizationType0  # noqa: PLC0415
        from ..models.agent_list_workspace_type_0 import AgentListWorkspaceType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = AgentListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> AgentListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = AgentListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> AgentListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = AgentListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = AgentListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_effective_criticality(data: object) -> EffectiveCriticalityEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_0 = check_effective_criticality_enum(data)

                return effective_criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EffectiveCriticalityEnum | None, data)

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        url = d.pop("url")

        kind = check_agent_kind_enum(d.pop("kind"))

        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))

        is_active = d.pop("is_active")

        def _parse_last_seen(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_type_0 = datetime.datetime.fromisoformat(data)

                return last_seen_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_seen = _parse_last_seen(d.pop("last_seen"))

        utilization = d.pop("utilization")

        agent_list = cls(
            id=id,
            name=name,
            state=state,
            labels=labels,
            conditions=conditions,
            condition_instance_count=condition_instance_count,
            active_condition_instances=active_condition_instances,
            organization=organization,
            organization_priority=organization_priority,
            workspace=workspace,
            created=created,
            archived=archived,
            reconciliation_running=reconciliation_running,
            effective_criticality=effective_criticality,
            url=url,
            kind=kind,
            version=version,
            is_active=is_active,
            last_seen=last_seen,
            utilization=utilization,
        )

        agent_list.additional_properties = d
        return agent_list

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
