from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_kind_enum import AlertKindEnum, check_alert_kind_enum
from ..models.alert_status_enum import AlertStatusEnum, check_alert_status_enum
from ..models.category_enum import CategoryEnum, check_category_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.alert_list_active_condition_instances_item import AlertListActiveConditionInstancesItem
    from ..models.alert_list_created import AlertListCreated
    from ..models.alert_list_organization_type_0 import AlertListOrganizationType0
    from ..models.alert_list_workspace_type_0 import AlertListWorkspaceType0


T = TypeVar("T", bound="AlertList")


@_attrs_define
class AlertList:
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
            active_condition_instances (list[AlertListActiveConditionInstancesItem]):
            organization (AlertListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (AlertListWorkspaceType0 | None):
            created (AlertListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            kind (AlertKindEnum): * `grafana` - Grafana Alert
                * `generic` - Generic Alert
                * `checkmk` - CheckMK Alert
            status (AlertStatusEnum | None):
            criticality (CriticalityEnum | None): Criticality level. Null = inherit from workspace, then org. Explicit value
                overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            category (CategoryEnum): * `cluster.node` - Cluster / Node
                * `workload.pod` - Workload / Pod
                * `storage.volume` - Storage / Volume
                * `data.cnpg` - Data / CNPG
                * `data.replication` - Data / Replication
                * `data.mariadb` - Data / MariaDB
                * `data.mongodb` - Data / MongoDB
                * `backup.velero` - Backup / Velero
                * `observability.metrics` - Observability / Metrics
                * `security.secrets` - Security / Secrets
                * `security.access` - Security / Access
                * `gitops.flux` - GitOps / Flux
                * `availability.http` - Availability / HTTP
                * `application.customer` - Application / Customer
                * `platform.test` - Platform / Test
                * `unknown` - Unknown
            title (None | str):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[AlertListActiveConditionInstancesItem]
    organization: AlertListOrganizationType0 | None
    organization_priority: bool
    workspace: AlertListWorkspaceType0 | None
    created: AlertListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    kind: AlertKindEnum
    status: AlertStatusEnum | None
    criticality: CriticalityEnum | None
    category: CategoryEnum
    title: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alert_list_organization_type_0 import AlertListOrganizationType0
        from ..models.alert_list_workspace_type_0 import AlertListWorkspaceType0

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
        if isinstance(self.organization, AlertListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, AlertListWorkspaceType0):
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

        status: None | str
        if isinstance(self.status, str):
            status = self.status
        else:
            status = self.status

        criticality: None | str
        if isinstance(self.criticality, str):
            criticality = self.criticality
        else:
            criticality = self.criticality

        category: str = self.category

        title: None | str
        title = self.title

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
                "status": status,
                "criticality": criticality,
                "category": category,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_list_active_condition_instances_item import AlertListActiveConditionInstancesItem
        from ..models.alert_list_created import AlertListCreated
        from ..models.alert_list_organization_type_0 import AlertListOrganizationType0
        from ..models.alert_list_workspace_type_0 import AlertListWorkspaceType0

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
            active_condition_instances_item = AlertListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> AlertListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = AlertListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> AlertListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = AlertListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = AlertListCreated.from_dict(d.pop("created"))

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

        kind = check_alert_kind_enum(d.pop("kind"))

        def _parse_status(data: object) -> AlertStatusEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = check_alert_status_enum(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertStatusEnum | None, data)

        status = _parse_status(d.pop("status"))

        def _parse_criticality(data: object) -> CriticalityEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_0 = check_criticality_enum(data)

                return criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CriticalityEnum | None, data)

        criticality = _parse_criticality(d.pop("criticality"))

        category = check_category_enum(d.pop("category"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        alert_list = cls(
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
            status=status,
            criticality=criticality,
            category=category,
            title=title,
        )

        alert_list.additional_properties = d
        return alert_list

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
