from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.compliance_report_list_active_condition_instances_item import (
        ComplianceReportListActiveConditionInstancesItem,
    )
    from ..models.compliance_report_list_created import ComplianceReportListCreated
    from ..models.compliance_report_list_organization_type_0 import ComplianceReportListOrganizationType0
    from ..models.compliance_report_list_workspace_type_0 import ComplianceReportListWorkspaceType0


T = TypeVar("T", bound="ComplianceReportList")


@_attrs_define
class ComplianceReportList:
    """Basis-Serializer für alle ManagedObject List-Endpoints.

    Liefert die generischen Felder die alle ManagedObjects teilen:
    - id: UUID
    - name: String-Repräsentation des Objects (__str__)
    - state: Object State
    - organization: Organization (id, slug, name)
    - workspace: Workspace (id, name) oder None
    - created: Kombifeld (created_at, created_at_humanized, created_at_display, created_by)

    Subclasses müssen:
    - model in Meta definieren
    - Zusätzliche model-spezifische Felder in Meta.fields hinzufügen

    Usage:
        class K8sClusterListSerializer(ManagedObjectListSerializer):
            class Meta(ManagedObjectListSerializer.Meta):
                model = K8sCluster
                fields = ManagedObjectListSerializer.Meta.fields + ['kubernetes_version', 'kind']

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
            active_condition_instances (list[ComplianceReportListActiveConditionInstancesItem]):
            organization (ComplianceReportListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (ComplianceReportListWorkspaceType0 | None):
            created (ComplianceReportListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            status (str):
            period_start (datetime.date):
            period_end (datetime.date):
            schema_version (str):
            generated_at (datetime.datetime | None):
            framework_refs (Any):
            payload_ready (bool):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[ComplianceReportListActiveConditionInstancesItem]
    organization: ComplianceReportListOrganizationType0 | None
    organization_priority: bool
    workspace: ComplianceReportListWorkspaceType0 | None
    created: ComplianceReportListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    status: str
    period_start: datetime.date
    period_end: datetime.date
    schema_version: str
    generated_at: datetime.datetime | None
    framework_refs: Any
    payload_ready: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_report_list_organization_type_0 import (
            ComplianceReportListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.compliance_report_list_workspace_type_0 import ComplianceReportListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, ComplianceReportListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, ComplianceReportListWorkspaceType0):
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

        status = self.status

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        schema_version = self.schema_version

        generated_at: None | str
        if isinstance(self.generated_at, datetime.datetime):
            generated_at = self.generated_at.isoformat()
        else:
            generated_at = self.generated_at

        framework_refs = self.framework_refs

        payload_ready = self.payload_ready

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
                "status": status,
                "period_start": period_start,
                "period_end": period_end,
                "schema_version": schema_version,
                "generated_at": generated_at,
                "framework_refs": framework_refs,
                "payload_ready": payload_ready,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_report_list_active_condition_instances_item import (
            ComplianceReportListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.compliance_report_list_created import ComplianceReportListCreated  # noqa: PLC0415
        from ..models.compliance_report_list_organization_type_0 import (
            ComplianceReportListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.compliance_report_list_workspace_type_0 import ComplianceReportListWorkspaceType0  # noqa: PLC0415

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
            active_condition_instances_item = ComplianceReportListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> ComplianceReportListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = ComplianceReportListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ComplianceReportListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> ComplianceReportListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = ComplianceReportListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ComplianceReportListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = ComplianceReportListCreated.from_dict(d.pop("created"))

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

        status = d.pop("status")

        period_start = datetime.date.fromisoformat(d.pop("period_start"))

        period_end = datetime.date.fromisoformat(d.pop("period_end"))

        schema_version = d.pop("schema_version")

        def _parse_generated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                generated_at_type_0 = datetime.datetime.fromisoformat(data)

                return generated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        generated_at = _parse_generated_at(d.pop("generated_at"))

        framework_refs = d.pop("framework_refs")

        payload_ready = d.pop("payload_ready")

        compliance_report_list = cls(
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
            status=status,
            period_start=period_start,
            period_end=period_end,
            schema_version=schema_version,
            generated_at=generated_at,
            framework_refs=framework_refs,
            payload_ready=payload_ready,
        )

        compliance_report_list.additional_properties = d
        return compliance_report_list

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
