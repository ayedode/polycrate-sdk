from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.block_rollout_config_kind_enum import BlockRolloutConfigKindEnum, check_block_rollout_config_kind_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..models.trigger_type_enum import TriggerTypeEnum, check_trigger_type_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedBlockRolloutConfigRequest")


@_attrs_define
class PatchedBlockRolloutConfigRequest:
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
            kind (BlockRolloutConfigKindEnum | Unset): * `trigger` - Trigger
                * `config` - Config Default: 'config'.
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
            block_name (None | str | Unset):
            active (bool | Unset):
            is_system_config (bool | Unset):  Default: False.
            trigger_type (BlankEnum | None | TriggerTypeEnum | Unset):
            cron_expression (None | str | Unset):
            action_name (None | str | Unset):
            target_version (None | str | Unset):
            template_block (None | str | Unset):
            enqueue_reason (None | str | Unset):
            block_config_template (None | str | Unset):
            scope_expressions (Any | Unset):
            auto_takeover (bool | Unset): When enabled, CLI-managed blocks that match this BRC will be automatically taken
                over: created_by_component is set to "api" and all config_to_credential_mappings are extracted as Credentials
                before the first BRC-managed install.
            config_to_credential_mappings (Any | Unset): List of {credential_name, config_path} mappings. Each entry
                extracts a value from block.config (dotted path) and stores it as a generic Credential for use in
                block_config_template. Takeover is aborted if any mapping cannot be resolved. Example: [{"credential_name":
                "velero-encryption-password", "config_path": "velero.credentials.encryptionKey"}]
            target_organizations (list[UUID] | Unset):
            target_workspaces (list[UUID] | Unset):
            max_concurrent_percent (int | Unset): Maximum percentage of wave items to dispatch concurrently (1-100)
            failure_threshold_percent (int | Unset): Failure rate (%) above which the wave is blocked
            max_retries (int | Unset):
            maintenance_window (None | Unset | UUID):
            bypass_maintenance_window (bool | Unset): When True, the maintenance window check is skipped for all items of
                this config.
            notify_on_wave_blocked (bool | Unset):
    """

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
    kind: BlockRolloutConfigKindEnum | Unset = "config"
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
    block_name: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    is_system_config: bool | Unset = False
    trigger_type: BlankEnum | None | TriggerTypeEnum | Unset = UNSET
    cron_expression: None | str | Unset = UNSET
    action_name: None | str | Unset = UNSET
    target_version: None | str | Unset = UNSET
    template_block: None | str | Unset = UNSET
    enqueue_reason: None | str | Unset = UNSET
    block_config_template: None | str | Unset = UNSET
    scope_expressions: Any | Unset = UNSET
    auto_takeover: bool | Unset = UNSET
    config_to_credential_mappings: Any | Unset = UNSET
    target_organizations: list[UUID] | Unset = UNSET
    target_workspaces: list[UUID] | Unset = UNSET
    max_concurrent_percent: int | Unset = UNSET
    failure_threshold_percent: int | Unset = UNSET
    max_retries: int | Unset = UNSET
    maintenance_window: None | Unset | UUID = UNSET
    bypass_maintenance_window: bool | Unset = UNSET
    notify_on_wave_blocked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        block_name: None | str | Unset
        if isinstance(self.block_name, Unset):
            block_name = UNSET
        else:
            block_name = self.block_name

        active = self.active

        is_system_config = self.is_system_config

        trigger_type: None | str | Unset
        if isinstance(self.trigger_type, Unset):
            trigger_type = UNSET
        elif isinstance(self.trigger_type, str):
            trigger_type = self.trigger_type
        elif isinstance(self.trigger_type, str):
            trigger_type = self.trigger_type
        else:
            trigger_type = self.trigger_type

        cron_expression: None | str | Unset
        if isinstance(self.cron_expression, Unset):
            cron_expression = UNSET
        else:
            cron_expression = self.cron_expression

        action_name: None | str | Unset
        if isinstance(self.action_name, Unset):
            action_name = UNSET
        else:
            action_name = self.action_name

        target_version: None | str | Unset
        if isinstance(self.target_version, Unset):
            target_version = UNSET
        else:
            target_version = self.target_version

        template_block: None | str | Unset
        if isinstance(self.template_block, Unset):
            template_block = UNSET
        else:
            template_block = self.template_block

        enqueue_reason: None | str | Unset
        if isinstance(self.enqueue_reason, Unset):
            enqueue_reason = UNSET
        else:
            enqueue_reason = self.enqueue_reason

        block_config_template: None | str | Unset
        if isinstance(self.block_config_template, Unset):
            block_config_template = UNSET
        else:
            block_config_template = self.block_config_template

        scope_expressions = self.scope_expressions

        auto_takeover = self.auto_takeover

        config_to_credential_mappings = self.config_to_credential_mappings

        target_organizations: list[str] | Unset = UNSET
        if not isinstance(self.target_organizations, Unset):
            target_organizations = []
            for target_organizations_item_data in self.target_organizations:
                target_organizations_item = str(target_organizations_item_data)
                target_organizations.append(target_organizations_item)

        target_workspaces: list[str] | Unset = UNSET
        if not isinstance(self.target_workspaces, Unset):
            target_workspaces = []
            for target_workspaces_item_data in self.target_workspaces:
                target_workspaces_item = str(target_workspaces_item_data)
                target_workspaces.append(target_workspaces_item)

        max_concurrent_percent = self.max_concurrent_percent

        failure_threshold_percent = self.failure_threshold_percent

        max_retries = self.max_retries

        maintenance_window: None | str | Unset
        if isinstance(self.maintenance_window, Unset):
            maintenance_window = UNSET
        elif isinstance(self.maintenance_window, UUID):
            maintenance_window = str(self.maintenance_window)
        else:
            maintenance_window = self.maintenance_window

        bypass_maintenance_window = self.bypass_maintenance_window

        notify_on_wave_blocked = self.notify_on_wave_blocked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if block_name is not UNSET:
            field_dict["block_name"] = block_name
        if active is not UNSET:
            field_dict["active"] = active
        if is_system_config is not UNSET:
            field_dict["is_system_config"] = is_system_config
        if trigger_type is not UNSET:
            field_dict["trigger_type"] = trigger_type
        if cron_expression is not UNSET:
            field_dict["cron_expression"] = cron_expression
        if action_name is not UNSET:
            field_dict["action_name"] = action_name
        if target_version is not UNSET:
            field_dict["target_version"] = target_version
        if template_block is not UNSET:
            field_dict["template_block"] = template_block
        if enqueue_reason is not UNSET:
            field_dict["enqueue_reason"] = enqueue_reason
        if block_config_template is not UNSET:
            field_dict["block_config_template"] = block_config_template
        if scope_expressions is not UNSET:
            field_dict["scope_expressions"] = scope_expressions
        if auto_takeover is not UNSET:
            field_dict["auto_takeover"] = auto_takeover
        if config_to_credential_mappings is not UNSET:
            field_dict["config_to_credential_mappings"] = config_to_credential_mappings
        if target_organizations is not UNSET:
            field_dict["target_organizations"] = target_organizations
        if target_workspaces is not UNSET:
            field_dict["target_workspaces"] = target_workspaces
        if max_concurrent_percent is not UNSET:
            field_dict["max_concurrent_percent"] = max_concurrent_percent
        if failure_threshold_percent is not UNSET:
            field_dict["failure_threshold_percent"] = failure_threshold_percent
        if max_retries is not UNSET:
            field_dict["max_retries"] = max_retries
        if maintenance_window is not UNSET:
            field_dict["maintenance_window"] = maintenance_window
        if bypass_maintenance_window is not UNSET:
            field_dict["bypass_maintenance_window"] = bypass_maintenance_window
        if notify_on_wave_blocked is not UNSET:
            field_dict["notify_on_wave_blocked"] = notify_on_wave_blocked

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.display_name, Unset):
            if isinstance(self.display_name, str):
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))
            else:
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))

        if not isinstance(self.labels, Unset):
            files.append(("labels", (None, str(self.labels).encode(), "text/plain")))

        if not isinstance(self.annotations, Unset):
            files.append(("annotations", (None, str(self.annotations).encode(), "text/plain")))

        if not isinstance(self.debug_mode, Unset):
            files.append(("debug_mode", (None, str(self.debug_mode).encode(), "text/plain")))

        if not isinstance(self.provider, Unset):
            files.append(("provider", (None, str(self.provider).encode(), "text/plain")))

        if not isinstance(self.provider_reference, Unset):
            if isinstance(self.provider_reference, str):
                files.append(("provider_reference", (None, str(self.provider_reference).encode(), "text/plain")))
            else:
                files.append(("provider_reference", (None, str(self.provider_reference).encode(), "text/plain")))

        if not isinstance(self.provider_id, Unset):
            if isinstance(self.provider_id, str):
                files.append(("provider_id", (None, str(self.provider_id).encode(), "text/plain")))
            else:
                files.append(("provider_id", (None, str(self.provider_id).encode(), "text/plain")))

        if not isinstance(self.state, Unset):
            files.append(("state", (None, str(self.state).encode(), "text/plain")))

        if not isinstance(self.state_reason, Unset):
            if isinstance(self.state_reason, str):
                files.append(("state_reason", (None, str(self.state_reason).encode(), "text/plain")))
            else:
                files.append(("state_reason", (None, str(self.state_reason).encode(), "text/plain")))

        if not isinstance(self.last_state, Unset):
            files.append(("last_state", (None, str(self.last_state).encode(), "text/plain")))

        if not isinstance(self.last_state_change, Unset):
            if isinstance(self.last_state_change, datetime.datetime):
                files.append(("last_state_change", (None, self.last_state_change.isoformat().encode(), "text/plain")))
            else:
                files.append(("last_state_change", (None, str(self.last_state_change).encode(), "text/plain")))

        if not isinstance(self.reconciliation_enabled, Unset):
            files.append(("reconciliation_enabled", (None, str(self.reconciliation_enabled).encode(), "text/plain")))

        if not isinstance(self.reconciliation_running, Unset):
            files.append(("reconciliation_running", (None, str(self.reconciliation_running).encode(), "text/plain")))

        if not isinstance(self.reconciliation_task_id, Unset):
            if isinstance(self.reconciliation_task_id, str):
                files.append(
                    ("reconciliation_task_id", (None, str(self.reconciliation_task_id).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("reconciliation_task_id", (None, str(self.reconciliation_task_id).encode(), "text/plain"))
                )

        if not isinstance(self.reconciliation_task_meta, Unset):
            files.append(
                ("reconciliation_task_meta", (None, str(self.reconciliation_task_meta).encode(), "text/plain"))
            )

        if not isinstance(self.discovery_enabled, Unset):
            files.append(("discovery_enabled", (None, str(self.discovery_enabled).encode(), "text/plain")))

        if not isinstance(self.discovery_running, Unset):
            files.append(("discovery_running", (None, str(self.discovery_running).encode(), "text/plain")))

        if not isinstance(self.discovery_task_id, Unset):
            if isinstance(self.discovery_task_id, str):
                files.append(("discovery_task_id", (None, str(self.discovery_task_id).encode(), "text/plain")))
            else:
                files.append(("discovery_task_id", (None, str(self.discovery_task_id).encode(), "text/plain")))

        if not isinstance(self.discovery_task_meta, Unset):
            files.append(("discovery_task_meta", (None, str(self.discovery_task_meta).encode(), "text/plain")))

        if not isinstance(self.repair_running, Unset):
            files.append(("repair_running", (None, str(self.repair_running).encode(), "text/plain")))

        if not isinstance(self.platform_service, Unset):
            files.append(("platform_service", (None, str(self.platform_service).encode(), "text/plain")))

        if not isinstance(self.repair_task_id, Unset):
            if isinstance(self.repair_task_id, str):
                files.append(("repair_task_id", (None, str(self.repair_task_id).encode(), "text/plain")))
            else:
                files.append(("repair_task_id", (None, str(self.repair_task_id).encode(), "text/plain")))

        if not isinstance(self.repair_task_meta, Unset):
            files.append(("repair_task_meta", (None, str(self.repair_task_meta).encode(), "text/plain")))

        if not isinstance(self.scope, Unset):
            files.append(("scope", (None, str(self.scope).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.conditions, Unset):
            files.append(("conditions", (None, str(self.conditions).encode(), "text/plain")))

        if not isinstance(self.tolerations, Unset):
            files.append(("tolerations", (None, str(self.tolerations).encode(), "text/plain")))

        if not isinstance(self.archived, Unset):
            files.append(("archived", (None, str(self.archived).encode(), "text/plain")))

        if not isinstance(self.archived_at, Unset):
            if isinstance(self.archived_at, datetime.datetime):
                files.append(("archived_at", (None, self.archived_at.isoformat().encode(), "text/plain")))
            else:
                files.append(("archived_at", (None, str(self.archived_at).encode(), "text/plain")))

        if not isinstance(self.archived_reason, Unset):
            if isinstance(self.archived_reason, str):
                files.append(("archived_reason", (None, str(self.archived_reason).encode(), "text/plain")))
            else:
                files.append(("archived_reason", (None, str(self.archived_reason).encode(), "text/plain")))

        if not isinstance(self.criticality, Unset):
            if isinstance(self.criticality, str):
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            elif isinstance(self.criticality, str):
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            else:
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))

        if not isinstance(self.target_availability, Unset):
            if isinstance(self.target_availability, str):
                files.append(("target_availability", (None, str(self.target_availability).encode(), "text/plain")))
            else:
                files.append(("target_availability", (None, str(self.target_availability).encode(), "text/plain")))

        if not isinstance(self.actual_availability, Unset):
            files.append(("actual_availability", (None, str(self.actual_availability).encode(), "text/plain")))

        if not isinstance(self.slo_target, Unset):
            if isinstance(self.slo_target, str):
                files.append(("slo_target", (None, str(self.slo_target).encode(), "text/plain")))
            else:
                files.append(("slo_target", (None, str(self.slo_target).encode(), "text/plain")))

        if not isinstance(self.slo_availability, Unset):
            files.append(("slo_availability", (None, str(self.slo_availability).encode(), "text/plain")))

        if not isinstance(self.sla_target, Unset):
            if isinstance(self.sla_target, str):
                files.append(("sla_target", (None, str(self.sla_target).encode(), "text/plain")))
            else:
                files.append(("sla_target", (None, str(self.sla_target).encode(), "text/plain")))

        if not isinstance(self.sla_availability, Unset):
            files.append(("sla_availability", (None, str(self.sla_availability).encode(), "text/plain")))

        if not isinstance(self.block_name, Unset):
            if isinstance(self.block_name, str):
                files.append(("block_name", (None, str(self.block_name).encode(), "text/plain")))
            else:
                files.append(("block_name", (None, str(self.block_name).encode(), "text/plain")))

        if not isinstance(self.active, Unset):
            files.append(("active", (None, str(self.active).encode(), "text/plain")))

        if not isinstance(self.is_system_config, Unset):
            files.append(("is_system_config", (None, str(self.is_system_config).encode(), "text/plain")))

        if not isinstance(self.trigger_type, Unset):
            if isinstance(self.trigger_type, str):
                files.append(("trigger_type", (None, str(self.trigger_type).encode(), "text/plain")))
            elif isinstance(self.trigger_type, str):
                files.append(("trigger_type", (None, str(self.trigger_type).encode(), "text/plain")))
            else:
                files.append(("trigger_type", (None, str(self.trigger_type).encode(), "text/plain")))

        if not isinstance(self.cron_expression, Unset):
            if isinstance(self.cron_expression, str):
                files.append(("cron_expression", (None, str(self.cron_expression).encode(), "text/plain")))
            else:
                files.append(("cron_expression", (None, str(self.cron_expression).encode(), "text/plain")))

        if not isinstance(self.action_name, Unset):
            if isinstance(self.action_name, str):
                files.append(("action_name", (None, str(self.action_name).encode(), "text/plain")))
            else:
                files.append(("action_name", (None, str(self.action_name).encode(), "text/plain")))

        if not isinstance(self.target_version, Unset):
            if isinstance(self.target_version, str):
                files.append(("target_version", (None, str(self.target_version).encode(), "text/plain")))
            else:
                files.append(("target_version", (None, str(self.target_version).encode(), "text/plain")))

        if not isinstance(self.template_block, Unset):
            if isinstance(self.template_block, str):
                files.append(("template_block", (None, str(self.template_block).encode(), "text/plain")))
            else:
                files.append(("template_block", (None, str(self.template_block).encode(), "text/plain")))

        if not isinstance(self.enqueue_reason, Unset):
            if isinstance(self.enqueue_reason, str):
                files.append(("enqueue_reason", (None, str(self.enqueue_reason).encode(), "text/plain")))
            else:
                files.append(("enqueue_reason", (None, str(self.enqueue_reason).encode(), "text/plain")))

        if not isinstance(self.block_config_template, Unset):
            if isinstance(self.block_config_template, str):
                files.append(("block_config_template", (None, str(self.block_config_template).encode(), "text/plain")))
            else:
                files.append(("block_config_template", (None, str(self.block_config_template).encode(), "text/plain")))

        if not isinstance(self.scope_expressions, Unset):
            files.append(("scope_expressions", (None, str(self.scope_expressions).encode(), "text/plain")))

        if not isinstance(self.auto_takeover, Unset):
            files.append(("auto_takeover", (None, str(self.auto_takeover).encode(), "text/plain")))

        if not isinstance(self.config_to_credential_mappings, Unset):
            files.append(
                (
                    "config_to_credential_mappings",
                    (None, str(self.config_to_credential_mappings).encode(), "text/plain"),
                )
            )

        if not isinstance(self.target_organizations, Unset):
            for target_organizations_item_element in self.target_organizations:
                files.append(("target_organizations", (None, str(target_organizations_item_element), "text/plain")))

        if not isinstance(self.target_workspaces, Unset):
            for target_workspaces_item_element in self.target_workspaces:
                files.append(("target_workspaces", (None, str(target_workspaces_item_element), "text/plain")))

        if not isinstance(self.max_concurrent_percent, Unset):
            files.append(("max_concurrent_percent", (None, str(self.max_concurrent_percent).encode(), "text/plain")))

        if not isinstance(self.failure_threshold_percent, Unset):
            files.append(
                ("failure_threshold_percent", (None, str(self.failure_threshold_percent).encode(), "text/plain"))
            )

        if not isinstance(self.max_retries, Unset):
            files.append(("max_retries", (None, str(self.max_retries).encode(), "text/plain")))

        if not isinstance(self.maintenance_window, Unset):
            if isinstance(self.maintenance_window, UUID):
                files.append(("maintenance_window", (None, str(self.maintenance_window), "text/plain")))
            else:
                files.append(("maintenance_window", (None, str(self.maintenance_window).encode(), "text/plain")))

        if not isinstance(self.bypass_maintenance_window, Unset):
            files.append(
                ("bypass_maintenance_window", (None, str(self.bypass_maintenance_window).encode(), "text/plain"))
            )

        if not isinstance(self.notify_on_wave_blocked, Unset):
            files.append(("notify_on_wave_blocked", (None, str(self.notify_on_wave_blocked).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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
        kind: BlockRolloutConfigKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_block_rollout_config_kind_enum(_kind)

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

        def _parse_block_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_name = _parse_block_name(d.pop("block_name", UNSET))

        active = d.pop("active", UNSET)

        is_system_config = d.pop("is_system_config", UNSET)

        def _parse_trigger_type(data: object) -> BlankEnum | None | TriggerTypeEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trigger_type_type_0 = check_trigger_type_enum(data)

                return trigger_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trigger_type_type_1 = check_blank_enum(data)

                return trigger_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | None | TriggerTypeEnum | Unset, data)

        trigger_type = _parse_trigger_type(d.pop("trigger_type", UNSET))

        def _parse_cron_expression(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cron_expression = _parse_cron_expression(d.pop("cron_expression", UNSET))

        def _parse_action_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action_name = _parse_action_name(d.pop("action_name", UNSET))

        def _parse_target_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_version = _parse_target_version(d.pop("target_version", UNSET))

        def _parse_template_block(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_block = _parse_template_block(d.pop("template_block", UNSET))

        def _parse_enqueue_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        enqueue_reason = _parse_enqueue_reason(d.pop("enqueue_reason", UNSET))

        def _parse_block_config_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_config_template = _parse_block_config_template(d.pop("block_config_template", UNSET))

        scope_expressions = d.pop("scope_expressions", UNSET)

        auto_takeover = d.pop("auto_takeover", UNSET)

        config_to_credential_mappings = d.pop("config_to_credential_mappings", UNSET)

        _target_organizations = d.pop("target_organizations", UNSET)
        target_organizations: list[UUID] | Unset = UNSET
        if _target_organizations is not UNSET:
            target_organizations = []
            for target_organizations_item_data in _target_organizations:
                target_organizations_item = UUID(target_organizations_item_data)

                target_organizations.append(target_organizations_item)

        _target_workspaces = d.pop("target_workspaces", UNSET)
        target_workspaces: list[UUID] | Unset = UNSET
        if _target_workspaces is not UNSET:
            target_workspaces = []
            for target_workspaces_item_data in _target_workspaces:
                target_workspaces_item = UUID(target_workspaces_item_data)

                target_workspaces.append(target_workspaces_item)

        max_concurrent_percent = d.pop("max_concurrent_percent", UNSET)

        failure_threshold_percent = d.pop("failure_threshold_percent", UNSET)

        max_retries = d.pop("max_retries", UNSET)

        def _parse_maintenance_window(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                maintenance_window_type_0 = UUID(data)

                return maintenance_window_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        maintenance_window = _parse_maintenance_window(d.pop("maintenance_window", UNSET))

        bypass_maintenance_window = d.pop("bypass_maintenance_window", UNSET)

        notify_on_wave_blocked = d.pop("notify_on_wave_blocked", UNSET)

        patched_block_rollout_config_request = cls(
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
            block_name=block_name,
            active=active,
            is_system_config=is_system_config,
            trigger_type=trigger_type,
            cron_expression=cron_expression,
            action_name=action_name,
            target_version=target_version,
            template_block=template_block,
            enqueue_reason=enqueue_reason,
            block_config_template=block_config_template,
            scope_expressions=scope_expressions,
            auto_takeover=auto_takeover,
            config_to_credential_mappings=config_to_credential_mappings,
            target_organizations=target_organizations,
            target_workspaces=target_workspaces,
            max_concurrent_percent=max_concurrent_percent,
            failure_threshold_percent=failure_threshold_percent,
            max_retries=max_retries,
            maintenance_window=maintenance_window,
            bypass_maintenance_window=bypass_maintenance_window,
            notify_on_wave_blocked=notify_on_wave_blocked,
        )

        patched_block_rollout_config_request.additional_properties = d
        return patched_block_rollout_config_request

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
