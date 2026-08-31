from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.purpose_f3b_enum import PurposeF3BEnum, check_purpose_f3b_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..models.workspace_endpoint_monitoring_mode_enum import (
    WorkspaceEndpointMonitoringModeEnum,
    check_workspace_endpoint_monitoring_mode_enum,
)
from ..models.workspace_kind_enum import WorkspaceKindEnum, check_workspace_kind_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_simple import BlockSimple
    from ..models.organization_membership_simple import OrganizationMembershipSimple
    from ..models.organization_simple import OrganizationSimple
    from ..models.pop_simple import PopSimple
    from ..models.workspace_created import WorkspaceCreated
    from ..models.workspace_deleted_by_user_type_0 import WorkspaceDeletedByUserType0
    from ..models.workspace_encryption_credential import WorkspaceEncryptionCredential
    from ..models.workspace_last_action_run_type_0 import WorkspaceLastActionRunType0
    from ..models.workspace_simple import WorkspaceSimple
    from ..models.workspace_snapshot import WorkspaceSnapshot
    from ..models.workspace_workspace_type_0 import WorkspaceWorkspaceType0


T = TypeVar("T", bound="Workspace")


@_attrs_define
class Workspace:
    """Full Workspace serializer for CRUD operations.

    Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
    per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

    Supports template-based creation using template name (slug).
    Template can be org-specific or system-wide (organization=null).

        Attributes:
            id (UUID):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            deleted_by_user (None | WorkspaceDeletedByUserType0):
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
            effective_criticality (EffectiveCriticalityEnum | None):
            organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            workspace (None | WorkspaceWorkspaceType0):
            created (WorkspaceCreated):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            last_action_run (None | WorkspaceLastActionRunType0):
            git_branch (None | str):
            git_commit_short_sha (None | str):
            edge_endpoint_monitor (bool): Auto-set when workspace Region has loadbalancer capability. If true, agent
                monitors PoP reachability ICMP endpoints (Spec 526). Not user-editable.
            monitoring_workspace_allowlist (list[WorkspaceSimple]):
            snapshot (WorkspaceSnapshot):
            git_web_url (None | str):
            git_http_url (None | str):
            git_ssh_url (None | str):
            workspace_poly_raw (None | str):
            logs_discovered_up_to_commit (None | str):
            git_reconciled_commit (None | str):
            blocks (list[BlockSimple]):
            credential (WorkspaceEncryptionCredential): Serializer for workspace encryption credentials - includes SSH keys
                for CLI.
            pop (PopSimple): Simple serializer for embedding Pop in other serializers.
            active_maintenances (list[Any]):
            workspace_version (None | str):
            workspace_app_version (None | str):
            owner (OrganizationMembershipSimple): Simple read-only serializer for OrganizationMembership — used in
                workspace/org owner field.
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
            discovery_enabled (bool | Unset):
            platform_service (bool | Unset):
            scope (ScopeEnum | Unset): * `system` - System
                * `user` - User
            kind (WorkspaceKindEnum | Unset): * `polycrate` - Polycrate
                * `generic` - Generic
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
            gitlab_project_id (int | None | Unset):
            gitlab_project_url (None | str | Unset): GitLab project URL (e.g., https://gitlab.com/user/project)
            on_premise (bool | Unset): If true, this workspace runs in a customer-managed environment that is not reachable
                from ayedo infrastructure. Endpoints in this workspace will only be monitored by the workspace's own agent —
                external global monitors are excluded. Also disables K8sCluster API server reachability checks for clusters in
                this workspace.
            endpoint_monitoring_mode (WorkspaceEndpointMonitoringModeEnum | Unset): * `auto` - AUTO - Monitor everything
                * `organization_only` - ORGANIZATION_ONLY - Only monitor endpoints from same organization
                * `workspace_only` - WORKSPACE_ONLY - Only monitor endpoints from same workspace
                * `pop_only` - POP_ONLY - Only monitor endpoints from same pop
            global_endpoint_monitor (bool | Unset): If true, the agent of this workspace receives endpoints from OTHER
                workspaces (subject to endpoint_monitoring_mode and target workspace's monitoring_workspace_allowlist). If false
                (default), agent only monitors own workspace's endpoints.
            notifications_enabled (bool | Unset):
            backup_enabled (bool | Unset): If false, ayedo does not evaluate workspace-level backup health
                (WORKSPACE_BACKUP_SCHEDULE_MISSING, WORKSPACE_BACKUP_SCHEDULE_OVERDUE, WORKSPACE_BACKUP_MISSING). Use when ayedo
                is not responsible for backups. May later gate related backup features; bucket provisioning stays independent
                for now.
            has_incompatible_kubeconfig (bool | Unset):
            endpoint_monitors (list[UUID] | Unset):
            secrets_poly_raw (None | str | Unset): Content of the secrets.poly file (sensitive data)
            workspace_inventory_raw (None | str | Unset):
            encrypted (bool | Unset): Indicates if workspace is encrypted (contains .workspace-encrypted file)
            description (None | str | Unset): Short free-text description of this workspace
            purpose (BlankEnum | None | PurposeF3BEnum | Unset): Purpose of this workspace (production, development,
                staging, qa, infrastructure, platform)

                * `production` - Production
                * `development` - Development
                * `staging` - Staging
                * `qa` - QA
                * `infrastructure` - Infrastructure
                * `platform` - Platform
            urls (Any | Unset): Named URLs for this workspace, e.g. [{"name": "Runbook", "url": "https://..."}]
            readme_md (None | str | Unset):
            alternative_name (None | str | Unset):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    deleted_by_user: None | WorkspaceDeletedByUserType0
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
    effective_criticality: EffectiveCriticalityEnum | None
    organization: OrganizationSimple
    workspace: None | WorkspaceWorkspaceType0
    created: WorkspaceCreated
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    last_action_run: None | WorkspaceLastActionRunType0
    git_branch: None | str
    git_commit_short_sha: None | str
    edge_endpoint_monitor: bool
    monitoring_workspace_allowlist: list[WorkspaceSimple]
    snapshot: WorkspaceSnapshot
    git_web_url: None | str
    git_http_url: None | str
    git_ssh_url: None | str
    workspace_poly_raw: None | str
    logs_discovered_up_to_commit: None | str
    git_reconciled_commit: None | str
    blocks: list[BlockSimple]
    credential: WorkspaceEncryptionCredential
    pop: PopSimple
    active_maintenances: list[Any]
    workspace_version: None | str
    workspace_app_version: None | str
    owner: OrganizationMembershipSimple
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    discovery_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    scope: ScopeEnum | Unset = UNSET
    kind: WorkspaceKindEnum | Unset = UNSET
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
    gitlab_project_id: int | None | Unset = UNSET
    gitlab_project_url: None | str | Unset = UNSET
    on_premise: bool | Unset = UNSET
    endpoint_monitoring_mode: WorkspaceEndpointMonitoringModeEnum | Unset = UNSET
    global_endpoint_monitor: bool | Unset = UNSET
    notifications_enabled: bool | Unset = UNSET
    backup_enabled: bool | Unset = UNSET
    has_incompatible_kubeconfig: bool | Unset = UNSET
    endpoint_monitors: list[UUID] | Unset = UNSET
    secrets_poly_raw: None | str | Unset = UNSET
    workspace_inventory_raw: None | str | Unset = UNSET
    encrypted: bool | Unset = UNSET
    description: None | str | Unset = UNSET
    purpose: BlankEnum | None | PurposeF3BEnum | Unset = UNSET
    urls: Any | Unset = UNSET
    readme_md: None | str | Unset = UNSET
    alternative_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workspace_deleted_by_user_type_0 import WorkspaceDeletedByUserType0
        from ..models.workspace_last_action_run_type_0 import WorkspaceLastActionRunType0
        from ..models.workspace_workspace_type_0 import WorkspaceWorkspaceType0

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
        if isinstance(self.deleted_by_user, WorkspaceDeletedByUserType0):
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

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        organization = self.organization.to_dict()

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, WorkspaceWorkspaceType0):
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
        if isinstance(self.last_action_run, WorkspaceLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        git_branch: None | str
        git_branch = self.git_branch

        git_commit_short_sha: None | str
        git_commit_short_sha = self.git_commit_short_sha

        edge_endpoint_monitor = self.edge_endpoint_monitor

        monitoring_workspace_allowlist = []
        for monitoring_workspace_allowlist_item_data in self.monitoring_workspace_allowlist:
            monitoring_workspace_allowlist_item = monitoring_workspace_allowlist_item_data.to_dict()
            monitoring_workspace_allowlist.append(monitoring_workspace_allowlist_item)

        snapshot = self.snapshot.to_dict()

        git_web_url: None | str
        git_web_url = self.git_web_url

        git_http_url: None | str
        git_http_url = self.git_http_url

        git_ssh_url: None | str
        git_ssh_url = self.git_ssh_url

        workspace_poly_raw: None | str
        workspace_poly_raw = self.workspace_poly_raw

        logs_discovered_up_to_commit: None | str
        logs_discovered_up_to_commit = self.logs_discovered_up_to_commit

        git_reconciled_commit: None | str
        git_reconciled_commit = self.git_reconciled_commit

        blocks = []
        for blocks_item_data in self.blocks:
            blocks_item = blocks_item_data.to_dict()
            blocks.append(blocks_item)

        credential = self.credential.to_dict()

        pop = self.pop.to_dict()

        active_maintenances = self.active_maintenances

        workspace_version: None | str
        workspace_version = self.workspace_version

        workspace_app_version: None | str
        workspace_app_version = self.workspace_app_version

        owner = self.owner.to_dict()

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

        discovery_enabled = self.discovery_enabled

        platform_service = self.platform_service

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

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

        gitlab_project_id: int | None | Unset
        if isinstance(self.gitlab_project_id, Unset):
            gitlab_project_id = UNSET
        else:
            gitlab_project_id = self.gitlab_project_id

        gitlab_project_url: None | str | Unset
        if isinstance(self.gitlab_project_url, Unset):
            gitlab_project_url = UNSET
        else:
            gitlab_project_url = self.gitlab_project_url

        on_premise = self.on_premise

        endpoint_monitoring_mode: str | Unset = UNSET
        if not isinstance(self.endpoint_monitoring_mode, Unset):
            endpoint_monitoring_mode = self.endpoint_monitoring_mode

        global_endpoint_monitor = self.global_endpoint_monitor

        notifications_enabled = self.notifications_enabled

        backup_enabled = self.backup_enabled

        has_incompatible_kubeconfig = self.has_incompatible_kubeconfig

        endpoint_monitors: list[str] | Unset = UNSET
        if not isinstance(self.endpoint_monitors, Unset):
            endpoint_monitors = []
            for endpoint_monitors_item_data in self.endpoint_monitors:
                endpoint_monitors_item = str(endpoint_monitors_item_data)
                endpoint_monitors.append(endpoint_monitors_item)

        secrets_poly_raw: None | str | Unset
        if isinstance(self.secrets_poly_raw, Unset):
            secrets_poly_raw = UNSET
        else:
            secrets_poly_raw = self.secrets_poly_raw

        workspace_inventory_raw: None | str | Unset
        if isinstance(self.workspace_inventory_raw, Unset):
            workspace_inventory_raw = UNSET
        else:
            workspace_inventory_raw = self.workspace_inventory_raw

        encrypted = self.encrypted

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        purpose: None | str | Unset
        if isinstance(self.purpose, Unset):
            purpose = UNSET
        elif isinstance(self.purpose, str):
            purpose = self.purpose
        elif isinstance(self.purpose, str):
            purpose = self.purpose
        else:
            purpose = self.purpose

        urls = self.urls

        readme_md: None | str | Unset
        if isinstance(self.readme_md, Unset):
            readme_md = UNSET
        else:
            readme_md = self.readme_md

        alternative_name: None | str | Unset
        if isinstance(self.alternative_name, Unset):
            alternative_name = UNSET
        else:
            alternative_name = self.alternative_name

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
                "git_branch": git_branch,
                "git_commit_short_sha": git_commit_short_sha,
                "edge_endpoint_monitor": edge_endpoint_monitor,
                "monitoring_workspace_allowlist": monitoring_workspace_allowlist,
                "snapshot": snapshot,
                "git_web_url": git_web_url,
                "git_http_url": git_http_url,
                "git_ssh_url": git_ssh_url,
                "workspace_poly_raw": workspace_poly_raw,
                "logs_discovered_up_to_commit": logs_discovered_up_to_commit,
                "git_reconciled_commit": git_reconciled_commit,
                "blocks": blocks,
                "credential": credential,
                "pop": pop,
                "active_maintenances": active_maintenances,
                "workspace_version": workspace_version,
                "workspace_app_version": workspace_app_version,
                "owner": owner,
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
        if discovery_enabled is not UNSET:
            field_dict["discovery_enabled"] = discovery_enabled
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if scope is not UNSET:
            field_dict["scope"] = scope
        if kind is not UNSET:
            field_dict["kind"] = kind
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
        if gitlab_project_id is not UNSET:
            field_dict["gitlab_project_id"] = gitlab_project_id
        if gitlab_project_url is not UNSET:
            field_dict["gitlab_project_url"] = gitlab_project_url
        if on_premise is not UNSET:
            field_dict["on_premise"] = on_premise
        if endpoint_monitoring_mode is not UNSET:
            field_dict["endpoint_monitoring_mode"] = endpoint_monitoring_mode
        if global_endpoint_monitor is not UNSET:
            field_dict["global_endpoint_monitor"] = global_endpoint_monitor
        if notifications_enabled is not UNSET:
            field_dict["notifications_enabled"] = notifications_enabled
        if backup_enabled is not UNSET:
            field_dict["backup_enabled"] = backup_enabled
        if has_incompatible_kubeconfig is not UNSET:
            field_dict["has_incompatible_kubeconfig"] = has_incompatible_kubeconfig
        if endpoint_monitors is not UNSET:
            field_dict["endpoint_monitors"] = endpoint_monitors
        if secrets_poly_raw is not UNSET:
            field_dict["secrets_poly_raw"] = secrets_poly_raw
        if workspace_inventory_raw is not UNSET:
            field_dict["workspace_inventory_raw"] = workspace_inventory_raw
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if description is not UNSET:
            field_dict["description"] = description
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if urls is not UNSET:
            field_dict["urls"] = urls
        if readme_md is not UNSET:
            field_dict["readme_md"] = readme_md
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.block_simple import BlockSimple
        from ..models.organization_membership_simple import OrganizationMembershipSimple
        from ..models.organization_simple import OrganizationSimple
        from ..models.pop_simple import PopSimple
        from ..models.workspace_created import WorkspaceCreated
        from ..models.workspace_deleted_by_user_type_0 import WorkspaceDeletedByUserType0
        from ..models.workspace_encryption_credential import WorkspaceEncryptionCredential
        from ..models.workspace_last_action_run_type_0 import WorkspaceLastActionRunType0
        from ..models.workspace_simple import WorkspaceSimple
        from ..models.workspace_snapshot import WorkspaceSnapshot
        from ..models.workspace_workspace_type_0 import WorkspaceWorkspaceType0

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

        def _parse_deleted_by_user(data: object) -> None | WorkspaceDeletedByUserType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = WorkspaceDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WorkspaceDeletedByUserType0, data)

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

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        def _parse_workspace(data: object) -> None | WorkspaceWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = WorkspaceWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WorkspaceWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = WorkspaceCreated.from_dict(d.pop("created"))

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

        def _parse_last_action_run(data: object) -> None | WorkspaceLastActionRunType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = WorkspaceLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WorkspaceLastActionRunType0, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        def _parse_git_branch(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        git_branch = _parse_git_branch(d.pop("git_branch"))

        def _parse_git_commit_short_sha(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        git_commit_short_sha = _parse_git_commit_short_sha(d.pop("git_commit_short_sha"))

        edge_endpoint_monitor = d.pop("edge_endpoint_monitor")

        monitoring_workspace_allowlist = []
        _monitoring_workspace_allowlist = d.pop("monitoring_workspace_allowlist")
        for monitoring_workspace_allowlist_item_data in _monitoring_workspace_allowlist:
            monitoring_workspace_allowlist_item = WorkspaceSimple.from_dict(monitoring_workspace_allowlist_item_data)

            monitoring_workspace_allowlist.append(monitoring_workspace_allowlist_item)

        snapshot = WorkspaceSnapshot.from_dict(d.pop("snapshot"))

        def _parse_git_web_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        git_web_url = _parse_git_web_url(d.pop("git_web_url"))

        def _parse_git_http_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        git_http_url = _parse_git_http_url(d.pop("git_http_url"))

        def _parse_git_ssh_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        git_ssh_url = _parse_git_ssh_url(d.pop("git_ssh_url"))

        def _parse_workspace_poly_raw(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        workspace_poly_raw = _parse_workspace_poly_raw(d.pop("workspace_poly_raw"))

        def _parse_logs_discovered_up_to_commit(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logs_discovered_up_to_commit = _parse_logs_discovered_up_to_commit(d.pop("logs_discovered_up_to_commit"))

        def _parse_git_reconciled_commit(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        git_reconciled_commit = _parse_git_reconciled_commit(d.pop("git_reconciled_commit"))

        blocks = []
        _blocks = d.pop("blocks")
        for blocks_item_data in _blocks:
            blocks_item = BlockSimple.from_dict(blocks_item_data)

            blocks.append(blocks_item)

        credential = WorkspaceEncryptionCredential.from_dict(d.pop("credential"))

        pop = PopSimple.from_dict(d.pop("pop"))

        active_maintenances = cast(list[Any], d.pop("active_maintenances"))

        def _parse_workspace_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        workspace_version = _parse_workspace_version(d.pop("workspace_version"))

        def _parse_workspace_app_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        workspace_app_version = _parse_workspace_app_version(d.pop("workspace_app_version"))

        owner = OrganizationMembershipSimple.from_dict(d.pop("owner"))

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

        discovery_enabled = d.pop("discovery_enabled", UNSET)

        platform_service = d.pop("platform_service", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ScopeEnum | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_scope_enum(_scope)

        _kind = d.pop("kind", UNSET)
        kind: WorkspaceKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_workspace_kind_enum(_kind)

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

        def _parse_gitlab_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        gitlab_project_id = _parse_gitlab_project_id(d.pop("gitlab_project_id", UNSET))

        def _parse_gitlab_project_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gitlab_project_url = _parse_gitlab_project_url(d.pop("gitlab_project_url", UNSET))

        on_premise = d.pop("on_premise", UNSET)

        _endpoint_monitoring_mode = d.pop("endpoint_monitoring_mode", UNSET)
        endpoint_monitoring_mode: WorkspaceEndpointMonitoringModeEnum | Unset
        if isinstance(_endpoint_monitoring_mode, Unset):
            endpoint_monitoring_mode = UNSET
        else:
            endpoint_monitoring_mode = check_workspace_endpoint_monitoring_mode_enum(_endpoint_monitoring_mode)

        global_endpoint_monitor = d.pop("global_endpoint_monitor", UNSET)

        notifications_enabled = d.pop("notifications_enabled", UNSET)

        backup_enabled = d.pop("backup_enabled", UNSET)

        has_incompatible_kubeconfig = d.pop("has_incompatible_kubeconfig", UNSET)

        _endpoint_monitors = d.pop("endpoint_monitors", UNSET)
        endpoint_monitors: list[UUID] | Unset = UNSET
        if _endpoint_monitors is not UNSET:
            endpoint_monitors = []
            for endpoint_monitors_item_data in _endpoint_monitors:
                endpoint_monitors_item = UUID(endpoint_monitors_item_data)

                endpoint_monitors.append(endpoint_monitors_item)

        def _parse_secrets_poly_raw(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secrets_poly_raw = _parse_secrets_poly_raw(d.pop("secrets_poly_raw", UNSET))

        def _parse_workspace_inventory_raw(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workspace_inventory_raw = _parse_workspace_inventory_raw(d.pop("workspace_inventory_raw", UNSET))

        encrypted = d.pop("encrypted", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_purpose(data: object) -> BlankEnum | None | PurposeF3BEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purpose_type_0 = check_purpose_f3b_enum(data)

                return purpose_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purpose_type_1 = check_blank_enum(data)

                return purpose_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | None | PurposeF3BEnum | Unset, data)

        purpose = _parse_purpose(d.pop("purpose", UNSET))

        urls = d.pop("urls", UNSET)

        def _parse_readme_md(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        readme_md = _parse_readme_md(d.pop("readme_md", UNSET))

        def _parse_alternative_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alternative_name = _parse_alternative_name(d.pop("alternative_name", UNSET))

        workspace = cls(
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
            git_branch=git_branch,
            git_commit_short_sha=git_commit_short_sha,
            edge_endpoint_monitor=edge_endpoint_monitor,
            monitoring_workspace_allowlist=monitoring_workspace_allowlist,
            snapshot=snapshot,
            git_web_url=git_web_url,
            git_http_url=git_http_url,
            git_ssh_url=git_ssh_url,
            workspace_poly_raw=workspace_poly_raw,
            logs_discovered_up_to_commit=logs_discovered_up_to_commit,
            git_reconciled_commit=git_reconciled_commit,
            blocks=blocks,
            credential=credential,
            pop=pop,
            active_maintenances=active_maintenances,
            workspace_version=workspace_version,
            workspace_app_version=workspace_app_version,
            owner=owner,
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            provider_id=provider_id,
            reconciliation_enabled=reconciliation_enabled,
            discovery_enabled=discovery_enabled,
            platform_service=platform_service,
            scope=scope,
            kind=kind,
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
            gitlab_project_id=gitlab_project_id,
            gitlab_project_url=gitlab_project_url,
            on_premise=on_premise,
            endpoint_monitoring_mode=endpoint_monitoring_mode,
            global_endpoint_monitor=global_endpoint_monitor,
            notifications_enabled=notifications_enabled,
            backup_enabled=backup_enabled,
            has_incompatible_kubeconfig=has_incompatible_kubeconfig,
            endpoint_monitors=endpoint_monitors,
            secrets_poly_raw=secrets_poly_raw,
            workspace_inventory_raw=workspace_inventory_raw,
            encrypted=encrypted,
            description=description,
            purpose=purpose,
            urls=urls,
            readme_md=readme_md,
            alternative_name=alternative_name,
        )

        workspace.additional_properties = d
        return workspace

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
