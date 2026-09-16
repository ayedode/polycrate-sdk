from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.block_rollout_item_status_enum import BlockRolloutItemStatusEnum, check_block_rollout_item_status_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.generic_object_kind_enum import GenericObjectKindEnum, check_generic_object_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..models.source_98d_enum import Source98DEnum, check_source_98d_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_rollout_item_created import BlockRolloutItemCreated
    from ..models.block_rollout_item_deleted_by_user_type_0 import BlockRolloutItemDeletedByUserType0
    from ..models.block_rollout_item_last_action_run_type_0 import BlockRolloutItemLastActionRunType0
    from ..models.block_rollout_item_organization_type_0 import BlockRolloutItemOrganizationType0
    from ..models.block_rollout_item_workspace_type_0 import BlockRolloutItemWorkspaceType0


T = TypeVar("T", bound="BlockRolloutItem")


@_attrs_define
class BlockRolloutItem:
    """Basis-Serializer für alle ManagedObject Detail-Endpoints.

    Enthält alle generischen Felder eines ManagedObjects.
    Subclasses erweitern diese Liste mit model-spezifischen Feldern.

    Inkludiert:
    - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
    - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
    - organization/workspace als generische ManagedObject-Referenzen (mit URL)
    - created: Kombifeld (created_at, created_at_humanized, created_by)
    - url: Absolute URL zum Object (via get_absolute_url())

    Usage:
        class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
            class Meta(ManagedObjectDetailSerializer.Meta):
                model = K8sCluster
                fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']

        Attributes:
            id (UUID):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            deleted_by_user (BlockRolloutItemDeletedByUserType0 | None):
            last_reconciliation (datetime.datetime | None):
            last_discovery (datetime.datetime | None):
            last_repair (datetime.datetime | None):
            effective_criticality (EffectiveCriticalityEnum | None):
            organization (BlockRolloutItemOrganizationType0 | None):
            workspace (BlockRolloutItemWorkspaceType0 | None):
            created (BlockRolloutItemCreated):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            last_action_run (BlockRolloutItemLastActionRunType0 | None):
            block (UUID):
            block_name (str):
            action_name (str):
            dispatched_at (datetime.datetime | None):
            completed_at (datetime.datetime | None):
            retry_count (int):
            retry_after (datetime.datetime | None):
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
            state (LastStateEnum | Unset): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            state_reason (None | str | Unset):
            last_state (LastStateEnum | Unset): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            last_state_change (datetime.datetime | None | Unset):
            reconciliation_enabled (bool | Unset):
            reconciliation_running (bool | Unset):
            reconciliation_task_id (None | str | Unset):
            reconciliation_task_meta (Any | Unset): Task metadata for reconciliation progress tracking (e.g., step,
                progress, started_at)
            discovery_enabled (bool | Unset):
            discovery_running (bool | Unset):
            discovery_task_id (None | str | Unset):
            discovery_task_meta (Any | Unset): Task metadata for discovery progress tracking
            repair_running (bool | Unset):
            platform_service (bool | Unset):
            repair_task_id (None | str | Unset):
            repair_task_meta (Any | Unset): Task metadata for repair progress tracking
            scope (ScopeEnum | Unset): * `system` - System
                * `user` - User
            kind (GenericObjectKindEnum | Unset): * `generic` - Generic
            conditions (Any | Unset): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
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
            actual_availability (str | Unset): Calculated actual availability as yearly average in %
            slo_target (None | str | Unset): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
            slo_availability (str | Unset): Calculated SLO availability in % (updated in reconcile)
            sla_target (None | str | Unset): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
            sla_availability (str | Unset): Calculated SLA availability in % (updated in reconcile)
            status (BlockRolloutItemStatusEnum | Unset): * `pending` - Pending
                * `in_progress` - In Progress
                * `completed` - Completed
                * `failed` - Failed
                * `retrying` - Retrying
                * `skipped` - Skipped
            source (Source98DEnum | Unset): * `scheduler` - Scheduler
                * `manual` - Manual
            source_user (int | None | Unset):
            rollout (None | Unset | UUID):
            action_run (None | Unset | UUID):
            reason (None | str | Unset):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    deleted_by_user: BlockRolloutItemDeletedByUserType0 | None
    last_reconciliation: datetime.datetime | None
    last_discovery: datetime.datetime | None
    last_repair: datetime.datetime | None
    effective_criticality: EffectiveCriticalityEnum | None
    organization: BlockRolloutItemOrganizationType0 | None
    workspace: BlockRolloutItemWorkspaceType0 | None
    created: BlockRolloutItemCreated
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    last_action_run: BlockRolloutItemLastActionRunType0 | None
    block: UUID
    block_name: str
    action_name: str
    dispatched_at: datetime.datetime | None
    completed_at: datetime.datetime | None
    retry_count: int
    retry_after: datetime.datetime | None
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    state: LastStateEnum | Unset = UNSET
    state_reason: None | str | Unset = UNSET
    last_state: LastStateEnum | Unset = UNSET
    last_state_change: datetime.datetime | None | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    reconciliation_running: bool | Unset = UNSET
    reconciliation_task_id: None | str | Unset = UNSET
    reconciliation_task_meta: Any | Unset = UNSET
    discovery_enabled: bool | Unset = UNSET
    discovery_running: bool | Unset = UNSET
    discovery_task_id: None | str | Unset = UNSET
    discovery_task_meta: Any | Unset = UNSET
    repair_running: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    repair_task_id: None | str | Unset = UNSET
    repair_task_meta: Any | Unset = UNSET
    scope: ScopeEnum | Unset = UNSET
    kind: GenericObjectKindEnum | Unset = UNSET
    conditions: Any | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    criticality: BlankEnum | CriticalityEnum | None | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    actual_availability: str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_availability: str | Unset = UNSET
    status: BlockRolloutItemStatusEnum | Unset = UNSET
    source: Source98DEnum | Unset = UNSET
    source_user: int | None | Unset = UNSET
    rollout: None | Unset | UUID = UNSET
    action_run: None | Unset | UUID = UNSET
    reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.block_rollout_item_deleted_by_user_type_0 import (
            BlockRolloutItemDeletedByUserType0,  # noqa: PLC0415
        )
        from ..models.block_rollout_item_last_action_run_type_0 import (
            BlockRolloutItemLastActionRunType0,  # noqa: PLC0415
        )
        from ..models.block_rollout_item_organization_type_0 import BlockRolloutItemOrganizationType0  # noqa: PLC0415
        from ..models.block_rollout_item_workspace_type_0 import BlockRolloutItemWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.deleted_by_user, BlockRolloutItemDeletedByUserType0):
            deleted_by_user = self.deleted_by_user.to_dict()
        else:
            deleted_by_user = self.deleted_by_user

        last_reconciliation: None | str
        if isinstance(self.last_reconciliation, datetime.datetime):
            last_reconciliation = self.last_reconciliation.isoformat()
        else:
            last_reconciliation = self.last_reconciliation

        last_discovery: None | str
        if isinstance(self.last_discovery, datetime.datetime):
            last_discovery = self.last_discovery.isoformat()
        else:
            last_discovery = self.last_discovery

        last_repair: None | str
        if isinstance(self.last_repair, datetime.datetime):
            last_repair = self.last_repair.isoformat()
        else:
            last_repair = self.last_repair

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        organization: dict[str, Any] | None
        if isinstance(self.organization, BlockRolloutItemOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, BlockRolloutItemWorkspaceType0):
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
        if isinstance(self.last_action_run, BlockRolloutItemLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        block = str(self.block)

        block_name = self.block_name

        action_name = self.action_name

        dispatched_at: None | str
        if isinstance(self.dispatched_at, datetime.datetime):
            dispatched_at = self.dispatched_at.isoformat()
        else:
            dispatched_at = self.dispatched_at

        completed_at: None | str
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        retry_count = self.retry_count

        retry_after: None | str
        if isinstance(self.retry_after, datetime.datetime):
            retry_after = self.retry_after.isoformat()
        else:
            retry_after = self.retry_after

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

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        state_reason: None | str | Unset
        if isinstance(self.state_reason, Unset):
            state_reason = UNSET
        else:
            state_reason = self.state_reason

        last_state: str | Unset = UNSET
        if not isinstance(self.last_state, Unset):
            last_state = self.last_state

        last_state_change: None | str | Unset
        if isinstance(self.last_state_change, Unset):
            last_state_change = UNSET
        elif isinstance(self.last_state_change, datetime.datetime):
            last_state_change = self.last_state_change.isoformat()
        else:
            last_state_change = self.last_state_change

        reconciliation_enabled = self.reconciliation_enabled

        reconciliation_running = self.reconciliation_running

        reconciliation_task_id: None | str | Unset
        if isinstance(self.reconciliation_task_id, Unset):
            reconciliation_task_id = UNSET
        else:
            reconciliation_task_id = self.reconciliation_task_id

        reconciliation_task_meta = self.reconciliation_task_meta

        discovery_enabled = self.discovery_enabled

        discovery_running = self.discovery_running

        discovery_task_id: None | str | Unset
        if isinstance(self.discovery_task_id, Unset):
            discovery_task_id = UNSET
        else:
            discovery_task_id = self.discovery_task_id

        discovery_task_meta = self.discovery_task_meta

        repair_running = self.repair_running

        platform_service = self.platform_service

        repair_task_id: None | str | Unset
        if isinstance(self.repair_task_id, Unset):
            repair_task_id = UNSET
        else:
            repair_task_id = self.repair_task_id

        repair_task_meta = self.repair_task_meta

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        conditions = self.conditions

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

        actual_availability = self.actual_availability

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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        source_user: int | None | Unset
        if isinstance(self.source_user, Unset):
            source_user = UNSET
        else:
            source_user = self.source_user

        rollout: None | str | Unset
        if isinstance(self.rollout, Unset):
            rollout = UNSET
        elif isinstance(self.rollout, UUID):
            rollout = str(self.rollout)
        else:
            rollout = self.rollout

        action_run: None | str | Unset
        if isinstance(self.action_run, Unset):
            action_run = UNSET
        elif isinstance(self.action_run, UUID):
            action_run = str(self.action_run)
        else:
            action_run = self.action_run

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

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
                "last_reconciliation": last_reconciliation,
                "last_discovery": last_discovery,
                "last_repair": last_repair,
                "effective_criticality": effective_criticality,
                "organization": organization,
                "workspace": workspace,
                "created": created,
                "url": url,
                "icon_url": icon_url,
                "is_class_icon": is_class_icon,
                "effective_slo_target": effective_slo_target,
                "effective_sla_target": effective_sla_target,
                "last_action_run": last_action_run,
                "block": block,
                "block_name": block_name,
                "action_name": action_name,
                "dispatched_at": dispatched_at,
                "completed_at": completed_at,
                "retry_count": retry_count,
                "retry_after": retry_after,
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
        if state is not UNSET:
            field_dict["state"] = state
        if state_reason is not UNSET:
            field_dict["state_reason"] = state_reason
        if last_state is not UNSET:
            field_dict["last_state"] = last_state
        if last_state_change is not UNSET:
            field_dict["last_state_change"] = last_state_change
        if reconciliation_enabled is not UNSET:
            field_dict["reconciliation_enabled"] = reconciliation_enabled
        if reconciliation_running is not UNSET:
            field_dict["reconciliation_running"] = reconciliation_running
        if reconciliation_task_id is not UNSET:
            field_dict["reconciliation_task_id"] = reconciliation_task_id
        if reconciliation_task_meta is not UNSET:
            field_dict["reconciliation_task_meta"] = reconciliation_task_meta
        if discovery_enabled is not UNSET:
            field_dict["discovery_enabled"] = discovery_enabled
        if discovery_running is not UNSET:
            field_dict["discovery_running"] = discovery_running
        if discovery_task_id is not UNSET:
            field_dict["discovery_task_id"] = discovery_task_id
        if discovery_task_meta is not UNSET:
            field_dict["discovery_task_meta"] = discovery_task_meta
        if repair_running is not UNSET:
            field_dict["repair_running"] = repair_running
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if repair_task_id is not UNSET:
            field_dict["repair_task_id"] = repair_task_id
        if repair_task_meta is not UNSET:
            field_dict["repair_task_meta"] = repair_task_meta
        if scope is not UNSET:
            field_dict["scope"] = scope
        if kind is not UNSET:
            field_dict["kind"] = kind
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
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
        if actual_availability is not UNSET:
            field_dict["actual_availability"] = actual_availability
        if slo_target is not UNSET:
            field_dict["slo_target"] = slo_target
        if slo_availability is not UNSET:
            field_dict["slo_availability"] = slo_availability
        if sla_target is not UNSET:
            field_dict["sla_target"] = sla_target
        if sla_availability is not UNSET:
            field_dict["sla_availability"] = sla_availability
        if status is not UNSET:
            field_dict["status"] = status
        if source is not UNSET:
            field_dict["source"] = source
        if source_user is not UNSET:
            field_dict["source_user"] = source_user
        if rollout is not UNSET:
            field_dict["rollout"] = rollout
        if action_run is not UNSET:
            field_dict["action_run"] = action_run
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.block_rollout_item_created import BlockRolloutItemCreated  # noqa: PLC0415
        from ..models.block_rollout_item_deleted_by_user_type_0 import (
            BlockRolloutItemDeletedByUserType0,  # noqa: PLC0415
        )
        from ..models.block_rollout_item_last_action_run_type_0 import (
            BlockRolloutItemLastActionRunType0,  # noqa: PLC0415
        )
        from ..models.block_rollout_item_organization_type_0 import BlockRolloutItemOrganizationType0  # noqa: PLC0415
        from ..models.block_rollout_item_workspace_type_0 import BlockRolloutItemWorkspaceType0  # noqa: PLC0415

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

        def _parse_deleted_by_user(data: object) -> BlockRolloutItemDeletedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = BlockRolloutItemDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockRolloutItemDeletedByUserType0 | None, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

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

        def _parse_organization(data: object) -> BlockRolloutItemOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = BlockRolloutItemOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockRolloutItemOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_workspace(data: object) -> BlockRolloutItemWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = BlockRolloutItemWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockRolloutItemWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = BlockRolloutItemCreated.from_dict(d.pop("created"))

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

        def _parse_last_action_run(data: object) -> BlockRolloutItemLastActionRunType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = BlockRolloutItemLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlockRolloutItemLastActionRunType0 | None, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        block = UUID(d.pop("block"))

        block_name = d.pop("block_name")

        action_name = d.pop("action_name")

        def _parse_dispatched_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dispatched_at_type_0 = datetime.datetime.fromisoformat(data)

                return dispatched_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        dispatched_at = _parse_dispatched_at(d.pop("dispatched_at"))

        def _parse_completed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        retry_count = d.pop("retry_count")

        def _parse_retry_after(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retry_after_type_0 = datetime.datetime.fromisoformat(data)

                return retry_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        retry_after = _parse_retry_after(d.pop("retry_after"))

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

        _state = d.pop("state", UNSET)
        state: LastStateEnum | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_last_state_enum(_state)

        def _parse_state_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state_reason = _parse_state_reason(d.pop("state_reason", UNSET))

        _last_state = d.pop("last_state", UNSET)
        last_state: LastStateEnum | Unset
        if isinstance(_last_state, Unset):
            last_state = UNSET
        else:
            last_state = check_last_state_enum(_last_state)

        def _parse_last_state_change(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_state_change_type_0 = datetime.datetime.fromisoformat(data)

                return last_state_change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_state_change = _parse_last_state_change(d.pop("last_state_change", UNSET))

        reconciliation_enabled = d.pop("reconciliation_enabled", UNSET)

        reconciliation_running = d.pop("reconciliation_running", UNSET)

        def _parse_reconciliation_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reconciliation_task_id = _parse_reconciliation_task_id(d.pop("reconciliation_task_id", UNSET))

        reconciliation_task_meta = d.pop("reconciliation_task_meta", UNSET)

        discovery_enabled = d.pop("discovery_enabled", UNSET)

        discovery_running = d.pop("discovery_running", UNSET)

        def _parse_discovery_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        discovery_task_id = _parse_discovery_task_id(d.pop("discovery_task_id", UNSET))

        discovery_task_meta = d.pop("discovery_task_meta", UNSET)

        repair_running = d.pop("repair_running", UNSET)

        platform_service = d.pop("platform_service", UNSET)

        def _parse_repair_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repair_task_id = _parse_repair_task_id(d.pop("repair_task_id", UNSET))

        repair_task_meta = d.pop("repair_task_meta", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ScopeEnum | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_scope_enum(_scope)

        _kind = d.pop("kind", UNSET)
        kind: GenericObjectKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_generic_object_kind_enum(_kind)

        conditions = d.pop("conditions", UNSET)

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

        actual_availability = d.pop("actual_availability", UNSET)

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

        _status = d.pop("status", UNSET)
        status: BlockRolloutItemStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_block_rollout_item_status_enum(_status)

        _source = d.pop("source", UNSET)
        source: Source98DEnum | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_source_98d_enum(_source)

        def _parse_source_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source_user = _parse_source_user(d.pop("source_user", UNSET))

        def _parse_rollout(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rollout_type_0 = UUID(data)

                return rollout_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        rollout = _parse_rollout(d.pop("rollout", UNSET))

        def _parse_action_run(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_run_type_0 = UUID(data)

                return action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        action_run = _parse_action_run(d.pop("action_run", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        block_rollout_item = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            is_deleted=is_deleted,
            deleted_by_user=deleted_by_user,
            last_reconciliation=last_reconciliation,
            last_discovery=last_discovery,
            last_repair=last_repair,
            effective_criticality=effective_criticality,
            organization=organization,
            workspace=workspace,
            created=created,
            url=url,
            icon_url=icon_url,
            is_class_icon=is_class_icon,
            effective_slo_target=effective_slo_target,
            effective_sla_target=effective_sla_target,
            last_action_run=last_action_run,
            block=block,
            block_name=block_name,
            action_name=action_name,
            dispatched_at=dispatched_at,
            completed_at=completed_at,
            retry_count=retry_count,
            retry_after=retry_after,
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            provider_id=provider_id,
            state=state,
            state_reason=state_reason,
            last_state=last_state,
            last_state_change=last_state_change,
            reconciliation_enabled=reconciliation_enabled,
            reconciliation_running=reconciliation_running,
            reconciliation_task_id=reconciliation_task_id,
            reconciliation_task_meta=reconciliation_task_meta,
            discovery_enabled=discovery_enabled,
            discovery_running=discovery_running,
            discovery_task_id=discovery_task_id,
            discovery_task_meta=discovery_task_meta,
            repair_running=repair_running,
            platform_service=platform_service,
            repair_task_id=repair_task_id,
            repair_task_meta=repair_task_meta,
            scope=scope,
            kind=kind,
            conditions=conditions,
            tolerations=tolerations,
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            criticality=criticality,
            target_availability=target_availability,
            actual_availability=actual_availability,
            slo_target=slo_target,
            slo_availability=slo_availability,
            sla_target=sla_target,
            sla_availability=sla_availability,
            status=status,
            source=source,
            source_user=source_user,
            rollout=rollout,
            action_run=action_run,
            reason=reason,
        )

        block_rollout_item.additional_properties = d
        return block_rollout_item

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
