from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.created_by_component_enum import CreatedByComponentEnum, check_created_by_component_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.s3_cluster_kind_enum import S3ClusterKindEnum, check_s3_cluster_kind_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_simple import OrganizationSimple
    from ..models.s3_bucket_list import S3BucketList
    from ..models.s3_cluster_created import S3ClusterCreated
    from ..models.s3_cluster_deleted_by_user_type_0 import S3ClusterDeletedByUserType0
    from ..models.s3_cluster_last_action_run_type_0 import S3ClusterLastActionRunType0
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="S3Cluster")


@_attrs_define
class S3Cluster:
    """S3Cluster detail — ManagedObjectDetailSerializer like K8sApp; workspace resolved via k8s_cluster FK.

    Attributes:
        id (UUID):
        created (S3ClusterCreated):
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        workspace (None | WorkspaceSimple):
        url (str): Gibt die absolute URL zum Object zurück.
        icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
            Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
        is_class_icon (bool):
        effective_slo_target (float | None):
        effective_sla_target (float | None):
        effective_criticality (EffectiveCriticalityEnum | None):
        last_action_run (None | S3ClusterLastActionRunType0):
        deleted_by_user (None | S3ClusterDeletedByUserType0):
        s3_buckets (list[S3BucketList]):
        backend_total_capacity_bytes (int | None):
        backend_logical_used_bytes (int | None):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
        is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
            runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
        state (LastStateEnum): * `OK` - Ok
            * `WARNING` - Warning
            * `CRITICAL` - Critical
            * `READY` - Ready
            * `DEGRADED` - Degraded
            * `DOWN` - Down
        state_reason (None | str):
        last_state (LastStateEnum): * `OK` - Ok
            * `WARNING` - Warning
            * `CRITICAL` - Critical
            * `READY` - Ready
            * `DEGRADED` - Degraded
            * `DOWN` - Down
        last_state_change (datetime.datetime | None):
        reconciliation_running (bool):
        reconciliation_task_id (None | str):
        reconciliation_task_meta (Any): Task metadata for reconciliation progress tracking (e.g., step, progress,
            started_at)
        last_reconciliation (datetime.datetime | None):
        discovery_running (bool):
        discovery_task_id (None | str):
        discovery_task_meta (Any): Task metadata for discovery progress tracking
        last_discovery (datetime.datetime | None):
        repair_running (bool):
        repair_task_id (None | str):
        repair_task_meta (Any): Task metadata for repair progress tracking
        last_repair (datetime.datetime | None):
        conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
            conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
        tolerations (Any): Tolerations match conditions. If a toleration for a condition exists for an object, the
            condition will not be applied.
        endpoint (str): $HOSTNAME (without protocol://)
        name (str | Unset): Object name
        display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
            from the name.
        labels (Any | Unset):
        annotations (Any | Unset):
        debug_mode (bool | Unset): Persists all Object Logs in the database
        provider (ProviderEnum | Unset): * `loopback` - Loopback
            * `hetzner_cloud` - HETZNER Cloud
            * `hetzner_robot` - HETZNER Robot
            * `bare_metal` - Bare-Metal
            * `powerdns` - PowerDNS
            * `cloudflare` - Cloudflare
            * `rook-ceph` - Rook Ceph
            * `polycrate` - Polycrate
            * `kubernetes` - Kubernetes
            * `helm` - Helm
            * `generic` - Generic
            * `victorialogs` - VictoriaLogs
            * `system` - System
        provider_reference (None | str | Unset):
        provider_id (None | str | Unset):
        reconciliation_enabled (bool | Unset):
        last_reconciliation_duration_seconds (float | None | Unset): Duration of the last reconciliation in seconds
        discovery_enabled (bool | Unset):
        scope (ScopeEnum | Unset): * `system` - System
            * `user` - User
        archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
        archived_at (datetime.datetime | None | Unset):
        archived_reason (None | str | Unset): The reason why the object was archived
        created_by_component (BlankEnum | CreatedByComponentEnum | None | Unset): Component that created this object:
            cli, operator, or api.

            * `cli` - CLI
            * `operator` - Operator
            * `api` - API
        target_availability (None | str | Unset): Target availability in % (overrides SystemConfig default). Null = use
            SystemConfig DEFAULT_TARGET_AVAILABILITY.
        actual_availability (str | Unset): Calculated actual availability as yearly average in %
        slo_target (None | str | Unset): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
        slo_window_days (int | None | Unset): SLO window in days. Null = use SystemConfig DEFAULT_SLO_WINDOW_DAYS
        slo_availability (str | Unset): Calculated SLO availability in % (updated in reconcile)
        sla_target (None | str | Unset): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
        sla_window_days (int | None | Unset): SLA window in days. Null = use SystemConfig DEFAULT_SLA_WINDOW_DAYS (365)
        sla_availability (str | Unset): Calculated SLA availability in % (updated in reconcile)
        criticality (BlankEnum | CriticalityEnum | None | Unset): Criticality level. Null = inherit from workspace, then
            org. Explicit value overrides inheritance.

            * `high` - High
            * `medium` - Medium
            * `low` - Low
        managed_by_object_id (None | str | Unset):
        platform_dns_record_created (bool | Unset):
        slug (None | str | Unset):
        alias (None | str | Unset):
        endpoint_secure (bool | Unset): Whether the endpoint is secure (https)
        admin_endpoint (None | str | Unset): https://$HOSTNAME (including protocol://)
        admin_endpoint_secure (bool | Unset): Whether the admin endpoint is secure (https)
        kind (S3ClusterKindEnum | Unset): * `rook-ceph` - Rook CEPH
            * `minio` - Minio Default: 'rook-ceph'.
        description (None | str | Unset):
        active (bool | Unset):
        platform_service (bool | Unset): Makes this cluster available for the whole platform instead of a single
            organization
        cluster_config (Any | Unset):
        cluster_info (Any | Unset):
        namespace (None | str | Unset):  Default: 'rook-ceph'.
        region (None | str | Unset):
        allow_new_buckets (bool | Unset): When False, no new S3 buckets can be created on this cluster. Can be set
            automatically via S3_CLUSTER_MAX_USAGE_PERCENT threshold.
        include_in_cost_statement (bool | Unset): When False, all buckets on this cluster are omitted from CostStatement
            generation.
        ceph_osd_cluster_total_bytes (int | None | Unset): rook-ceph: Ceph OSD total capacity (bytes) from
            ceph_cluster_total_bytes.
        radosgw_buckets_logical_used_bytes (int | None | Unset): rook-ceph: RGW-reported sum of bucket actual sizes
            (bytes).
        minio_cluster_capacity_usable_bytes (int | None | Unset): minio: Usable cluster capacity (bytes); sourced from
            v2 minio_cluster_capacity_usable_total_bytes or v3 minio_cluster_health_capacity_usable_total_bytes.
        minio_cluster_usage_bytes (int | None | Unset): minio: Cluster usage (bytes) via
            sum(minio_cluster_usage_buckets_total_bytes).
        managed_buckets_usage_kb (int | None | Unset): Sum of S3Bucket.current_usage (KB) for non-archived buckets on
            this cluster.
        managed_buckets_object_count (int | None | Unset): Sum of S3Bucket.current_object_count for non-archived buckets
            on this cluster.
        archived_by (int | None | Unset): The user who archived the object
        managed_by_content_type (int | None | Unset):
        modified_by_user (int | None | Unset): The user who last modified the object
        created_by_user (int | None | Unset): The user who created the object
        credential (None | Unset | UUID):
        k8s_cluster (None | Unset | UUID):
        default_product (None | Unset | UUID): Default product assigned to new S3 Buckets in this cluster.
    """

    id: UUID
    created: S3ClusterCreated
    organization: OrganizationSimple
    workspace: None | WorkspaceSimple
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    effective_criticality: EffectiveCriticalityEnum | None
    last_action_run: None | S3ClusterLastActionRunType0
    deleted_by_user: None | S3ClusterDeletedByUserType0
    s3_buckets: list[S3BucketList]
    backend_total_capacity_bytes: int | None
    backend_logical_used_bytes: int | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    state: LastStateEnum
    state_reason: None | str
    last_state: LastStateEnum
    last_state_change: datetime.datetime | None
    reconciliation_running: bool
    reconciliation_task_id: None | str
    reconciliation_task_meta: Any
    last_reconciliation: datetime.datetime | None
    discovery_running: bool
    discovery_task_id: None | str
    discovery_task_meta: Any
    last_discovery: datetime.datetime | None
    repair_running: bool
    repair_task_id: None | str
    repair_task_meta: Any
    last_repair: datetime.datetime | None
    conditions: Any
    tolerations: Any
    endpoint: str
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    last_reconciliation_duration_seconds: float | None | Unset = UNSET
    discovery_enabled: bool | Unset = UNSET
    scope: ScopeEnum | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    created_by_component: BlankEnum | CreatedByComponentEnum | None | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    actual_availability: str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_window_days: int | None | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_window_days: int | None | Unset = UNSET
    sla_availability: str | Unset = UNSET
    criticality: BlankEnum | CriticalityEnum | None | Unset = UNSET
    managed_by_object_id: None | str | Unset = UNSET
    platform_dns_record_created: bool | Unset = UNSET
    slug: None | str | Unset = UNSET
    alias: None | str | Unset = UNSET
    endpoint_secure: bool | Unset = UNSET
    admin_endpoint: None | str | Unset = UNSET
    admin_endpoint_secure: bool | Unset = UNSET
    kind: S3ClusterKindEnum | Unset = "rook-ceph"
    description: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    cluster_config: Any | Unset = UNSET
    cluster_info: Any | Unset = UNSET
    namespace: None | str | Unset = "rook-ceph"
    region: None | str | Unset = UNSET
    allow_new_buckets: bool | Unset = UNSET
    include_in_cost_statement: bool | Unset = UNSET
    ceph_osd_cluster_total_bytes: int | None | Unset = UNSET
    radosgw_buckets_logical_used_bytes: int | None | Unset = UNSET
    minio_cluster_capacity_usable_bytes: int | None | Unset = UNSET
    minio_cluster_usage_bytes: int | None | Unset = UNSET
    managed_buckets_usage_kb: int | None | Unset = UNSET
    managed_buckets_object_count: int | None | Unset = UNSET
    archived_by: int | None | Unset = UNSET
    managed_by_content_type: int | None | Unset = UNSET
    modified_by_user: int | None | Unset = UNSET
    created_by_user: int | None | Unset = UNSET
    credential: None | Unset | UUID = UNSET
    k8s_cluster: None | Unset | UUID = UNSET
    default_product: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.s3_cluster_deleted_by_user_type_0 import S3ClusterDeletedByUserType0  # noqa: PLC0415
        from ..models.s3_cluster_last_action_run_type_0 import S3ClusterLastActionRunType0  # noqa: PLC0415
        from ..models.workspace_simple import WorkspaceSimple  # noqa: PLC0415

        id = str(self.id)

        created = self.created.to_dict()

        organization = self.organization.to_dict()

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, WorkspaceSimple):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        url = self.url

        icon_url = self.icon_url

        is_class_icon = self.is_class_icon

        effective_slo_target: float | None
        effective_slo_target = self.effective_slo_target

        effective_sla_target: float | None
        effective_sla_target = self.effective_sla_target

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        last_action_run: dict[str, Any] | None
        if isinstance(self.last_action_run, S3ClusterLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        deleted_by_user: dict[str, Any] | None
        if isinstance(self.deleted_by_user, S3ClusterDeletedByUserType0):
            deleted_by_user = self.deleted_by_user.to_dict()
        else:
            deleted_by_user = self.deleted_by_user

        s3_buckets = []
        for s3_buckets_item_data in self.s3_buckets:
            s3_buckets_item = s3_buckets_item_data.to_dict()
            s3_buckets.append(s3_buckets_item)

        backend_total_capacity_bytes: int | None
        backend_total_capacity_bytes = self.backend_total_capacity_bytes

        backend_logical_used_bytes: int | None
        backend_logical_used_bytes = self.backend_logical_used_bytes

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        is_deleted = self.is_deleted

        state: str = self.state

        state_reason: None | str
        state_reason = self.state_reason

        last_state: str = self.last_state

        last_state_change: None | str
        if isinstance(self.last_state_change, datetime.datetime):
            last_state_change = self.last_state_change.isoformat()
        else:
            last_state_change = self.last_state_change

        reconciliation_running = self.reconciliation_running

        reconciliation_task_id: None | str
        reconciliation_task_id = self.reconciliation_task_id

        reconciliation_task_meta = self.reconciliation_task_meta

        last_reconciliation: None | str
        if isinstance(self.last_reconciliation, datetime.datetime):
            last_reconciliation = self.last_reconciliation.isoformat()
        else:
            last_reconciliation = self.last_reconciliation

        discovery_running = self.discovery_running

        discovery_task_id: None | str
        discovery_task_id = self.discovery_task_id

        discovery_task_meta = self.discovery_task_meta

        last_discovery: None | str
        if isinstance(self.last_discovery, datetime.datetime):
            last_discovery = self.last_discovery.isoformat()
        else:
            last_discovery = self.last_discovery

        repair_running = self.repair_running

        repair_task_id: None | str
        repair_task_id = self.repair_task_id

        repair_task_meta = self.repair_task_meta

        last_repair: None | str
        if isinstance(self.last_repair, datetime.datetime):
            last_repair = self.last_repair.isoformat()
        else:
            last_repair = self.last_repair

        conditions = self.conditions

        tolerations = self.tolerations

        endpoint = self.endpoint

        name = self.name

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        labels = self.labels

        annotations = self.annotations

        debug_mode = self.debug_mode

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        provider_reference: None | str | Unset
        if isinstance(self.provider_reference, Unset):
            provider_reference = UNSET
        else:
            provider_reference = self.provider_reference

        provider_id: None | str | Unset
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        reconciliation_enabled = self.reconciliation_enabled

        last_reconciliation_duration_seconds: float | None | Unset
        if isinstance(self.last_reconciliation_duration_seconds, Unset):
            last_reconciliation_duration_seconds = UNSET
        else:
            last_reconciliation_duration_seconds = self.last_reconciliation_duration_seconds

        discovery_enabled = self.discovery_enabled

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        archived = self.archived

        archived_at: None | str | Unset
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        archived_reason: None | str | Unset
        if isinstance(self.archived_reason, Unset):
            archived_reason = UNSET
        else:
            archived_reason = self.archived_reason

        created_by_component: None | str | Unset
        if isinstance(self.created_by_component, Unset):
            created_by_component = UNSET
        elif isinstance(self.created_by_component, str):
            created_by_component = self.created_by_component
        elif isinstance(self.created_by_component, str):
            created_by_component = self.created_by_component
        else:
            created_by_component = self.created_by_component

        target_availability: None | str | Unset
        if isinstance(self.target_availability, Unset):
            target_availability = UNSET
        else:
            target_availability = self.target_availability

        actual_availability = self.actual_availability

        slo_target: None | str | Unset
        if isinstance(self.slo_target, Unset):
            slo_target = UNSET
        else:
            slo_target = self.slo_target

        slo_window_days: int | None | Unset
        if isinstance(self.slo_window_days, Unset):
            slo_window_days = UNSET
        else:
            slo_window_days = self.slo_window_days

        slo_availability = self.slo_availability

        sla_target: None | str | Unset
        if isinstance(self.sla_target, Unset):
            sla_target = UNSET
        else:
            sla_target = self.sla_target

        sla_window_days: int | None | Unset
        if isinstance(self.sla_window_days, Unset):
            sla_window_days = UNSET
        else:
            sla_window_days = self.sla_window_days

        sla_availability = self.sla_availability

        criticality: None | str | Unset
        if isinstance(self.criticality, Unset):
            criticality = UNSET
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        else:
            criticality = self.criticality

        managed_by_object_id: None | str | Unset
        if isinstance(self.managed_by_object_id, Unset):
            managed_by_object_id = UNSET
        else:
            managed_by_object_id = self.managed_by_object_id

        platform_dns_record_created = self.platform_dns_record_created

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        endpoint_secure = self.endpoint_secure

        admin_endpoint: None | str | Unset
        if isinstance(self.admin_endpoint, Unset):
            admin_endpoint = UNSET
        else:
            admin_endpoint = self.admin_endpoint

        admin_endpoint_secure = self.admin_endpoint_secure

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        active = self.active

        platform_service = self.platform_service

        cluster_config = self.cluster_config

        cluster_info = self.cluster_info

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        allow_new_buckets = self.allow_new_buckets

        include_in_cost_statement = self.include_in_cost_statement

        ceph_osd_cluster_total_bytes: int | None | Unset
        if isinstance(self.ceph_osd_cluster_total_bytes, Unset):
            ceph_osd_cluster_total_bytes = UNSET
        else:
            ceph_osd_cluster_total_bytes = self.ceph_osd_cluster_total_bytes

        radosgw_buckets_logical_used_bytes: int | None | Unset
        if isinstance(self.radosgw_buckets_logical_used_bytes, Unset):
            radosgw_buckets_logical_used_bytes = UNSET
        else:
            radosgw_buckets_logical_used_bytes = self.radosgw_buckets_logical_used_bytes

        minio_cluster_capacity_usable_bytes: int | None | Unset
        if isinstance(self.minio_cluster_capacity_usable_bytes, Unset):
            minio_cluster_capacity_usable_bytes = UNSET
        else:
            minio_cluster_capacity_usable_bytes = self.minio_cluster_capacity_usable_bytes

        minio_cluster_usage_bytes: int | None | Unset
        if isinstance(self.minio_cluster_usage_bytes, Unset):
            minio_cluster_usage_bytes = UNSET
        else:
            minio_cluster_usage_bytes = self.minio_cluster_usage_bytes

        managed_buckets_usage_kb: int | None | Unset
        if isinstance(self.managed_buckets_usage_kb, Unset):
            managed_buckets_usage_kb = UNSET
        else:
            managed_buckets_usage_kb = self.managed_buckets_usage_kb

        managed_buckets_object_count: int | None | Unset
        if isinstance(self.managed_buckets_object_count, Unset):
            managed_buckets_object_count = UNSET
        else:
            managed_buckets_object_count = self.managed_buckets_object_count

        archived_by: int | None | Unset
        if isinstance(self.archived_by, Unset):
            archived_by = UNSET
        else:
            archived_by = self.archived_by

        managed_by_content_type: int | None | Unset
        if isinstance(self.managed_by_content_type, Unset):
            managed_by_content_type = UNSET
        else:
            managed_by_content_type = self.managed_by_content_type

        modified_by_user: int | None | Unset
        if isinstance(self.modified_by_user, Unset):
            modified_by_user = UNSET
        else:
            modified_by_user = self.modified_by_user

        created_by_user: int | None | Unset
        if isinstance(self.created_by_user, Unset):
            created_by_user = UNSET
        else:
            created_by_user = self.created_by_user

        credential: None | str | Unset
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, UUID):
            credential = str(self.credential)
        else:
            credential = self.credential

        k8s_cluster: None | str | Unset
        if isinstance(self.k8s_cluster, Unset):
            k8s_cluster = UNSET
        elif isinstance(self.k8s_cluster, UUID):
            k8s_cluster = str(self.k8s_cluster)
        else:
            k8s_cluster = self.k8s_cluster

        default_product: None | str | Unset
        if isinstance(self.default_product, Unset):
            default_product = UNSET
        elif isinstance(self.default_product, UUID):
            default_product = str(self.default_product)
        else:
            default_product = self.default_product

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "organization": organization,
                "workspace": workspace,
                "url": url,
                "icon_url": icon_url,
                "is_class_icon": is_class_icon,
                "effective_slo_target": effective_slo_target,
                "effective_sla_target": effective_sla_target,
                "effective_criticality": effective_criticality,
                "last_action_run": last_action_run,
                "deleted_by_user": deleted_by_user,
                "s3_buckets": s3_buckets,
                "backend_total_capacity_bytes": backend_total_capacity_bytes,
                "backend_logical_used_bytes": backend_logical_used_bytes,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
                "is_deleted": is_deleted,
                "state": state,
                "state_reason": state_reason,
                "last_state": last_state,
                "last_state_change": last_state_change,
                "reconciliation_running": reconciliation_running,
                "reconciliation_task_id": reconciliation_task_id,
                "reconciliation_task_meta": reconciliation_task_meta,
                "last_reconciliation": last_reconciliation,
                "discovery_running": discovery_running,
                "discovery_task_id": discovery_task_id,
                "discovery_task_meta": discovery_task_meta,
                "last_discovery": last_discovery,
                "repair_running": repair_running,
                "repair_task_id": repair_task_id,
                "repair_task_meta": repair_task_meta,
                "last_repair": last_repair,
                "conditions": conditions,
                "tolerations": tolerations,
                "endpoint": endpoint,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if debug_mode is not UNSET:
            field_dict["debug_mode"] = debug_mode
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_reference is not UNSET:
            field_dict["provider_reference"] = provider_reference
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if reconciliation_enabled is not UNSET:
            field_dict["reconciliation_enabled"] = reconciliation_enabled
        if last_reconciliation_duration_seconds is not UNSET:
            field_dict["last_reconciliation_duration_seconds"] = last_reconciliation_duration_seconds
        if discovery_enabled is not UNSET:
            field_dict["discovery_enabled"] = discovery_enabled
        if scope is not UNSET:
            field_dict["scope"] = scope
        if archived is not UNSET:
            field_dict["archived"] = archived
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if archived_reason is not UNSET:
            field_dict["archived_reason"] = archived_reason
        if created_by_component is not UNSET:
            field_dict["created_by_component"] = created_by_component
        if target_availability is not UNSET:
            field_dict["target_availability"] = target_availability
        if actual_availability is not UNSET:
            field_dict["actual_availability"] = actual_availability
        if slo_target is not UNSET:
            field_dict["slo_target"] = slo_target
        if slo_window_days is not UNSET:
            field_dict["slo_window_days"] = slo_window_days
        if slo_availability is not UNSET:
            field_dict["slo_availability"] = slo_availability
        if sla_target is not UNSET:
            field_dict["sla_target"] = sla_target
        if sla_window_days is not UNSET:
            field_dict["sla_window_days"] = sla_window_days
        if sla_availability is not UNSET:
            field_dict["sla_availability"] = sla_availability
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if managed_by_object_id is not UNSET:
            field_dict["managed_by_object_id"] = managed_by_object_id
        if platform_dns_record_created is not UNSET:
            field_dict["platform_dns_record_created"] = platform_dns_record_created
        if slug is not UNSET:
            field_dict["slug"] = slug
        if alias is not UNSET:
            field_dict["alias"] = alias
        if endpoint_secure is not UNSET:
            field_dict["endpoint_secure"] = endpoint_secure
        if admin_endpoint is not UNSET:
            field_dict["admin_endpoint"] = admin_endpoint
        if admin_endpoint_secure is not UNSET:
            field_dict["admin_endpoint_secure"] = admin_endpoint_secure
        if kind is not UNSET:
            field_dict["kind"] = kind
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if cluster_config is not UNSET:
            field_dict["cluster_config"] = cluster_config
        if cluster_info is not UNSET:
            field_dict["cluster_info"] = cluster_info
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if region is not UNSET:
            field_dict["region"] = region
        if allow_new_buckets is not UNSET:
            field_dict["allow_new_buckets"] = allow_new_buckets
        if include_in_cost_statement is not UNSET:
            field_dict["include_in_cost_statement"] = include_in_cost_statement
        if ceph_osd_cluster_total_bytes is not UNSET:
            field_dict["ceph_osd_cluster_total_bytes"] = ceph_osd_cluster_total_bytes
        if radosgw_buckets_logical_used_bytes is not UNSET:
            field_dict["radosgw_buckets_logical_used_bytes"] = radosgw_buckets_logical_used_bytes
        if minio_cluster_capacity_usable_bytes is not UNSET:
            field_dict["minio_cluster_capacity_usable_bytes"] = minio_cluster_capacity_usable_bytes
        if minio_cluster_usage_bytes is not UNSET:
            field_dict["minio_cluster_usage_bytes"] = minio_cluster_usage_bytes
        if managed_buckets_usage_kb is not UNSET:
            field_dict["managed_buckets_usage_kb"] = managed_buckets_usage_kb
        if managed_buckets_object_count is not UNSET:
            field_dict["managed_buckets_object_count"] = managed_buckets_object_count
        if archived_by is not UNSET:
            field_dict["archived_by"] = archived_by
        if managed_by_content_type is not UNSET:
            field_dict["managed_by_content_type"] = managed_by_content_type
        if modified_by_user is not UNSET:
            field_dict["modified_by_user"] = modified_by_user
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if credential is not UNSET:
            field_dict["credential"] = credential
        if k8s_cluster is not UNSET:
            field_dict["k8s_cluster"] = k8s_cluster
        if default_product is not UNSET:
            field_dict["default_product"] = default_product

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415
        from ..models.s3_bucket_list import S3BucketList  # noqa: PLC0415
        from ..models.s3_cluster_created import S3ClusterCreated  # noqa: PLC0415
        from ..models.s3_cluster_deleted_by_user_type_0 import S3ClusterDeletedByUserType0  # noqa: PLC0415
        from ..models.s3_cluster_last_action_run_type_0 import S3ClusterLastActionRunType0  # noqa: PLC0415
        from ..models.workspace_simple import WorkspaceSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created = S3ClusterCreated.from_dict(d.pop("created"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        def _parse_workspace(data: object) -> None | WorkspaceSimple:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_1 = WorkspaceSimple.from_dict(data)

                return workspace_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WorkspaceSimple, data)

        workspace = _parse_workspace(d.pop("workspace"))

        url = d.pop("url")

        icon_url = d.pop("icon_url")

        is_class_icon = d.pop("is_class_icon")

        def _parse_effective_slo_target(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        effective_slo_target = _parse_effective_slo_target(d.pop("effective_slo_target"))

        def _parse_effective_sla_target(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        effective_sla_target = _parse_effective_sla_target(d.pop("effective_sla_target"))

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

        def _parse_last_action_run(data: object) -> None | S3ClusterLastActionRunType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = S3ClusterLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | S3ClusterLastActionRunType0, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        def _parse_deleted_by_user(data: object) -> None | S3ClusterDeletedByUserType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = S3ClusterDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | S3ClusterDeletedByUserType0, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

        s3_buckets = []
        _s3_buckets = d.pop("s3_buckets")
        for s3_buckets_item_data in _s3_buckets:
            s3_buckets_item = S3BucketList.from_dict(s3_buckets_item_data)

            s3_buckets.append(s3_buckets_item)

        def _parse_backend_total_capacity_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        backend_total_capacity_bytes = _parse_backend_total_capacity_bytes(d.pop("backend_total_capacity_bytes"))

        def _parse_backend_logical_used_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        backend_logical_used_bytes = _parse_backend_logical_used_bytes(d.pop("backend_logical_used_bytes"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

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

        is_deleted = d.pop("is_deleted")

        state = check_last_state_enum(d.pop("state"))

        def _parse_state_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_reason = _parse_state_reason(d.pop("state_reason"))

        last_state = check_last_state_enum(d.pop("last_state"))

        def _parse_last_state_change(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_state_change_type_0 = datetime.datetime.fromisoformat(data)

                return last_state_change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_state_change = _parse_last_state_change(d.pop("last_state_change"))

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_reconciliation_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reconciliation_task_id = _parse_reconciliation_task_id(d.pop("reconciliation_task_id"))

        reconciliation_task_meta = d.pop("reconciliation_task_meta")

        def _parse_last_reconciliation(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_reconciliation_type_0 = datetime.datetime.fromisoformat(data)

                return last_reconciliation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_reconciliation = _parse_last_reconciliation(d.pop("last_reconciliation"))

        discovery_running = d.pop("discovery_running")

        def _parse_discovery_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        discovery_task_id = _parse_discovery_task_id(d.pop("discovery_task_id"))

        discovery_task_meta = d.pop("discovery_task_meta")

        def _parse_last_discovery(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_discovery_type_0 = datetime.datetime.fromisoformat(data)

                return last_discovery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_discovery = _parse_last_discovery(d.pop("last_discovery"))

        repair_running = d.pop("repair_running")

        def _parse_repair_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        repair_task_id = _parse_repair_task_id(d.pop("repair_task_id"))

        repair_task_meta = d.pop("repair_task_meta")

        def _parse_last_repair(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_repair_type_0 = datetime.datetime.fromisoformat(data)

                return last_repair_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_repair = _parse_last_repair(d.pop("last_repair"))

        conditions = d.pop("conditions")

        tolerations = d.pop("tolerations")

        endpoint = d.pop("endpoint")

        name = d.pop("name", UNSET)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        labels = d.pop("labels", UNSET)

        annotations = d.pop("annotations", UNSET)

        debug_mode = d.pop("debug_mode", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: ProviderEnum | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_provider_enum(_provider)

        def _parse_provider_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_reference = _parse_provider_reference(d.pop("provider_reference", UNSET))

        def _parse_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        reconciliation_enabled = d.pop("reconciliation_enabled", UNSET)

        def _parse_last_reconciliation_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        last_reconciliation_duration_seconds = _parse_last_reconciliation_duration_seconds(
            d.pop("last_reconciliation_duration_seconds", UNSET)
        )

        discovery_enabled = d.pop("discovery_enabled", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ScopeEnum | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_scope_enum(_scope)

        archived = d.pop("archived", UNSET)

        def _parse_archived_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = datetime.datetime.fromisoformat(data)

                return archived_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        archived_at = _parse_archived_at(d.pop("archived_at", UNSET))

        def _parse_archived_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        archived_reason = _parse_archived_reason(d.pop("archived_reason", UNSET))

        def _parse_created_by_component(data: object) -> BlankEnum | CreatedByComponentEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_0 = check_created_by_component_enum(data)

                return created_by_component_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_1 = check_blank_enum(data)

                return created_by_component_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | CreatedByComponentEnum | None | Unset, data)

        created_by_component = _parse_created_by_component(d.pop("created_by_component", UNSET))

        def _parse_target_availability(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_availability = _parse_target_availability(d.pop("target_availability", UNSET))

        actual_availability = d.pop("actual_availability", UNSET)

        def _parse_slo_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slo_target = _parse_slo_target(d.pop("slo_target", UNSET))

        def _parse_slo_window_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        slo_window_days = _parse_slo_window_days(d.pop("slo_window_days", UNSET))

        slo_availability = d.pop("slo_availability", UNSET)

        def _parse_sla_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sla_target = _parse_sla_target(d.pop("sla_target", UNSET))

        def _parse_sla_window_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sla_window_days = _parse_sla_window_days(d.pop("sla_window_days", UNSET))

        sla_availability = d.pop("sla_availability", UNSET)

        def _parse_criticality(data: object) -> BlankEnum | CriticalityEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_0 = check_criticality_enum(data)

                return criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = check_blank_enum(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | CriticalityEnum | None | Unset, data)

        criticality = _parse_criticality(d.pop("criticality", UNSET))

        def _parse_managed_by_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_by_object_id = _parse_managed_by_object_id(d.pop("managed_by_object_id", UNSET))

        platform_dns_record_created = d.pop("platform_dns_record_created", UNSET)

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        endpoint_secure = d.pop("endpoint_secure", UNSET)

        def _parse_admin_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_endpoint = _parse_admin_endpoint(d.pop("admin_endpoint", UNSET))

        admin_endpoint_secure = d.pop("admin_endpoint_secure", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: S3ClusterKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_s3_cluster_kind_enum(_kind)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        active = d.pop("active", UNSET)

        platform_service = d.pop("platform_service", UNSET)

        cluster_config = d.pop("cluster_config", UNSET)

        cluster_info = d.pop("cluster_info", UNSET)

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        allow_new_buckets = d.pop("allow_new_buckets", UNSET)

        include_in_cost_statement = d.pop("include_in_cost_statement", UNSET)

        def _parse_ceph_osd_cluster_total_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ceph_osd_cluster_total_bytes = _parse_ceph_osd_cluster_total_bytes(d.pop("ceph_osd_cluster_total_bytes", UNSET))

        def _parse_radosgw_buckets_logical_used_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        radosgw_buckets_logical_used_bytes = _parse_radosgw_buckets_logical_used_bytes(
            d.pop("radosgw_buckets_logical_used_bytes", UNSET)
        )

        def _parse_minio_cluster_capacity_usable_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        minio_cluster_capacity_usable_bytes = _parse_minio_cluster_capacity_usable_bytes(
            d.pop("minio_cluster_capacity_usable_bytes", UNSET)
        )

        def _parse_minio_cluster_usage_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        minio_cluster_usage_bytes = _parse_minio_cluster_usage_bytes(d.pop("minio_cluster_usage_bytes", UNSET))

        def _parse_managed_buckets_usage_kb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        managed_buckets_usage_kb = _parse_managed_buckets_usage_kb(d.pop("managed_buckets_usage_kb", UNSET))

        def _parse_managed_buckets_object_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        managed_buckets_object_count = _parse_managed_buckets_object_count(d.pop("managed_buckets_object_count", UNSET))

        def _parse_archived_by(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archived_by = _parse_archived_by(d.pop("archived_by", UNSET))

        def _parse_managed_by_content_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        managed_by_content_type = _parse_managed_by_content_type(d.pop("managed_by_content_type", UNSET))

        def _parse_modified_by_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        modified_by_user = _parse_modified_by_user(d.pop("modified_by_user", UNSET))

        def _parse_created_by_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        created_by_user = _parse_created_by_user(d.pop("created_by_user", UNSET))

        def _parse_credential(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credential_type_0 = UUID(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        credential = _parse_credential(d.pop("credential", UNSET))

        def _parse_k8s_cluster(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                k8s_cluster_type_0 = UUID(data)

                return k8s_cluster_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        k8s_cluster = _parse_k8s_cluster(d.pop("k8s_cluster", UNSET))

        def _parse_default_product(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_product_type_0 = UUID(data)

                return default_product_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_product = _parse_default_product(d.pop("default_product", UNSET))

        s3_cluster = cls(
            id=id,
            created=created,
            organization=organization,
            workspace=workspace,
            url=url,
            icon_url=icon_url,
            is_class_icon=is_class_icon,
            effective_slo_target=effective_slo_target,
            effective_sla_target=effective_sla_target,
            effective_criticality=effective_criticality,
            last_action_run=last_action_run,
            deleted_by_user=deleted_by_user,
            s3_buckets=s3_buckets,
            backend_total_capacity_bytes=backend_total_capacity_bytes,
            backend_logical_used_bytes=backend_logical_used_bytes,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            is_deleted=is_deleted,
            state=state,
            state_reason=state_reason,
            last_state=last_state,
            last_state_change=last_state_change,
            reconciliation_running=reconciliation_running,
            reconciliation_task_id=reconciliation_task_id,
            reconciliation_task_meta=reconciliation_task_meta,
            last_reconciliation=last_reconciliation,
            discovery_running=discovery_running,
            discovery_task_id=discovery_task_id,
            discovery_task_meta=discovery_task_meta,
            last_discovery=last_discovery,
            repair_running=repair_running,
            repair_task_id=repair_task_id,
            repair_task_meta=repair_task_meta,
            last_repair=last_repair,
            conditions=conditions,
            tolerations=tolerations,
            endpoint=endpoint,
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            provider_id=provider_id,
            reconciliation_enabled=reconciliation_enabled,
            last_reconciliation_duration_seconds=last_reconciliation_duration_seconds,
            discovery_enabled=discovery_enabled,
            scope=scope,
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            created_by_component=created_by_component,
            target_availability=target_availability,
            actual_availability=actual_availability,
            slo_target=slo_target,
            slo_window_days=slo_window_days,
            slo_availability=slo_availability,
            sla_target=sla_target,
            sla_window_days=sla_window_days,
            sla_availability=sla_availability,
            criticality=criticality,
            managed_by_object_id=managed_by_object_id,
            platform_dns_record_created=platform_dns_record_created,
            slug=slug,
            alias=alias,
            endpoint_secure=endpoint_secure,
            admin_endpoint=admin_endpoint,
            admin_endpoint_secure=admin_endpoint_secure,
            kind=kind,
            description=description,
            active=active,
            platform_service=platform_service,
            cluster_config=cluster_config,
            cluster_info=cluster_info,
            namespace=namespace,
            region=region,
            allow_new_buckets=allow_new_buckets,
            include_in_cost_statement=include_in_cost_statement,
            ceph_osd_cluster_total_bytes=ceph_osd_cluster_total_bytes,
            radosgw_buckets_logical_used_bytes=radosgw_buckets_logical_used_bytes,
            minio_cluster_capacity_usable_bytes=minio_cluster_capacity_usable_bytes,
            minio_cluster_usage_bytes=minio_cluster_usage_bytes,
            managed_buckets_usage_kb=managed_buckets_usage_kb,
            managed_buckets_object_count=managed_buckets_object_count,
            archived_by=archived_by,
            managed_by_content_type=managed_by_content_type,
            modified_by_user=modified_by_user,
            created_by_user=created_by_user,
            credential=credential,
            k8s_cluster=k8s_cluster,
            default_product=default_product,
        )

        s3_cluster.additional_properties = d
        return s3_cluster

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
