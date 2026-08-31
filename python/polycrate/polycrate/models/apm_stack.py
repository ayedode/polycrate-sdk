from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.apm_stack_kind_enum import APMStackKindEnum, check_apm_stack_kind_enum
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apm_stack_created import APMStackCreated
    from ..models.apm_stack_deleted_by_user_type_0 import APMStackDeletedByUserType0
    from ..models.apm_stack_last_action_run_type_0 import APMStackLastActionRunType0
    from ..models.apm_stack_organization_type_0 import APMStackOrganizationType0
    from ..models.apm_stack_workspace_type_0 import APMStackWorkspaceType0


T = TypeVar("T", bound="APMStack")


@_attrs_define
class APMStack:
    """Full serializer for APMStack detail views.

    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
        is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
            runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
        deleted_by_user (APMStackDeletedByUserType0 | None):
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
        organization (APMStackOrganizationType0 | None):
        workspace (APMStackWorkspaceType0 | None):
        created (APMStackCreated):
        url (str): Gibt die absolute URL zum Object zurück.
        icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
            Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
        is_class_icon (bool):
        effective_slo_target (float | None):
        effective_sla_target (float | None):
        last_action_run (APMStackLastActionRunType0 | None):
        active_tools (list[Any]):
        tools_active_count (int):
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
        kind (APMStackKindEnum | Unset): * `generic` - Generic APM Stack
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
        victoriametrics_k8s_app (None | Unset | UUID): VictoriaMetrics K8sApp
        vmauth_k8s_app (None | Unset | UUID): VMAuth K8sApp
        victorialogs_k8s_app (None | Unset | UUID): VictoriaLogs K8sApp
        grafana_k8s_app (None | Unset | UUID): Grafana K8sApp (can be same as victoriametrics)
        tempo_k8s_app (None | Unset | UUID): Grafana Tempo K8sApp
        loki_k8s_app (None | Unset | UUID): Grafana Loki K8sApp
        vector_k8s_app (None | Unset | UUID): Vector K8sApp (Log collector)
        victoriametrics_hostname (None | str | Unset): VictoriaMetrics URL
        vmauth_hostname (None | str | Unset): VMAuth URL
        victorialogs_hostname (None | str | Unset): VictoriaLogs URL
        grafana_hostname (None | str | Unset): Grafana URL
        tempo_hostname (None | str | Unset): Grafana Tempo URL
        loki_hostname (None | str | Unset): Grafana Loki URL
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    deleted_by_user: APMStackDeletedByUserType0 | None
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
    organization: APMStackOrganizationType0 | None
    workspace: APMStackWorkspaceType0 | None
    created: APMStackCreated
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    last_action_run: APMStackLastActionRunType0 | None
    active_tools: list[Any]
    tools_active_count: int
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
    kind: APMStackKindEnum | Unset = UNSET
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
    victoriametrics_k8s_app: None | Unset | UUID = UNSET
    vmauth_k8s_app: None | Unset | UUID = UNSET
    victorialogs_k8s_app: None | Unset | UUID = UNSET
    grafana_k8s_app: None | Unset | UUID = UNSET
    tempo_k8s_app: None | Unset | UUID = UNSET
    loki_k8s_app: None | Unset | UUID = UNSET
    vector_k8s_app: None | Unset | UUID = UNSET
    victoriametrics_hostname: None | str | Unset = UNSET
    vmauth_hostname: None | str | Unset = UNSET
    victorialogs_hostname: None | str | Unset = UNSET
    grafana_hostname: None | str | Unset = UNSET
    tempo_hostname: None | str | Unset = UNSET
    loki_hostname: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.apm_stack_deleted_by_user_type_0 import APMStackDeletedByUserType0
        from ..models.apm_stack_last_action_run_type_0 import APMStackLastActionRunType0
        from ..models.apm_stack_organization_type_0 import APMStackOrganizationType0
        from ..models.apm_stack_workspace_type_0 import APMStackWorkspaceType0

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
        if isinstance(self.deleted_by_user, APMStackDeletedByUserType0):
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
        if isinstance(self.organization, APMStackOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, APMStackWorkspaceType0):
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
        if isinstance(self.last_action_run, APMStackLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        active_tools = self.active_tools

        tools_active_count = self.tools_active_count

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

        victoriametrics_k8s_app: None | str | Unset
        if isinstance(self.victoriametrics_k8s_app, Unset):
            victoriametrics_k8s_app = UNSET
        elif isinstance(self.victoriametrics_k8s_app, UUID):
            victoriametrics_k8s_app = str(self.victoriametrics_k8s_app)
        else:
            victoriametrics_k8s_app = self.victoriametrics_k8s_app

        vmauth_k8s_app: None | str | Unset
        if isinstance(self.vmauth_k8s_app, Unset):
            vmauth_k8s_app = UNSET
        elif isinstance(self.vmauth_k8s_app, UUID):
            vmauth_k8s_app = str(self.vmauth_k8s_app)
        else:
            vmauth_k8s_app = self.vmauth_k8s_app

        victorialogs_k8s_app: None | str | Unset
        if isinstance(self.victorialogs_k8s_app, Unset):
            victorialogs_k8s_app = UNSET
        elif isinstance(self.victorialogs_k8s_app, UUID):
            victorialogs_k8s_app = str(self.victorialogs_k8s_app)
        else:
            victorialogs_k8s_app = self.victorialogs_k8s_app

        grafana_k8s_app: None | str | Unset
        if isinstance(self.grafana_k8s_app, Unset):
            grafana_k8s_app = UNSET
        elif isinstance(self.grafana_k8s_app, UUID):
            grafana_k8s_app = str(self.grafana_k8s_app)
        else:
            grafana_k8s_app = self.grafana_k8s_app

        tempo_k8s_app: None | str | Unset
        if isinstance(self.tempo_k8s_app, Unset):
            tempo_k8s_app = UNSET
        elif isinstance(self.tempo_k8s_app, UUID):
            tempo_k8s_app = str(self.tempo_k8s_app)
        else:
            tempo_k8s_app = self.tempo_k8s_app

        loki_k8s_app: None | str | Unset
        if isinstance(self.loki_k8s_app, Unset):
            loki_k8s_app = UNSET
        elif isinstance(self.loki_k8s_app, UUID):
            loki_k8s_app = str(self.loki_k8s_app)
        else:
            loki_k8s_app = self.loki_k8s_app

        vector_k8s_app: None | str | Unset
        if isinstance(self.vector_k8s_app, Unset):
            vector_k8s_app = UNSET
        elif isinstance(self.vector_k8s_app, UUID):
            vector_k8s_app = str(self.vector_k8s_app)
        else:
            vector_k8s_app = self.vector_k8s_app

        victoriametrics_hostname: None | str | Unset
        if isinstance(self.victoriametrics_hostname, Unset):
            victoriametrics_hostname = UNSET
        else:
            victoriametrics_hostname = self.victoriametrics_hostname

        vmauth_hostname: None | str | Unset
        if isinstance(self.vmauth_hostname, Unset):
            vmauth_hostname = UNSET
        else:
            vmauth_hostname = self.vmauth_hostname

        victorialogs_hostname: None | str | Unset
        if isinstance(self.victorialogs_hostname, Unset):
            victorialogs_hostname = UNSET
        else:
            victorialogs_hostname = self.victorialogs_hostname

        grafana_hostname: None | str | Unset
        if isinstance(self.grafana_hostname, Unset):
            grafana_hostname = UNSET
        else:
            grafana_hostname = self.grafana_hostname

        tempo_hostname: None | str | Unset
        if isinstance(self.tempo_hostname, Unset):
            tempo_hostname = UNSET
        else:
            tempo_hostname = self.tempo_hostname

        loki_hostname: None | str | Unset
        if isinstance(self.loki_hostname, Unset):
            loki_hostname = UNSET
        else:
            loki_hostname = self.loki_hostname

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
                "active_tools": active_tools,
                "tools_active_count": tools_active_count,
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
        if victoriametrics_k8s_app is not UNSET:
            field_dict["victoriametrics_k8s_app"] = victoriametrics_k8s_app
        if vmauth_k8s_app is not UNSET:
            field_dict["vmauth_k8s_app"] = vmauth_k8s_app
        if victorialogs_k8s_app is not UNSET:
            field_dict["victorialogs_k8s_app"] = victorialogs_k8s_app
        if grafana_k8s_app is not UNSET:
            field_dict["grafana_k8s_app"] = grafana_k8s_app
        if tempo_k8s_app is not UNSET:
            field_dict["tempo_k8s_app"] = tempo_k8s_app
        if loki_k8s_app is not UNSET:
            field_dict["loki_k8s_app"] = loki_k8s_app
        if vector_k8s_app is not UNSET:
            field_dict["vector_k8s_app"] = vector_k8s_app
        if victoriametrics_hostname is not UNSET:
            field_dict["victoriametrics_hostname"] = victoriametrics_hostname
        if vmauth_hostname is not UNSET:
            field_dict["vmauth_hostname"] = vmauth_hostname
        if victorialogs_hostname is not UNSET:
            field_dict["victorialogs_hostname"] = victorialogs_hostname
        if grafana_hostname is not UNSET:
            field_dict["grafana_hostname"] = grafana_hostname
        if tempo_hostname is not UNSET:
            field_dict["tempo_hostname"] = tempo_hostname
        if loki_hostname is not UNSET:
            field_dict["loki_hostname"] = loki_hostname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apm_stack_created import APMStackCreated
        from ..models.apm_stack_deleted_by_user_type_0 import APMStackDeletedByUserType0
        from ..models.apm_stack_last_action_run_type_0 import APMStackLastActionRunType0
        from ..models.apm_stack_organization_type_0 import APMStackOrganizationType0
        from ..models.apm_stack_workspace_type_0 import APMStackWorkspaceType0

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

        def _parse_deleted_by_user(data: object) -> APMStackDeletedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = APMStackDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(APMStackDeletedByUserType0 | None, data)

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

        def _parse_organization(data: object) -> APMStackOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = APMStackOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(APMStackOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_workspace(data: object) -> APMStackWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = APMStackWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(APMStackWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = APMStackCreated.from_dict(d.pop("created"))

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

        def _parse_last_action_run(data: object) -> APMStackLastActionRunType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = APMStackLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(APMStackLastActionRunType0 | None, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        active_tools = cast(list[Any], d.pop("active_tools"))

        tools_active_count = d.pop("tools_active_count")

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
        kind: APMStackKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_apm_stack_kind_enum(_kind)

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

        def _parse_victoriametrics_k8s_app(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                victoriametrics_k8s_app_type_0 = UUID(data)

                return victoriametrics_k8s_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        victoriametrics_k8s_app = _parse_victoriametrics_k8s_app(d.pop("victoriametrics_k8s_app", UNSET))

        def _parse_vmauth_k8s_app(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vmauth_k8s_app_type_0 = UUID(data)

                return vmauth_k8s_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        vmauth_k8s_app = _parse_vmauth_k8s_app(d.pop("vmauth_k8s_app", UNSET))

        def _parse_victorialogs_k8s_app(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                victorialogs_k8s_app_type_0 = UUID(data)

                return victorialogs_k8s_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        victorialogs_k8s_app = _parse_victorialogs_k8s_app(d.pop("victorialogs_k8s_app", UNSET))

        def _parse_grafana_k8s_app(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                grafana_k8s_app_type_0 = UUID(data)

                return grafana_k8s_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        grafana_k8s_app = _parse_grafana_k8s_app(d.pop("grafana_k8s_app", UNSET))

        def _parse_tempo_k8s_app(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tempo_k8s_app_type_0 = UUID(data)

                return tempo_k8s_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        tempo_k8s_app = _parse_tempo_k8s_app(d.pop("tempo_k8s_app", UNSET))

        def _parse_loki_k8s_app(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                loki_k8s_app_type_0 = UUID(data)

                return loki_k8s_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        loki_k8s_app = _parse_loki_k8s_app(d.pop("loki_k8s_app", UNSET))

        def _parse_vector_k8s_app(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vector_k8s_app_type_0 = UUID(data)

                return vector_k8s_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        vector_k8s_app = _parse_vector_k8s_app(d.pop("vector_k8s_app", UNSET))

        def _parse_victoriametrics_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        victoriametrics_hostname = _parse_victoriametrics_hostname(d.pop("victoriametrics_hostname", UNSET))

        def _parse_vmauth_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vmauth_hostname = _parse_vmauth_hostname(d.pop("vmauth_hostname", UNSET))

        def _parse_victorialogs_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        victorialogs_hostname = _parse_victorialogs_hostname(d.pop("victorialogs_hostname", UNSET))

        def _parse_grafana_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grafana_hostname = _parse_grafana_hostname(d.pop("grafana_hostname", UNSET))

        def _parse_tempo_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tempo_hostname = _parse_tempo_hostname(d.pop("tempo_hostname", UNSET))

        def _parse_loki_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loki_hostname = _parse_loki_hostname(d.pop("loki_hostname", UNSET))

        apm_stack = cls(
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
            active_tools=active_tools,
            tools_active_count=tools_active_count,
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
            victoriametrics_k8s_app=victoriametrics_k8s_app,
            vmauth_k8s_app=vmauth_k8s_app,
            victorialogs_k8s_app=victorialogs_k8s_app,
            grafana_k8s_app=grafana_k8s_app,
            tempo_k8s_app=tempo_k8s_app,
            loki_k8s_app=loki_k8s_app,
            vector_k8s_app=vector_k8s_app,
            victoriametrics_hostname=victoriametrics_hostname,
            vmauth_hostname=vmauth_hostname,
            victorialogs_hostname=victorialogs_hostname,
            grafana_hostname=grafana_hostname,
            tempo_hostname=tempo_hostname,
            loki_hostname=loki_hostname,
        )

        apm_stack.additional_properties = d
        return apm_stack

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
