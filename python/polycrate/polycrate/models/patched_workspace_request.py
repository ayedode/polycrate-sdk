from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.purpose_f3b_enum import PurposeF3BEnum, check_purpose_f3b_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..models.workspace_endpoint_monitoring_mode_enum import (
    WorkspaceEndpointMonitoringModeEnum,
    check_workspace_endpoint_monitoring_mode_enum,
)
from ..models.workspace_kind_enum import WorkspaceKindEnum, check_workspace_kind_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedWorkspaceRequest")


@_attrs_define
class PatchedWorkspaceRequest:
    """Full Workspace serializer for CRUD operations.

    Inherits ManagedObject fields (last_action_run, icon_url, SLO/SLA, etc.)
    per polycrate spec inspect 36 — same pattern as K8sClusterSerializer.

    Supports template-based creation using template name (slug).
    Template can be org-specific or system-wide (organization=null).

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
            monitoring_workspace_allowlist_ids (list[UUID] | Unset):
            notifications_enabled (bool | Unset):
            backup_enabled (bool | Unset): If false, ayedo does not evaluate workspace-level backup health
                (WORKSPACE_BACKUP_SCHEDULE_MISSING, WORKSPACE_BACKUP_SCHEDULE_OVERDUE, WORKSPACE_BACKUP_MISSING). Use when ayedo
                is not responsible for backups. May later gate related backup features; bucket provisioning stays independent
                for now.
            has_incompatible_kubeconfig (bool | Unset):
            endpoint_monitors (list[UUID] | Unset):
            secrets_poly_raw (None | str | Unset): Content of the secrets.poly file (sensitive data)
            workspace_inventory_raw (None | str | Unset):
            organization_id (None | Unset | UUID):
            encrypted (bool | Unset): Indicates if workspace is encrypted (contains .workspace-encrypted file)
            pop_id (UUID | Unset):
            template (None | str | Unset): Name of the workspace template to use (write-only)
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
            owner_id (int | None | Unset):
            readme_md (None | str | Unset):
            alternative_name (None | str | Unset):
    """

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
    monitoring_workspace_allowlist_ids: list[UUID] | Unset = UNSET
    notifications_enabled: bool | Unset = UNSET
    backup_enabled: bool | Unset = UNSET
    has_incompatible_kubeconfig: bool | Unset = UNSET
    endpoint_monitors: list[UUID] | Unset = UNSET
    secrets_poly_raw: None | str | Unset = UNSET
    workspace_inventory_raw: None | str | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    encrypted: bool | Unset = UNSET
    pop_id: UUID | Unset = UNSET
    template: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    purpose: BlankEnum | None | PurposeF3BEnum | Unset = UNSET
    urls: Any | Unset = UNSET
    owner_id: int | None | Unset = UNSET
    readme_md: None | str | Unset = UNSET
    alternative_name: None | str | Unset = UNSET
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

        monitoring_workspace_allowlist_ids: list[str] | Unset = UNSET
        if not isinstance(self.monitoring_workspace_allowlist_ids, Unset):
            monitoring_workspace_allowlist_ids = []
            for monitoring_workspace_allowlist_ids_item_data in self.monitoring_workspace_allowlist_ids:
                monitoring_workspace_allowlist_ids_item = str(monitoring_workspace_allowlist_ids_item_data)
                monitoring_workspace_allowlist_ids.append(monitoring_workspace_allowlist_ids_item)

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

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        encrypted = self.encrypted

        pop_id: str | Unset = UNSET
        if not isinstance(self.pop_id, Unset):
            pop_id = str(self.pop_id)

        template: None | str | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        else:
            template = self.template

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

        owner_id: int | None | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

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
        if monitoring_workspace_allowlist_ids is not UNSET:
            field_dict["monitoring_workspace_allowlist_ids"] = monitoring_workspace_allowlist_ids
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
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if pop_id is not UNSET:
            field_dict["pop_id"] = pop_id
        if template is not UNSET:
            field_dict["template"] = template
        if description is not UNSET:
            field_dict["description"] = description
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if urls is not UNSET:
            field_dict["urls"] = urls
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if readme_md is not UNSET:
            field_dict["readme_md"] = readme_md
        if alternative_name is not UNSET:
            field_dict["alternative_name"] = alternative_name

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

        if not isinstance(self.reconciliation_enabled, Unset):
            files.append(("reconciliation_enabled", (None, str(self.reconciliation_enabled).encode(), "text/plain")))

        if not isinstance(self.discovery_enabled, Unset):
            files.append(("discovery_enabled", (None, str(self.discovery_enabled).encode(), "text/plain")))

        if not isinstance(self.platform_service, Unset):
            files.append(("platform_service", (None, str(self.platform_service).encode(), "text/plain")))

        if not isinstance(self.scope, Unset):
            files.append(("scope", (None, str(self.scope).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

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

        if not isinstance(self.gitlab_project_id, Unset):
            if isinstance(self.gitlab_project_id, int):
                files.append(("gitlab_project_id", (None, str(self.gitlab_project_id).encode(), "text/plain")))
            else:
                files.append(("gitlab_project_id", (None, str(self.gitlab_project_id).encode(), "text/plain")))

        if not isinstance(self.gitlab_project_url, Unset):
            if isinstance(self.gitlab_project_url, str):
                files.append(("gitlab_project_url", (None, str(self.gitlab_project_url).encode(), "text/plain")))
            else:
                files.append(("gitlab_project_url", (None, str(self.gitlab_project_url).encode(), "text/plain")))

        if not isinstance(self.on_premise, Unset):
            files.append(("on_premise", (None, str(self.on_premise).encode(), "text/plain")))

        if not isinstance(self.endpoint_monitoring_mode, Unset):
            files.append(
                ("endpoint_monitoring_mode", (None, str(self.endpoint_monitoring_mode).encode(), "text/plain"))
            )

        if not isinstance(self.global_endpoint_monitor, Unset):
            files.append(("global_endpoint_monitor", (None, str(self.global_endpoint_monitor).encode(), "text/plain")))

        if not isinstance(self.monitoring_workspace_allowlist_ids, Unset):
            for monitoring_workspace_allowlist_ids_item_element in self.monitoring_workspace_allowlist_ids:
                files.append(
                    (
                        "monitoring_workspace_allowlist_ids",
                        (None, str(monitoring_workspace_allowlist_ids_item_element), "text/plain"),
                    )
                )

        if not isinstance(self.notifications_enabled, Unset):
            files.append(("notifications_enabled", (None, str(self.notifications_enabled).encode(), "text/plain")))

        if not isinstance(self.backup_enabled, Unset):
            files.append(("backup_enabled", (None, str(self.backup_enabled).encode(), "text/plain")))

        if not isinstance(self.has_incompatible_kubeconfig, Unset):
            files.append(
                ("has_incompatible_kubeconfig", (None, str(self.has_incompatible_kubeconfig).encode(), "text/plain"))
            )

        if not isinstance(self.endpoint_monitors, Unset):
            for endpoint_monitors_item_element in self.endpoint_monitors:
                files.append(("endpoint_monitors", (None, str(endpoint_monitors_item_element), "text/plain")))

        if not isinstance(self.secrets_poly_raw, Unset):
            if isinstance(self.secrets_poly_raw, str):
                files.append(("secrets_poly_raw", (None, str(self.secrets_poly_raw).encode(), "text/plain")))
            else:
                files.append(("secrets_poly_raw", (None, str(self.secrets_poly_raw).encode(), "text/plain")))

        if not isinstance(self.workspace_inventory_raw, Unset):
            if isinstance(self.workspace_inventory_raw, str):
                files.append(
                    ("workspace_inventory_raw", (None, str(self.workspace_inventory_raw).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("workspace_inventory_raw", (None, str(self.workspace_inventory_raw).encode(), "text/plain"))
                )

        if not isinstance(self.organization_id, Unset):
            if isinstance(self.organization_id, UUID):
                files.append(("organization_id", (None, str(self.organization_id), "text/plain")))
            else:
                files.append(("organization_id", (None, str(self.organization_id).encode(), "text/plain")))

        if not isinstance(self.encrypted, Unset):
            files.append(("encrypted", (None, str(self.encrypted).encode(), "text/plain")))

        if not isinstance(self.pop_id, Unset):
            files.append(("pop_id", (None, str(self.pop_id), "text/plain")))

        if not isinstance(self.template, Unset):
            if isinstance(self.template, str):
                files.append(("template", (None, str(self.template).encode(), "text/plain")))
            else:
                files.append(("template", (None, str(self.template).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.purpose, Unset):
            if isinstance(self.purpose, str):
                files.append(("purpose", (None, str(self.purpose).encode(), "text/plain")))
            elif isinstance(self.purpose, str):
                files.append(("purpose", (None, str(self.purpose).encode(), "text/plain")))
            else:
                files.append(("purpose", (None, str(self.purpose).encode(), "text/plain")))

        if not isinstance(self.urls, Unset):
            files.append(("urls", (None, str(self.urls).encode(), "text/plain")))

        if not isinstance(self.owner_id, Unset):
            if isinstance(self.owner_id, int):
                files.append(("owner_id", (None, str(self.owner_id).encode(), "text/plain")))
            else:
                files.append(("owner_id", (None, str(self.owner_id).encode(), "text/plain")))

        if not isinstance(self.readme_md, Unset):
            if isinstance(self.readme_md, str):
                files.append(("readme_md", (None, str(self.readme_md).encode(), "text/plain")))
            else:
                files.append(("readme_md", (None, str(self.readme_md).encode(), "text/plain")))

        if not isinstance(self.alternative_name, Unset):
            if isinstance(self.alternative_name, str):
                files.append(("alternative_name", (None, str(self.alternative_name).encode(), "text/plain")))
            else:
                files.append(("alternative_name", (None, str(self.alternative_name).encode(), "text/plain")))

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

        _monitoring_workspace_allowlist_ids = d.pop("monitoring_workspace_allowlist_ids", UNSET)
        monitoring_workspace_allowlist_ids: list[UUID] | Unset = UNSET
        if _monitoring_workspace_allowlist_ids is not UNSET:
            monitoring_workspace_allowlist_ids = []
            for monitoring_workspace_allowlist_ids_item_data in _monitoring_workspace_allowlist_ids:
                monitoring_workspace_allowlist_ids_item = UUID(monitoring_workspace_allowlist_ids_item_data)

                monitoring_workspace_allowlist_ids.append(monitoring_workspace_allowlist_ids_item)

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

        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)

                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        encrypted = d.pop("encrypted", UNSET)

        _pop_id = d.pop("pop_id", UNSET)
        pop_id: UUID | Unset
        if isinstance(_pop_id, Unset):
            pop_id = UNSET
        else:
            pop_id = UUID(_pop_id)

        def _parse_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

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

        def _parse_owner_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))

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

        patched_workspace_request = cls(
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
            monitoring_workspace_allowlist_ids=monitoring_workspace_allowlist_ids,
            notifications_enabled=notifications_enabled,
            backup_enabled=backup_enabled,
            has_incompatible_kubeconfig=has_incompatible_kubeconfig,
            endpoint_monitors=endpoint_monitors,
            secrets_poly_raw=secrets_poly_raw,
            workspace_inventory_raw=workspace_inventory_raw,
            organization_id=organization_id,
            encrypted=encrypted,
            pop_id=pop_id,
            template=template,
            description=description,
            purpose=purpose,
            urls=urls,
            owner_id=owner_id,
            readme_md=readme_md,
            alternative_name=alternative_name,
        )

        patched_workspace_request.additional_properties = d
        return patched_workspace_request

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
