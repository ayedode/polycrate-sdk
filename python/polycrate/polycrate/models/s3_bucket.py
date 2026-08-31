from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.delegation_source_enum import DelegationSourceEnum, check_delegation_source_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.generic_object_kind_enum import GenericObjectKindEnum, check_generic_object_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..models.versioning_status_enum import VersioningStatusEnum, check_versioning_status_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_simple import OrganizationSimple
    from ..models.product_simple import ProductSimple
    from ..models.region_simple import RegionSimple
    from ..models.s3_bucket_created import S3BucketCreated
    from ..models.s3_bucket_deleted_by_user_type_0 import S3BucketDeletedByUserType0
    from ..models.s3_bucket_last_action_run_type_0 import S3BucketLastActionRunType0
    from ..models.s3_bucket_organization_type_0 import S3BucketOrganizationType0
    from ..models.s3_bucket_workspace_type_0 import S3BucketWorkspaceType0
    from ..models.s3_credential import S3Credential
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="S3Bucket")


@_attrs_define
class S3Bucket:
    """S3Bucket detail serializer — erbt von ManagedObjectDetailSerializer
    für icon_url, url, effective_slo/sla_target im Dashboard.

        Attributes:
            id (UUID):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            deleted_by_user (None | S3BucketDeletedByUserType0):
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
            discovery_enabled (bool):
            discovery_running (bool):
            discovery_task_id (None | str):
            discovery_task_meta (Any): Task metadata for discovery progress tracking
            last_discovery (datetime.datetime | None):
            repair_running (bool):
            repair_task_id (None | str):
            repair_task_meta (Any): Task metadata for repair progress tracking
            last_repair (datetime.datetime | None):
            scope (ScopeEnum): * `system` - System
                * `user` - User
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            effective_criticality (EffectiveCriticalityEnum | None):
            actual_availability (str): Calculated actual availability as yearly average in %
            organization (None | S3BucketOrganizationType0):
            workspace (None | S3BucketWorkspaceType0):
            created (S3BucketCreated):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            last_action_run (None | S3BucketLastActionRunType0): Gibt den letzten ActionRun für das Objekt zurück (für
                Dashboard Footer).

                Unterstützte Relationen:
                - Direkter action_runs Manager (Workspace, Block, Organization)
                - Workspace-FK-Fallback, nur wenn show_last_action_run=True (K8sCluster, K8sApp)

                Spec: polycrate spec inspect 271
            region (RegionSimple):
            s3_endpoint (None | str):
            s3_region (None | str):
            user_id (None | str):
            credential (S3Credential): S3 Access Key metadata — no secrets.

                Additional access keys (type=additional) are only supported for rook-ceph
                (RadosGW) clusters. MinIO clusters do not support sub-user management;
                the credentials/create endpoint returns 400 for MinIO buckets.

                The `active` field is inherited from ManagedObject and has no semantic
                meaning for S3 access keys — do not use it to display key status.

                Spec 629: `principal_arn` is a computed Ceph/RGW IAM principal for bucket
                policies (no tenant). Consumers assemble policies themselves.
            current_usage (int): Size in KB
            current_usage_bytes (int | None):
            current_object_count (int):
            access_keys (list[S3Credential]):
            product (ProductSimple): Compact serializer for embedding Product as FK reference.
            computed_cost (float):
            provider_metadata (Any): Full metadata from provider Admin API (versioning, quota, encryption, etc.), updated
                during reconciliation
            versioning_status (None | VersioningStatusEnum):
            encryption_enabled (bool | None):
            additional_access_keys_supported (bool):
            presigned_upload_supported (bool):
            max_upload_bytes (int):
            delegated_organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            delegated_workspace (WorkspaceSimple):
            loopback_resource_id (None | str): Loopback API entity id (v3 object-store id).
            delegation_source (DelegationSourceEnum | None): Source of the delegation mapping.

                * `loopback_lb` - Loopback Load Balancer
                * `loopback_object_store` - Loopback Object Store
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
            platform_service (bool | Unset):
            kind (GenericObjectKindEnum | Unset): * `generic` - Generic
            tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
                the condition will not be applied.
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            criticality (BlankEnum | CriticalityEnum | None | Unset): Criticality level. Null = inherit from workspace, then
                org. Explicit value overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            target_availability (None | str | Unset): Target availability in % (overrides SystemConfig default). Null = use
                SystemConfig DEFAULT_TARGET_AVAILABILITY.
            slo_target (None | str | Unset): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
            slo_availability (str | Unset): Calculated SLO availability in % (updated in reconcile)
            sla_target (None | str | Unset): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
            sla_availability (str | Unset): Calculated SLA availability in % (updated in reconcile)
            include_in_cost_statement (bool | Unset): When False, this bucket is omitted from CostStatement generation even
                if the cluster is included. Cluster-level False still excludes the bucket.
            cors_allow_all (bool | Unset): Apply a permissive CORS configuration to this bucket. Only effective for Ceph
                clusters.
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    deleted_by_user: None | S3BucketDeletedByUserType0
    state: LastStateEnum
    state_reason: None | str
    last_state: LastStateEnum
    last_state_change: datetime.datetime | None
    reconciliation_running: bool
    reconciliation_task_id: None | str
    reconciliation_task_meta: Any
    last_reconciliation: datetime.datetime | None
    discovery_enabled: bool
    discovery_running: bool
    discovery_task_id: None | str
    discovery_task_meta: Any
    last_discovery: datetime.datetime | None
    repair_running: bool
    repair_task_id: None | str
    repair_task_meta: Any
    last_repair: datetime.datetime | None
    scope: ScopeEnum
    conditions: Any
    effective_criticality: EffectiveCriticalityEnum | None
    actual_availability: str
    organization: None | S3BucketOrganizationType0
    workspace: None | S3BucketWorkspaceType0
    created: S3BucketCreated
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    last_action_run: None | S3BucketLastActionRunType0
    region: RegionSimple
    s3_endpoint: None | str
    s3_region: None | str
    user_id: None | str
    credential: S3Credential
    current_usage: int
    current_usage_bytes: int | None
    current_object_count: int
    access_keys: list[S3Credential]
    product: ProductSimple
    computed_cost: float
    provider_metadata: Any
    versioning_status: None | VersioningStatusEnum
    encryption_enabled: bool | None
    additional_access_keys_supported: bool
    presigned_upload_supported: bool
    max_upload_bytes: int
    delegated_organization: OrganizationSimple
    delegated_workspace: WorkspaceSimple
    loopback_resource_id: None | str
    delegation_source: DelegationSourceEnum | None
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: GenericObjectKindEnum | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    criticality: BlankEnum | CriticalityEnum | None | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_availability: str | Unset = UNSET
    include_in_cost_statement: bool | Unset = UNSET
    cors_allow_all: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.s3_bucket_deleted_by_user_type_0 import S3BucketDeletedByUserType0
        from ..models.s3_bucket_last_action_run_type_0 import S3BucketLastActionRunType0
        from ..models.s3_bucket_organization_type_0 import S3BucketOrganizationType0
        from ..models.s3_bucket_workspace_type_0 import S3BucketWorkspaceType0

        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        is_deleted = self.is_deleted

        deleted_by_user: dict[str, Any] | None
        if isinstance(self.deleted_by_user, S3BucketDeletedByUserType0):
            deleted_by_user = self.deleted_by_user.to_dict()
        else:
            deleted_by_user = self.deleted_by_user

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

        discovery_enabled = self.discovery_enabled

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

        scope: str = self.scope

        conditions = self.conditions

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        actual_availability = self.actual_availability

        organization: dict[str, Any] | None
        if isinstance(self.organization, S3BucketOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, S3BucketWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        url = self.url

        icon_url = self.icon_url

        is_class_icon = self.is_class_icon

        effective_slo_target: float | None
        effective_slo_target = self.effective_slo_target

        effective_sla_target: float | None
        effective_sla_target = self.effective_sla_target

        last_action_run: dict[str, Any] | None
        if isinstance(self.last_action_run, S3BucketLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        region = self.region.to_dict()

        s3_endpoint: None | str
        s3_endpoint = self.s3_endpoint

        s3_region: None | str
        s3_region = self.s3_region

        user_id: None | str
        user_id = self.user_id

        credential = self.credential.to_dict()

        current_usage = self.current_usage

        current_usage_bytes: int | None
        current_usage_bytes = self.current_usage_bytes

        current_object_count = self.current_object_count

        access_keys = []
        for access_keys_item_data in self.access_keys:
            access_keys_item = access_keys_item_data.to_dict()
            access_keys.append(access_keys_item)

        product = self.product.to_dict()

        computed_cost = self.computed_cost

        provider_metadata = self.provider_metadata

        versioning_status: None | str
        if isinstance(self.versioning_status, str):
            versioning_status = self.versioning_status
        else:
            versioning_status = self.versioning_status

        encryption_enabled: bool | None
        encryption_enabled = self.encryption_enabled

        additional_access_keys_supported = self.additional_access_keys_supported

        presigned_upload_supported = self.presigned_upload_supported

        max_upload_bytes = self.max_upload_bytes

        delegated_organization = self.delegated_organization.to_dict()

        delegated_workspace = self.delegated_workspace.to_dict()

        loopback_resource_id: None | str
        loopback_resource_id = self.loopback_resource_id

        delegation_source: None | str
        if isinstance(self.delegation_source, str):
            delegation_source = self.delegation_source
        else:
            delegation_source = self.delegation_source

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

        platform_service = self.platform_service

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        tolerations = self.tolerations

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

        criticality: None | str | Unset
        if isinstance(self.criticality, Unset):
            criticality = UNSET
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        else:
            criticality = self.criticality

        target_availability: None | str | Unset
        if isinstance(self.target_availability, Unset):
            target_availability = UNSET
        else:
            target_availability = self.target_availability

        slo_target: None | str | Unset
        if isinstance(self.slo_target, Unset):
            slo_target = UNSET
        else:
            slo_target = self.slo_target

        slo_availability = self.slo_availability

        sla_target: None | str | Unset
        if isinstance(self.sla_target, Unset):
            sla_target = UNSET
        else:
            sla_target = self.sla_target

        sla_availability = self.sla_availability

        include_in_cost_statement = self.include_in_cost_statement

        cors_allow_all = self.cors_allow_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
                "is_deleted": is_deleted,
                "deleted_by_user": deleted_by_user,
                "state": state,
                "state_reason": state_reason,
                "last_state": last_state,
                "last_state_change": last_state_change,
                "reconciliation_running": reconciliation_running,
                "reconciliation_task_id": reconciliation_task_id,
                "reconciliation_task_meta": reconciliation_task_meta,
                "last_reconciliation": last_reconciliation,
                "discovery_enabled": discovery_enabled,
                "discovery_running": discovery_running,
                "discovery_task_id": discovery_task_id,
                "discovery_task_meta": discovery_task_meta,
                "last_discovery": last_discovery,
                "repair_running": repair_running,
                "repair_task_id": repair_task_id,
                "repair_task_meta": repair_task_meta,
                "last_repair": last_repair,
                "scope": scope,
                "conditions": conditions,
                "effective_criticality": effective_criticality,
                "actual_availability": actual_availability,
                "organization": organization,
                "workspace": workspace,
                "created": created,
                "url": url,
                "icon_url": icon_url,
                "is_class_icon": is_class_icon,
                "effective_slo_target": effective_slo_target,
                "effective_sla_target": effective_sla_target,
                "last_action_run": last_action_run,
                "region": region,
                "s3_endpoint": s3_endpoint,
                "s3_region": s3_region,
                "user_id": user_id,
                "credential": credential,
                "current_usage": current_usage,
                "current_usage_bytes": current_usage_bytes,
                "current_object_count": current_object_count,
                "access_keys": access_keys,
                "product": product,
                "computed_cost": computed_cost,
                "provider_metadata": provider_metadata,
                "versioning_status": versioning_status,
                "encryption_enabled": encryption_enabled,
                "additional_access_keys_supported": additional_access_keys_supported,
                "presigned_upload_supported": presigned_upload_supported,
                "max_upload_bytes": max_upload_bytes,
                "delegated_organization": delegated_organization,
                "delegated_workspace": delegated_workspace,
                "loopback_resource_id": loopback_resource_id,
                "delegation_source": delegation_source,
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
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if kind is not UNSET:
            field_dict["kind"] = kind
        if tolerations is not UNSET:
            field_dict["tolerations"] = tolerations
        if archived is not UNSET:
            field_dict["archived"] = archived
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if archived_reason is not UNSET:
            field_dict["archived_reason"] = archived_reason
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if target_availability is not UNSET:
            field_dict["target_availability"] = target_availability
        if slo_target is not UNSET:
            field_dict["slo_target"] = slo_target
        if slo_availability is not UNSET:
            field_dict["slo_availability"] = slo_availability
        if sla_target is not UNSET:
            field_dict["sla_target"] = sla_target
        if sla_availability is not UNSET:
            field_dict["sla_availability"] = sla_availability
        if include_in_cost_statement is not UNSET:
            field_dict["include_in_cost_statement"] = include_in_cost_statement
        if cors_allow_all is not UNSET:
            field_dict["cors_allow_all"] = cors_allow_all

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_simple import OrganizationSimple
        from ..models.product_simple import ProductSimple
        from ..models.region_simple import RegionSimple
        from ..models.s3_bucket_created import S3BucketCreated
        from ..models.s3_bucket_deleted_by_user_type_0 import S3BucketDeletedByUserType0
        from ..models.s3_bucket_last_action_run_type_0 import S3BucketLastActionRunType0
        from ..models.s3_bucket_organization_type_0 import S3BucketOrganizationType0
        from ..models.s3_bucket_workspace_type_0 import S3BucketWorkspaceType0
        from ..models.s3_credential import S3Credential
        from ..models.workspace_simple import WorkspaceSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

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

        def _parse_deleted_by_user(data: object) -> None | S3BucketDeletedByUserType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = S3BucketDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | S3BucketDeletedByUserType0, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

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

        discovery_enabled = d.pop("discovery_enabled")

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

        scope = check_scope_enum(d.pop("scope"))

        conditions = d.pop("conditions")

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

        actual_availability = d.pop("actual_availability")

        def _parse_organization(data: object) -> None | S3BucketOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = S3BucketOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | S3BucketOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_workspace(data: object) -> None | S3BucketWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = S3BucketWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | S3BucketWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = S3BucketCreated.from_dict(d.pop("created"))

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

        def _parse_last_action_run(data: object) -> None | S3BucketLastActionRunType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = S3BucketLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | S3BucketLastActionRunType0, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        region = RegionSimple.from_dict(d.pop("region"))

        def _parse_s3_endpoint(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        s3_endpoint = _parse_s3_endpoint(d.pop("s3_endpoint"))

        def _parse_s3_region(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        s3_region = _parse_s3_region(d.pop("s3_region"))

        def _parse_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_id = _parse_user_id(d.pop("user_id"))

        credential = S3Credential.from_dict(d.pop("credential"))

        current_usage = d.pop("current_usage")

        def _parse_current_usage_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        current_usage_bytes = _parse_current_usage_bytes(d.pop("current_usage_bytes"))

        current_object_count = d.pop("current_object_count")

        access_keys = []
        _access_keys = d.pop("access_keys")
        for access_keys_item_data in _access_keys:
            access_keys_item = S3Credential.from_dict(access_keys_item_data)

            access_keys.append(access_keys_item)

        product = ProductSimple.from_dict(d.pop("product"))

        computed_cost = d.pop("computed_cost")

        provider_metadata = d.pop("provider_metadata")

        def _parse_versioning_status(data: object) -> None | VersioningStatusEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                versioning_status_type_1 = check_versioning_status_enum(data)

                return versioning_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | VersioningStatusEnum, data)

        versioning_status = _parse_versioning_status(d.pop("versioning_status"))

        def _parse_encryption_enabled(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        encryption_enabled = _parse_encryption_enabled(d.pop("encryption_enabled"))

        additional_access_keys_supported = d.pop("additional_access_keys_supported")

        presigned_upload_supported = d.pop("presigned_upload_supported")

        max_upload_bytes = d.pop("max_upload_bytes")

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

        platform_service = d.pop("platform_service", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: GenericObjectKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_generic_object_kind_enum(_kind)

        tolerations = d.pop("tolerations", UNSET)

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

        def _parse_target_availability(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_availability = _parse_target_availability(d.pop("target_availability", UNSET))

        def _parse_slo_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slo_target = _parse_slo_target(d.pop("slo_target", UNSET))

        slo_availability = d.pop("slo_availability", UNSET)

        def _parse_sla_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sla_target = _parse_sla_target(d.pop("sla_target", UNSET))

        sla_availability = d.pop("sla_availability", UNSET)

        include_in_cost_statement = d.pop("include_in_cost_statement", UNSET)

        cors_allow_all = d.pop("cors_allow_all", UNSET)

        s3_bucket = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            is_deleted=is_deleted,
            deleted_by_user=deleted_by_user,
            state=state,
            state_reason=state_reason,
            last_state=last_state,
            last_state_change=last_state_change,
            reconciliation_running=reconciliation_running,
            reconciliation_task_id=reconciliation_task_id,
            reconciliation_task_meta=reconciliation_task_meta,
            last_reconciliation=last_reconciliation,
            discovery_enabled=discovery_enabled,
            discovery_running=discovery_running,
            discovery_task_id=discovery_task_id,
            discovery_task_meta=discovery_task_meta,
            last_discovery=last_discovery,
            repair_running=repair_running,
            repair_task_id=repair_task_id,
            repair_task_meta=repair_task_meta,
            last_repair=last_repair,
            scope=scope,
            conditions=conditions,
            effective_criticality=effective_criticality,
            actual_availability=actual_availability,
            organization=organization,
            workspace=workspace,
            created=created,
            url=url,
            icon_url=icon_url,
            is_class_icon=is_class_icon,
            effective_slo_target=effective_slo_target,
            effective_sla_target=effective_sla_target,
            last_action_run=last_action_run,
            region=region,
            s3_endpoint=s3_endpoint,
            s3_region=s3_region,
            user_id=user_id,
            credential=credential,
            current_usage=current_usage,
            current_usage_bytes=current_usage_bytes,
            current_object_count=current_object_count,
            access_keys=access_keys,
            product=product,
            computed_cost=computed_cost,
            provider_metadata=provider_metadata,
            versioning_status=versioning_status,
            encryption_enabled=encryption_enabled,
            additional_access_keys_supported=additional_access_keys_supported,
            presigned_upload_supported=presigned_upload_supported,
            max_upload_bytes=max_upload_bytes,
            delegated_organization=delegated_organization,
            delegated_workspace=delegated_workspace,
            loopback_resource_id=loopback_resource_id,
            delegation_source=delegation_source,
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            provider_id=provider_id,
            reconciliation_enabled=reconciliation_enabled,
            platform_service=platform_service,
            kind=kind,
            tolerations=tolerations,
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            criticality=criticality,
            target_availability=target_availability,
            slo_target=slo_target,
            slo_availability=slo_availability,
            sla_target=sla_target,
            sla_availability=sla_availability,
            include_in_cost_statement=include_in_cost_statement,
            cors_allow_all=cors_allow_all,
        )

        s3_bucket.additional_properties = d
        return s3_bucket

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
