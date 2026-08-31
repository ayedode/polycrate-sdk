from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.endpoint_kind_enum import EndpointKindEnum, check_endpoint_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.endpoint_list_active_condition_instances_item import EndpointListActiveConditionInstancesItem
    from ..models.endpoint_list_created import EndpointListCreated
    from ..models.endpoint_list_organization_type_0 import EndpointListOrganizationType0
    from ..models.endpoint_list_workspace_type_0 import EndpointListWorkspaceType0


T = TypeVar("T", bound="EndpointList")


@_attrs_define
class EndpointList:
    """Endpoint List serializer - erbt von ManagedObjectListSerializer.

    Generische Felder (von ManagedObjectListSerializer):
    - id, name, state, organization, workspace, created_at, reconciliation_running, url

    Endpoint-spezifische Felder:
    - kind, remote_address
    - slo_availability, sla_availability (Spec: .specs/0.11.24/sre-sla-slo-sli-framework.md)

    has_active_downtime entfernt: Exists()-Subquery war zu teuer in Prod (558+ Endpoints).
    See: .specs/0.14.13/endpoint-table-performance.md

    uptime_24h_percent entfernt: Historische Uptime-Werte kommen jetzt aus VictoriaMetrics
    via polycrate_io_api_endpoint_up (metric_functions Dashboard-Tab).

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
            active_condition_instances (list[EndpointListActiveConditionInstancesItem]):
            organization (EndpointListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (EndpointListWorkspaceType0 | None):
            created (EndpointListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            kind (EndpointKindEnum): * `icmp` - ICMP Endpoint
                * `http` - HTTP Endpoint
                * `tcp` - TCP Endpoint
                * `dns` - DNS Endpoint
            remote_address (str):
            slo_availability (None | str):
            sla_availability (None | str):
            slo_status (str):
            sla_status (str):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[EndpointListActiveConditionInstancesItem]
    organization: EndpointListOrganizationType0 | None
    organization_priority: bool
    workspace: EndpointListWorkspaceType0 | None
    created: EndpointListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    kind: EndpointKindEnum
    remote_address: str
    slo_availability: None | str
    sla_availability: None | str
    slo_status: str
    sla_status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.endpoint_list_organization_type_0 import EndpointListOrganizationType0
        from ..models.endpoint_list_workspace_type_0 import EndpointListWorkspaceType0

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
        if isinstance(self.organization, EndpointListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, EndpointListWorkspaceType0):
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

        remote_address = self.remote_address

        slo_availability: None | str
        slo_availability = self.slo_availability

        sla_availability: None | str
        sla_availability = self.sla_availability

        slo_status = self.slo_status

        sla_status = self.sla_status

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
                "remote_address": remote_address,
                "slo_availability": slo_availability,
                "sla_availability": sla_availability,
                "slo_status": slo_status,
                "sla_status": sla_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_list_active_condition_instances_item import EndpointListActiveConditionInstancesItem
        from ..models.endpoint_list_created import EndpointListCreated
        from ..models.endpoint_list_organization_type_0 import EndpointListOrganizationType0
        from ..models.endpoint_list_workspace_type_0 import EndpointListWorkspaceType0

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
            active_condition_instances_item = EndpointListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> EndpointListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = EndpointListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> EndpointListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = EndpointListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = EndpointListCreated.from_dict(d.pop("created"))

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

        kind = check_endpoint_kind_enum(d.pop("kind"))

        remote_address = d.pop("remote_address")

        def _parse_slo_availability(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slo_availability = _parse_slo_availability(d.pop("slo_availability"))

        def _parse_sla_availability(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sla_availability = _parse_sla_availability(d.pop("sla_availability"))

        slo_status = d.pop("slo_status")

        sla_status = d.pop("sla_status")

        endpoint_list = cls(
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
            remote_address=remote_address,
            slo_availability=slo_availability,
            sla_availability=sla_availability,
            slo_status=slo_status,
            sla_status=sla_status,
        )

        endpoint_list.additional_properties = d
        return endpoint_list

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
