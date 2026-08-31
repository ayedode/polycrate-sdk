from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.k8s_app_list_active_condition_instances_item import K8SAppListActiveConditionInstancesItem
    from ..models.k8s_app_list_catalogue_app_type_0 import K8SAppListCatalogueAppType0
    from ..models.k8s_app_list_created import K8SAppListCreated
    from ..models.k8s_app_list_k8s_cluster_type_0 import K8SAppListK8SClusterType0
    from ..models.k8s_app_list_organization_type_0 import K8SAppListOrganizationType0
    from ..models.k8s_app_list_workspace_type_0 import K8SAppListWorkspaceType0


T = TypeVar("T", bound="K8SAppList")


@_attrs_define
class K8SAppList:
    """List serializer for K8sApp - V2 Dynamic Tables.

    Includes SLO/SLA fields per .specs/0.11.24/sre-sla-slo-sli-framework.md
    Includes Pod status fields per .specs/0.11.27/k8sapp-pod-status-tracking.md

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
            active_condition_instances (list[K8SAppListActiveConditionInstancesItem]):
            organization (K8SAppListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (K8SAppListWorkspaceType0 | None):
            created (K8SAppListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            kind (str):
            k8s_cluster (K8SAppListK8SClusterType0 | None):
            installed (bool):
            active (bool):
            pods_total (int):
            pods_ready (int):
            pods_health (None | str):
            slo_availability (str):
            sla_availability (str):
            slo_status (str):
            sla_status (str):
            has_active_downtime (bool):
            catalogue_app (K8SAppListCatalogueAppType0 | None):
            block_version (None | str):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[K8SAppListActiveConditionInstancesItem]
    organization: K8SAppListOrganizationType0 | None
    organization_priority: bool
    workspace: K8SAppListWorkspaceType0 | None
    created: K8SAppListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    kind: str
    k8s_cluster: K8SAppListK8SClusterType0 | None
    installed: bool
    active: bool
    pods_total: int
    pods_ready: int
    pods_health: None | str
    slo_availability: str
    sla_availability: str
    slo_status: str
    sla_status: str
    has_active_downtime: bool
    catalogue_app: K8SAppListCatalogueAppType0 | None
    block_version: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.k8s_app_list_catalogue_app_type_0 import K8SAppListCatalogueAppType0
        from ..models.k8s_app_list_k8s_cluster_type_0 import K8SAppListK8SClusterType0
        from ..models.k8s_app_list_organization_type_0 import K8SAppListOrganizationType0
        from ..models.k8s_app_list_workspace_type_0 import K8SAppListWorkspaceType0

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
        if isinstance(self.organization, K8SAppListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, K8SAppListWorkspaceType0):
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

        kind = self.kind

        k8s_cluster: dict[str, Any] | None
        if isinstance(self.k8s_cluster, K8SAppListK8SClusterType0):
            k8s_cluster = self.k8s_cluster.to_dict()
        else:
            k8s_cluster = self.k8s_cluster

        installed = self.installed

        active = self.active

        pods_total = self.pods_total

        pods_ready = self.pods_ready

        pods_health: None | str
        pods_health = self.pods_health

        slo_availability = self.slo_availability

        sla_availability = self.sla_availability

        slo_status = self.slo_status

        sla_status = self.sla_status

        has_active_downtime = self.has_active_downtime

        catalogue_app: dict[str, Any] | None
        if isinstance(self.catalogue_app, K8SAppListCatalogueAppType0):
            catalogue_app = self.catalogue_app.to_dict()
        else:
            catalogue_app = self.catalogue_app

        block_version: None | str
        block_version = self.block_version

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
                "k8s_cluster": k8s_cluster,
                "installed": installed,
                "active": active,
                "pods_total": pods_total,
                "pods_ready": pods_ready,
                "pods_health": pods_health,
                "slo_availability": slo_availability,
                "sla_availability": sla_availability,
                "slo_status": slo_status,
                "sla_status": sla_status,
                "has_active_downtime": has_active_downtime,
                "catalogue_app": catalogue_app,
                "block_version": block_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.k8s_app_list_active_condition_instances_item import K8SAppListActiveConditionInstancesItem
        from ..models.k8s_app_list_catalogue_app_type_0 import K8SAppListCatalogueAppType0
        from ..models.k8s_app_list_created import K8SAppListCreated
        from ..models.k8s_app_list_k8s_cluster_type_0 import K8SAppListK8SClusterType0
        from ..models.k8s_app_list_organization_type_0 import K8SAppListOrganizationType0
        from ..models.k8s_app_list_workspace_type_0 import K8SAppListWorkspaceType0

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
            active_condition_instances_item = K8SAppListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> K8SAppListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = K8SAppListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SAppListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> K8SAppListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = K8SAppListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SAppListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = K8SAppListCreated.from_dict(d.pop("created"))

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

        kind = d.pop("kind")

        def _parse_k8s_cluster(data: object) -> K8SAppListK8SClusterType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                k8s_cluster_type_0 = K8SAppListK8SClusterType0.from_dict(data)

                return k8s_cluster_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SAppListK8SClusterType0 | None, data)

        k8s_cluster = _parse_k8s_cluster(d.pop("k8s_cluster"))

        installed = d.pop("installed")

        active = d.pop("active")

        pods_total = d.pop("pods_total")

        pods_ready = d.pop("pods_ready")

        def _parse_pods_health(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pods_health = _parse_pods_health(d.pop("pods_health"))

        slo_availability = d.pop("slo_availability")

        sla_availability = d.pop("sla_availability")

        slo_status = d.pop("slo_status")

        sla_status = d.pop("sla_status")

        has_active_downtime = d.pop("has_active_downtime")

        def _parse_catalogue_app(data: object) -> K8SAppListCatalogueAppType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                catalogue_app_type_0 = K8SAppListCatalogueAppType0.from_dict(data)

                return catalogue_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SAppListCatalogueAppType0 | None, data)

        catalogue_app = _parse_catalogue_app(d.pop("catalogue_app"))

        def _parse_block_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        block_version = _parse_block_version(d.pop("block_version"))

        k8s_app_list = cls(
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
            k8s_cluster=k8s_cluster,
            installed=installed,
            active=active,
            pods_total=pods_total,
            pods_ready=pods_ready,
            pods_health=pods_health,
            slo_availability=slo_availability,
            sla_availability=sla_availability,
            slo_status=slo_status,
            sla_status=sla_status,
            has_active_downtime=has_active_downtime,
            catalogue_app=catalogue_app,
            block_version=block_version,
        )

        k8s_app_list.additional_properties = d
        return k8s_app_list

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
