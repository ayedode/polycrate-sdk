from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delegation_source_enum import DelegationSourceEnum, check_delegation_source_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.ip_address_simple import IPAddressSimple
    from ..models.loadbalancer_instance_list_active_condition_instances_item import (
        LoadbalancerInstanceListActiveConditionInstancesItem,
    )
    from ..models.loadbalancer_instance_list_created import LoadbalancerInstanceListCreated
    from ..models.loadbalancer_instance_list_deployment_summary import LoadbalancerInstanceListDeploymentSummary
    from ..models.loadbalancer_instance_list_organization_type_0 import LoadbalancerInstanceListOrganizationType0
    from ..models.loadbalancer_instance_list_workspace_type_0 import LoadbalancerInstanceListWorkspaceType0
    from ..models.organization_simple import OrganizationSimple
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="LoadbalancerInstanceList")


@_attrs_define
class LoadbalancerInstanceList:
    """LoadbalancerInstance List serializer - erbt von ManagedObjectListSerializer.

    Generische Felder (von ManagedObjectListSerializer):
    - id, name, state, organization, workspace, created_at, reconciliation_running, url

    LoadbalancerInstance-spezifische Felder:
    - ip_address, deployment_summary, deployments_ready, deployments_total, last_deployment
    - traffic_30d_bytes_in, traffic_30d_bytes_out (Spec 182 / 589)
    - last_config_deployed_at, ports (Spec 205)
    - bytes_in_30d, bytes_out_30d, metrics_last_updated (Spec 381/589)

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
            active_condition_instances (list[LoadbalancerInstanceListActiveConditionInstancesItem]):
            organization (LoadbalancerInstanceListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (LoadbalancerInstanceListWorkspaceType0 | None):
            created (LoadbalancerInstanceListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            ip_address (IPAddressSimple): Simple serializer for IPAddress references in LoadBalancer context
            ip_address_value (None | str):
            deployment_summary (LoadbalancerInstanceListDeploymentSummary):
            deployments_ready (int):
            deployments_total (int):
            last_deployment (datetime.datetime | None):
            traffic_30d_bytes_in (int):
            traffic_30d_bytes_out (int):
            last_config_deployed_at (datetime.datetime):
            ports (Any):
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            bytes_in_30d (int):
            bytes_out_30d (int):
            metrics_last_updated (datetime.datetime):
            delegated_organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            delegated_workspace (WorkspaceSimple):
            loopback_resource_id (None | str): Loopback API entity id (e.g. load-balancer id).
            delegation_source (DelegationSourceEnum | None): Source of the delegation mapping.

                * `loopback_lb` - Loopback Load Balancer
                * `loopback_object_store` - Loopback Object Store
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[LoadbalancerInstanceListActiveConditionInstancesItem]
    organization: LoadbalancerInstanceListOrganizationType0 | None
    organization_priority: bool
    workspace: LoadbalancerInstanceListWorkspaceType0 | None
    created: LoadbalancerInstanceListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    ip_address: IPAddressSimple
    ip_address_value: None | str
    deployment_summary: LoadbalancerInstanceListDeploymentSummary
    deployments_ready: int
    deployments_total: int
    last_deployment: datetime.datetime | None
    traffic_30d_bytes_in: int
    traffic_30d_bytes_out: int
    last_config_deployed_at: datetime.datetime
    ports: Any
    is_deleted: bool
    deleted_at: datetime.datetime | None
    bytes_in_30d: int
    bytes_out_30d: int
    metrics_last_updated: datetime.datetime
    delegated_organization: OrganizationSimple
    delegated_workspace: WorkspaceSimple
    loopback_resource_id: None | str
    delegation_source: DelegationSourceEnum | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.loadbalancer_instance_list_organization_type_0 import LoadbalancerInstanceListOrganizationType0
        from ..models.loadbalancer_instance_list_workspace_type_0 import LoadbalancerInstanceListWorkspaceType0

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
        if isinstance(self.organization, LoadbalancerInstanceListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, LoadbalancerInstanceListWorkspaceType0):
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

        ip_address = self.ip_address.to_dict()

        ip_address_value: None | str
        ip_address_value = self.ip_address_value

        deployment_summary = self.deployment_summary.to_dict()

        deployments_ready = self.deployments_ready

        deployments_total = self.deployments_total

        last_deployment: None | str
        if isinstance(self.last_deployment, datetime.datetime):
            last_deployment = self.last_deployment.isoformat()
        else:
            last_deployment = self.last_deployment

        traffic_30d_bytes_in = self.traffic_30d_bytes_in

        traffic_30d_bytes_out = self.traffic_30d_bytes_out

        last_config_deployed_at = self.last_config_deployed_at.isoformat()

        ports = self.ports

        is_deleted = self.is_deleted

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        bytes_in_30d = self.bytes_in_30d

        bytes_out_30d = self.bytes_out_30d

        metrics_last_updated = self.metrics_last_updated.isoformat()

        delegated_organization = self.delegated_organization.to_dict()

        delegated_workspace = self.delegated_workspace.to_dict()

        loopback_resource_id: None | str
        loopback_resource_id = self.loopback_resource_id

        delegation_source: None | str
        if isinstance(self.delegation_source, str):
            delegation_source = self.delegation_source
        else:
            delegation_source = self.delegation_source

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
                "ip_address": ip_address,
                "ip_address_value": ip_address_value,
                "deployment_summary": deployment_summary,
                "deployments_ready": deployments_ready,
                "deployments_total": deployments_total,
                "last_deployment": last_deployment,
                "traffic_30d_bytes_in": traffic_30d_bytes_in,
                "traffic_30d_bytes_out": traffic_30d_bytes_out,
                "last_config_deployed_at": last_config_deployed_at,
                "ports": ports,
                "is_deleted": is_deleted,
                "deleted_at": deleted_at,
                "bytes_in_30d": bytes_in_30d,
                "bytes_out_30d": bytes_out_30d,
                "metrics_last_updated": metrics_last_updated,
                "delegated_organization": delegated_organization,
                "delegated_workspace": delegated_workspace,
                "loopback_resource_id": loopback_resource_id,
                "delegation_source": delegation_source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_address_simple import IPAddressSimple
        from ..models.loadbalancer_instance_list_active_condition_instances_item import (
            LoadbalancerInstanceListActiveConditionInstancesItem,
        )
        from ..models.loadbalancer_instance_list_created import LoadbalancerInstanceListCreated
        from ..models.loadbalancer_instance_list_deployment_summary import LoadbalancerInstanceListDeploymentSummary
        from ..models.loadbalancer_instance_list_organization_type_0 import LoadbalancerInstanceListOrganizationType0
        from ..models.loadbalancer_instance_list_workspace_type_0 import LoadbalancerInstanceListWorkspaceType0
        from ..models.organization_simple import OrganizationSimple
        from ..models.workspace_simple import WorkspaceSimple

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
            active_condition_instances_item = LoadbalancerInstanceListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> LoadbalancerInstanceListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = LoadbalancerInstanceListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LoadbalancerInstanceListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> LoadbalancerInstanceListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = LoadbalancerInstanceListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LoadbalancerInstanceListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = LoadbalancerInstanceListCreated.from_dict(d.pop("created"))

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

        ip_address = IPAddressSimple.from_dict(d.pop("ip_address"))

        def _parse_ip_address_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip_address_value = _parse_ip_address_value(d.pop("ip_address_value"))

        deployment_summary = LoadbalancerInstanceListDeploymentSummary.from_dict(d.pop("deployment_summary"))

        deployments_ready = d.pop("deployments_ready")

        deployments_total = d.pop("deployments_total")

        def _parse_last_deployment(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_deployment_type_0 = datetime.datetime.fromisoformat(data)

                return last_deployment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_deployment = _parse_last_deployment(d.pop("last_deployment"))

        traffic_30d_bytes_in = d.pop("traffic_30d_bytes_in")

        traffic_30d_bytes_out = d.pop("traffic_30d_bytes_out")

        last_config_deployed_at = datetime.datetime.fromisoformat(d.pop("last_config_deployed_at"))

        ports = d.pop("ports")

        is_deleted = d.pop("is_deleted")

        def _parse_deleted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at"))

        bytes_in_30d = d.pop("bytes_in_30d")

        bytes_out_30d = d.pop("bytes_out_30d")

        metrics_last_updated = datetime.datetime.fromisoformat(d.pop("metrics_last_updated"))

        delegated_organization = OrganizationSimple.from_dict(d.pop("delegated_organization"))

        delegated_workspace = WorkspaceSimple.from_dict(d.pop("delegated_workspace"))

        def _parse_loopback_resource_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        loopback_resource_id = _parse_loopback_resource_id(d.pop("loopback_resource_id"))

        def _parse_delegation_source(data: object) -> DelegationSourceEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegation_source_type_0 = check_delegation_source_enum(data)

                return delegation_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DelegationSourceEnum | None, data)

        delegation_source = _parse_delegation_source(d.pop("delegation_source"))

        loadbalancer_instance_list = cls(
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
            ip_address=ip_address,
            ip_address_value=ip_address_value,
            deployment_summary=deployment_summary,
            deployments_ready=deployments_ready,
            deployments_total=deployments_total,
            last_deployment=last_deployment,
            traffic_30d_bytes_in=traffic_30d_bytes_in,
            traffic_30d_bytes_out=traffic_30d_bytes_out,
            last_config_deployed_at=last_config_deployed_at,
            ports=ports,
            is_deleted=is_deleted,
            deleted_at=deleted_at,
            bytes_in_30d=bytes_in_30d,
            bytes_out_30d=bytes_out_30d,
            metrics_last_updated=metrics_last_updated,
            delegated_organization=delegated_organization,
            delegated_workspace=delegated_workspace,
            loopback_resource_id=loopback_resource_id,
            delegation_source=delegation_source,
        )

        loadbalancer_instance_list.additional_properties = d
        return loadbalancer_instance_list

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
