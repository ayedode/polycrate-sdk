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
    from ..models.organization_list_active_condition_instances_item import OrganizationListActiveConditionInstancesItem
    from ..models.organization_list_created import OrganizationListCreated
    from ..models.organization_list_organization_type_0 import OrganizationListOrganizationType0
    from ..models.organization_list_workspace_type_0 import OrganizationListWorkspaceType0


T = TypeVar("T", bound="OrganizationList")


@_attrs_define
class OrganizationList:
    """Organization List serializer - erbt von ManagedObjectListSerializer.

    Generische Felder (von ManagedObjectListSerializer):
    - id, name, state, organization (None für Org), workspace (None für Org),
    - created_at, reconciliation_running, url

    Organization-spezifische Felder:
    - priority, tenant_id, legal_name
    - Billable values: s3_storage_bytes (preferred), s3_storage_kb (deprecated alias), lb_traffic_30d,
    registry_quota_used_bytes

    Performance: Billable values use cached fields from Organization model.
    Spec: .specs/0.11.25/org-cached-metrics.md

    Spec 663: has_active_downtime / firing_alerts_count / active_maintenances_count
    removed from list (V2 table no longer shows those columns).

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
            active_condition_instances (list[OrganizationListActiveConditionInstancesItem]):
            organization (None | OrganizationListOrganizationType0):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (None | OrganizationListWorkspaceType0):
            created (OrganizationListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            priority (bool): High priority organization flag
            tenant_id (None | str): 3-8 digit numeric tenant identifier
            legal_name (str):
            support_pin (None | str): 8-digit numeric PIN for support authentication
            has_icon (bool):
            icon_url (None | str):
            is_class_icon (bool):
            s3_storage_bytes (int): Total S3 storage in bytes across all buckets.
            s3_storage_kb (int): DEPRECATED: misnamed value is bytes; prefer s3_storage_bytes.
            lb_traffic_30d (int):
            registry_quota_used_bytes (int | None):
            cached_s3_storage_bytes (int): Total S3 storage in bytes across all buckets
            cached_s3_bucket_count (int): Cached S3 bucket count
            cached_s3_object_count (int): Cached total S3 object count across all buckets
            cached_lb_count (int): Cached loadbalancer instance count
            cached_lb_traffic_30d_bytes (int): Total 30-day loadbalancer traffic in bytes; COALESCE traffic.*.30d_total then
                bytes.*.30d_total
            cached_lb_traffic_30d_in_bytes (int): Cached inbound 30-day loadbalancer traffic in bytes; COALESCE
                traffic.in.30d_total then bytes.in.30d_total
            cached_lb_traffic_30d_out_bytes (int): Cached outbound 30-day loadbalancer traffic in bytes; COALESCE
                traffic.out.30d_total then bytes.out.30d_total
            cached_volume_count (int): Cached total K8sVolume count across all workspaces
            cached_volume_capacity_bytes (int): Cached total K8sVolume capacity in bytes across all workspaces
            cached_metrics_updated_at (datetime.datetime | None): Last time cached metrics were updated
            upstream_organization_id (None | str): ID of the external system object managing this organization
            upstream_system_id (None | str): Identifier of the external system managing this organization
            keycloak_org_id (None | str):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[OrganizationListActiveConditionInstancesItem]
    organization: None | OrganizationListOrganizationType0
    organization_priority: bool
    workspace: None | OrganizationListWorkspaceType0
    created: OrganizationListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    priority: bool
    tenant_id: None | str
    legal_name: str
    support_pin: None | str
    has_icon: bool
    icon_url: None | str
    is_class_icon: bool
    s3_storage_bytes: int
    s3_storage_kb: int
    lb_traffic_30d: int
    registry_quota_used_bytes: int | None
    cached_s3_storage_bytes: int
    cached_s3_bucket_count: int
    cached_s3_object_count: int
    cached_lb_count: int
    cached_lb_traffic_30d_bytes: int
    cached_lb_traffic_30d_in_bytes: int
    cached_lb_traffic_30d_out_bytes: int
    cached_volume_count: int
    cached_volume_capacity_bytes: int
    cached_metrics_updated_at: datetime.datetime | None
    upstream_organization_id: None | str
    upstream_system_id: None | str
    keycloak_org_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_list_organization_type_0 import OrganizationListOrganizationType0
        from ..models.organization_list_workspace_type_0 import OrganizationListWorkspaceType0

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
        if isinstance(self.organization, OrganizationListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, OrganizationListWorkspaceType0):
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

        priority = self.priority

        tenant_id: None | str
        tenant_id = self.tenant_id

        legal_name = self.legal_name

        support_pin: None | str
        support_pin = self.support_pin

        has_icon = self.has_icon

        icon_url: None | str
        icon_url = self.icon_url

        is_class_icon = self.is_class_icon

        s3_storage_bytes = self.s3_storage_bytes

        s3_storage_kb = self.s3_storage_kb

        lb_traffic_30d = self.lb_traffic_30d

        registry_quota_used_bytes: int | None
        registry_quota_used_bytes = self.registry_quota_used_bytes

        cached_s3_storage_bytes = self.cached_s3_storage_bytes

        cached_s3_bucket_count = self.cached_s3_bucket_count

        cached_s3_object_count = self.cached_s3_object_count

        cached_lb_count = self.cached_lb_count

        cached_lb_traffic_30d_bytes = self.cached_lb_traffic_30d_bytes

        cached_lb_traffic_30d_in_bytes = self.cached_lb_traffic_30d_in_bytes

        cached_lb_traffic_30d_out_bytes = self.cached_lb_traffic_30d_out_bytes

        cached_volume_count = self.cached_volume_count

        cached_volume_capacity_bytes = self.cached_volume_capacity_bytes

        cached_metrics_updated_at: None | str
        if isinstance(self.cached_metrics_updated_at, datetime.datetime):
            cached_metrics_updated_at = self.cached_metrics_updated_at.isoformat()
        else:
            cached_metrics_updated_at = self.cached_metrics_updated_at

        upstream_organization_id: None | str
        upstream_organization_id = self.upstream_organization_id

        upstream_system_id: None | str
        upstream_system_id = self.upstream_system_id

        keycloak_org_id: None | str
        keycloak_org_id = self.keycloak_org_id

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
                "priority": priority,
                "tenant_id": tenant_id,
                "legal_name": legal_name,
                "support_pin": support_pin,
                "has_icon": has_icon,
                "icon_url": icon_url,
                "is_class_icon": is_class_icon,
                "s3_storage_bytes": s3_storage_bytes,
                "s3_storage_kb": s3_storage_kb,
                "lb_traffic_30d": lb_traffic_30d,
                "registry_quota_used_bytes": registry_quota_used_bytes,
                "cached_s3_storage_bytes": cached_s3_storage_bytes,
                "cached_s3_bucket_count": cached_s3_bucket_count,
                "cached_s3_object_count": cached_s3_object_count,
                "cached_lb_count": cached_lb_count,
                "cached_lb_traffic_30d_bytes": cached_lb_traffic_30d_bytes,
                "cached_lb_traffic_30d_in_bytes": cached_lb_traffic_30d_in_bytes,
                "cached_lb_traffic_30d_out_bytes": cached_lb_traffic_30d_out_bytes,
                "cached_volume_count": cached_volume_count,
                "cached_volume_capacity_bytes": cached_volume_capacity_bytes,
                "cached_metrics_updated_at": cached_metrics_updated_at,
                "upstream_organization_id": upstream_organization_id,
                "upstream_system_id": upstream_system_id,
                "keycloak_org_id": keycloak_org_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_list_active_condition_instances_item import (
            OrganizationListActiveConditionInstancesItem,
        )
        from ..models.organization_list_created import OrganizationListCreated
        from ..models.organization_list_organization_type_0 import OrganizationListOrganizationType0
        from ..models.organization_list_workspace_type_0 import OrganizationListWorkspaceType0

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
            active_condition_instances_item = OrganizationListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> None | OrganizationListOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = OrganizationListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationListOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> None | OrganizationListWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = OrganizationListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationListWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = OrganizationListCreated.from_dict(d.pop("created"))

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

        priority = d.pop("priority")

        def _parse_tenant_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tenant_id = _parse_tenant_id(d.pop("tenant_id"))

        legal_name = d.pop("legal_name")

        def _parse_support_pin(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        support_pin = _parse_support_pin(d.pop("support_pin"))

        has_icon = d.pop("has_icon")

        def _parse_icon_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        icon_url = _parse_icon_url(d.pop("icon_url"))

        is_class_icon = d.pop("is_class_icon")

        s3_storage_bytes = d.pop("s3_storage_bytes")

        s3_storage_kb = d.pop("s3_storage_kb")

        lb_traffic_30d = d.pop("lb_traffic_30d")

        def _parse_registry_quota_used_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        registry_quota_used_bytes = _parse_registry_quota_used_bytes(d.pop("registry_quota_used_bytes"))

        cached_s3_storage_bytes = d.pop("cached_s3_storage_bytes")

        cached_s3_bucket_count = d.pop("cached_s3_bucket_count")

        cached_s3_object_count = d.pop("cached_s3_object_count")

        cached_lb_count = d.pop("cached_lb_count")

        cached_lb_traffic_30d_bytes = d.pop("cached_lb_traffic_30d_bytes")

        cached_lb_traffic_30d_in_bytes = d.pop("cached_lb_traffic_30d_in_bytes")

        cached_lb_traffic_30d_out_bytes = d.pop("cached_lb_traffic_30d_out_bytes")

        cached_volume_count = d.pop("cached_volume_count")

        cached_volume_capacity_bytes = d.pop("cached_volume_capacity_bytes")

        def _parse_cached_metrics_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cached_metrics_updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return cached_metrics_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        cached_metrics_updated_at = _parse_cached_metrics_updated_at(d.pop("cached_metrics_updated_at"))

        def _parse_upstream_organization_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        upstream_organization_id = _parse_upstream_organization_id(d.pop("upstream_organization_id"))

        def _parse_upstream_system_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        upstream_system_id = _parse_upstream_system_id(d.pop("upstream_system_id"))

        def _parse_keycloak_org_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        keycloak_org_id = _parse_keycloak_org_id(d.pop("keycloak_org_id"))

        organization_list = cls(
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
            priority=priority,
            tenant_id=tenant_id,
            legal_name=legal_name,
            support_pin=support_pin,
            has_icon=has_icon,
            icon_url=icon_url,
            is_class_icon=is_class_icon,
            s3_storage_bytes=s3_storage_bytes,
            s3_storage_kb=s3_storage_kb,
            lb_traffic_30d=lb_traffic_30d,
            registry_quota_used_bytes=registry_quota_used_bytes,
            cached_s3_storage_bytes=cached_s3_storage_bytes,
            cached_s3_bucket_count=cached_s3_bucket_count,
            cached_s3_object_count=cached_s3_object_count,
            cached_lb_count=cached_lb_count,
            cached_lb_traffic_30d_bytes=cached_lb_traffic_30d_bytes,
            cached_lb_traffic_30d_in_bytes=cached_lb_traffic_30d_in_bytes,
            cached_lb_traffic_30d_out_bytes=cached_lb_traffic_30d_out_bytes,
            cached_volume_count=cached_volume_count,
            cached_volume_capacity_bytes=cached_volume_capacity_bytes,
            cached_metrics_updated_at=cached_metrics_updated_at,
            upstream_organization_id=upstream_organization_id,
            upstream_system_id=upstream_system_id,
            keycloak_org_id=keycloak_org_id,
        )

        organization_list.additional_properties = d
        return organization_list

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
