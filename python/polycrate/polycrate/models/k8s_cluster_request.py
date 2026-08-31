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
from ..models.k8s_cluster_kind_enum import K8SClusterKindEnum, check_k8s_cluster_kind_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="K8SClusterRequest")


@_attrs_define
class K8SClusterRequest:
    """K8sCluster Detail Serializer - erbt von ManagedObjectDetailSerializer.

    Generische Felder (von ManagedObjectDetailSerializer):
    - Alle BaseObject Felder (id, name, display_name, labels, etc.)
    - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
    - organization, workspace als generische Referenzen (mit URL)
    - created (Kombifeld), url

    K8sCluster-spezifische Felder:
    - kubernetes_version, block, kubernetes_apps, etc.

    Per .specs/0.11.4/dynamic-table-v2.md

        Attributes:
            kind (K8SClusterKindEnum): * `polycrate` - Polycrate
                * `generic` - Generic
                * `loopback` - Loopback
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
            kubernetes_version (None | str | Unset):
            installed (bool | Unset):
            is_host_cluster (bool | Unset):
            is_infrastructure_cluster (bool | Unset):
            kubeconfig_ca_cert_expiry_date (datetime.datetime | None | Unset):
            kubeconfig_client_cert_expiry_date (datetime.datetime | None | Unset):
            api_server_cert_expiry_date (datetime.datetime | None | Unset):
            credential (None | Unset | UUID):
            discovery_ignored_namespaces (Any | Unset): Namespaces to ignore for discovery
            operator_loglevel (Any | Unset): Operator loglevel override (1=Info, 2=Debug, 3=Trace). Null = SystemConfig
                default.
            operator_ignore_namespaces (Any | Unset): List of namespaces the operator ignores for discovery. Null =
                SystemConfig default.
            alias (None | str | Unset):
            description (None | str | Unset):
            addons (Any | Unset):
            active (bool | Unset):
            backup_schedules (Any | Unset): List of backup schedules (from various providers: Velero, CloudnativePG, etc.)
            baserow_id (int | None | Unset):
            gitlab_project_id (int | None | Unset):
            last_backup_import (datetime.datetime | None | Unset): Timestamp of last backup import (for reference only, uses
                24h window)
            platform_dns_record_created (bool | Unset):
            slug (None | str | Unset):
            managed_by_content_type (int | None | Unset):
            managed_by_object_id (None | str | Unset):
    """

    kind: K8SClusterKindEnum
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
    kubernetes_version: None | str | Unset = UNSET
    installed: bool | Unset = UNSET
    is_host_cluster: bool | Unset = UNSET
    is_infrastructure_cluster: bool | Unset = UNSET
    kubeconfig_ca_cert_expiry_date: datetime.datetime | None | Unset = UNSET
    kubeconfig_client_cert_expiry_date: datetime.datetime | None | Unset = UNSET
    api_server_cert_expiry_date: datetime.datetime | None | Unset = UNSET
    credential: None | Unset | UUID = UNSET
    discovery_ignored_namespaces: Any | Unset = UNSET
    operator_loglevel: Any | Unset = UNSET
    operator_ignore_namespaces: Any | Unset = UNSET
    alias: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    addons: Any | Unset = UNSET
    active: bool | Unset = UNSET
    backup_schedules: Any | Unset = UNSET
    baserow_id: int | None | Unset = UNSET
    gitlab_project_id: int | None | Unset = UNSET
    last_backup_import: datetime.datetime | None | Unset = UNSET
    platform_dns_record_created: bool | Unset = UNSET
    slug: None | str | Unset = UNSET
    managed_by_content_type: int | None | Unset = UNSET
    managed_by_object_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

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

        kubernetes_version: None | str | Unset
        if isinstance(self.kubernetes_version, Unset):
            kubernetes_version = UNSET
        else:
            kubernetes_version = self.kubernetes_version

        installed = self.installed

        is_host_cluster = self.is_host_cluster

        is_infrastructure_cluster = self.is_infrastructure_cluster

        kubeconfig_ca_cert_expiry_date: None | str | Unset
        if isinstance(self.kubeconfig_ca_cert_expiry_date, Unset):
            kubeconfig_ca_cert_expiry_date = UNSET
        elif isinstance(self.kubeconfig_ca_cert_expiry_date, datetime.datetime):
            kubeconfig_ca_cert_expiry_date = self.kubeconfig_ca_cert_expiry_date.isoformat()
        else:
            kubeconfig_ca_cert_expiry_date = self.kubeconfig_ca_cert_expiry_date

        kubeconfig_client_cert_expiry_date: None | str | Unset
        if isinstance(self.kubeconfig_client_cert_expiry_date, Unset):
            kubeconfig_client_cert_expiry_date = UNSET
        elif isinstance(self.kubeconfig_client_cert_expiry_date, datetime.datetime):
            kubeconfig_client_cert_expiry_date = self.kubeconfig_client_cert_expiry_date.isoformat()
        else:
            kubeconfig_client_cert_expiry_date = self.kubeconfig_client_cert_expiry_date

        api_server_cert_expiry_date: None | str | Unset
        if isinstance(self.api_server_cert_expiry_date, Unset):
            api_server_cert_expiry_date = UNSET
        elif isinstance(self.api_server_cert_expiry_date, datetime.datetime):
            api_server_cert_expiry_date = self.api_server_cert_expiry_date.isoformat()
        else:
            api_server_cert_expiry_date = self.api_server_cert_expiry_date

        credential: None | str | Unset
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, UUID):
            credential = str(self.credential)
        else:
            credential = self.credential

        discovery_ignored_namespaces = self.discovery_ignored_namespaces

        operator_loglevel = self.operator_loglevel

        operator_ignore_namespaces = self.operator_ignore_namespaces

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        addons = self.addons

        active = self.active

        backup_schedules = self.backup_schedules

        baserow_id: int | None | Unset
        if isinstance(self.baserow_id, Unset):
            baserow_id = UNSET
        else:
            baserow_id = self.baserow_id

        gitlab_project_id: int | None | Unset
        if isinstance(self.gitlab_project_id, Unset):
            gitlab_project_id = UNSET
        else:
            gitlab_project_id = self.gitlab_project_id

        last_backup_import: None | str | Unset
        if isinstance(self.last_backup_import, Unset):
            last_backup_import = UNSET
        elif isinstance(self.last_backup_import, datetime.datetime):
            last_backup_import = self.last_backup_import.isoformat()
        else:
            last_backup_import = self.last_backup_import

        platform_dns_record_created = self.platform_dns_record_created

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        managed_by_content_type: int | None | Unset
        if isinstance(self.managed_by_content_type, Unset):
            managed_by_content_type = UNSET
        else:
            managed_by_content_type = self.managed_by_content_type

        managed_by_object_id: None | str | Unset
        if isinstance(self.managed_by_object_id, Unset):
            managed_by_object_id = UNSET
        else:
            managed_by_object_id = self.managed_by_object_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
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
        if kubernetes_version is not UNSET:
            field_dict["kubernetes_version"] = kubernetes_version
        if installed is not UNSET:
            field_dict["installed"] = installed
        if is_host_cluster is not UNSET:
            field_dict["is_host_cluster"] = is_host_cluster
        if is_infrastructure_cluster is not UNSET:
            field_dict["is_infrastructure_cluster"] = is_infrastructure_cluster
        if kubeconfig_ca_cert_expiry_date is not UNSET:
            field_dict["kubeconfig_ca_cert_expiry_date"] = kubeconfig_ca_cert_expiry_date
        if kubeconfig_client_cert_expiry_date is not UNSET:
            field_dict["kubeconfig_client_cert_expiry_date"] = kubeconfig_client_cert_expiry_date
        if api_server_cert_expiry_date is not UNSET:
            field_dict["api_server_cert_expiry_date"] = api_server_cert_expiry_date
        if credential is not UNSET:
            field_dict["credential"] = credential
        if discovery_ignored_namespaces is not UNSET:
            field_dict["discovery_ignored_namespaces"] = discovery_ignored_namespaces
        if operator_loglevel is not UNSET:
            field_dict["operator_loglevel"] = operator_loglevel
        if operator_ignore_namespaces is not UNSET:
            field_dict["operator_ignore_namespaces"] = operator_ignore_namespaces
        if alias is not UNSET:
            field_dict["alias"] = alias
        if description is not UNSET:
            field_dict["description"] = description
        if addons is not UNSET:
            field_dict["addons"] = addons
        if active is not UNSET:
            field_dict["active"] = active
        if backup_schedules is not UNSET:
            field_dict["backup_schedules"] = backup_schedules
        if baserow_id is not UNSET:
            field_dict["baserow_id"] = baserow_id
        if gitlab_project_id is not UNSET:
            field_dict["gitlab_project_id"] = gitlab_project_id
        if last_backup_import is not UNSET:
            field_dict["last_backup_import"] = last_backup_import
        if platform_dns_record_created is not UNSET:
            field_dict["platform_dns_record_created"] = platform_dns_record_created
        if slug is not UNSET:
            field_dict["slug"] = slug
        if managed_by_content_type is not UNSET:
            field_dict["managed_by_content_type"] = managed_by_content_type
        if managed_by_object_id is not UNSET:
            field_dict["managed_by_object_id"] = managed_by_object_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

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

        if not isinstance(self.kubernetes_version, Unset):
            if isinstance(self.kubernetes_version, str):
                files.append(("kubernetes_version", (None, str(self.kubernetes_version).encode(), "text/plain")))
            else:
                files.append(("kubernetes_version", (None, str(self.kubernetes_version).encode(), "text/plain")))

        if not isinstance(self.installed, Unset):
            files.append(("installed", (None, str(self.installed).encode(), "text/plain")))

        if not isinstance(self.is_host_cluster, Unset):
            files.append(("is_host_cluster", (None, str(self.is_host_cluster).encode(), "text/plain")))

        if not isinstance(self.is_infrastructure_cluster, Unset):
            files.append(
                ("is_infrastructure_cluster", (None, str(self.is_infrastructure_cluster).encode(), "text/plain"))
            )

        if not isinstance(self.kubeconfig_ca_cert_expiry_date, Unset):
            if isinstance(self.kubeconfig_ca_cert_expiry_date, datetime.datetime):
                files.append(
                    (
                        "kubeconfig_ca_cert_expiry_date",
                        (None, self.kubeconfig_ca_cert_expiry_date.isoformat().encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "kubeconfig_ca_cert_expiry_date",
                        (None, str(self.kubeconfig_ca_cert_expiry_date).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.kubeconfig_client_cert_expiry_date, Unset):
            if isinstance(self.kubeconfig_client_cert_expiry_date, datetime.datetime):
                files.append(
                    (
                        "kubeconfig_client_cert_expiry_date",
                        (None, self.kubeconfig_client_cert_expiry_date.isoformat().encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "kubeconfig_client_cert_expiry_date",
                        (None, str(self.kubeconfig_client_cert_expiry_date).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.api_server_cert_expiry_date, Unset):
            if isinstance(self.api_server_cert_expiry_date, datetime.datetime):
                files.append(
                    (
                        "api_server_cert_expiry_date",
                        (None, self.api_server_cert_expiry_date.isoformat().encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "api_server_cert_expiry_date",
                        (None, str(self.api_server_cert_expiry_date).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.credential, Unset):
            if isinstance(self.credential, UUID):
                files.append(("credential", (None, str(self.credential), "text/plain")))
            else:
                files.append(("credential", (None, str(self.credential).encode(), "text/plain")))

        if not isinstance(self.discovery_ignored_namespaces, Unset):
            files.append(
                ("discovery_ignored_namespaces", (None, str(self.discovery_ignored_namespaces).encode(), "text/plain"))
            )

        if not isinstance(self.operator_loglevel, Unset):
            files.append(("operator_loglevel", (None, str(self.operator_loglevel).encode(), "text/plain")))

        if not isinstance(self.operator_ignore_namespaces, Unset):
            files.append(
                ("operator_ignore_namespaces", (None, str(self.operator_ignore_namespaces).encode(), "text/plain"))
            )

        if not isinstance(self.alias, Unset):
            if isinstance(self.alias, str):
                files.append(("alias", (None, str(self.alias).encode(), "text/plain")))
            else:
                files.append(("alias", (None, str(self.alias).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.addons, Unset):
            files.append(("addons", (None, str(self.addons).encode(), "text/plain")))

        if not isinstance(self.active, Unset):
            files.append(("active", (None, str(self.active).encode(), "text/plain")))

        if not isinstance(self.backup_schedules, Unset):
            files.append(("backup_schedules", (None, str(self.backup_schedules).encode(), "text/plain")))

        if not isinstance(self.baserow_id, Unset):
            if isinstance(self.baserow_id, int):
                files.append(("baserow_id", (None, str(self.baserow_id).encode(), "text/plain")))
            else:
                files.append(("baserow_id", (None, str(self.baserow_id).encode(), "text/plain")))

        if not isinstance(self.gitlab_project_id, Unset):
            if isinstance(self.gitlab_project_id, int):
                files.append(("gitlab_project_id", (None, str(self.gitlab_project_id).encode(), "text/plain")))
            else:
                files.append(("gitlab_project_id", (None, str(self.gitlab_project_id).encode(), "text/plain")))

        if not isinstance(self.last_backup_import, Unset):
            if isinstance(self.last_backup_import, datetime.datetime):
                files.append(("last_backup_import", (None, self.last_backup_import.isoformat().encode(), "text/plain")))
            else:
                files.append(("last_backup_import", (None, str(self.last_backup_import).encode(), "text/plain")))

        if not isinstance(self.platform_dns_record_created, Unset):
            files.append(
                ("platform_dns_record_created", (None, str(self.platform_dns_record_created).encode(), "text/plain"))
            )

        if not isinstance(self.slug, Unset):
            if isinstance(self.slug, str):
                files.append(("slug", (None, str(self.slug).encode(), "text/plain")))
            else:
                files.append(("slug", (None, str(self.slug).encode(), "text/plain")))

        if not isinstance(self.managed_by_content_type, Unset):
            if isinstance(self.managed_by_content_type, int):
                files.append(
                    ("managed_by_content_type", (None, str(self.managed_by_content_type).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("managed_by_content_type", (None, str(self.managed_by_content_type).encode(), "text/plain"))
                )

        if not isinstance(self.managed_by_object_id, Unset):
            if isinstance(self.managed_by_object_id, str):
                files.append(("managed_by_object_id", (None, str(self.managed_by_object_id).encode(), "text/plain")))
            else:
                files.append(("managed_by_object_id", (None, str(self.managed_by_object_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = check_k8s_cluster_kind_enum(d.pop("kind"))

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

        def _parse_kubernetes_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kubernetes_version = _parse_kubernetes_version(d.pop("kubernetes_version", UNSET))

        installed = d.pop("installed", UNSET)

        is_host_cluster = d.pop("is_host_cluster", UNSET)

        is_infrastructure_cluster = d.pop("is_infrastructure_cluster", UNSET)

        def _parse_kubeconfig_ca_cert_expiry_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kubeconfig_ca_cert_expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return kubeconfig_ca_cert_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        kubeconfig_ca_cert_expiry_date = _parse_kubeconfig_ca_cert_expiry_date(
            d.pop("kubeconfig_ca_cert_expiry_date", UNSET)
        )

        def _parse_kubeconfig_client_cert_expiry_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kubeconfig_client_cert_expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return kubeconfig_client_cert_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        kubeconfig_client_cert_expiry_date = _parse_kubeconfig_client_cert_expiry_date(
            d.pop("kubeconfig_client_cert_expiry_date", UNSET)
        )

        def _parse_api_server_cert_expiry_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                api_server_cert_expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return api_server_cert_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        api_server_cert_expiry_date = _parse_api_server_cert_expiry_date(d.pop("api_server_cert_expiry_date", UNSET))

        def _parse_credential(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credential_type_0 = UUID(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        credential = _parse_credential(d.pop("credential", UNSET))

        discovery_ignored_namespaces = d.pop("discovery_ignored_namespaces", UNSET)

        operator_loglevel = d.pop("operator_loglevel", UNSET)

        operator_ignore_namespaces = d.pop("operator_ignore_namespaces", UNSET)

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        addons = d.pop("addons", UNSET)

        active = d.pop("active", UNSET)

        backup_schedules = d.pop("backup_schedules", UNSET)

        def _parse_baserow_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        baserow_id = _parse_baserow_id(d.pop("baserow_id", UNSET))

        def _parse_gitlab_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        gitlab_project_id = _parse_gitlab_project_id(d.pop("gitlab_project_id", UNSET))

        def _parse_last_backup_import(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_import_type_0 = datetime.datetime.fromisoformat(data)

                return last_backup_import_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_backup_import = _parse_last_backup_import(d.pop("last_backup_import", UNSET))

        platform_dns_record_created = d.pop("platform_dns_record_created", UNSET)

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_managed_by_content_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        managed_by_content_type = _parse_managed_by_content_type(d.pop("managed_by_content_type", UNSET))

        def _parse_managed_by_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_by_object_id = _parse_managed_by_object_id(d.pop("managed_by_object_id", UNSET))

        k8s_cluster_request = cls(
            kind=kind,
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
            kubernetes_version=kubernetes_version,
            installed=installed,
            is_host_cluster=is_host_cluster,
            is_infrastructure_cluster=is_infrastructure_cluster,
            kubeconfig_ca_cert_expiry_date=kubeconfig_ca_cert_expiry_date,
            kubeconfig_client_cert_expiry_date=kubeconfig_client_cert_expiry_date,
            api_server_cert_expiry_date=api_server_cert_expiry_date,
            credential=credential,
            discovery_ignored_namespaces=discovery_ignored_namespaces,
            operator_loglevel=operator_loglevel,
            operator_ignore_namespaces=operator_ignore_namespaces,
            alias=alias,
            description=description,
            addons=addons,
            active=active,
            backup_schedules=backup_schedules,
            baserow_id=baserow_id,
            gitlab_project_id=gitlab_project_id,
            last_backup_import=last_backup_import,
            platform_dns_record_created=platform_dns_record_created,
            slug=slug,
            managed_by_content_type=managed_by_content_type,
            managed_by_object_id=managed_by_object_id,
        )

        k8s_cluster_request.additional_properties = d
        return k8s_cluster_request

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
