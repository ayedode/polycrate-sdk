from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.alert_kind_enum import AlertKindEnum, check_alert_kind_enum
from ..models.alert_status_enum import AlertStatusEnum, check_alert_status_enum
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.category_enum import CategoryEnum, check_category_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAlertRequest")


@_attrs_define
class PatchedAlertRequest:
    """Detail serializer for Alert.
    Extends ManagedObjectDetailSerializer to include icon_url, is_class_icon, url, etc.
    organization and workspace are provided as serialize_managed_object_simple dicts by the base class.

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
            platform_service (bool | Unset):
            kind (AlertKindEnum | Unset): * `grafana` - Grafana Alert
                * `generic` - Generic Alert
                * `checkmk` - CheckMK Alert
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
            status (AlertStatusEnum | BlankEnum | None | Unset):
            title (None | str | Unset):
            fingerprint (None | str | Unset):
            external_url (None | str | Unset):
            message (None | str | Unset):
            last_seen (datetime.datetime | None | Unset):
            suppressed (bool | Unset):
            pod (None | str | Unset): Pod name from Grafana labels
            namespace (None | str | Unset): Namespace from Grafana labels
            category (CategoryEnum | Unset): * `cluster.node` - Cluster / Node
                * `workload.pod` - Workload / Pod
                * `storage.volume` - Storage / Volume
                * `data.cnpg` - Data / CNPG
                * `data.replication` - Data / Replication
                * `data.mariadb` - Data / MariaDB
                * `data.mongodb` - Data / MongoDB
                * `backup.velero` - Backup / Velero
                * `observability.metrics` - Observability / Metrics
                * `security.secrets` - Security / Secrets
                * `security.access` - Security / Access
                * `gitops.flux` - GitOps / Flux
                * `availability.http` - Availability / HTTP
                * `application.customer` - Application / Customer
                * `platform.test` - Platform / Test
                * `unknown` - Unknown
            dashboard_url (None | str | Unset):
            panel_url (None | str | Unset):
            silence_url (None | str | Unset):
            silence_ends_at (datetime.datetime | None | Unset): When the active Grafana silence ends (from Alertmanager
                endsAt)
            generator_url (None | str | Unset):
            alert_router (None | Unset | UUID):
            k8s_cluster (None | Unset | UUID):
            k8s_app (None | Unset | UUID):
            block (None | Unset | UUID):
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
    platform_service: bool | Unset = UNSET
    kind: AlertKindEnum | Unset = UNSET
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
    status: AlertStatusEnum | BlankEnum | None | Unset = UNSET
    title: None | str | Unset = UNSET
    fingerprint: None | str | Unset = UNSET
    external_url: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    last_seen: datetime.datetime | None | Unset = UNSET
    suppressed: bool | Unset = UNSET
    pod: None | str | Unset = UNSET
    namespace: None | str | Unset = UNSET
    category: CategoryEnum | Unset = UNSET
    dashboard_url: None | str | Unset = UNSET
    panel_url: None | str | Unset = UNSET
    silence_url: None | str | Unset = UNSET
    silence_ends_at: datetime.datetime | None | Unset = UNSET
    generator_url: None | str | Unset = UNSET
    alert_router: None | Unset | UUID = UNSET
    k8s_cluster: None | Unset | UUID = UNSET
    k8s_app: None | Unset | UUID = UNSET
    block: None | Unset | UUID = UNSET
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

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, str):
            status = self.status
        elif isinstance(self.status, str):
            status = self.status
        else:
            status = self.status

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        fingerprint: None | str | Unset
        if isinstance(self.fingerprint, Unset):
            fingerprint = UNSET
        else:
            fingerprint = self.fingerprint

        external_url: None | str | Unset
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        last_seen: None | str | Unset
        if isinstance(self.last_seen, Unset):
            last_seen = UNSET
        elif isinstance(self.last_seen, datetime.datetime):
            last_seen = self.last_seen.isoformat()
        else:
            last_seen = self.last_seen

        suppressed = self.suppressed

        pod: None | str | Unset
        if isinstance(self.pod, Unset):
            pod = UNSET
        else:
            pod = self.pod

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        dashboard_url: None | str | Unset
        if isinstance(self.dashboard_url, Unset):
            dashboard_url = UNSET
        else:
            dashboard_url = self.dashboard_url

        panel_url: None | str | Unset
        if isinstance(self.panel_url, Unset):
            panel_url = UNSET
        else:
            panel_url = self.panel_url

        silence_url: None | str | Unset
        if isinstance(self.silence_url, Unset):
            silence_url = UNSET
        else:
            silence_url = self.silence_url

        silence_ends_at: None | str | Unset
        if isinstance(self.silence_ends_at, Unset):
            silence_ends_at = UNSET
        elif isinstance(self.silence_ends_at, datetime.datetime):
            silence_ends_at = self.silence_ends_at.isoformat()
        else:
            silence_ends_at = self.silence_ends_at

        generator_url: None | str | Unset
        if isinstance(self.generator_url, Unset):
            generator_url = UNSET
        else:
            generator_url = self.generator_url

        alert_router: None | str | Unset
        if isinstance(self.alert_router, Unset):
            alert_router = UNSET
        elif isinstance(self.alert_router, UUID):
            alert_router = str(self.alert_router)
        else:
            alert_router = self.alert_router

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

        block: None | str | Unset
        if isinstance(self.block, Unset):
            block = UNSET
        elif isinstance(self.block, UUID):
            block = str(self.block)
        else:
            block = self.block

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
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if message is not UNSET:
            field_dict["message"] = message
        if last_seen is not UNSET:
            field_dict["last_seen"] = last_seen
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed
        if pod is not UNSET:
            field_dict["pod"] = pod
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if category is not UNSET:
            field_dict["category"] = category
        if dashboard_url is not UNSET:
            field_dict["dashboard_url"] = dashboard_url
        if panel_url is not UNSET:
            field_dict["panel_url"] = panel_url
        if silence_url is not UNSET:
            field_dict["silence_url"] = silence_url
        if silence_ends_at is not UNSET:
            field_dict["silence_ends_at"] = silence_ends_at
        if generator_url is not UNSET:
            field_dict["generator_url"] = generator_url
        if alert_router is not UNSET:
            field_dict["alert_router"] = alert_router
        if k8s_cluster is not UNSET:
            field_dict["k8s_cluster"] = k8s_cluster
        if k8s_app is not UNSET:
            field_dict["k8s_app"] = k8s_app
        if block is not UNSET:
            field_dict["block"] = block

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

        if not isinstance(self.platform_service, Unset):
            files.append(("platform_service", (None, str(self.platform_service).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

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

        if not isinstance(self.status, Unset):
            if isinstance(self.status, str):
                files.append(("status", (None, str(self.status).encode(), "text/plain")))
            elif isinstance(self.status, str):
                files.append(("status", (None, str(self.status).encode(), "text/plain")))
            else:
                files.append(("status", (None, str(self.status).encode(), "text/plain")))

        if not isinstance(self.title, Unset):
            if isinstance(self.title, str):
                files.append(("title", (None, str(self.title).encode(), "text/plain")))
            else:
                files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.fingerprint, Unset):
            if isinstance(self.fingerprint, str):
                files.append(("fingerprint", (None, str(self.fingerprint).encode(), "text/plain")))
            else:
                files.append(("fingerprint", (None, str(self.fingerprint).encode(), "text/plain")))

        if not isinstance(self.external_url, Unset):
            if isinstance(self.external_url, str):
                files.append(("external_url", (None, str(self.external_url).encode(), "text/plain")))
            else:
                files.append(("external_url", (None, str(self.external_url).encode(), "text/plain")))

        if not isinstance(self.message, Unset):
            if isinstance(self.message, str):
                files.append(("message", (None, str(self.message).encode(), "text/plain")))
            else:
                files.append(("message", (None, str(self.message).encode(), "text/plain")))

        if not isinstance(self.last_seen, Unset):
            if isinstance(self.last_seen, datetime.datetime):
                files.append(("last_seen", (None, self.last_seen.isoformat().encode(), "text/plain")))
            else:
                files.append(("last_seen", (None, str(self.last_seen).encode(), "text/plain")))

        if not isinstance(self.suppressed, Unset):
            files.append(("suppressed", (None, str(self.suppressed).encode(), "text/plain")))

        if not isinstance(self.pod, Unset):
            if isinstance(self.pod, str):
                files.append(("pod", (None, str(self.pod).encode(), "text/plain")))
            else:
                files.append(("pod", (None, str(self.pod).encode(), "text/plain")))

        if not isinstance(self.namespace, Unset):
            if isinstance(self.namespace, str):
                files.append(("namespace", (None, str(self.namespace).encode(), "text/plain")))
            else:
                files.append(("namespace", (None, str(self.namespace).encode(), "text/plain")))

        if not isinstance(self.category, Unset):
            files.append(("category", (None, str(self.category).encode(), "text/plain")))

        if not isinstance(self.dashboard_url, Unset):
            if isinstance(self.dashboard_url, str):
                files.append(("dashboard_url", (None, str(self.dashboard_url).encode(), "text/plain")))
            else:
                files.append(("dashboard_url", (None, str(self.dashboard_url).encode(), "text/plain")))

        if not isinstance(self.panel_url, Unset):
            if isinstance(self.panel_url, str):
                files.append(("panel_url", (None, str(self.panel_url).encode(), "text/plain")))
            else:
                files.append(("panel_url", (None, str(self.panel_url).encode(), "text/plain")))

        if not isinstance(self.silence_url, Unset):
            if isinstance(self.silence_url, str):
                files.append(("silence_url", (None, str(self.silence_url).encode(), "text/plain")))
            else:
                files.append(("silence_url", (None, str(self.silence_url).encode(), "text/plain")))

        if not isinstance(self.silence_ends_at, Unset):
            if isinstance(self.silence_ends_at, datetime.datetime):
                files.append(("silence_ends_at", (None, self.silence_ends_at.isoformat().encode(), "text/plain")))
            else:
                files.append(("silence_ends_at", (None, str(self.silence_ends_at).encode(), "text/plain")))

        if not isinstance(self.generator_url, Unset):
            if isinstance(self.generator_url, str):
                files.append(("generator_url", (None, str(self.generator_url).encode(), "text/plain")))
            else:
                files.append(("generator_url", (None, str(self.generator_url).encode(), "text/plain")))

        if not isinstance(self.alert_router, Unset):
            if isinstance(self.alert_router, UUID):
                files.append(("alert_router", (None, str(self.alert_router), "text/plain")))
            else:
                files.append(("alert_router", (None, str(self.alert_router).encode(), "text/plain")))

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

        if not isinstance(self.block, Unset):
            if isinstance(self.block, UUID):
                files.append(("block", (None, str(self.block), "text/plain")))
            else:
                files.append(("block", (None, str(self.block).encode(), "text/plain")))

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

        platform_service = d.pop("platform_service", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: AlertKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_alert_kind_enum(_kind)

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

        def _parse_status(data: object) -> AlertStatusEnum | BlankEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = check_alert_status_enum(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = check_blank_enum(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlertStatusEnum | BlankEnum | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fingerprint = _parse_fingerprint(d.pop("fingerprint", UNSET))

        def _parse_external_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_last_seen(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_type_0 = datetime.datetime.fromisoformat(data)

                return last_seen_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_seen = _parse_last_seen(d.pop("last_seen", UNSET))

        suppressed = d.pop("suppressed", UNSET)

        def _parse_pod(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pod = _parse_pod(d.pop("pod", UNSET))

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        _category = d.pop("category", UNSET)
        category: CategoryEnum | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_category_enum(_category)

        def _parse_dashboard_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dashboard_url = _parse_dashboard_url(d.pop("dashboard_url", UNSET))

        def _parse_panel_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        panel_url = _parse_panel_url(d.pop("panel_url", UNSET))

        def _parse_silence_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        silence_url = _parse_silence_url(d.pop("silence_url", UNSET))

        def _parse_silence_ends_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                silence_ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return silence_ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        silence_ends_at = _parse_silence_ends_at(d.pop("silence_ends_at", UNSET))

        def _parse_generator_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generator_url = _parse_generator_url(d.pop("generator_url", UNSET))

        def _parse_alert_router(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                alert_router_type_0 = UUID(data)

                return alert_router_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        alert_router = _parse_alert_router(d.pop("alert_router", UNSET))

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

        def _parse_block(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                block_type_0 = UUID(data)

                return block_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        block = _parse_block(d.pop("block", UNSET))

        patched_alert_request = cls(
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
            status=status,
            title=title,
            fingerprint=fingerprint,
            external_url=external_url,
            message=message,
            last_seen=last_seen,
            suppressed=suppressed,
            pod=pod,
            namespace=namespace,
            category=category,
            dashboard_url=dashboard_url,
            panel_url=panel_url,
            silence_url=silence_url,
            silence_ends_at=silence_ends_at,
            generator_url=generator_url,
            alert_router=alert_router,
            k8s_cluster=k8s_cluster,
            k8s_app=k8s_app,
            block=block,
        )

        patched_alert_request.additional_properties = d
        return patched_alert_request

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
