from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.created_by_component_enum import CreatedByComponentEnum, check_created_by_component_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.generic_object_kind_enum import GenericObjectKindEnum, check_generic_object_kind_enum
from ..models.organization_endpoint_monitoring_mode_enum import (
    OrganizationEndpointMonitoringModeEnum,
    check_organization_endpoint_monitoring_mode_enum,
)
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedOrganizationRequest")


@_attrs_define
class PatchedOrganizationRequest:
    """
    Attributes:
        owner_id (int | None | Unset):
        workspace_default_owner_id (int | None | Unset):
        name (str | Unset):
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
        platform_service (bool | Unset):
        scope (ScopeEnum | Unset): * `system` - System
            * `user` - User
        kind (GenericObjectKindEnum | Unset): * `generic` - Generic
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
        legal_name (str | Unset):
        alias (None | str | Unset):
        slug (None | str | Unset):
        domains (Any | Unset):
        description (None | str | Unset):
        active (bool | Unset):
        keycloak_tenant_enabled (bool | Unset):
        keycloak_tenant_name (None | str | Unset):
        keycloak_tenant_id (None | str | Unset):
        keycloak_role_group_ids (Any | Unset): Cached Keycloak organization group IDs for role groups
            (admin/billing/developer/viewer/owner)
        harbor_group_id (None | str | Unset):
        harbor_project_id (None | str | Unset):
        harbor_project_membership_id (None | str | Unset):
        harbor_quota_used_bytes (int | None | Unset):
        harbor_quota_hard_bytes (int | None | Unset):
        harbor_quota_updated_at (datetime.datetime | None | Unset):
        grafana_org_id (None | str | Unset):
        gitlab_group_id (int | None | Unset):
        gitlab_group_url (None | str | Unset): GitLab group URL (e.g., https://gitlab.com/group)
        endpoint_monitoring_mode (OrganizationEndpointMonitoringModeEnum | Unset): * `auto` - AUTO
            * `manual` - MANUAL
        color (None | str | Unset): RGB color in hex format (e.g., #ff6b6b)
        priority (bool | Unset): High priority organization flag
        upstream_organization_id (None | str | Unset): ID of the external system object managing this organization
        upstream_system_id (None | str | Unset): Identifier of the external system managing this organization
        loopback_org_id (None | str | Unset): Loopback Organization ID. Set only on the SystemOwner organization
            (Loopback tenant).
        loopback_project_id (None | str | Unset): Loopback Project ID for this organization. Each Polycrate org maps to
            one Loopback project.
        urls (Any | Unset): List of named URLs, e.g. [{"name": "Portal", "url": "https://..."}]
        emails (Any | Unset): List of typed contact emails, e.g. [{"type": "billing", "email": "billing@..."}]. Types:
            billing, security, support, legal, notifications
        rocketchat_channel_id (None | str | Unset): RocketChat channel ID for this organization
        rocketchat_channel_name (None | str | Unset): RocketChat channel name (= prefix + slug)
        rocketchat_channel_avatar_hash (None | str | Unset): MD5 hash of the last successfully uploaded RocketChat
            channel avatar
        rocketchat_channel_announcement (str | Unset): Override for the RocketChat channel announcement banner. Leave
            empty to use the SystemConfig default.
        icon_content_type (None | str | Unset): MIME type of the icon (e.g., image/svg+xml, image/png)
        icon_filename (None | str | Unset): Original filename of the uploaded icon
        apm_vmuser_manifest_last_applied_sha256 (None | str | Unset): SHA-256 (hex) of the last successfully applied
            unified APM VMUser manifest (canonical JSON). Spec: polycrate spec inspect 172.
        observability_metrics (Any | Unset): Observability metrics for billing (logs ingested, active metric series)
        cached_s3_storage_bytes (int | Unset): Total S3 storage in bytes across all buckets
        cached_lb_traffic_30d_bytes (int | Unset): Total 30-day loadbalancer traffic in bytes; COALESCE
            traffic.*.30d_total then bytes.*.30d_total
        cached_logs_30d (int | Unset): Total log ingestion count in last 30 days
        cached_metrics_30d_avg (int | Unset): Average active metric series in last 30 days
        cached_metrics_updated_at (datetime.datetime | None | Unset): Last time cached metrics were updated
        cached_s3_bucket_count (int | Unset): Cached S3 bucket count
        cached_s3_object_count (int | Unset): Cached total S3 object count across all buckets
        cached_lb_count (int | Unset): Cached loadbalancer instance count
        cached_lb_traffic_30d_in_bytes (int | Unset): Cached inbound 30-day loadbalancer traffic in bytes; COALESCE
            traffic.in.30d_total then bytes.in.30d_total
        cached_lb_traffic_30d_out_bytes (int | Unset): Cached outbound 30-day loadbalancer traffic in bytes; COALESCE
            traffic.out.30d_total then bytes.out.30d_total
        cached_volume_count (int | Unset): Cached total K8sVolume count across all workspaces
        cached_volume_capacity_bytes (int | Unset): Cached total K8sVolume capacity in bytes across all workspaces
        cached_k8s_cluster_count (int | Unset): Portal-visible K8sCluster count: cluster and workspace not archived,
            neither kind generic (Spec 630 / 781)
        cached_workspace_count (int | Unset): Non-archived Workspace count for this organization (Spec 630)
        cached_endpoint_count (int | Unset): Non-archived Endpoint count for this organization (Spec 630)
        cached_endpoint_down_count (int | Unset): Non-archived Endpoints with state=CRITICAL (Spec 630)
        cached_member_count (int | Unset): OrganizationMembership count (Spec 630)
        cached_member_active_count (int | Unset): Memberships whose user.is_active is True (Spec 630)
        cached_active_maintenances_count (int | Unset): Active maintenances for org plus system-wide (Spec 630 / 532)
        cached_open_incidents_count (int | Unset): Open incidents for org plus system-wide (Spec 630)
        cached_active_downtimes_count (int | Unset): Active downtimes for this organization (Spec 630)
        cached_firing_alerts_count (int | Unset): Firing alerts for this organization (Spec 630)
        cached_total_product_cost (None | str | Unset): Total monthly product cost across all OrganizationProducts
            (cached)
        cached_product_cost_updated_at (datetime.datetime | None | Unset): Last time cached_total_product_cost was
            recalculated
        archived_by (int | None | Unset): The user who archived the object
        managed_by_content_type (int | None | Unset):
        modified_by_user (int | None | Unset): The user who last modified the object
        created_by_user (int | None | Unset): The user who created the object
        unified_harbor_credential (None | Unset | UUID): Auto-generated unified Harbor registry credential (robot
            token).
        endpoint_monitors (list[UUID] | Unset):
    """

    owner_id: int | None | Unset = UNSET
    workspace_default_owner_id: int | None | Unset = UNSET
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
    platform_service: bool | Unset = UNSET
    scope: ScopeEnum | Unset = UNSET
    kind: GenericObjectKindEnum | Unset = UNSET
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
    legal_name: str | Unset = UNSET
    alias: None | str | Unset = UNSET
    slug: None | str | Unset = UNSET
    domains: Any | Unset = UNSET
    description: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    keycloak_tenant_enabled: bool | Unset = UNSET
    keycloak_tenant_name: None | str | Unset = UNSET
    keycloak_tenant_id: None | str | Unset = UNSET
    keycloak_role_group_ids: Any | Unset = UNSET
    harbor_group_id: None | str | Unset = UNSET
    harbor_project_id: None | str | Unset = UNSET
    harbor_project_membership_id: None | str | Unset = UNSET
    harbor_quota_used_bytes: int | None | Unset = UNSET
    harbor_quota_hard_bytes: int | None | Unset = UNSET
    harbor_quota_updated_at: datetime.datetime | None | Unset = UNSET
    grafana_org_id: None | str | Unset = UNSET
    gitlab_group_id: int | None | Unset = UNSET
    gitlab_group_url: None | str | Unset = UNSET
    endpoint_monitoring_mode: OrganizationEndpointMonitoringModeEnum | Unset = UNSET
    color: None | str | Unset = UNSET
    priority: bool | Unset = UNSET
    upstream_organization_id: None | str | Unset = UNSET
    upstream_system_id: None | str | Unset = UNSET
    loopback_org_id: None | str | Unset = UNSET
    loopback_project_id: None | str | Unset = UNSET
    urls: Any | Unset = UNSET
    emails: Any | Unset = UNSET
    rocketchat_channel_id: None | str | Unset = UNSET
    rocketchat_channel_name: None | str | Unset = UNSET
    rocketchat_channel_avatar_hash: None | str | Unset = UNSET
    rocketchat_channel_announcement: str | Unset = UNSET
    icon_content_type: None | str | Unset = UNSET
    icon_filename: None | str | Unset = UNSET
    apm_vmuser_manifest_last_applied_sha256: None | str | Unset = UNSET
    observability_metrics: Any | Unset = UNSET
    cached_s3_storage_bytes: int | Unset = UNSET
    cached_lb_traffic_30d_bytes: int | Unset = UNSET
    cached_logs_30d: int | Unset = UNSET
    cached_metrics_30d_avg: int | Unset = UNSET
    cached_metrics_updated_at: datetime.datetime | None | Unset = UNSET
    cached_s3_bucket_count: int | Unset = UNSET
    cached_s3_object_count: int | Unset = UNSET
    cached_lb_count: int | Unset = UNSET
    cached_lb_traffic_30d_in_bytes: int | Unset = UNSET
    cached_lb_traffic_30d_out_bytes: int | Unset = UNSET
    cached_volume_count: int | Unset = UNSET
    cached_volume_capacity_bytes: int | Unset = UNSET
    cached_k8s_cluster_count: int | Unset = UNSET
    cached_workspace_count: int | Unset = UNSET
    cached_endpoint_count: int | Unset = UNSET
    cached_endpoint_down_count: int | Unset = UNSET
    cached_member_count: int | Unset = UNSET
    cached_member_active_count: int | Unset = UNSET
    cached_active_maintenances_count: int | Unset = UNSET
    cached_open_incidents_count: int | Unset = UNSET
    cached_active_downtimes_count: int | Unset = UNSET
    cached_firing_alerts_count: int | Unset = UNSET
    cached_total_product_cost: None | str | Unset = UNSET
    cached_product_cost_updated_at: datetime.datetime | None | Unset = UNSET
    archived_by: int | None | Unset = UNSET
    managed_by_content_type: int | None | Unset = UNSET
    modified_by_user: int | None | Unset = UNSET
    created_by_user: int | None | Unset = UNSET
    unified_harbor_credential: None | Unset | UUID = UNSET
    endpoint_monitors: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_id: int | None | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        workspace_default_owner_id: int | None | Unset
        if isinstance(self.workspace_default_owner_id, Unset):
            workspace_default_owner_id = UNSET
        else:
            workspace_default_owner_id = self.workspace_default_owner_id

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

        legal_name = self.legal_name

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        domains = self.domains

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        active = self.active

        keycloak_tenant_enabled = self.keycloak_tenant_enabled

        keycloak_tenant_name: None | str | Unset
        if isinstance(self.keycloak_tenant_name, Unset):
            keycloak_tenant_name = UNSET
        else:
            keycloak_tenant_name = self.keycloak_tenant_name

        keycloak_tenant_id: None | str | Unset
        if isinstance(self.keycloak_tenant_id, Unset):
            keycloak_tenant_id = UNSET
        else:
            keycloak_tenant_id = self.keycloak_tenant_id

        keycloak_role_group_ids = self.keycloak_role_group_ids

        harbor_group_id: None | str | Unset
        if isinstance(self.harbor_group_id, Unset):
            harbor_group_id = UNSET
        else:
            harbor_group_id = self.harbor_group_id

        harbor_project_id: None | str | Unset
        if isinstance(self.harbor_project_id, Unset):
            harbor_project_id = UNSET
        else:
            harbor_project_id = self.harbor_project_id

        harbor_project_membership_id: None | str | Unset
        if isinstance(self.harbor_project_membership_id, Unset):
            harbor_project_membership_id = UNSET
        else:
            harbor_project_membership_id = self.harbor_project_membership_id

        harbor_quota_used_bytes: int | None | Unset
        if isinstance(self.harbor_quota_used_bytes, Unset):
            harbor_quota_used_bytes = UNSET
        else:
            harbor_quota_used_bytes = self.harbor_quota_used_bytes

        harbor_quota_hard_bytes: int | None | Unset
        if isinstance(self.harbor_quota_hard_bytes, Unset):
            harbor_quota_hard_bytes = UNSET
        else:
            harbor_quota_hard_bytes = self.harbor_quota_hard_bytes

        harbor_quota_updated_at: None | str | Unset
        if isinstance(self.harbor_quota_updated_at, Unset):
            harbor_quota_updated_at = UNSET
        elif isinstance(self.harbor_quota_updated_at, datetime.datetime):
            harbor_quota_updated_at = self.harbor_quota_updated_at.isoformat()
        else:
            harbor_quota_updated_at = self.harbor_quota_updated_at

        grafana_org_id: None | str | Unset
        if isinstance(self.grafana_org_id, Unset):
            grafana_org_id = UNSET
        else:
            grafana_org_id = self.grafana_org_id

        gitlab_group_id: int | None | Unset
        if isinstance(self.gitlab_group_id, Unset):
            gitlab_group_id = UNSET
        else:
            gitlab_group_id = self.gitlab_group_id

        gitlab_group_url: None | str | Unset
        if isinstance(self.gitlab_group_url, Unset):
            gitlab_group_url = UNSET
        else:
            gitlab_group_url = self.gitlab_group_url

        endpoint_monitoring_mode: str | Unset = UNSET
        if not isinstance(self.endpoint_monitoring_mode, Unset):
            endpoint_monitoring_mode = self.endpoint_monitoring_mode

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        priority = self.priority

        upstream_organization_id: None | str | Unset
        if isinstance(self.upstream_organization_id, Unset):
            upstream_organization_id = UNSET
        else:
            upstream_organization_id = self.upstream_organization_id

        upstream_system_id: None | str | Unset
        if isinstance(self.upstream_system_id, Unset):
            upstream_system_id = UNSET
        else:
            upstream_system_id = self.upstream_system_id

        loopback_org_id: None | str | Unset
        if isinstance(self.loopback_org_id, Unset):
            loopback_org_id = UNSET
        else:
            loopback_org_id = self.loopback_org_id

        loopback_project_id: None | str | Unset
        if isinstance(self.loopback_project_id, Unset):
            loopback_project_id = UNSET
        else:
            loopback_project_id = self.loopback_project_id

        urls = self.urls

        emails = self.emails

        rocketchat_channel_id: None | str | Unset
        if isinstance(self.rocketchat_channel_id, Unset):
            rocketchat_channel_id = UNSET
        else:
            rocketchat_channel_id = self.rocketchat_channel_id

        rocketchat_channel_name: None | str | Unset
        if isinstance(self.rocketchat_channel_name, Unset):
            rocketchat_channel_name = UNSET
        else:
            rocketchat_channel_name = self.rocketchat_channel_name

        rocketchat_channel_avatar_hash: None | str | Unset
        if isinstance(self.rocketchat_channel_avatar_hash, Unset):
            rocketchat_channel_avatar_hash = UNSET
        else:
            rocketchat_channel_avatar_hash = self.rocketchat_channel_avatar_hash

        rocketchat_channel_announcement = self.rocketchat_channel_announcement

        icon_content_type: None | str | Unset
        if isinstance(self.icon_content_type, Unset):
            icon_content_type = UNSET
        else:
            icon_content_type = self.icon_content_type

        icon_filename: None | str | Unset
        if isinstance(self.icon_filename, Unset):
            icon_filename = UNSET
        else:
            icon_filename = self.icon_filename

        apm_vmuser_manifest_last_applied_sha256: None | str | Unset
        if isinstance(self.apm_vmuser_manifest_last_applied_sha256, Unset):
            apm_vmuser_manifest_last_applied_sha256 = UNSET
        else:
            apm_vmuser_manifest_last_applied_sha256 = self.apm_vmuser_manifest_last_applied_sha256

        observability_metrics = self.observability_metrics

        cached_s3_storage_bytes = self.cached_s3_storage_bytes

        cached_lb_traffic_30d_bytes = self.cached_lb_traffic_30d_bytes

        cached_logs_30d = self.cached_logs_30d

        cached_metrics_30d_avg = self.cached_metrics_30d_avg

        cached_metrics_updated_at: None | str | Unset
        if isinstance(self.cached_metrics_updated_at, Unset):
            cached_metrics_updated_at = UNSET
        elif isinstance(self.cached_metrics_updated_at, datetime.datetime):
            cached_metrics_updated_at = self.cached_metrics_updated_at.isoformat()
        else:
            cached_metrics_updated_at = self.cached_metrics_updated_at

        cached_s3_bucket_count = self.cached_s3_bucket_count

        cached_s3_object_count = self.cached_s3_object_count

        cached_lb_count = self.cached_lb_count

        cached_lb_traffic_30d_in_bytes = self.cached_lb_traffic_30d_in_bytes

        cached_lb_traffic_30d_out_bytes = self.cached_lb_traffic_30d_out_bytes

        cached_volume_count = self.cached_volume_count

        cached_volume_capacity_bytes = self.cached_volume_capacity_bytes

        cached_k8s_cluster_count = self.cached_k8s_cluster_count

        cached_workspace_count = self.cached_workspace_count

        cached_endpoint_count = self.cached_endpoint_count

        cached_endpoint_down_count = self.cached_endpoint_down_count

        cached_member_count = self.cached_member_count

        cached_member_active_count = self.cached_member_active_count

        cached_active_maintenances_count = self.cached_active_maintenances_count

        cached_open_incidents_count = self.cached_open_incidents_count

        cached_active_downtimes_count = self.cached_active_downtimes_count

        cached_firing_alerts_count = self.cached_firing_alerts_count

        cached_total_product_cost: None | str | Unset
        if isinstance(self.cached_total_product_cost, Unset):
            cached_total_product_cost = UNSET
        else:
            cached_total_product_cost = self.cached_total_product_cost

        cached_product_cost_updated_at: None | str | Unset
        if isinstance(self.cached_product_cost_updated_at, Unset):
            cached_product_cost_updated_at = UNSET
        elif isinstance(self.cached_product_cost_updated_at, datetime.datetime):
            cached_product_cost_updated_at = self.cached_product_cost_updated_at.isoformat()
        else:
            cached_product_cost_updated_at = self.cached_product_cost_updated_at

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

        unified_harbor_credential: None | str | Unset
        if isinstance(self.unified_harbor_credential, Unset):
            unified_harbor_credential = UNSET
        elif isinstance(self.unified_harbor_credential, UUID):
            unified_harbor_credential = str(self.unified_harbor_credential)
        else:
            unified_harbor_credential = self.unified_harbor_credential

        endpoint_monitors: list[str] | Unset = UNSET
        if not isinstance(self.endpoint_monitors, Unset):
            endpoint_monitors = []
            for endpoint_monitors_item_data in self.endpoint_monitors:
                endpoint_monitors_item = str(endpoint_monitors_item_data)
                endpoint_monitors.append(endpoint_monitors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if workspace_default_owner_id is not UNSET:
            field_dict["workspace_default_owner_id"] = workspace_default_owner_id
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
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if alias is not UNSET:
            field_dict["alias"] = alias
        if slug is not UNSET:
            field_dict["slug"] = slug
        if domains is not UNSET:
            field_dict["domains"] = domains
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if keycloak_tenant_enabled is not UNSET:
            field_dict["keycloak_tenant_enabled"] = keycloak_tenant_enabled
        if keycloak_tenant_name is not UNSET:
            field_dict["keycloak_tenant_name"] = keycloak_tenant_name
        if keycloak_tenant_id is not UNSET:
            field_dict["keycloak_tenant_id"] = keycloak_tenant_id
        if keycloak_role_group_ids is not UNSET:
            field_dict["keycloak_role_group_ids"] = keycloak_role_group_ids
        if harbor_group_id is not UNSET:
            field_dict["harbor_group_id"] = harbor_group_id
        if harbor_project_id is not UNSET:
            field_dict["harbor_project_id"] = harbor_project_id
        if harbor_project_membership_id is not UNSET:
            field_dict["harbor_project_membership_id"] = harbor_project_membership_id
        if harbor_quota_used_bytes is not UNSET:
            field_dict["harbor_quota_used_bytes"] = harbor_quota_used_bytes
        if harbor_quota_hard_bytes is not UNSET:
            field_dict["harbor_quota_hard_bytes"] = harbor_quota_hard_bytes
        if harbor_quota_updated_at is not UNSET:
            field_dict["harbor_quota_updated_at"] = harbor_quota_updated_at
        if grafana_org_id is not UNSET:
            field_dict["grafana_org_id"] = grafana_org_id
        if gitlab_group_id is not UNSET:
            field_dict["gitlab_group_id"] = gitlab_group_id
        if gitlab_group_url is not UNSET:
            field_dict["gitlab_group_url"] = gitlab_group_url
        if endpoint_monitoring_mode is not UNSET:
            field_dict["endpoint_monitoring_mode"] = endpoint_monitoring_mode
        if color is not UNSET:
            field_dict["color"] = color
        if priority is not UNSET:
            field_dict["priority"] = priority
        if upstream_organization_id is not UNSET:
            field_dict["upstream_organization_id"] = upstream_organization_id
        if upstream_system_id is not UNSET:
            field_dict["upstream_system_id"] = upstream_system_id
        if loopback_org_id is not UNSET:
            field_dict["loopback_org_id"] = loopback_org_id
        if loopback_project_id is not UNSET:
            field_dict["loopback_project_id"] = loopback_project_id
        if urls is not UNSET:
            field_dict["urls"] = urls
        if emails is not UNSET:
            field_dict["emails"] = emails
        if rocketchat_channel_id is not UNSET:
            field_dict["rocketchat_channel_id"] = rocketchat_channel_id
        if rocketchat_channel_name is not UNSET:
            field_dict["rocketchat_channel_name"] = rocketchat_channel_name
        if rocketchat_channel_avatar_hash is not UNSET:
            field_dict["rocketchat_channel_avatar_hash"] = rocketchat_channel_avatar_hash
        if rocketchat_channel_announcement is not UNSET:
            field_dict["rocketchat_channel_announcement"] = rocketchat_channel_announcement
        if icon_content_type is not UNSET:
            field_dict["icon_content_type"] = icon_content_type
        if icon_filename is not UNSET:
            field_dict["icon_filename"] = icon_filename
        if apm_vmuser_manifest_last_applied_sha256 is not UNSET:
            field_dict["apm_vmuser_manifest_last_applied_sha256"] = apm_vmuser_manifest_last_applied_sha256
        if observability_metrics is not UNSET:
            field_dict["observability_metrics"] = observability_metrics
        if cached_s3_storage_bytes is not UNSET:
            field_dict["cached_s3_storage_bytes"] = cached_s3_storage_bytes
        if cached_lb_traffic_30d_bytes is not UNSET:
            field_dict["cached_lb_traffic_30d_bytes"] = cached_lb_traffic_30d_bytes
        if cached_logs_30d is not UNSET:
            field_dict["cached_logs_30d"] = cached_logs_30d
        if cached_metrics_30d_avg is not UNSET:
            field_dict["cached_metrics_30d_avg"] = cached_metrics_30d_avg
        if cached_metrics_updated_at is not UNSET:
            field_dict["cached_metrics_updated_at"] = cached_metrics_updated_at
        if cached_s3_bucket_count is not UNSET:
            field_dict["cached_s3_bucket_count"] = cached_s3_bucket_count
        if cached_s3_object_count is not UNSET:
            field_dict["cached_s3_object_count"] = cached_s3_object_count
        if cached_lb_count is not UNSET:
            field_dict["cached_lb_count"] = cached_lb_count
        if cached_lb_traffic_30d_in_bytes is not UNSET:
            field_dict["cached_lb_traffic_30d_in_bytes"] = cached_lb_traffic_30d_in_bytes
        if cached_lb_traffic_30d_out_bytes is not UNSET:
            field_dict["cached_lb_traffic_30d_out_bytes"] = cached_lb_traffic_30d_out_bytes
        if cached_volume_count is not UNSET:
            field_dict["cached_volume_count"] = cached_volume_count
        if cached_volume_capacity_bytes is not UNSET:
            field_dict["cached_volume_capacity_bytes"] = cached_volume_capacity_bytes
        if cached_k8s_cluster_count is not UNSET:
            field_dict["cached_k8s_cluster_count"] = cached_k8s_cluster_count
        if cached_workspace_count is not UNSET:
            field_dict["cached_workspace_count"] = cached_workspace_count
        if cached_endpoint_count is not UNSET:
            field_dict["cached_endpoint_count"] = cached_endpoint_count
        if cached_endpoint_down_count is not UNSET:
            field_dict["cached_endpoint_down_count"] = cached_endpoint_down_count
        if cached_member_count is not UNSET:
            field_dict["cached_member_count"] = cached_member_count
        if cached_member_active_count is not UNSET:
            field_dict["cached_member_active_count"] = cached_member_active_count
        if cached_active_maintenances_count is not UNSET:
            field_dict["cached_active_maintenances_count"] = cached_active_maintenances_count
        if cached_open_incidents_count is not UNSET:
            field_dict["cached_open_incidents_count"] = cached_open_incidents_count
        if cached_active_downtimes_count is not UNSET:
            field_dict["cached_active_downtimes_count"] = cached_active_downtimes_count
        if cached_firing_alerts_count is not UNSET:
            field_dict["cached_firing_alerts_count"] = cached_firing_alerts_count
        if cached_total_product_cost is not UNSET:
            field_dict["cached_total_product_cost"] = cached_total_product_cost
        if cached_product_cost_updated_at is not UNSET:
            field_dict["cached_product_cost_updated_at"] = cached_product_cost_updated_at
        if archived_by is not UNSET:
            field_dict["archived_by"] = archived_by
        if managed_by_content_type is not UNSET:
            field_dict["managed_by_content_type"] = managed_by_content_type
        if modified_by_user is not UNSET:
            field_dict["modified_by_user"] = modified_by_user
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if unified_harbor_credential is not UNSET:
            field_dict["unified_harbor_credential"] = unified_harbor_credential
        if endpoint_monitors is not UNSET:
            field_dict["endpoint_monitors"] = endpoint_monitors

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.owner_id, Unset):
            if isinstance(self.owner_id, int):
                files.append(("owner_id", (None, str(self.owner_id).encode(), "text/plain")))
            else:
                files.append(("owner_id", (None, str(self.owner_id).encode(), "text/plain")))

        if not isinstance(self.workspace_default_owner_id, Unset):
            if isinstance(self.workspace_default_owner_id, int):
                files.append(
                    ("workspace_default_owner_id", (None, str(self.workspace_default_owner_id).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("workspace_default_owner_id", (None, str(self.workspace_default_owner_id).encode(), "text/plain"))
                )

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

        if not isinstance(self.last_reconciliation_duration_seconds, Unset):
            if isinstance(self.last_reconciliation_duration_seconds, float):
                files.append(
                    (
                        "last_reconciliation_duration_seconds",
                        (None, str(self.last_reconciliation_duration_seconds).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "last_reconciliation_duration_seconds",
                        (None, str(self.last_reconciliation_duration_seconds).encode(), "text/plain"),
                    )
                )

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

        if not isinstance(self.created_by_component, Unset):
            if isinstance(self.created_by_component, str):
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))
            elif isinstance(self.created_by_component, str):
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))
            else:
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))

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

        if not isinstance(self.slo_window_days, Unset):
            if isinstance(self.slo_window_days, int):
                files.append(("slo_window_days", (None, str(self.slo_window_days).encode(), "text/plain")))
            else:
                files.append(("slo_window_days", (None, str(self.slo_window_days).encode(), "text/plain")))

        if not isinstance(self.slo_availability, Unset):
            files.append(("slo_availability", (None, str(self.slo_availability).encode(), "text/plain")))

        if not isinstance(self.sla_target, Unset):
            if isinstance(self.sla_target, str):
                files.append(("sla_target", (None, str(self.sla_target).encode(), "text/plain")))
            else:
                files.append(("sla_target", (None, str(self.sla_target).encode(), "text/plain")))

        if not isinstance(self.sla_window_days, Unset):
            if isinstance(self.sla_window_days, int):
                files.append(("sla_window_days", (None, str(self.sla_window_days).encode(), "text/plain")))
            else:
                files.append(("sla_window_days", (None, str(self.sla_window_days).encode(), "text/plain")))

        if not isinstance(self.sla_availability, Unset):
            files.append(("sla_availability", (None, str(self.sla_availability).encode(), "text/plain")))

        if not isinstance(self.criticality, Unset):
            if isinstance(self.criticality, str):
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            elif isinstance(self.criticality, str):
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            else:
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))

        if not isinstance(self.managed_by_object_id, Unset):
            if isinstance(self.managed_by_object_id, str):
                files.append(("managed_by_object_id", (None, str(self.managed_by_object_id).encode(), "text/plain")))
            else:
                files.append(("managed_by_object_id", (None, str(self.managed_by_object_id).encode(), "text/plain")))

        if not isinstance(self.platform_dns_record_created, Unset):
            files.append(
                ("platform_dns_record_created", (None, str(self.platform_dns_record_created).encode(), "text/plain"))
            )

        if not isinstance(self.legal_name, Unset):
            files.append(("legal_name", (None, str(self.legal_name).encode(), "text/plain")))

        if not isinstance(self.alias, Unset):
            if isinstance(self.alias, str):
                files.append(("alias", (None, str(self.alias).encode(), "text/plain")))
            else:
                files.append(("alias", (None, str(self.alias).encode(), "text/plain")))

        if not isinstance(self.slug, Unset):
            if isinstance(self.slug, str):
                files.append(("slug", (None, str(self.slug).encode(), "text/plain")))
            else:
                files.append(("slug", (None, str(self.slug).encode(), "text/plain")))

        if not isinstance(self.domains, Unset):
            files.append(("domains", (None, str(self.domains).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.active, Unset):
            files.append(("active", (None, str(self.active).encode(), "text/plain")))

        if not isinstance(self.keycloak_tenant_enabled, Unset):
            files.append(("keycloak_tenant_enabled", (None, str(self.keycloak_tenant_enabled).encode(), "text/plain")))

        if not isinstance(self.keycloak_tenant_name, Unset):
            if isinstance(self.keycloak_tenant_name, str):
                files.append(("keycloak_tenant_name", (None, str(self.keycloak_tenant_name).encode(), "text/plain")))
            else:
                files.append(("keycloak_tenant_name", (None, str(self.keycloak_tenant_name).encode(), "text/plain")))

        if not isinstance(self.keycloak_tenant_id, Unset):
            if isinstance(self.keycloak_tenant_id, str):
                files.append(("keycloak_tenant_id", (None, str(self.keycloak_tenant_id).encode(), "text/plain")))
            else:
                files.append(("keycloak_tenant_id", (None, str(self.keycloak_tenant_id).encode(), "text/plain")))

        if not isinstance(self.keycloak_role_group_ids, Unset):
            files.append(("keycloak_role_group_ids", (None, str(self.keycloak_role_group_ids).encode(), "text/plain")))

        if not isinstance(self.harbor_group_id, Unset):
            if isinstance(self.harbor_group_id, str):
                files.append(("harbor_group_id", (None, str(self.harbor_group_id).encode(), "text/plain")))
            else:
                files.append(("harbor_group_id", (None, str(self.harbor_group_id).encode(), "text/plain")))

        if not isinstance(self.harbor_project_id, Unset):
            if isinstance(self.harbor_project_id, str):
                files.append(("harbor_project_id", (None, str(self.harbor_project_id).encode(), "text/plain")))
            else:
                files.append(("harbor_project_id", (None, str(self.harbor_project_id).encode(), "text/plain")))

        if not isinstance(self.harbor_project_membership_id, Unset):
            if isinstance(self.harbor_project_membership_id, str):
                files.append(
                    (
                        "harbor_project_membership_id",
                        (None, str(self.harbor_project_membership_id).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "harbor_project_membership_id",
                        (None, str(self.harbor_project_membership_id).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.harbor_quota_used_bytes, Unset):
            if isinstance(self.harbor_quota_used_bytes, int):
                files.append(
                    ("harbor_quota_used_bytes", (None, str(self.harbor_quota_used_bytes).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("harbor_quota_used_bytes", (None, str(self.harbor_quota_used_bytes).encode(), "text/plain"))
                )

        if not isinstance(self.harbor_quota_hard_bytes, Unset):
            if isinstance(self.harbor_quota_hard_bytes, int):
                files.append(
                    ("harbor_quota_hard_bytes", (None, str(self.harbor_quota_hard_bytes).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("harbor_quota_hard_bytes", (None, str(self.harbor_quota_hard_bytes).encode(), "text/plain"))
                )

        if not isinstance(self.harbor_quota_updated_at, Unset):
            if isinstance(self.harbor_quota_updated_at, datetime.datetime):
                files.append(
                    ("harbor_quota_updated_at", (None, self.harbor_quota_updated_at.isoformat().encode(), "text/plain"))
                )
            else:
                files.append(
                    ("harbor_quota_updated_at", (None, str(self.harbor_quota_updated_at).encode(), "text/plain"))
                )

        if not isinstance(self.grafana_org_id, Unset):
            if isinstance(self.grafana_org_id, str):
                files.append(("grafana_org_id", (None, str(self.grafana_org_id).encode(), "text/plain")))
            else:
                files.append(("grafana_org_id", (None, str(self.grafana_org_id).encode(), "text/plain")))

        if not isinstance(self.gitlab_group_id, Unset):
            if isinstance(self.gitlab_group_id, int):
                files.append(("gitlab_group_id", (None, str(self.gitlab_group_id).encode(), "text/plain")))
            else:
                files.append(("gitlab_group_id", (None, str(self.gitlab_group_id).encode(), "text/plain")))

        if not isinstance(self.gitlab_group_url, Unset):
            if isinstance(self.gitlab_group_url, str):
                files.append(("gitlab_group_url", (None, str(self.gitlab_group_url).encode(), "text/plain")))
            else:
                files.append(("gitlab_group_url", (None, str(self.gitlab_group_url).encode(), "text/plain")))

        if not isinstance(self.endpoint_monitoring_mode, Unset):
            files.append(
                ("endpoint_monitoring_mode", (None, str(self.endpoint_monitoring_mode).encode(), "text/plain"))
            )

        if not isinstance(self.color, Unset):
            if isinstance(self.color, str):
                files.append(("color", (None, str(self.color).encode(), "text/plain")))
            else:
                files.append(("color", (None, str(self.color).encode(), "text/plain")))

        if not isinstance(self.priority, Unset):
            files.append(("priority", (None, str(self.priority).encode(), "text/plain")))

        if not isinstance(self.upstream_organization_id, Unset):
            if isinstance(self.upstream_organization_id, str):
                files.append(
                    ("upstream_organization_id", (None, str(self.upstream_organization_id).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("upstream_organization_id", (None, str(self.upstream_organization_id).encode(), "text/plain"))
                )

        if not isinstance(self.upstream_system_id, Unset):
            if isinstance(self.upstream_system_id, str):
                files.append(("upstream_system_id", (None, str(self.upstream_system_id).encode(), "text/plain")))
            else:
                files.append(("upstream_system_id", (None, str(self.upstream_system_id).encode(), "text/plain")))

        if not isinstance(self.loopback_org_id, Unset):
            if isinstance(self.loopback_org_id, str):
                files.append(("loopback_org_id", (None, str(self.loopback_org_id).encode(), "text/plain")))
            else:
                files.append(("loopback_org_id", (None, str(self.loopback_org_id).encode(), "text/plain")))

        if not isinstance(self.loopback_project_id, Unset):
            if isinstance(self.loopback_project_id, str):
                files.append(("loopback_project_id", (None, str(self.loopback_project_id).encode(), "text/plain")))
            else:
                files.append(("loopback_project_id", (None, str(self.loopback_project_id).encode(), "text/plain")))

        if not isinstance(self.urls, Unset):
            files.append(("urls", (None, str(self.urls).encode(), "text/plain")))

        if not isinstance(self.emails, Unset):
            files.append(("emails", (None, str(self.emails).encode(), "text/plain")))

        if not isinstance(self.rocketchat_channel_id, Unset):
            if isinstance(self.rocketchat_channel_id, str):
                files.append(("rocketchat_channel_id", (None, str(self.rocketchat_channel_id).encode(), "text/plain")))
            else:
                files.append(("rocketchat_channel_id", (None, str(self.rocketchat_channel_id).encode(), "text/plain")))

        if not isinstance(self.rocketchat_channel_name, Unset):
            if isinstance(self.rocketchat_channel_name, str):
                files.append(
                    ("rocketchat_channel_name", (None, str(self.rocketchat_channel_name).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("rocketchat_channel_name", (None, str(self.rocketchat_channel_name).encode(), "text/plain"))
                )

        if not isinstance(self.rocketchat_channel_avatar_hash, Unset):
            if isinstance(self.rocketchat_channel_avatar_hash, str):
                files.append(
                    (
                        "rocketchat_channel_avatar_hash",
                        (None, str(self.rocketchat_channel_avatar_hash).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "rocketchat_channel_avatar_hash",
                        (None, str(self.rocketchat_channel_avatar_hash).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.rocketchat_channel_announcement, Unset):
            files.append(
                (
                    "rocketchat_channel_announcement",
                    (None, str(self.rocketchat_channel_announcement).encode(), "text/plain"),
                )
            )

        if not isinstance(self.icon_content_type, Unset):
            if isinstance(self.icon_content_type, str):
                files.append(("icon_content_type", (None, str(self.icon_content_type).encode(), "text/plain")))
            else:
                files.append(("icon_content_type", (None, str(self.icon_content_type).encode(), "text/plain")))

        if not isinstance(self.icon_filename, Unset):
            if isinstance(self.icon_filename, str):
                files.append(("icon_filename", (None, str(self.icon_filename).encode(), "text/plain")))
            else:
                files.append(("icon_filename", (None, str(self.icon_filename).encode(), "text/plain")))

        if not isinstance(self.apm_vmuser_manifest_last_applied_sha256, Unset):
            if isinstance(self.apm_vmuser_manifest_last_applied_sha256, str):
                files.append(
                    (
                        "apm_vmuser_manifest_last_applied_sha256",
                        (None, str(self.apm_vmuser_manifest_last_applied_sha256).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "apm_vmuser_manifest_last_applied_sha256",
                        (None, str(self.apm_vmuser_manifest_last_applied_sha256).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.observability_metrics, Unset):
            files.append(("observability_metrics", (None, str(self.observability_metrics).encode(), "text/plain")))

        if not isinstance(self.cached_s3_storage_bytes, Unset):
            files.append(("cached_s3_storage_bytes", (None, str(self.cached_s3_storage_bytes).encode(), "text/plain")))

        if not isinstance(self.cached_lb_traffic_30d_bytes, Unset):
            files.append(
                ("cached_lb_traffic_30d_bytes", (None, str(self.cached_lb_traffic_30d_bytes).encode(), "text/plain"))
            )

        if not isinstance(self.cached_logs_30d, Unset):
            files.append(("cached_logs_30d", (None, str(self.cached_logs_30d).encode(), "text/plain")))

        if not isinstance(self.cached_metrics_30d_avg, Unset):
            files.append(("cached_metrics_30d_avg", (None, str(self.cached_metrics_30d_avg).encode(), "text/plain")))

        if not isinstance(self.cached_metrics_updated_at, Unset):
            if isinstance(self.cached_metrics_updated_at, datetime.datetime):
                files.append(
                    (
                        "cached_metrics_updated_at",
                        (None, self.cached_metrics_updated_at.isoformat().encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    ("cached_metrics_updated_at", (None, str(self.cached_metrics_updated_at).encode(), "text/plain"))
                )

        if not isinstance(self.cached_s3_bucket_count, Unset):
            files.append(("cached_s3_bucket_count", (None, str(self.cached_s3_bucket_count).encode(), "text/plain")))

        if not isinstance(self.cached_s3_object_count, Unset):
            files.append(("cached_s3_object_count", (None, str(self.cached_s3_object_count).encode(), "text/plain")))

        if not isinstance(self.cached_lb_count, Unset):
            files.append(("cached_lb_count", (None, str(self.cached_lb_count).encode(), "text/plain")))

        if not isinstance(self.cached_lb_traffic_30d_in_bytes, Unset):
            files.append(
                (
                    "cached_lb_traffic_30d_in_bytes",
                    (None, str(self.cached_lb_traffic_30d_in_bytes).encode(), "text/plain"),
                )
            )

        if not isinstance(self.cached_lb_traffic_30d_out_bytes, Unset):
            files.append(
                (
                    "cached_lb_traffic_30d_out_bytes",
                    (None, str(self.cached_lb_traffic_30d_out_bytes).encode(), "text/plain"),
                )
            )

        if not isinstance(self.cached_volume_count, Unset):
            files.append(("cached_volume_count", (None, str(self.cached_volume_count).encode(), "text/plain")))

        if not isinstance(self.cached_volume_capacity_bytes, Unset):
            files.append(
                ("cached_volume_capacity_bytes", (None, str(self.cached_volume_capacity_bytes).encode(), "text/plain"))
            )

        if not isinstance(self.cached_k8s_cluster_count, Unset):
            files.append(
                ("cached_k8s_cluster_count", (None, str(self.cached_k8s_cluster_count).encode(), "text/plain"))
            )

        if not isinstance(self.cached_workspace_count, Unset):
            files.append(("cached_workspace_count", (None, str(self.cached_workspace_count).encode(), "text/plain")))

        if not isinstance(self.cached_endpoint_count, Unset):
            files.append(("cached_endpoint_count", (None, str(self.cached_endpoint_count).encode(), "text/plain")))

        if not isinstance(self.cached_endpoint_down_count, Unset):
            files.append(
                ("cached_endpoint_down_count", (None, str(self.cached_endpoint_down_count).encode(), "text/plain"))
            )

        if not isinstance(self.cached_member_count, Unset):
            files.append(("cached_member_count", (None, str(self.cached_member_count).encode(), "text/plain")))

        if not isinstance(self.cached_member_active_count, Unset):
            files.append(
                ("cached_member_active_count", (None, str(self.cached_member_active_count).encode(), "text/plain"))
            )

        if not isinstance(self.cached_active_maintenances_count, Unset):
            files.append(
                (
                    "cached_active_maintenances_count",
                    (None, str(self.cached_active_maintenances_count).encode(), "text/plain"),
                )
            )

        if not isinstance(self.cached_open_incidents_count, Unset):
            files.append(
                ("cached_open_incidents_count", (None, str(self.cached_open_incidents_count).encode(), "text/plain"))
            )

        if not isinstance(self.cached_active_downtimes_count, Unset):
            files.append(
                (
                    "cached_active_downtimes_count",
                    (None, str(self.cached_active_downtimes_count).encode(), "text/plain"),
                )
            )

        if not isinstance(self.cached_firing_alerts_count, Unset):
            files.append(
                ("cached_firing_alerts_count", (None, str(self.cached_firing_alerts_count).encode(), "text/plain"))
            )

        if not isinstance(self.cached_total_product_cost, Unset):
            if isinstance(self.cached_total_product_cost, str):
                files.append(
                    ("cached_total_product_cost", (None, str(self.cached_total_product_cost).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("cached_total_product_cost", (None, str(self.cached_total_product_cost).encode(), "text/plain"))
                )

        if not isinstance(self.cached_product_cost_updated_at, Unset):
            if isinstance(self.cached_product_cost_updated_at, datetime.datetime):
                files.append(
                    (
                        "cached_product_cost_updated_at",
                        (None, self.cached_product_cost_updated_at.isoformat().encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "cached_product_cost_updated_at",
                        (None, str(self.cached_product_cost_updated_at).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.archived_by, Unset):
            if isinstance(self.archived_by, int):
                files.append(("archived_by", (None, str(self.archived_by).encode(), "text/plain")))
            else:
                files.append(("archived_by", (None, str(self.archived_by).encode(), "text/plain")))

        if not isinstance(self.managed_by_content_type, Unset):
            if isinstance(self.managed_by_content_type, int):
                files.append(
                    ("managed_by_content_type", (None, str(self.managed_by_content_type).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("managed_by_content_type", (None, str(self.managed_by_content_type).encode(), "text/plain"))
                )

        if not isinstance(self.modified_by_user, Unset):
            if isinstance(self.modified_by_user, int):
                files.append(("modified_by_user", (None, str(self.modified_by_user).encode(), "text/plain")))
            else:
                files.append(("modified_by_user", (None, str(self.modified_by_user).encode(), "text/plain")))

        if not isinstance(self.created_by_user, Unset):
            if isinstance(self.created_by_user, int):
                files.append(("created_by_user", (None, str(self.created_by_user).encode(), "text/plain")))
            else:
                files.append(("created_by_user", (None, str(self.created_by_user).encode(), "text/plain")))

        if not isinstance(self.unified_harbor_credential, Unset):
            if isinstance(self.unified_harbor_credential, UUID):
                files.append(("unified_harbor_credential", (None, str(self.unified_harbor_credential), "text/plain")))
            else:
                files.append(
                    ("unified_harbor_credential", (None, str(self.unified_harbor_credential).encode(), "text/plain"))
                )

        if not isinstance(self.endpoint_monitors, Unset):
            for endpoint_monitors_item_element in self.endpoint_monitors:
                files.append(("endpoint_monitors", (None, str(endpoint_monitors_item_element), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_owner_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))

        def _parse_workspace_default_owner_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        workspace_default_owner_id = _parse_workspace_default_owner_id(d.pop("workspace_default_owner_id", UNSET))

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

        platform_service = d.pop("platform_service", UNSET)

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

        legal_name = d.pop("legal_name", UNSET)

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        domains = d.pop("domains", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        active = d.pop("active", UNSET)

        keycloak_tenant_enabled = d.pop("keycloak_tenant_enabled", UNSET)

        def _parse_keycloak_tenant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keycloak_tenant_name = _parse_keycloak_tenant_name(d.pop("keycloak_tenant_name", UNSET))

        def _parse_keycloak_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keycloak_tenant_id = _parse_keycloak_tenant_id(d.pop("keycloak_tenant_id", UNSET))

        keycloak_role_group_ids = d.pop("keycloak_role_group_ids", UNSET)

        def _parse_harbor_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        harbor_group_id = _parse_harbor_group_id(d.pop("harbor_group_id", UNSET))

        def _parse_harbor_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        harbor_project_id = _parse_harbor_project_id(d.pop("harbor_project_id", UNSET))

        def _parse_harbor_project_membership_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        harbor_project_membership_id = _parse_harbor_project_membership_id(d.pop("harbor_project_membership_id", UNSET))

        def _parse_harbor_quota_used_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        harbor_quota_used_bytes = _parse_harbor_quota_used_bytes(d.pop("harbor_quota_used_bytes", UNSET))

        def _parse_harbor_quota_hard_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        harbor_quota_hard_bytes = _parse_harbor_quota_hard_bytes(d.pop("harbor_quota_hard_bytes", UNSET))

        def _parse_harbor_quota_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                harbor_quota_updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return harbor_quota_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        harbor_quota_updated_at = _parse_harbor_quota_updated_at(d.pop("harbor_quota_updated_at", UNSET))

        def _parse_grafana_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grafana_org_id = _parse_grafana_org_id(d.pop("grafana_org_id", UNSET))

        def _parse_gitlab_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        gitlab_group_id = _parse_gitlab_group_id(d.pop("gitlab_group_id", UNSET))

        def _parse_gitlab_group_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gitlab_group_url = _parse_gitlab_group_url(d.pop("gitlab_group_url", UNSET))

        _endpoint_monitoring_mode = d.pop("endpoint_monitoring_mode", UNSET)
        endpoint_monitoring_mode: OrganizationEndpointMonitoringModeEnum | Unset
        if isinstance(_endpoint_monitoring_mode, Unset):
            endpoint_monitoring_mode = UNSET
        else:
            endpoint_monitoring_mode = check_organization_endpoint_monitoring_mode_enum(_endpoint_monitoring_mode)

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        priority = d.pop("priority", UNSET)

        def _parse_upstream_organization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upstream_organization_id = _parse_upstream_organization_id(d.pop("upstream_organization_id", UNSET))

        def _parse_upstream_system_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upstream_system_id = _parse_upstream_system_id(d.pop("upstream_system_id", UNSET))

        def _parse_loopback_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loopback_org_id = _parse_loopback_org_id(d.pop("loopback_org_id", UNSET))

        def _parse_loopback_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loopback_project_id = _parse_loopback_project_id(d.pop("loopback_project_id", UNSET))

        urls = d.pop("urls", UNSET)

        emails = d.pop("emails", UNSET)

        def _parse_rocketchat_channel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rocketchat_channel_id = _parse_rocketchat_channel_id(d.pop("rocketchat_channel_id", UNSET))

        def _parse_rocketchat_channel_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rocketchat_channel_name = _parse_rocketchat_channel_name(d.pop("rocketchat_channel_name", UNSET))

        def _parse_rocketchat_channel_avatar_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rocketchat_channel_avatar_hash = _parse_rocketchat_channel_avatar_hash(
            d.pop("rocketchat_channel_avatar_hash", UNSET)
        )

        rocketchat_channel_announcement = d.pop("rocketchat_channel_announcement", UNSET)

        def _parse_icon_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_content_type = _parse_icon_content_type(d.pop("icon_content_type", UNSET))

        def _parse_icon_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_filename = _parse_icon_filename(d.pop("icon_filename", UNSET))

        def _parse_apm_vmuser_manifest_last_applied_sha256(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        apm_vmuser_manifest_last_applied_sha256 = _parse_apm_vmuser_manifest_last_applied_sha256(
            d.pop("apm_vmuser_manifest_last_applied_sha256", UNSET)
        )

        observability_metrics = d.pop("observability_metrics", UNSET)

        cached_s3_storage_bytes = d.pop("cached_s3_storage_bytes", UNSET)

        cached_lb_traffic_30d_bytes = d.pop("cached_lb_traffic_30d_bytes", UNSET)

        cached_logs_30d = d.pop("cached_logs_30d", UNSET)

        cached_metrics_30d_avg = d.pop("cached_metrics_30d_avg", UNSET)

        def _parse_cached_metrics_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cached_metrics_updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return cached_metrics_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        cached_metrics_updated_at = _parse_cached_metrics_updated_at(d.pop("cached_metrics_updated_at", UNSET))

        cached_s3_bucket_count = d.pop("cached_s3_bucket_count", UNSET)

        cached_s3_object_count = d.pop("cached_s3_object_count", UNSET)

        cached_lb_count = d.pop("cached_lb_count", UNSET)

        cached_lb_traffic_30d_in_bytes = d.pop("cached_lb_traffic_30d_in_bytes", UNSET)

        cached_lb_traffic_30d_out_bytes = d.pop("cached_lb_traffic_30d_out_bytes", UNSET)

        cached_volume_count = d.pop("cached_volume_count", UNSET)

        cached_volume_capacity_bytes = d.pop("cached_volume_capacity_bytes", UNSET)

        cached_k8s_cluster_count = d.pop("cached_k8s_cluster_count", UNSET)

        cached_workspace_count = d.pop("cached_workspace_count", UNSET)

        cached_endpoint_count = d.pop("cached_endpoint_count", UNSET)

        cached_endpoint_down_count = d.pop("cached_endpoint_down_count", UNSET)

        cached_member_count = d.pop("cached_member_count", UNSET)

        cached_member_active_count = d.pop("cached_member_active_count", UNSET)

        cached_active_maintenances_count = d.pop("cached_active_maintenances_count", UNSET)

        cached_open_incidents_count = d.pop("cached_open_incidents_count", UNSET)

        cached_active_downtimes_count = d.pop("cached_active_downtimes_count", UNSET)

        cached_firing_alerts_count = d.pop("cached_firing_alerts_count", UNSET)

        def _parse_cached_total_product_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cached_total_product_cost = _parse_cached_total_product_cost(d.pop("cached_total_product_cost", UNSET))

        def _parse_cached_product_cost_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cached_product_cost_updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return cached_product_cost_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        cached_product_cost_updated_at = _parse_cached_product_cost_updated_at(
            d.pop("cached_product_cost_updated_at", UNSET)
        )

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

        def _parse_unified_harbor_credential(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                unified_harbor_credential_type_0 = UUID(data)

                return unified_harbor_credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        unified_harbor_credential = _parse_unified_harbor_credential(d.pop("unified_harbor_credential", UNSET))

        _endpoint_monitors = d.pop("endpoint_monitors", UNSET)
        endpoint_monitors: list[UUID] | Unset = UNSET
        if _endpoint_monitors is not UNSET:
            endpoint_monitors = []
            for endpoint_monitors_item_data in _endpoint_monitors:
                endpoint_monitors_item = UUID(endpoint_monitors_item_data)

                endpoint_monitors.append(endpoint_monitors_item)

        patched_organization_request = cls(
            owner_id=owner_id,
            workspace_default_owner_id=workspace_default_owner_id,
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
            platform_service=platform_service,
            scope=scope,
            kind=kind,
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
            legal_name=legal_name,
            alias=alias,
            slug=slug,
            domains=domains,
            description=description,
            active=active,
            keycloak_tenant_enabled=keycloak_tenant_enabled,
            keycloak_tenant_name=keycloak_tenant_name,
            keycloak_tenant_id=keycloak_tenant_id,
            keycloak_role_group_ids=keycloak_role_group_ids,
            harbor_group_id=harbor_group_id,
            harbor_project_id=harbor_project_id,
            harbor_project_membership_id=harbor_project_membership_id,
            harbor_quota_used_bytes=harbor_quota_used_bytes,
            harbor_quota_hard_bytes=harbor_quota_hard_bytes,
            harbor_quota_updated_at=harbor_quota_updated_at,
            grafana_org_id=grafana_org_id,
            gitlab_group_id=gitlab_group_id,
            gitlab_group_url=gitlab_group_url,
            endpoint_monitoring_mode=endpoint_monitoring_mode,
            color=color,
            priority=priority,
            upstream_organization_id=upstream_organization_id,
            upstream_system_id=upstream_system_id,
            loopback_org_id=loopback_org_id,
            loopback_project_id=loopback_project_id,
            urls=urls,
            emails=emails,
            rocketchat_channel_id=rocketchat_channel_id,
            rocketchat_channel_name=rocketchat_channel_name,
            rocketchat_channel_avatar_hash=rocketchat_channel_avatar_hash,
            rocketchat_channel_announcement=rocketchat_channel_announcement,
            icon_content_type=icon_content_type,
            icon_filename=icon_filename,
            apm_vmuser_manifest_last_applied_sha256=apm_vmuser_manifest_last_applied_sha256,
            observability_metrics=observability_metrics,
            cached_s3_storage_bytes=cached_s3_storage_bytes,
            cached_lb_traffic_30d_bytes=cached_lb_traffic_30d_bytes,
            cached_logs_30d=cached_logs_30d,
            cached_metrics_30d_avg=cached_metrics_30d_avg,
            cached_metrics_updated_at=cached_metrics_updated_at,
            cached_s3_bucket_count=cached_s3_bucket_count,
            cached_s3_object_count=cached_s3_object_count,
            cached_lb_count=cached_lb_count,
            cached_lb_traffic_30d_in_bytes=cached_lb_traffic_30d_in_bytes,
            cached_lb_traffic_30d_out_bytes=cached_lb_traffic_30d_out_bytes,
            cached_volume_count=cached_volume_count,
            cached_volume_capacity_bytes=cached_volume_capacity_bytes,
            cached_k8s_cluster_count=cached_k8s_cluster_count,
            cached_workspace_count=cached_workspace_count,
            cached_endpoint_count=cached_endpoint_count,
            cached_endpoint_down_count=cached_endpoint_down_count,
            cached_member_count=cached_member_count,
            cached_member_active_count=cached_member_active_count,
            cached_active_maintenances_count=cached_active_maintenances_count,
            cached_open_incidents_count=cached_open_incidents_count,
            cached_active_downtimes_count=cached_active_downtimes_count,
            cached_firing_alerts_count=cached_firing_alerts_count,
            cached_total_product_cost=cached_total_product_cost,
            cached_product_cost_updated_at=cached_product_cost_updated_at,
            archived_by=archived_by,
            managed_by_content_type=managed_by_content_type,
            modified_by_user=modified_by_user,
            created_by_user=created_by_user,
            unified_harbor_credential=unified_harbor_credential,
            endpoint_monitors=endpoint_monitors,
        )

        patched_organization_request.additional_properties = d
        return patched_organization_request

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
