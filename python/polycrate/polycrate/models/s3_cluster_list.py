from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.s3_cluster_kind_enum import S3ClusterKindEnum, check_s3_cluster_kind_enum

if TYPE_CHECKING:
    from ..models.s3_cluster_list_active_condition_instances_item import S3ClusterListActiveConditionInstancesItem
    from ..models.s3_cluster_list_created import S3ClusterListCreated
    from ..models.s3_cluster_list_organization_type_0 import S3ClusterListOrganizationType0
    from ..models.s3_cluster_list_workspace_type_0 import S3ClusterListWorkspaceType0


T = TypeVar("T", bound="S3ClusterList")


@_attrs_define
class S3ClusterList:
    """S3Cluster List serializer - erbt von ManagedObjectListSerializer.

    Per .specs/0.11.4/dynamic-table-v2.md
    Per spec 358: managed_buckets_usage_bytes + backend_utilization_percent für V2 Table

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
            active_condition_instances (list[S3ClusterListActiveConditionInstancesItem]):
            organization (None | S3ClusterListOrganizationType0):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (None | S3ClusterListWorkspaceType0):
            created (S3ClusterListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            kind (S3ClusterKindEnum): * `rook-ceph` - Rook CEPH
                * `minio` - Minio
            endpoint (str): $HOSTNAME (without protocol://)
            platform_service (bool): Makes this cluster available for the whole platform instead of a single organization
            allow_new_buckets (bool): When False, no new S3 buckets can be created on this cluster. Can be set automatically
                via S3_CLUSTER_MAX_USAGE_PERCENT threshold.
            include_in_cost_statement (bool): When False, all buckets on this cluster are omitted from CostStatement
                generation.
            managed_buckets_usage_bytes (int | None):
            backend_utilization_percent (float | None):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[S3ClusterListActiveConditionInstancesItem]
    organization: None | S3ClusterListOrganizationType0
    organization_priority: bool
    workspace: None | S3ClusterListWorkspaceType0
    created: S3ClusterListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    kind: S3ClusterKindEnum
    endpoint: str
    platform_service: bool
    allow_new_buckets: bool
    include_in_cost_statement: bool
    managed_buckets_usage_bytes: int | None
    backend_utilization_percent: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.s3_cluster_list_organization_type_0 import S3ClusterListOrganizationType0
        from ..models.s3_cluster_list_workspace_type_0 import S3ClusterListWorkspaceType0

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
        if isinstance(self.organization, S3ClusterListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, S3ClusterListWorkspaceType0):
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

        endpoint = self.endpoint

        platform_service = self.platform_service

        allow_new_buckets = self.allow_new_buckets

        include_in_cost_statement = self.include_in_cost_statement

        managed_buckets_usage_bytes: int | None
        managed_buckets_usage_bytes = self.managed_buckets_usage_bytes

        backend_utilization_percent: float | None
        backend_utilization_percent = self.backend_utilization_percent

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
                "endpoint": endpoint,
                "platform_service": platform_service,
                "allow_new_buckets": allow_new_buckets,
                "include_in_cost_statement": include_in_cost_statement,
                "managed_buckets_usage_bytes": managed_buckets_usage_bytes,
                "backend_utilization_percent": backend_utilization_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.s3_cluster_list_active_condition_instances_item import S3ClusterListActiveConditionInstancesItem
        from ..models.s3_cluster_list_created import S3ClusterListCreated
        from ..models.s3_cluster_list_organization_type_0 import S3ClusterListOrganizationType0
        from ..models.s3_cluster_list_workspace_type_0 import S3ClusterListWorkspaceType0

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
            active_condition_instances_item = S3ClusterListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> None | S3ClusterListOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = S3ClusterListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | S3ClusterListOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> None | S3ClusterListWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = S3ClusterListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | S3ClusterListWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = S3ClusterListCreated.from_dict(d.pop("created"))

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

        kind = check_s3_cluster_kind_enum(d.pop("kind"))

        endpoint = d.pop("endpoint")

        platform_service = d.pop("platform_service")

        allow_new_buckets = d.pop("allow_new_buckets")

        include_in_cost_statement = d.pop("include_in_cost_statement")

        def _parse_managed_buckets_usage_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        managed_buckets_usage_bytes = _parse_managed_buckets_usage_bytes(d.pop("managed_buckets_usage_bytes"))

        def _parse_backend_utilization_percent(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        backend_utilization_percent = _parse_backend_utilization_percent(d.pop("backend_utilization_percent"))

        s3_cluster_list = cls(
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
            endpoint=endpoint,
            platform_service=platform_service,
            allow_new_buckets=allow_new_buckets,
            include_in_cost_statement=include_in_cost_statement,
            managed_buckets_usage_bytes=managed_buckets_usage_bytes,
            backend_utilization_percent=backend_utilization_percent,
        )

        s3_cluster_list.additional_properties = d
        return s3_cluster_list

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
