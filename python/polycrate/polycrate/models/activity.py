from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_kind_enum import ActivityKindEnum, check_activity_kind_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_created import ActivityCreated
    from ..models.activity_deleted_by_user_type_0 import ActivityDeletedByUserType0
    from ..models.activity_last_action_run_type_0 import ActivityLastActionRunType0
    from ..models.organization_simple import OrganizationSimple
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="Activity")


@_attrs_define
class Activity:
    """Full serializer for Activity detail views.

    Read-only as activities are system-generated.

        Attributes:
            id (UUID):
            display_name (None | str): The display name is used to display the object in the UI. It can be different from
                the name.
            labels (Any):
            annotations (Any):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            deleted_by_user (ActivityDeletedByUserType0 | None):
            debug_mode (bool): Persists all Object Logs in the database
            provider (ProviderEnum): * `loopback` - Loopback
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
            provider_reference (None | str):
            provider_id (None | str):
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
            reconciliation_enabled (bool):
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
            platform_service (bool):
            repair_task_id (None | str):
            repair_task_meta (Any): Task metadata for repair progress tracking
            last_repair (datetime.datetime | None):
            scope (ScopeEnum): * `system` - System
                * `user` - User
            kind (ActivityKindEnum): * `generic` - Generic
                * `creation` - Creation
                * `update` - Update
                * `deletion` - Deletion
                * `reconciliation` - Reconciliation
                * `discovery` - Discovery
                * `repair` - Repair
                * `check` - Check
                * `alert` - Alert
                * `announcement` - Announcement
                * `replicaset_created` - Replicaset Created
                * `statefulset_created` - Statefulset Created
                * `k8s_app_instance_installed` - K8s App Instance Installed
                * `k8s_app_instance_uninstalled` - K8s App Instance Uninstalled
                * `k8s_app_installed` - K8s App Installed
                * `k8s_app_uninstalled` - K8s App Uninstalled
                * `k8s_app_installation_failed` - K8s App Installation Failed
                * `k8s_app_uninstallation_failed` - K8s App Uninstallation Failed
                * `block_action_run` - Block Action Run
                * `block_action_run_start` - Block Action Run Start
                * `block_action_run_finish` - Block Action Run Finish
                * `condition_added` - Condition Added
                * `condition_removed` - Condition Removed
                * `state_changed` - State Changed
                * `long_running_task_detected` - Long Running Task Detected
                * `price_changed` - Price Changed
                * `product_subscribed` - Product Subscribed
                * `product_cancelled` - Product Cancelled
                * `downtime` - Downtime
                * `downtime_started` - Downtime Started
                * `downtime_ended` - Downtime Ended
                * `downtime_triggered` - Downtime Triggered
                * `downtime_updated` - Downtime Updated
                * `downtime_object_added` - Downtime Object Added
                * `downtime_object_recovered` - Downtime Object Recovered
                * `downtime_closed_manually` - Downtime Closed Manually
                * `maintenance_scheduled` - Maintenance Scheduled
                * `maintenance_started` - Maintenance Started
                * `maintenance_ended` - Maintenance Ended
                * `incident_created` - Incident Created
                * `incident_status_changed` - Incident Status Changed
                * `incident_downtime_linked` - Incident Downtime Linked
                * `incident_downtime_unlinked` - Incident Downtime Unlinked
                * `notification_sent` - Notification Sent
                * `notification_send_failed` - Notification Send Failed
                * `note_created` - Note Created
                * `note_reply` - Note Reply
                * `note_resolved` - Note Resolved
                * `note_reminder` - Note Reminder
                * `ssh-session` - SSH Session
                * `workspace-sync` - Workspace Sync
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            tolerations (Any): Tolerations match conditions. If a toleration for a condition exists for an object, the
                condition will not be applied.
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None):
            archived_reason (None | str): The reason why the object was archived
            criticality (CriticalityEnum | None): Criticality level. Null = inherit from workspace, then org. Explicit value
                overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            effective_criticality (EffectiveCriticalityEnum | None):
            target_availability (None | str): Target availability in % (overrides SystemConfig default). Null = use
                SystemConfig DEFAULT_TARGET_AVAILABILITY.
            actual_availability (str): Calculated actual availability as yearly average in %
            slo_target (None | str): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
            slo_availability (str): Calculated SLO availability in % (updated in reconcile)
            sla_target (None | str): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
            sla_availability (str): Calculated SLA availability in % (updated in reconcile)
            organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            workspace (WorkspaceSimple):
            created (ActivityCreated):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            last_action_run (ActivityLastActionRunType0 | None):
            kind_display (str):
            message (None | str): Human-readable activity description
            user_email (None | str):
            metadata (Any): Structured metadata about the activity
            object_id (None | str): ID of the object this activity relates to
            object_type (None | str): Type of the object this activity relates to
            object_name (None | str): Name of the object this activity relates to
            object_url (None | str): URL of the object this activity relates to
            object_urn (None | str): URN of the object this activity relates to
            object_icon_url (str): Deterministic class icon of the referenced object, derived from object_type. Spec 484.
            name (str | Unset): Object name
    """

    id: UUID
    display_name: None | str
    labels: Any
    annotations: Any
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    deleted_by_user: ActivityDeletedByUserType0 | None
    debug_mode: bool
    provider: ProviderEnum
    provider_reference: None | str
    provider_id: None | str
    state: LastStateEnum
    state_reason: None | str
    last_state: LastStateEnum
    last_state_change: datetime.datetime | None
    reconciliation_enabled: bool
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
    platform_service: bool
    repair_task_id: None | str
    repair_task_meta: Any
    last_repair: datetime.datetime | None
    scope: ScopeEnum
    kind: ActivityKindEnum
    conditions: Any
    tolerations: Any
    archived: bool
    archived_at: datetime.datetime | None
    archived_reason: None | str
    criticality: CriticalityEnum | None
    effective_criticality: EffectiveCriticalityEnum | None
    target_availability: None | str
    actual_availability: str
    slo_target: None | str
    slo_availability: str
    sla_target: None | str
    sla_availability: str
    organization: OrganizationSimple
    workspace: WorkspaceSimple
    created: ActivityCreated
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    last_action_run: ActivityLastActionRunType0 | None
    kind_display: str
    message: None | str
    user_email: None | str
    metadata: Any
    object_id: None | str
    object_type: None | str
    object_name: None | str
    object_url: None | str
    object_urn: None | str
    object_icon_url: str
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_deleted_by_user_type_0 import ActivityDeletedByUserType0
        from ..models.activity_last_action_run_type_0 import ActivityLastActionRunType0

        id = str(self.id)

        display_name: None | str
        display_name = self.display_name

        labels = self.labels

        annotations = self.annotations

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        is_deleted = self.is_deleted

        deleted_by_user: dict[str, Any] | None
        if isinstance(self.deleted_by_user, ActivityDeletedByUserType0):
            deleted_by_user = self.deleted_by_user.to_dict()
        else:
            deleted_by_user = self.deleted_by_user

        debug_mode = self.debug_mode

        provider: str = self.provider

        provider_reference: None | str
        provider_reference = self.provider_reference

        provider_id: None | str
        provider_id = self.provider_id

        state: str = self.state

        state_reason: None | str
        state_reason = self.state_reason

        last_state: str = self.last_state

        last_state_change: None | str
        if isinstance(self.last_state_change, datetime.datetime):
            last_state_change = self.last_state_change.isoformat()
        else:
            last_state_change = self.last_state_change

        reconciliation_enabled = self.reconciliation_enabled

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

        platform_service = self.platform_service

        repair_task_id: None | str
        repair_task_id = self.repair_task_id

        repair_task_meta = self.repair_task_meta

        last_repair: None | str
        if isinstance(self.last_repair, datetime.datetime):
            last_repair = self.last_repair.isoformat()
        else:
            last_repair = self.last_repair

        scope: str = self.scope

        kind: str = self.kind

        conditions = self.conditions

        tolerations = self.tolerations

        archived = self.archived

        archived_at: None | str
        if isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        archived_reason: None | str
        archived_reason = self.archived_reason

        criticality: None | str
        if isinstance(self.criticality, str):
            criticality = self.criticality
        else:
            criticality = self.criticality

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        target_availability: None | str
        target_availability = self.target_availability

        actual_availability = self.actual_availability

        slo_target: None | str
        slo_target = self.slo_target

        slo_availability = self.slo_availability

        sla_target: None | str
        sla_target = self.sla_target

        sla_availability = self.sla_availability

        organization = self.organization.to_dict()

        workspace = self.workspace.to_dict()

        created = self.created.to_dict()

        url = self.url

        icon_url = self.icon_url

        is_class_icon = self.is_class_icon

        effective_slo_target: float | None
        effective_slo_target = self.effective_slo_target

        effective_sla_target: float | None
        effective_sla_target = self.effective_sla_target

        last_action_run: dict[str, Any] | None
        if isinstance(self.last_action_run, ActivityLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        kind_display = self.kind_display

        message: None | str
        message = self.message

        user_email: None | str
        user_email = self.user_email

        metadata = self.metadata

        object_id: None | str
        object_id = self.object_id

        object_type: None | str
        object_type = self.object_type

        object_name: None | str
        object_name = self.object_name

        object_url: None | str
        object_url = self.object_url

        object_urn: None | str
        object_urn = self.object_urn

        object_icon_url = self.object_icon_url

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
                "labels": labels,
                "annotations": annotations,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
                "is_deleted": is_deleted,
                "deleted_by_user": deleted_by_user,
                "debug_mode": debug_mode,
                "provider": provider,
                "provider_reference": provider_reference,
                "provider_id": provider_id,
                "state": state,
                "state_reason": state_reason,
                "last_state": last_state,
                "last_state_change": last_state_change,
                "reconciliation_enabled": reconciliation_enabled,
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
                "platform_service": platform_service,
                "repair_task_id": repair_task_id,
                "repair_task_meta": repair_task_meta,
                "last_repair": last_repair,
                "scope": scope,
                "kind": kind,
                "conditions": conditions,
                "tolerations": tolerations,
                "archived": archived,
                "archived_at": archived_at,
                "archived_reason": archived_reason,
                "criticality": criticality,
                "effective_criticality": effective_criticality,
                "target_availability": target_availability,
                "actual_availability": actual_availability,
                "slo_target": slo_target,
                "slo_availability": slo_availability,
                "sla_target": sla_target,
                "sla_availability": sla_availability,
                "organization": organization,
                "workspace": workspace,
                "created": created,
                "url": url,
                "icon_url": icon_url,
                "is_class_icon": is_class_icon,
                "effective_slo_target": effective_slo_target,
                "effective_sla_target": effective_sla_target,
                "last_action_run": last_action_run,
                "kind_display": kind_display,
                "message": message,
                "user_email": user_email,
                "metadata": metadata,
                "object_id": object_id,
                "object_type": object_type,
                "object_name": object_name,
                "object_url": object_url,
                "object_urn": object_urn,
                "object_icon_url": object_icon_url,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_created import ActivityCreated
        from ..models.activity_deleted_by_user_type_0 import ActivityDeletedByUserType0
        from ..models.activity_last_action_run_type_0 import ActivityLastActionRunType0
        from ..models.organization_simple import OrganizationSimple
        from ..models.workspace_simple import WorkspaceSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        labels = d.pop("labels")

        annotations = d.pop("annotations")

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

        def _parse_deleted_by_user(data: object) -> ActivityDeletedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = ActivityDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActivityDeletedByUserType0 | None, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

        debug_mode = d.pop("debug_mode")

        provider = check_provider_enum(d.pop("provider"))

        def _parse_provider_reference(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_reference = _parse_provider_reference(d.pop("provider_reference"))

        def _parse_provider_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_id = _parse_provider_id(d.pop("provider_id"))

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

        reconciliation_enabled = d.pop("reconciliation_enabled")

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

        platform_service = d.pop("platform_service")

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

        kind = check_activity_kind_enum(d.pop("kind"))

        conditions = d.pop("conditions")

        tolerations = d.pop("tolerations")

        archived = d.pop("archived")

        def _parse_archived_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = datetime.datetime.fromisoformat(data)

                return archived_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        archived_at = _parse_archived_at(d.pop("archived_at"))

        def _parse_archived_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        archived_reason = _parse_archived_reason(d.pop("archived_reason"))

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

        def _parse_target_availability(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_availability = _parse_target_availability(d.pop("target_availability"))

        actual_availability = d.pop("actual_availability")

        def _parse_slo_target(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slo_target = _parse_slo_target(d.pop("slo_target"))

        slo_availability = d.pop("slo_availability")

        def _parse_sla_target(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sla_target = _parse_sla_target(d.pop("sla_target"))

        sla_availability = d.pop("sla_availability")

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

        created = ActivityCreated.from_dict(d.pop("created"))

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

        def _parse_last_action_run(data: object) -> ActivityLastActionRunType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = ActivityLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActivityLastActionRunType0 | None, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        kind_display = d.pop("kind_display")

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        def _parse_user_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_email = _parse_user_email(d.pop("user_email"))

        metadata = d.pop("metadata")

        def _parse_object_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        object_id = _parse_object_id(d.pop("object_id"))

        def _parse_object_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        object_type = _parse_object_type(d.pop("object_type"))

        def _parse_object_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        object_name = _parse_object_name(d.pop("object_name"))

        def _parse_object_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        object_url = _parse_object_url(d.pop("object_url"))

        def _parse_object_urn(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        object_urn = _parse_object_urn(d.pop("object_urn"))

        object_icon_url = d.pop("object_icon_url")

        name = d.pop("name", UNSET)

        activity = cls(
            id=id,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            is_deleted=is_deleted,
            deleted_by_user=deleted_by_user,
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
            last_reconciliation=last_reconciliation,
            discovery_enabled=discovery_enabled,
            discovery_running=discovery_running,
            discovery_task_id=discovery_task_id,
            discovery_task_meta=discovery_task_meta,
            last_discovery=last_discovery,
            repair_running=repair_running,
            platform_service=platform_service,
            repair_task_id=repair_task_id,
            repair_task_meta=repair_task_meta,
            last_repair=last_repair,
            scope=scope,
            kind=kind,
            conditions=conditions,
            tolerations=tolerations,
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            criticality=criticality,
            effective_criticality=effective_criticality,
            target_availability=target_availability,
            actual_availability=actual_availability,
            slo_target=slo_target,
            slo_availability=slo_availability,
            sla_target=sla_target,
            sla_availability=sla_availability,
            organization=organization,
            workspace=workspace,
            created=created,
            url=url,
            icon_url=icon_url,
            is_class_icon=is_class_icon,
            effective_slo_target=effective_slo_target,
            effective_sla_target=effective_sla_target,
            last_action_run=last_action_run,
            kind_display=kind_display,
            message=message,
            user_email=user_email,
            metadata=metadata,
            object_id=object_id,
            object_type=object_type,
            object_name=object_name,
            object_url=object_url,
            object_urn=object_urn,
            object_icon_url=object_icon_url,
            name=name,
        )

        activity.additional_properties = d
        return activity

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
