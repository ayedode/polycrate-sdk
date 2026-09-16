from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_run_status_enum import ActionRunStatusEnum, check_action_run_status_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.generic_object_kind_enum import GenericObjectKindEnum, check_generic_object_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_run_created import ActionRunCreated
    from ..models.action_run_deleted_by_user_type_0 import ActionRunDeletedByUserType0
    from ..models.action_run_last_action_run_type_0 import ActionRunLastActionRunType0
    from ..models.action_run_organization_type_0 import ActionRunOrganizationType0
    from ..models.action_run_workspace_type_0 import ActionRunWorkspaceType0
    from ..models.block_rollout_simple import BlockRolloutSimple
    from ..models.block_simple import BlockSimple


T = TypeVar("T", bound="ActionRun")


@_attrs_define
class ActionRun:
    """ActionRun Detail serializer - inherits from ManagedObjectDetailSerializer
    for icon_url and other dashboard-relevant fields.

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
            deleted_by_user (ActionRunDeletedByUserType0 | None):
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
            kind (GenericObjectKindEnum): * `generic` - Generic
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
            organization (ActionRunOrganizationType0 | None):
            workspace (ActionRunWorkspaceType0 | None):
            created (ActionRunCreated):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            last_action_run (ActionRunLastActionRunType0 | None):
            status (ActionRunStatusEnum): * `pending` - Pending
                * `running` - Running
                * `success` - Success
                * `failed` - Failed
                * `cancelled` - Cancelled
            status_reason (None | str):
            block (BlockSimple):
            action (None | str):
            command (None | str):
            exit_code (int | None): Exit code of the action run
            started_at (datetime.datetime | None):
            finished_at (datetime.datetime | None):
            log_stdout (None | str):
            log_stderr (None | str):
            block_config (Any):
            block_version (None | str):
            block_labels (Any): Block labels at the time of action run execution
            workspace_poly (None | str):
            workspace_snapshot (Any):
            workspace_config (Any):
            task_id (None | str):
            raw_data (Any): Raw submission data from CLI or API
            metadata (Any): Metadata about the action run
            rollout (BlockRolloutSimple):
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
    deleted_by_user: ActionRunDeletedByUserType0 | None
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
    kind: GenericObjectKindEnum
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
    organization: ActionRunOrganizationType0 | None
    workspace: ActionRunWorkspaceType0 | None
    created: ActionRunCreated
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    last_action_run: ActionRunLastActionRunType0 | None
    status: ActionRunStatusEnum
    status_reason: None | str
    block: BlockSimple
    action: None | str
    command: None | str
    exit_code: int | None
    started_at: datetime.datetime | None
    finished_at: datetime.datetime | None
    log_stdout: None | str
    log_stderr: None | str
    block_config: Any
    block_version: None | str
    block_labels: Any
    workspace_poly: None | str
    workspace_snapshot: Any
    workspace_config: Any
    task_id: None | str
    raw_data: Any
    metadata: Any
    rollout: BlockRolloutSimple
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_run_deleted_by_user_type_0 import ActionRunDeletedByUserType0  # noqa: PLC0415
        from ..models.action_run_last_action_run_type_0 import ActionRunLastActionRunType0  # noqa: PLC0415
        from ..models.action_run_organization_type_0 import ActionRunOrganizationType0  # noqa: PLC0415
        from ..models.action_run_workspace_type_0 import ActionRunWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.deleted_by_user, ActionRunDeletedByUserType0):
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

        organization: dict[str, Any] | None
        if isinstance(self.organization, ActionRunOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, ActionRunWorkspaceType0):
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
        if isinstance(self.last_action_run, ActionRunLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        status: str = self.status

        status_reason: None | str
        status_reason = self.status_reason

        block = self.block.to_dict()

        action: None | str
        action = self.action

        command: None | str
        command = self.command

        exit_code: int | None
        exit_code = self.exit_code

        started_at: None | str
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        finished_at: None | str
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        log_stdout: None | str
        log_stdout = self.log_stdout

        log_stderr: None | str
        log_stderr = self.log_stderr

        block_config = self.block_config

        block_version: None | str
        block_version = self.block_version

        block_labels = self.block_labels

        workspace_poly: None | str
        workspace_poly = self.workspace_poly

        workspace_snapshot = self.workspace_snapshot

        workspace_config = self.workspace_config

        task_id: None | str
        task_id = self.task_id

        raw_data = self.raw_data

        metadata = self.metadata

        rollout = self.rollout.to_dict()

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
                "status": status,
                "status_reason": status_reason,
                "block": block,
                "action": action,
                "command": command,
                "exit_code": exit_code,
                "started_at": started_at,
                "finished_at": finished_at,
                "log_stdout": log_stdout,
                "log_stderr": log_stderr,
                "block_config": block_config,
                "block_version": block_version,
                "block_labels": block_labels,
                "workspace_poly": workspace_poly,
                "workspace_snapshot": workspace_snapshot,
                "workspace_config": workspace_config,
                "task_id": task_id,
                "raw_data": raw_data,
                "metadata": metadata,
                "rollout": rollout,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_run_created import ActionRunCreated  # noqa: PLC0415
        from ..models.action_run_deleted_by_user_type_0 import ActionRunDeletedByUserType0  # noqa: PLC0415
        from ..models.action_run_last_action_run_type_0 import ActionRunLastActionRunType0  # noqa: PLC0415
        from ..models.action_run_organization_type_0 import ActionRunOrganizationType0  # noqa: PLC0415
        from ..models.action_run_workspace_type_0 import ActionRunWorkspaceType0  # noqa: PLC0415
        from ..models.block_rollout_simple import BlockRolloutSimple  # noqa: PLC0415
        from ..models.block_simple import BlockSimple  # noqa: PLC0415

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

        def _parse_deleted_by_user(data: object) -> ActionRunDeletedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = ActionRunDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionRunDeletedByUserType0 | None, data)

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

        kind = check_generic_object_kind_enum(d.pop("kind"))

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

        def _parse_organization(data: object) -> ActionRunOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = ActionRunOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionRunOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_workspace(data: object) -> ActionRunWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = ActionRunWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionRunWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = ActionRunCreated.from_dict(d.pop("created"))

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

        def _parse_last_action_run(data: object) -> ActionRunLastActionRunType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = ActionRunLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionRunLastActionRunType0 | None, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        status = check_action_run_status_enum(d.pop("status"))

        def _parse_status_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status_reason = _parse_status_reason(d.pop("status_reason"))

        block = BlockSimple.from_dict(d.pop("block"))

        def _parse_action(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        action = _parse_action(d.pop("action"))

        def _parse_command(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        command = _parse_command(d.pop("command"))

        def _parse_exit_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        exit_code = _parse_exit_code(d.pop("exit_code"))

        def _parse_started_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        started_at = _parse_started_at(d.pop("started_at"))

        def _parse_finished_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = datetime.datetime.fromisoformat(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        finished_at = _parse_finished_at(d.pop("finished_at"))

        def _parse_log_stdout(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        log_stdout = _parse_log_stdout(d.pop("log_stdout"))

        def _parse_log_stderr(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        log_stderr = _parse_log_stderr(d.pop("log_stderr"))

        block_config = d.pop("block_config")

        def _parse_block_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        block_version = _parse_block_version(d.pop("block_version"))

        block_labels = d.pop("block_labels")

        def _parse_workspace_poly(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        workspace_poly = _parse_workspace_poly(d.pop("workspace_poly"))

        workspace_snapshot = d.pop("workspace_snapshot")

        workspace_config = d.pop("workspace_config")

        def _parse_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        task_id = _parse_task_id(d.pop("task_id"))

        raw_data = d.pop("raw_data")

        metadata = d.pop("metadata")

        rollout = BlockRolloutSimple.from_dict(d.pop("rollout"))

        name = d.pop("name", UNSET)

        action_run = cls(
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
            status=status,
            status_reason=status_reason,
            block=block,
            action=action,
            command=command,
            exit_code=exit_code,
            started_at=started_at,
            finished_at=finished_at,
            log_stdout=log_stdout,
            log_stderr=log_stderr,
            block_config=block_config,
            block_version=block_version,
            block_labels=block_labels,
            workspace_poly=workspace_poly,
            workspace_snapshot=workspace_snapshot,
            workspace_config=workspace_config,
            task_id=task_id,
            raw_data=raw_data,
            metadata=metadata,
            rollout=rollout,
            name=name,
        )

        action_run.additional_properties = d
        return action_run

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
