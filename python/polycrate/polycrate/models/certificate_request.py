from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.certificate_kind_enum import CertificateKindEnum, check_certificate_kind_enum
from ..models.certificate_status_enum import CertificateStatusEnum, check_certificate_status_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.issuer_kind_enum import IssuerKindEnum, check_issuer_kind_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateRequest")


@_attrs_define
class CertificateRequest:
    """Full serializer for Certificate detail views.

    Name validation per .specs/0.11.16/certificate-name-validation.md

        Attributes:
            name (str): Certificate name (required, must match regex ^[a-z0-9]+(?:-[a-z0-9]+)*$)
            secret_name (str): Name of the Kubernetes Secret containing the certificate
            namespace (str): Kubernetes namespace where the certificate/secret exists
            k8s_cluster (UUID): Kubernetes cluster where this certificate exists
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
            kind (CertificateKindEnum | Unset): * `tls` - TLS
                * `mtls` - mTLS
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
            dns_names (Any | Unset): List of DNS names covered by this certificate
            ip_addresses (Any | Unset): List of IP addresses covered by this certificate
            issuer_name (None | str | Unset): Name of the Issuer or ClusterIssuer
            issuer_kind (BlankEnum | IssuerKindEnum | None | Unset): Kind of the issuer (Issuer or ClusterIssuer)

                * `issuer` - Issuer
                * `clusterissuer` - ClusterIssuer
            issuer_group (str | Unset): API group of the issuer
            not_before (datetime.datetime | None | Unset): Certificate valid from
            not_after (datetime.datetime | None | Unset): Certificate expires at
            renewal_time (datetime.datetime | None | Unset): When the certificate should be renewed
            certificate_status (CertificateStatusEnum | Unset): * `ready` - Ready
                * `pending` - Pending
                * `failed` - Failed
                * `expired` - Expired
                * `expiring_soon` - Expiring Soon
            is_ready (bool | Unset): Whether the certificate is ready
            current_challenge_type (None | str | Unset): Current challenge type (http01, dns01)
            current_challenge_status (None | str | Unset): Status of the current challenge
            challenge_reason (None | str | Unset): Reason/message from the challenge
            last_failure_time (datetime.datetime | None | Unset): Last time a renewal/issuance failed
            failure_reason (None | str | Unset): Reason for the last failure
            last_synced_from_cluster (datetime.datetime | None | Unset): Last time this certificate was synced from the
                cluster
            cert_manager_status (Any | Unset): Raw status from cert-manager Certificate CR
            metadata (Any | Unset): Additional metadata
    """

    name: str
    secret_name: str
    namespace: str
    k8s_cluster: UUID
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: CertificateKindEnum | Unset = UNSET
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
    dns_names: Any | Unset = UNSET
    ip_addresses: Any | Unset = UNSET
    issuer_name: None | str | Unset = UNSET
    issuer_kind: BlankEnum | IssuerKindEnum | None | Unset = UNSET
    issuer_group: str | Unset = UNSET
    not_before: datetime.datetime | None | Unset = UNSET
    not_after: datetime.datetime | None | Unset = UNSET
    renewal_time: datetime.datetime | None | Unset = UNSET
    certificate_status: CertificateStatusEnum | Unset = UNSET
    is_ready: bool | Unset = UNSET
    current_challenge_type: None | str | Unset = UNSET
    current_challenge_status: None | str | Unset = UNSET
    challenge_reason: None | str | Unset = UNSET
    last_failure_time: datetime.datetime | None | Unset = UNSET
    failure_reason: None | str | Unset = UNSET
    last_synced_from_cluster: datetime.datetime | None | Unset = UNSET
    cert_manager_status: Any | Unset = UNSET
    metadata: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        secret_name = self.secret_name

        namespace = self.namespace

        k8s_cluster = str(self.k8s_cluster)

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

        dns_names = self.dns_names

        ip_addresses = self.ip_addresses

        issuer_name: None | str | Unset
        if isinstance(self.issuer_name, Unset):
            issuer_name = UNSET
        else:
            issuer_name = self.issuer_name

        issuer_kind: None | str | Unset
        if isinstance(self.issuer_kind, Unset):
            issuer_kind = UNSET
        elif isinstance(self.issuer_kind, str):
            issuer_kind = self.issuer_kind
        elif isinstance(self.issuer_kind, str):
            issuer_kind = self.issuer_kind
        else:
            issuer_kind = self.issuer_kind

        issuer_group = self.issuer_group

        not_before: None | str | Unset
        if isinstance(self.not_before, Unset):
            not_before = UNSET
        elif isinstance(self.not_before, datetime.datetime):
            not_before = self.not_before.isoformat()
        else:
            not_before = self.not_before

        not_after: None | str | Unset
        if isinstance(self.not_after, Unset):
            not_after = UNSET
        elif isinstance(self.not_after, datetime.datetime):
            not_after = self.not_after.isoformat()
        else:
            not_after = self.not_after

        renewal_time: None | str | Unset
        if isinstance(self.renewal_time, Unset):
            renewal_time = UNSET
        elif isinstance(self.renewal_time, datetime.datetime):
            renewal_time = self.renewal_time.isoformat()
        else:
            renewal_time = self.renewal_time

        certificate_status: str | Unset = UNSET
        if not isinstance(self.certificate_status, Unset):
            certificate_status = self.certificate_status

        is_ready = self.is_ready

        current_challenge_type: None | str | Unset
        if isinstance(self.current_challenge_type, Unset):
            current_challenge_type = UNSET
        else:
            current_challenge_type = self.current_challenge_type

        current_challenge_status: None | str | Unset
        if isinstance(self.current_challenge_status, Unset):
            current_challenge_status = UNSET
        else:
            current_challenge_status = self.current_challenge_status

        challenge_reason: None | str | Unset
        if isinstance(self.challenge_reason, Unset):
            challenge_reason = UNSET
        else:
            challenge_reason = self.challenge_reason

        last_failure_time: None | str | Unset
        if isinstance(self.last_failure_time, Unset):
            last_failure_time = UNSET
        elif isinstance(self.last_failure_time, datetime.datetime):
            last_failure_time = self.last_failure_time.isoformat()
        else:
            last_failure_time = self.last_failure_time

        failure_reason: None | str | Unset
        if isinstance(self.failure_reason, Unset):
            failure_reason = UNSET
        else:
            failure_reason = self.failure_reason

        last_synced_from_cluster: None | str | Unset
        if isinstance(self.last_synced_from_cluster, Unset):
            last_synced_from_cluster = UNSET
        elif isinstance(self.last_synced_from_cluster, datetime.datetime):
            last_synced_from_cluster = self.last_synced_from_cluster.isoformat()
        else:
            last_synced_from_cluster = self.last_synced_from_cluster

        cert_manager_status = self.cert_manager_status

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "secret_name": secret_name,
                "namespace": namespace,
                "k8s_cluster": k8s_cluster,
            }
        )
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
        if dns_names is not UNSET:
            field_dict["dns_names"] = dns_names
        if ip_addresses is not UNSET:
            field_dict["ip_addresses"] = ip_addresses
        if issuer_name is not UNSET:
            field_dict["issuer_name"] = issuer_name
        if issuer_kind is not UNSET:
            field_dict["issuer_kind"] = issuer_kind
        if issuer_group is not UNSET:
            field_dict["issuer_group"] = issuer_group
        if not_before is not UNSET:
            field_dict["not_before"] = not_before
        if not_after is not UNSET:
            field_dict["not_after"] = not_after
        if renewal_time is not UNSET:
            field_dict["renewal_time"] = renewal_time
        if certificate_status is not UNSET:
            field_dict["certificate_status"] = certificate_status
        if is_ready is not UNSET:
            field_dict["is_ready"] = is_ready
        if current_challenge_type is not UNSET:
            field_dict["current_challenge_type"] = current_challenge_type
        if current_challenge_status is not UNSET:
            field_dict["current_challenge_status"] = current_challenge_status
        if challenge_reason is not UNSET:
            field_dict["challenge_reason"] = challenge_reason
        if last_failure_time is not UNSET:
            field_dict["last_failure_time"] = last_failure_time
        if failure_reason is not UNSET:
            field_dict["failure_reason"] = failure_reason
        if last_synced_from_cluster is not UNSET:
            field_dict["last_synced_from_cluster"] = last_synced_from_cluster
        if cert_manager_status is not UNSET:
            field_dict["cert_manager_status"] = cert_manager_status
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("secret_name", (None, str(self.secret_name).encode(), "text/plain")))

        files.append(("namespace", (None, str(self.namespace).encode(), "text/plain")))

        files.append(("k8s_cluster", (None, str(self.k8s_cluster), "text/plain")))

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

        if not isinstance(self.dns_names, Unset):
            files.append(("dns_names", (None, str(self.dns_names).encode(), "text/plain")))

        if not isinstance(self.ip_addresses, Unset):
            files.append(("ip_addresses", (None, str(self.ip_addresses).encode(), "text/plain")))

        if not isinstance(self.issuer_name, Unset):
            if isinstance(self.issuer_name, str):
                files.append(("issuer_name", (None, str(self.issuer_name).encode(), "text/plain")))
            else:
                files.append(("issuer_name", (None, str(self.issuer_name).encode(), "text/plain")))

        if not isinstance(self.issuer_kind, Unset):
            if isinstance(self.issuer_kind, str):
                files.append(("issuer_kind", (None, str(self.issuer_kind).encode(), "text/plain")))
            elif isinstance(self.issuer_kind, str):
                files.append(("issuer_kind", (None, str(self.issuer_kind).encode(), "text/plain")))
            else:
                files.append(("issuer_kind", (None, str(self.issuer_kind).encode(), "text/plain")))

        if not isinstance(self.issuer_group, Unset):
            files.append(("issuer_group", (None, str(self.issuer_group).encode(), "text/plain")))

        if not isinstance(self.not_before, Unset):
            if isinstance(self.not_before, datetime.datetime):
                files.append(("not_before", (None, self.not_before.isoformat().encode(), "text/plain")))
            else:
                files.append(("not_before", (None, str(self.not_before).encode(), "text/plain")))

        if not isinstance(self.not_after, Unset):
            if isinstance(self.not_after, datetime.datetime):
                files.append(("not_after", (None, self.not_after.isoformat().encode(), "text/plain")))
            else:
                files.append(("not_after", (None, str(self.not_after).encode(), "text/plain")))

        if not isinstance(self.renewal_time, Unset):
            if isinstance(self.renewal_time, datetime.datetime):
                files.append(("renewal_time", (None, self.renewal_time.isoformat().encode(), "text/plain")))
            else:
                files.append(("renewal_time", (None, str(self.renewal_time).encode(), "text/plain")))

        if not isinstance(self.certificate_status, Unset):
            files.append(("certificate_status", (None, str(self.certificate_status).encode(), "text/plain")))

        if not isinstance(self.is_ready, Unset):
            files.append(("is_ready", (None, str(self.is_ready).encode(), "text/plain")))

        if not isinstance(self.current_challenge_type, Unset):
            if isinstance(self.current_challenge_type, str):
                files.append(
                    ("current_challenge_type", (None, str(self.current_challenge_type).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("current_challenge_type", (None, str(self.current_challenge_type).encode(), "text/plain"))
                )

        if not isinstance(self.current_challenge_status, Unset):
            if isinstance(self.current_challenge_status, str):
                files.append(
                    ("current_challenge_status", (None, str(self.current_challenge_status).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("current_challenge_status", (None, str(self.current_challenge_status).encode(), "text/plain"))
                )

        if not isinstance(self.challenge_reason, Unset):
            if isinstance(self.challenge_reason, str):
                files.append(("challenge_reason", (None, str(self.challenge_reason).encode(), "text/plain")))
            else:
                files.append(("challenge_reason", (None, str(self.challenge_reason).encode(), "text/plain")))

        if not isinstance(self.last_failure_time, Unset):
            if isinstance(self.last_failure_time, datetime.datetime):
                files.append(("last_failure_time", (None, self.last_failure_time.isoformat().encode(), "text/plain")))
            else:
                files.append(("last_failure_time", (None, str(self.last_failure_time).encode(), "text/plain")))

        if not isinstance(self.failure_reason, Unset):
            if isinstance(self.failure_reason, str):
                files.append(("failure_reason", (None, str(self.failure_reason).encode(), "text/plain")))
            else:
                files.append(("failure_reason", (None, str(self.failure_reason).encode(), "text/plain")))

        if not isinstance(self.last_synced_from_cluster, Unset):
            if isinstance(self.last_synced_from_cluster, datetime.datetime):
                files.append(
                    (
                        "last_synced_from_cluster",
                        (None, self.last_synced_from_cluster.isoformat().encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    ("last_synced_from_cluster", (None, str(self.last_synced_from_cluster).encode(), "text/plain"))
                )

        if not isinstance(self.cert_manager_status, Unset):
            files.append(("cert_manager_status", (None, str(self.cert_manager_status).encode(), "text/plain")))

        if not isinstance(self.metadata, Unset):
            files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        secret_name = d.pop("secret_name")

        namespace = d.pop("namespace")

        k8s_cluster = UUID(d.pop("k8s_cluster"))

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
        kind: CertificateKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_certificate_kind_enum(_kind)

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

        dns_names = d.pop("dns_names", UNSET)

        ip_addresses = d.pop("ip_addresses", UNSET)

        def _parse_issuer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_name = _parse_issuer_name(d.pop("issuer_name", UNSET))

        def _parse_issuer_kind(data: object) -> BlankEnum | IssuerKindEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                issuer_kind_type_0 = check_issuer_kind_enum(data)

                return issuer_kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                issuer_kind_type_1 = check_blank_enum(data)

                return issuer_kind_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | IssuerKindEnum | None | Unset, data)

        issuer_kind = _parse_issuer_kind(d.pop("issuer_kind", UNSET))

        issuer_group = d.pop("issuer_group", UNSET)

        def _parse_not_before(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                not_before_type_0 = datetime.datetime.fromisoformat(data)

                return not_before_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        not_before = _parse_not_before(d.pop("not_before", UNSET))

        def _parse_not_after(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                not_after_type_0 = datetime.datetime.fromisoformat(data)

                return not_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        not_after = _parse_not_after(d.pop("not_after", UNSET))

        def _parse_renewal_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                renewal_time_type_0 = datetime.datetime.fromisoformat(data)

                return renewal_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        renewal_time = _parse_renewal_time(d.pop("renewal_time", UNSET))

        _certificate_status = d.pop("certificate_status", UNSET)
        certificate_status: CertificateStatusEnum | Unset
        if isinstance(_certificate_status, Unset):
            certificate_status = UNSET
        else:
            certificate_status = check_certificate_status_enum(_certificate_status)

        is_ready = d.pop("is_ready", UNSET)

        def _parse_current_challenge_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_challenge_type = _parse_current_challenge_type(d.pop("current_challenge_type", UNSET))

        def _parse_current_challenge_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_challenge_status = _parse_current_challenge_status(d.pop("current_challenge_status", UNSET))

        def _parse_challenge_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        challenge_reason = _parse_challenge_reason(d.pop("challenge_reason", UNSET))

        def _parse_last_failure_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_failure_time_type_0 = datetime.datetime.fromisoformat(data)

                return last_failure_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_failure_time = _parse_last_failure_time(d.pop("last_failure_time", UNSET))

        def _parse_failure_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_reason = _parse_failure_reason(d.pop("failure_reason", UNSET))

        def _parse_last_synced_from_cluster(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_from_cluster_type_0 = datetime.datetime.fromisoformat(data)

                return last_synced_from_cluster_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_synced_from_cluster = _parse_last_synced_from_cluster(d.pop("last_synced_from_cluster", UNSET))

        cert_manager_status = d.pop("cert_manager_status", UNSET)

        metadata = d.pop("metadata", UNSET)

        certificate_request = cls(
            name=name,
            secret_name=secret_name,
            namespace=namespace,
            k8s_cluster=k8s_cluster,
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
            dns_names=dns_names,
            ip_addresses=ip_addresses,
            issuer_name=issuer_name,
            issuer_kind=issuer_kind,
            issuer_group=issuer_group,
            not_before=not_before,
            not_after=not_after,
            renewal_time=renewal_time,
            certificate_status=certificate_status,
            is_ready=is_ready,
            current_challenge_type=current_challenge_type,
            current_challenge_status=current_challenge_status,
            challenge_reason=challenge_reason,
            last_failure_time=last_failure_time,
            failure_reason=failure_reason,
            last_synced_from_cluster=last_synced_from_cluster,
            cert_manager_status=cert_manager_status,
            metadata=metadata,
        )

        certificate_request.additional_properties = d
        return certificate_request

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
