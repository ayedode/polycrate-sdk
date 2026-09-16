from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grafana_dashboard_list_active_condition_instances_item import (
        GrafanaDashboardListActiveConditionInstancesItem,
    )
    from ..models.grafana_dashboard_list_created import GrafanaDashboardListCreated
    from ..models.grafana_dashboard_list_organization_type_0 import GrafanaDashboardListOrganizationType0
    from ..models.grafana_dashboard_list_workspace_type_0 import GrafanaDashboardListWorkspaceType0


T = TypeVar("T", bound="GrafanaDashboardList")


@_attrs_define
class GrafanaDashboardList:
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
            active_condition_instances (list[GrafanaDashboardListActiveConditionInstancesItem]):
            organization (GrafanaDashboardListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (GrafanaDashboardListWorkspaceType0 | None):
            created (GrafanaDashboardListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            source_uid (str): UID in Operations Grafana.
            latest_revision_number (int | None):
            is_default (bool | Unset): New organizations automatically subscribe to this dashboard. Catalog sync overwrites
                this from GRAFANA_OPERATIONS_DEFAULT_TAG when that setting is non-empty.
            tags (Any | Unset): Dashboard tags as reported by Operations Grafana.
            last_imported_at (datetime.datetime | None | Unset): Timestamp of the last successful import from Operations
                Grafana.
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[GrafanaDashboardListActiveConditionInstancesItem]
    organization: GrafanaDashboardListOrganizationType0 | None
    organization_priority: bool
    workspace: GrafanaDashboardListWorkspaceType0 | None
    created: GrafanaDashboardListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    source_uid: str
    latest_revision_number: int | None
    is_default: bool | Unset = UNSET
    tags: Any | Unset = UNSET
    last_imported_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.grafana_dashboard_list_organization_type_0 import (
            GrafanaDashboardListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.grafana_dashboard_list_workspace_type_0 import GrafanaDashboardListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, GrafanaDashboardListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, GrafanaDashboardListWorkspaceType0):
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

        source_uid = self.source_uid

        latest_revision_number: int | None
        latest_revision_number = self.latest_revision_number

        is_default = self.is_default

        tags = self.tags

        last_imported_at: None | str | Unset
        if isinstance(self.last_imported_at, Unset):
            last_imported_at = UNSET
        elif isinstance(self.last_imported_at, datetime.datetime):
            last_imported_at = self.last_imported_at.isoformat()
        else:
            last_imported_at = self.last_imported_at

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
                "source_uid": source_uid,
                "latest_revision_number": latest_revision_number,
            }
        )
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if tags is not UNSET:
            field_dict["tags"] = tags
        if last_imported_at is not UNSET:
            field_dict["last_imported_at"] = last_imported_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grafana_dashboard_list_active_condition_instances_item import (
            GrafanaDashboardListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.grafana_dashboard_list_created import GrafanaDashboardListCreated  # noqa: PLC0415
        from ..models.grafana_dashboard_list_organization_type_0 import (
            GrafanaDashboardListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.grafana_dashboard_list_workspace_type_0 import GrafanaDashboardListWorkspaceType0  # noqa: PLC0415

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
            active_condition_instances_item = GrafanaDashboardListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> GrafanaDashboardListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = GrafanaDashboardListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GrafanaDashboardListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> GrafanaDashboardListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = GrafanaDashboardListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GrafanaDashboardListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = GrafanaDashboardListCreated.from_dict(d.pop("created"))

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

        source_uid = d.pop("source_uid")

        def _parse_latest_revision_number(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        latest_revision_number = _parse_latest_revision_number(d.pop("latest_revision_number"))

        is_default = d.pop("is_default", UNSET)

        tags = d.pop("tags", UNSET)

        def _parse_last_imported_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_imported_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_imported_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_imported_at = _parse_last_imported_at(d.pop("last_imported_at", UNSET))

        grafana_dashboard_list = cls(
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
            source_uid=source_uid,
            latest_revision_number=latest_revision_number,
            is_default=is_default,
            tags=tags,
            last_imported_at=last_imported_at,
        )

        grafana_dashboard_list.additional_properties = d
        return grafana_dashboard_list

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
