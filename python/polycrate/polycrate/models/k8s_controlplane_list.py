from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.k8s_controlplane_list_active_condition_instances_item import (
        K8SControlplaneListActiveConditionInstancesItem,
    )
    from ..models.k8s_controlplane_list_block_type_0 import K8SControlplaneListBlockType0
    from ..models.k8s_controlplane_list_created import K8SControlplaneListCreated
    from ..models.k8s_controlplane_list_k8s_cluster_type_0 import K8SControlplaneListK8SClusterType0
    from ..models.k8s_controlplane_list_organization_type_0 import K8SControlplaneListOrganizationType0
    from ..models.k8s_controlplane_list_region_type_0 import K8SControlplaneListRegionType0
    from ..models.k8s_controlplane_list_workspace_type_0 import K8SControlplaneListWorkspaceType0


T = TypeVar("T", bound="K8SControlplaneList")


@_attrs_define
class K8SControlplaneList:
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
            active_condition_instances (list[K8SControlplaneListActiveConditionInstancesItem]):
            organization (K8SControlplaneListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (K8SControlplaneListWorkspaceType0 | None):
            created (K8SControlplaneListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            region (K8SControlplaneListRegionType0 | None):
            block (K8SControlplaneListBlockType0 | None):
            k8s_cluster (K8SControlplaneListK8SClusterType0 | None):
            ip_address (None | str):
            loadbalancer_mode (str):
            storage_class (str):
            cluster_domain (str):
            hostname (None | str):
            deployment_checksum (None | str):
            last_deployed_checksum (None | str):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[K8SControlplaneListActiveConditionInstancesItem]
    organization: K8SControlplaneListOrganizationType0 | None
    organization_priority: bool
    workspace: K8SControlplaneListWorkspaceType0 | None
    created: K8SControlplaneListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    region: K8SControlplaneListRegionType0 | None
    block: K8SControlplaneListBlockType0 | None
    k8s_cluster: K8SControlplaneListK8SClusterType0 | None
    ip_address: None | str
    loadbalancer_mode: str
    storage_class: str
    cluster_domain: str
    hostname: None | str
    deployment_checksum: None | str
    last_deployed_checksum: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.k8s_controlplane_list_block_type_0 import K8SControlplaneListBlockType0
        from ..models.k8s_controlplane_list_k8s_cluster_type_0 import K8SControlplaneListK8SClusterType0
        from ..models.k8s_controlplane_list_organization_type_0 import K8SControlplaneListOrganizationType0
        from ..models.k8s_controlplane_list_region_type_0 import K8SControlplaneListRegionType0
        from ..models.k8s_controlplane_list_workspace_type_0 import K8SControlplaneListWorkspaceType0

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
        if isinstance(self.organization, K8SControlplaneListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, K8SControlplaneListWorkspaceType0):
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

        region: dict[str, Any] | None
        if isinstance(self.region, K8SControlplaneListRegionType0):
            region = self.region.to_dict()
        else:
            region = self.region

        block: dict[str, Any] | None
        if isinstance(self.block, K8SControlplaneListBlockType0):
            block = self.block.to_dict()
        else:
            block = self.block

        k8s_cluster: dict[str, Any] | None
        if isinstance(self.k8s_cluster, K8SControlplaneListK8SClusterType0):
            k8s_cluster = self.k8s_cluster.to_dict()
        else:
            k8s_cluster = self.k8s_cluster

        ip_address: None | str
        ip_address = self.ip_address

        loadbalancer_mode = self.loadbalancer_mode

        storage_class = self.storage_class

        cluster_domain = self.cluster_domain

        hostname: None | str
        hostname = self.hostname

        deployment_checksum: None | str
        deployment_checksum = self.deployment_checksum

        last_deployed_checksum: None | str
        last_deployed_checksum = self.last_deployed_checksum

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
                "region": region,
                "block": block,
                "k8s_cluster": k8s_cluster,
                "ip_address": ip_address,
                "loadbalancer_mode": loadbalancer_mode,
                "storage_class": storage_class,
                "cluster_domain": cluster_domain,
                "hostname": hostname,
                "deployment_checksum": deployment_checksum,
                "last_deployed_checksum": last_deployed_checksum,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.k8s_controlplane_list_active_condition_instances_item import (
            K8SControlplaneListActiveConditionInstancesItem,
        )
        from ..models.k8s_controlplane_list_block_type_0 import K8SControlplaneListBlockType0
        from ..models.k8s_controlplane_list_created import K8SControlplaneListCreated
        from ..models.k8s_controlplane_list_k8s_cluster_type_0 import K8SControlplaneListK8SClusterType0
        from ..models.k8s_controlplane_list_organization_type_0 import K8SControlplaneListOrganizationType0
        from ..models.k8s_controlplane_list_region_type_0 import K8SControlplaneListRegionType0
        from ..models.k8s_controlplane_list_workspace_type_0 import K8SControlplaneListWorkspaceType0

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
            active_condition_instances_item = K8SControlplaneListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> K8SControlplaneListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = K8SControlplaneListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SControlplaneListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> K8SControlplaneListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = K8SControlplaneListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SControlplaneListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = K8SControlplaneListCreated.from_dict(d.pop("created"))

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

        def _parse_region(data: object) -> K8SControlplaneListRegionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                region_type_0 = K8SControlplaneListRegionType0.from_dict(data)

                return region_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SControlplaneListRegionType0 | None, data)

        region = _parse_region(d.pop("region"))

        def _parse_block(data: object) -> K8SControlplaneListBlockType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                block_type_0 = K8SControlplaneListBlockType0.from_dict(data)

                return block_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SControlplaneListBlockType0 | None, data)

        block = _parse_block(d.pop("block"))

        def _parse_k8s_cluster(data: object) -> K8SControlplaneListK8SClusterType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                k8s_cluster_type_0 = K8SControlplaneListK8SClusterType0.from_dict(data)

                return k8s_cluster_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SControlplaneListK8SClusterType0 | None, data)

        k8s_cluster = _parse_k8s_cluster(d.pop("k8s_cluster"))

        def _parse_ip_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip_address = _parse_ip_address(d.pop("ip_address"))

        loadbalancer_mode = d.pop("loadbalancer_mode")

        storage_class = d.pop("storage_class")

        cluster_domain = d.pop("cluster_domain")

        def _parse_hostname(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        hostname = _parse_hostname(d.pop("hostname"))

        def _parse_deployment_checksum(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deployment_checksum = _parse_deployment_checksum(d.pop("deployment_checksum"))

        def _parse_last_deployed_checksum(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_deployed_checksum = _parse_last_deployed_checksum(d.pop("last_deployed_checksum"))

        k8s_controlplane_list = cls(
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
            region=region,
            block=block,
            k8s_cluster=k8s_cluster,
            ip_address=ip_address,
            loadbalancer_mode=loadbalancer_mode,
            storage_class=storage_class,
            cluster_domain=cluster_domain,
            hostname=hostname,
            deployment_checksum=deployment_checksum,
            last_deployed_checksum=last_deployed_checksum,
        )

        k8s_controlplane_list.additional_properties = d
        return k8s_controlplane_list

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
