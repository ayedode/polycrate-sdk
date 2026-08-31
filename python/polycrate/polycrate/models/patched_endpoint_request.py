from __future__ import annotations

import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.created_by_component_enum import CreatedByComponentEnum, check_created_by_component_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.endpoint_kind_enum import EndpointKindEnum, check_endpoint_kind_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.endpoint_spec_request import EndpointSpecRequest


T = TypeVar("T", bound="PatchedEndpointRequest")


@_attrs_define
class PatchedEndpointRequest:
    """Endpoint detail — same pattern as K8sAppSerializer: ManagedObjectDetailSerializer + exported_fields.

    organization/workspace stay OrganizationSimpleSerializer / WorkspaceSimpleSerializer (not generic dict).
    Spec 517: organization_id / workspace_id are write-only for Create (System/Org API Keys).
    spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema, which means
    the generated Go API client has a fully typed Spec struct (no interface{} reimplementation needed).

        Attributes:
            name (str | Unset): Object name (must be a slug)
            organization_id (UUID | Unset): UUID of the Organization this endpoint belongs to. Required on create for System
                and Organization API Keys. Org API Key users can only set their own organization.
            workspace_id (None | Unset | UUID): Optional workspace UUID. Customer Portal creates may omit this
                (workspace=null).
            spec (EndpointSpecRequest | None | Unset):
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
            kind (EndpointKindEnum | Unset): * `icmp` - ICMP Endpoint
                * `http` - HTTP Endpoint
                * `tcp` - TCP Endpoint
                * `dns` - DNS Endpoint
            remote_address (str | Unset):
            remote_port (int | None | Unset):
            check_results (Any | Unset):
            do_not_monitor (bool | Unset):
            pop_endpoint (bool | Unset): If true, this endpoint represents reachability of an entire PoP (Spec 526).
            last_agent_metrics (Any | Unset):
            resolved_ip (None | str | Unset):
            max_agents_per_endpoint (int | None | Unset): Maximum number of agents that monitor this endpoint
                simultaneously. Null = use system default (1).
            check_result_retention_days (int | None | Unset): Check result retention in days. Null = use system-wide default
                (ENDPOINT_CHECK_RESULT_RETENTION_DAYS).
            archived_by (int | None | Unset): The user who archived the object
            managed_by_content_type (int | None | Unset):
            modified_by_user (int | None | Unset): The user who last modified the object
            created_by_user (int | None | Unset): The user who created the object
            k8s_cluster (None | Unset | UUID):
            k8s_app (None | Unset | UUID):
            s3_cluster (None | Unset | UUID):
            region (None | Unset | UUID):
            loadbalancer_instance (None | Unset | UUID):
    """

    name: str | Unset = UNSET
    organization_id: UUID | Unset = UNSET
    workspace_id: None | Unset | UUID = UNSET
    spec: EndpointSpecRequest | None | Unset = UNSET
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
    kind: EndpointKindEnum | Unset = UNSET
    remote_address: str | Unset = UNSET
    remote_port: int | None | Unset = UNSET
    check_results: Any | Unset = UNSET
    do_not_monitor: bool | Unset = UNSET
    pop_endpoint: bool | Unset = UNSET
    last_agent_metrics: Any | Unset = UNSET
    resolved_ip: None | str | Unset = UNSET
    max_agents_per_endpoint: int | None | Unset = UNSET
    check_result_retention_days: int | None | Unset = UNSET
    archived_by: int | None | Unset = UNSET
    managed_by_content_type: int | None | Unset = UNSET
    modified_by_user: int | None | Unset = UNSET
    created_by_user: int | None | Unset = UNSET
    k8s_cluster: None | Unset | UUID = UNSET
    k8s_app: None | Unset | UUID = UNSET
    s3_cluster: None | Unset | UUID = UNSET
    region: None | Unset | UUID = UNSET
    loadbalancer_instance: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.endpoint_spec_request import EndpointSpecRequest

        name = self.name

        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        workspace_id: None | str | Unset
        if isinstance(self.workspace_id, Unset):
            workspace_id = UNSET
        elif isinstance(self.workspace_id, UUID):
            workspace_id = str(self.workspace_id)
        else:
            workspace_id = self.workspace_id

        spec: dict[str, Any] | None | Unset
        if isinstance(self.spec, Unset):
            spec = UNSET
        elif isinstance(self.spec, EndpointSpecRequest):
            spec = self.spec.to_dict()
        else:
            spec = self.spec

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

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        remote_address = self.remote_address

        remote_port: int | None | Unset
        if isinstance(self.remote_port, Unset):
            remote_port = UNSET
        else:
            remote_port = self.remote_port

        check_results = self.check_results

        do_not_monitor = self.do_not_monitor

        pop_endpoint = self.pop_endpoint

        last_agent_metrics = self.last_agent_metrics

        resolved_ip: None | str | Unset
        if isinstance(self.resolved_ip, Unset):
            resolved_ip = UNSET
        else:
            resolved_ip = self.resolved_ip

        max_agents_per_endpoint: int | None | Unset
        if isinstance(self.max_agents_per_endpoint, Unset):
            max_agents_per_endpoint = UNSET
        else:
            max_agents_per_endpoint = self.max_agents_per_endpoint

        check_result_retention_days: int | None | Unset
        if isinstance(self.check_result_retention_days, Unset):
            check_result_retention_days = UNSET
        else:
            check_result_retention_days = self.check_result_retention_days

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

        k8s_cluster: None | str | Unset
        if isinstance(self.k8s_cluster, Unset):
            k8s_cluster = UNSET
        elif isinstance(self.k8s_cluster, UUID):
            k8s_cluster = str(self.k8s_cluster)
        else:
            k8s_cluster = self.k8s_cluster

        k8s_app: None | str | Unset
        if isinstance(self.k8s_app, Unset):
            k8s_app = UNSET
        elif isinstance(self.k8s_app, UUID):
            k8s_app = str(self.k8s_app)
        else:
            k8s_app = self.k8s_app

        s3_cluster: None | str | Unset
        if isinstance(self.s3_cluster, Unset):
            s3_cluster = UNSET
        elif isinstance(self.s3_cluster, UUID):
            s3_cluster = str(self.s3_cluster)
        else:
            s3_cluster = self.s3_cluster

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        elif isinstance(self.region, UUID):
            region = str(self.region)
        else:
            region = self.region

        loadbalancer_instance: None | str | Unset
        if isinstance(self.loadbalancer_instance, Unset):
            loadbalancer_instance = UNSET
        elif isinstance(self.loadbalancer_instance, UUID):
            loadbalancer_instance = str(self.loadbalancer_instance)
        else:
            loadbalancer_instance = self.loadbalancer_instance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id
        if spec is not UNSET:
            field_dict["spec"] = spec
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
        if kind is not UNSET:
            field_dict["kind"] = kind
        if remote_address is not UNSET:
            field_dict["remote_address"] = remote_address
        if remote_port is not UNSET:
            field_dict["remote_port"] = remote_port
        if check_results is not UNSET:
            field_dict["check_results"] = check_results
        if do_not_monitor is not UNSET:
            field_dict["do_not_monitor"] = do_not_monitor
        if pop_endpoint is not UNSET:
            field_dict["pop_endpoint"] = pop_endpoint
        if last_agent_metrics is not UNSET:
            field_dict["last_agent_metrics"] = last_agent_metrics
        if resolved_ip is not UNSET:
            field_dict["resolved_ip"] = resolved_ip
        if max_agents_per_endpoint is not UNSET:
            field_dict["max_agents_per_endpoint"] = max_agents_per_endpoint
        if check_result_retention_days is not UNSET:
            field_dict["check_result_retention_days"] = check_result_retention_days
        if archived_by is not UNSET:
            field_dict["archived_by"] = archived_by
        if managed_by_content_type is not UNSET:
            field_dict["managed_by_content_type"] = managed_by_content_type
        if modified_by_user is not UNSET:
            field_dict["modified_by_user"] = modified_by_user
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if k8s_cluster is not UNSET:
            field_dict["k8s_cluster"] = k8s_cluster
        if k8s_app is not UNSET:
            field_dict["k8s_app"] = k8s_app
        if s3_cluster is not UNSET:
            field_dict["s3_cluster"] = s3_cluster
        if region is not UNSET:
            field_dict["region"] = region
        if loadbalancer_instance is not UNSET:
            field_dict["loadbalancer_instance"] = loadbalancer_instance

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.organization_id, Unset):
            files.append(("organization_id", (None, str(self.organization_id), "text/plain")))

        if not isinstance(self.workspace_id, Unset):
            if isinstance(self.workspace_id, UUID):
                files.append(("workspace_id", (None, str(self.workspace_id), "text/plain")))
            else:
                files.append(("workspace_id", (None, str(self.workspace_id).encode(), "text/plain")))

        if not isinstance(self.spec, Unset):
            if self.spec is None:
                files.append(("spec", (None, str(self.spec).encode(), "text/plain")))
            else:
                files.append(("spec", (None, json.dumps(self.spec.to_dict()).encode(), "application/json")))

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

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.remote_address, Unset):
            files.append(("remote_address", (None, str(self.remote_address).encode(), "text/plain")))

        if not isinstance(self.remote_port, Unset):
            if isinstance(self.remote_port, int):
                files.append(("remote_port", (None, str(self.remote_port).encode(), "text/plain")))
            else:
                files.append(("remote_port", (None, str(self.remote_port).encode(), "text/plain")))

        if not isinstance(self.check_results, Unset):
            files.append(("check_results", (None, str(self.check_results).encode(), "text/plain")))

        if not isinstance(self.do_not_monitor, Unset):
            files.append(("do_not_monitor", (None, str(self.do_not_monitor).encode(), "text/plain")))

        if not isinstance(self.pop_endpoint, Unset):
            files.append(("pop_endpoint", (None, str(self.pop_endpoint).encode(), "text/plain")))

        if not isinstance(self.last_agent_metrics, Unset):
            files.append(("last_agent_metrics", (None, str(self.last_agent_metrics).encode(), "text/plain")))

        if not isinstance(self.resolved_ip, Unset):
            if isinstance(self.resolved_ip, str):
                files.append(("resolved_ip", (None, str(self.resolved_ip).encode(), "text/plain")))
            else:
                files.append(("resolved_ip", (None, str(self.resolved_ip).encode(), "text/plain")))

        if not isinstance(self.max_agents_per_endpoint, Unset):
            if isinstance(self.max_agents_per_endpoint, int):
                files.append(
                    ("max_agents_per_endpoint", (None, str(self.max_agents_per_endpoint).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("max_agents_per_endpoint", (None, str(self.max_agents_per_endpoint).encode(), "text/plain"))
                )

        if not isinstance(self.check_result_retention_days, Unset):
            if isinstance(self.check_result_retention_days, int):
                files.append(
                    (
                        "check_result_retention_days",
                        (None, str(self.check_result_retention_days).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "check_result_retention_days",
                        (None, str(self.check_result_retention_days).encode(), "text/plain"),
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

        if not isinstance(self.k8s_cluster, Unset):
            if isinstance(self.k8s_cluster, UUID):
                files.append(("k8s_cluster", (None, str(self.k8s_cluster), "text/plain")))
            else:
                files.append(("k8s_cluster", (None, str(self.k8s_cluster).encode(), "text/plain")))

        if not isinstance(self.k8s_app, Unset):
            if isinstance(self.k8s_app, UUID):
                files.append(("k8s_app", (None, str(self.k8s_app), "text/plain")))
            else:
                files.append(("k8s_app", (None, str(self.k8s_app).encode(), "text/plain")))

        if not isinstance(self.s3_cluster, Unset):
            if isinstance(self.s3_cluster, UUID):
                files.append(("s3_cluster", (None, str(self.s3_cluster), "text/plain")))
            else:
                files.append(("s3_cluster", (None, str(self.s3_cluster).encode(), "text/plain")))

        if not isinstance(self.region, Unset):
            if isinstance(self.region, UUID):
                files.append(("region", (None, str(self.region), "text/plain")))
            else:
                files.append(("region", (None, str(self.region).encode(), "text/plain")))

        if not isinstance(self.loadbalancer_instance, Unset):
            if isinstance(self.loadbalancer_instance, UUID):
                files.append(("loadbalancer_instance", (None, str(self.loadbalancer_instance), "text/plain")))
            else:
                files.append(("loadbalancer_instance", (None, str(self.loadbalancer_instance).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_spec_request import EndpointSpecRequest

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _organization_id = d.pop("organization_id", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)

        def _parse_workspace_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                workspace_id_type_0 = UUID(data)

                return workspace_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id", UNSET))

        def _parse_spec(data: object) -> EndpointSpecRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                spec_type_1 = EndpointSpecRequest.from_dict(data)

                return spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointSpecRequest | None | Unset, data)

        spec = _parse_spec(d.pop("spec", UNSET))

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

        _kind = d.pop("kind", UNSET)
        kind: EndpointKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_endpoint_kind_enum(_kind)

        remote_address = d.pop("remote_address", UNSET)

        def _parse_remote_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        remote_port = _parse_remote_port(d.pop("remote_port", UNSET))

        check_results = d.pop("check_results", UNSET)

        do_not_monitor = d.pop("do_not_monitor", UNSET)

        pop_endpoint = d.pop("pop_endpoint", UNSET)

        last_agent_metrics = d.pop("last_agent_metrics", UNSET)

        def _parse_resolved_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_ip = _parse_resolved_ip(d.pop("resolved_ip", UNSET))

        def _parse_max_agents_per_endpoint(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_agents_per_endpoint = _parse_max_agents_per_endpoint(d.pop("max_agents_per_endpoint", UNSET))

        def _parse_check_result_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        check_result_retention_days = _parse_check_result_retention_days(d.pop("check_result_retention_days", UNSET))

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

        def _parse_k8s_app(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                k8s_app_type_0 = UUID(data)

                return k8s_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        k8s_app = _parse_k8s_app(d.pop("k8s_app", UNSET))

        def _parse_s3_cluster(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                s3_cluster_type_0 = UUID(data)

                return s3_cluster_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        s3_cluster = _parse_s3_cluster(d.pop("s3_cluster", UNSET))

        def _parse_region(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                region_type_0 = UUID(data)

                return region_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_loadbalancer_instance(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                loadbalancer_instance_type_0 = UUID(data)

                return loadbalancer_instance_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        loadbalancer_instance = _parse_loadbalancer_instance(d.pop("loadbalancer_instance", UNSET))

        patched_endpoint_request = cls(
            name=name,
            organization_id=organization_id,
            workspace_id=workspace_id,
            spec=spec,
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
            kind=kind,
            remote_address=remote_address,
            remote_port=remote_port,
            check_results=check_results,
            do_not_monitor=do_not_monitor,
            pop_endpoint=pop_endpoint,
            last_agent_metrics=last_agent_metrics,
            resolved_ip=resolved_ip,
            max_agents_per_endpoint=max_agents_per_endpoint,
            check_result_retention_days=check_result_retention_days,
            archived_by=archived_by,
            managed_by_content_type=managed_by_content_type,
            modified_by_user=modified_by_user,
            created_by_user=created_by_user,
            k8s_cluster=k8s_cluster,
            k8s_app=k8s_app,
            s3_cluster=s3_cluster,
            region=region,
            loadbalancer_instance=loadbalancer_instance,
        )

        patched_endpoint_request.additional_properties = d
        return patched_endpoint_request

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
