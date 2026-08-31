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
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.renewal_mode_enum import RenewalModeEnum, check_renewal_mode_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainDetailRequest")


@_attrs_define
class DomainDetailRequest:
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
            registrar_id (UUID | Unset): UUID of the DomainRegistrar (required on create).
            dns_zone_id (None | Unset | UUID):
            use_platform_dns (bool | Unset):  Default: False.
            owner_contact_id (None | Unset | UUID):
            admin_contact_id (None | Unset | UUID):
            tech_contact_id (None | Unset | UUID):
            auth_code_credential_id (None | Unset | UUID):
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
            platform_service (bool | Unset):
            kind (GenericObjectKindEnum | Unset): * `generic` - Generic
            tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
                the condition will not be applied.
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
            nameservers (Any | Unset): List of FQDN nameserver hostnames (max 3). Normalised (lowercase, no trailing dot).
            renewal_mode (RenewalModeEnum | Unset): * `AUTORENEW` - Auto Renew — domain renews automatically
                * `AUTODELETE` - Auto Delete — domain deleted at expiry
            transfer_lock (bool | Unset): Transfer lock enabled at registrar.
            registrar_domain_id (None | str | Unset): Registrar-side domain identifier (usually the FQDN).
            provider_status (None | str | Unset): Raw domain status string as returned by the registrar.
            expiry_date (datetime.datetime | None | Unset): Domain expiry / renewal date.
            registrar_metadata (Any | Unset): Full raw status response from the registrar (for debugging).
            archived_by (int | None | Unset): The user who archived the object
            managed_by_content_type (int | None | Unset):
            modified_by_user (int | None | Unset): The user who last modified the object
            created_by_user (int | None | Unset): The user who created the object
    """

    name: str | Unset = UNSET
    registrar_id: UUID | Unset = UNSET
    dns_zone_id: None | Unset | UUID = UNSET
    use_platform_dns: bool | Unset = False
    owner_contact_id: None | Unset | UUID = UNSET
    admin_contact_id: None | Unset | UUID = UNSET
    tech_contact_id: None | Unset | UUID = UNSET
    auth_code_credential_id: None | Unset | UUID = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    last_reconciliation_duration_seconds: float | None | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: GenericObjectKindEnum | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    created_by_component: BlankEnum | CreatedByComponentEnum | None | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_window_days: int | None | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_window_days: int | None | Unset = UNSET
    sla_availability: str | Unset = UNSET
    criticality: BlankEnum | CriticalityEnum | None | Unset = UNSET
    managed_by_object_id: None | str | Unset = UNSET
    platform_dns_record_created: bool | Unset = UNSET
    nameservers: Any | Unset = UNSET
    renewal_mode: RenewalModeEnum | Unset = UNSET
    transfer_lock: bool | Unset = UNSET
    registrar_domain_id: None | str | Unset = UNSET
    provider_status: None | str | Unset = UNSET
    expiry_date: datetime.datetime | None | Unset = UNSET
    registrar_metadata: Any | Unset = UNSET
    archived_by: int | None | Unset = UNSET
    managed_by_content_type: int | None | Unset = UNSET
    modified_by_user: int | None | Unset = UNSET
    created_by_user: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        registrar_id: str | Unset = UNSET
        if not isinstance(self.registrar_id, Unset):
            registrar_id = str(self.registrar_id)

        dns_zone_id: None | str | Unset
        if isinstance(self.dns_zone_id, Unset):
            dns_zone_id = UNSET
        elif isinstance(self.dns_zone_id, UUID):
            dns_zone_id = str(self.dns_zone_id)
        else:
            dns_zone_id = self.dns_zone_id

        use_platform_dns = self.use_platform_dns

        owner_contact_id: None | str | Unset
        if isinstance(self.owner_contact_id, Unset):
            owner_contact_id = UNSET
        elif isinstance(self.owner_contact_id, UUID):
            owner_contact_id = str(self.owner_contact_id)
        else:
            owner_contact_id = self.owner_contact_id

        admin_contact_id: None | str | Unset
        if isinstance(self.admin_contact_id, Unset):
            admin_contact_id = UNSET
        elif isinstance(self.admin_contact_id, UUID):
            admin_contact_id = str(self.admin_contact_id)
        else:
            admin_contact_id = self.admin_contact_id

        tech_contact_id: None | str | Unset
        if isinstance(self.tech_contact_id, Unset):
            tech_contact_id = UNSET
        elif isinstance(self.tech_contact_id, UUID):
            tech_contact_id = str(self.tech_contact_id)
        else:
            tech_contact_id = self.tech_contact_id

        auth_code_credential_id: None | str | Unset
        if isinstance(self.auth_code_credential_id, Unset):
            auth_code_credential_id = UNSET
        elif isinstance(self.auth_code_credential_id, UUID):
            auth_code_credential_id = str(self.auth_code_credential_id)
        else:
            auth_code_credential_id = self.auth_code_credential_id

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

        nameservers = self.nameservers

        renewal_mode: str | Unset = UNSET
        if not isinstance(self.renewal_mode, Unset):
            renewal_mode = self.renewal_mode

        transfer_lock = self.transfer_lock

        registrar_domain_id: None | str | Unset
        if isinstance(self.registrar_domain_id, Unset):
            registrar_domain_id = UNSET
        else:
            registrar_domain_id = self.registrar_domain_id

        provider_status: None | str | Unset
        if isinstance(self.provider_status, Unset):
            provider_status = UNSET
        else:
            provider_status = self.provider_status

        expiry_date: None | str | Unset
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.datetime):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        registrar_metadata = self.registrar_metadata

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if registrar_id is not UNSET:
            field_dict["registrar_id"] = registrar_id
        if dns_zone_id is not UNSET:
            field_dict["dns_zone_id"] = dns_zone_id
        if use_platform_dns is not UNSET:
            field_dict["use_platform_dns"] = use_platform_dns
        if owner_contact_id is not UNSET:
            field_dict["owner_contact_id"] = owner_contact_id
        if admin_contact_id is not UNSET:
            field_dict["admin_contact_id"] = admin_contact_id
        if tech_contact_id is not UNSET:
            field_dict["tech_contact_id"] = tech_contact_id
        if auth_code_credential_id is not UNSET:
            field_dict["auth_code_credential_id"] = auth_code_credential_id
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
        if created_by_component is not UNSET:
            field_dict["created_by_component"] = created_by_component
        if target_availability is not UNSET:
            field_dict["target_availability"] = target_availability
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
        if nameservers is not UNSET:
            field_dict["nameservers"] = nameservers
        if renewal_mode is not UNSET:
            field_dict["renewal_mode"] = renewal_mode
        if transfer_lock is not UNSET:
            field_dict["transfer_lock"] = transfer_lock
        if registrar_domain_id is not UNSET:
            field_dict["registrar_domain_id"] = registrar_domain_id
        if provider_status is not UNSET:
            field_dict["provider_status"] = provider_status
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date
        if registrar_metadata is not UNSET:
            field_dict["registrar_metadata"] = registrar_metadata
        if archived_by is not UNSET:
            field_dict["archived_by"] = archived_by
        if managed_by_content_type is not UNSET:
            field_dict["managed_by_content_type"] = managed_by_content_type
        if modified_by_user is not UNSET:
            field_dict["modified_by_user"] = modified_by_user
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.registrar_id, Unset):
            files.append(("registrar_id", (None, str(self.registrar_id), "text/plain")))

        if not isinstance(self.dns_zone_id, Unset):
            if isinstance(self.dns_zone_id, UUID):
                files.append(("dns_zone_id", (None, str(self.dns_zone_id), "text/plain")))
            else:
                files.append(("dns_zone_id", (None, str(self.dns_zone_id).encode(), "text/plain")))

        if not isinstance(self.use_platform_dns, Unset):
            files.append(("use_platform_dns", (None, str(self.use_platform_dns).encode(), "text/plain")))

        if not isinstance(self.owner_contact_id, Unset):
            if isinstance(self.owner_contact_id, UUID):
                files.append(("owner_contact_id", (None, str(self.owner_contact_id), "text/plain")))
            else:
                files.append(("owner_contact_id", (None, str(self.owner_contact_id).encode(), "text/plain")))

        if not isinstance(self.admin_contact_id, Unset):
            if isinstance(self.admin_contact_id, UUID):
                files.append(("admin_contact_id", (None, str(self.admin_contact_id), "text/plain")))
            else:
                files.append(("admin_contact_id", (None, str(self.admin_contact_id).encode(), "text/plain")))

        if not isinstance(self.tech_contact_id, Unset):
            if isinstance(self.tech_contact_id, UUID):
                files.append(("tech_contact_id", (None, str(self.tech_contact_id), "text/plain")))
            else:
                files.append(("tech_contact_id", (None, str(self.tech_contact_id).encode(), "text/plain")))

        if not isinstance(self.auth_code_credential_id, Unset):
            if isinstance(self.auth_code_credential_id, UUID):
                files.append(("auth_code_credential_id", (None, str(self.auth_code_credential_id), "text/plain")))
            else:
                files.append(
                    ("auth_code_credential_id", (None, str(self.auth_code_credential_id).encode(), "text/plain"))
                )

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

        if not isinstance(self.nameservers, Unset):
            files.append(("nameservers", (None, str(self.nameservers).encode(), "text/plain")))

        if not isinstance(self.renewal_mode, Unset):
            files.append(("renewal_mode", (None, str(self.renewal_mode).encode(), "text/plain")))

        if not isinstance(self.transfer_lock, Unset):
            files.append(("transfer_lock", (None, str(self.transfer_lock).encode(), "text/plain")))

        if not isinstance(self.registrar_domain_id, Unset):
            if isinstance(self.registrar_domain_id, str):
                files.append(("registrar_domain_id", (None, str(self.registrar_domain_id).encode(), "text/plain")))
            else:
                files.append(("registrar_domain_id", (None, str(self.registrar_domain_id).encode(), "text/plain")))

        if not isinstance(self.provider_status, Unset):
            if isinstance(self.provider_status, str):
                files.append(("provider_status", (None, str(self.provider_status).encode(), "text/plain")))
            else:
                files.append(("provider_status", (None, str(self.provider_status).encode(), "text/plain")))

        if not isinstance(self.expiry_date, Unset):
            if isinstance(self.expiry_date, datetime.datetime):
                files.append(("expiry_date", (None, self.expiry_date.isoformat().encode(), "text/plain")))
            else:
                files.append(("expiry_date", (None, str(self.expiry_date).encode(), "text/plain")))

        if not isinstance(self.registrar_metadata, Unset):
            files.append(("registrar_metadata", (None, str(self.registrar_metadata).encode(), "text/plain")))

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

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _registrar_id = d.pop("registrar_id", UNSET)
        registrar_id: UUID | Unset
        if isinstance(_registrar_id, Unset):
            registrar_id = UNSET
        else:
            registrar_id = UUID(_registrar_id)

        def _parse_dns_zone_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dns_zone_id_type_0 = UUID(data)

                return dns_zone_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dns_zone_id = _parse_dns_zone_id(d.pop("dns_zone_id", UNSET))

        use_platform_dns = d.pop("use_platform_dns", UNSET)

        def _parse_owner_contact_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_contact_id_type_0 = UUID(data)

                return owner_contact_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_contact_id = _parse_owner_contact_id(d.pop("owner_contact_id", UNSET))

        def _parse_admin_contact_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                admin_contact_id_type_0 = UUID(data)

                return admin_contact_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        admin_contact_id = _parse_admin_contact_id(d.pop("admin_contact_id", UNSET))

        def _parse_tech_contact_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tech_contact_id_type_0 = UUID(data)

                return tech_contact_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        tech_contact_id = _parse_tech_contact_id(d.pop("tech_contact_id", UNSET))

        def _parse_auth_code_credential_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_code_credential_id_type_0 = UUID(data)

                return auth_code_credential_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        auth_code_credential_id = _parse_auth_code_credential_id(d.pop("auth_code_credential_id", UNSET))

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

        platform_service = d.pop("platform_service", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: GenericObjectKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_generic_object_kind_enum(_kind)

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

        nameservers = d.pop("nameservers", UNSET)

        _renewal_mode = d.pop("renewal_mode", UNSET)
        renewal_mode: RenewalModeEnum | Unset
        if isinstance(_renewal_mode, Unset):
            renewal_mode = UNSET
        else:
            renewal_mode = check_renewal_mode_enum(_renewal_mode)

        transfer_lock = d.pop("transfer_lock", UNSET)

        def _parse_registrar_domain_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registrar_domain_id = _parse_registrar_domain_id(d.pop("registrar_domain_id", UNSET))

        def _parse_provider_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_status = _parse_provider_status(d.pop("provider_status", UNSET))

        def _parse_expiry_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expiry_date = _parse_expiry_date(d.pop("expiry_date", UNSET))

        registrar_metadata = d.pop("registrar_metadata", UNSET)

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

        domain_detail_request = cls(
            name=name,
            registrar_id=registrar_id,
            dns_zone_id=dns_zone_id,
            use_platform_dns=use_platform_dns,
            owner_contact_id=owner_contact_id,
            admin_contact_id=admin_contact_id,
            tech_contact_id=tech_contact_id,
            auth_code_credential_id=auth_code_credential_id,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            provider_id=provider_id,
            reconciliation_enabled=reconciliation_enabled,
            last_reconciliation_duration_seconds=last_reconciliation_duration_seconds,
            platform_service=platform_service,
            kind=kind,
            tolerations=tolerations,
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            created_by_component=created_by_component,
            target_availability=target_availability,
            slo_target=slo_target,
            slo_window_days=slo_window_days,
            slo_availability=slo_availability,
            sla_target=sla_target,
            sla_window_days=sla_window_days,
            sla_availability=sla_availability,
            criticality=criticality,
            managed_by_object_id=managed_by_object_id,
            platform_dns_record_created=platform_dns_record_created,
            nameservers=nameservers,
            renewal_mode=renewal_mode,
            transfer_lock=transfer_lock,
            registrar_domain_id=registrar_domain_id,
            provider_status=provider_status,
            expiry_date=expiry_date,
            registrar_metadata=registrar_metadata,
            archived_by=archived_by,
            managed_by_content_type=managed_by_content_type,
            modified_by_user=modified_by_user,
            created_by_user=created_by_user,
        )

        domain_detail_request.additional_properties = d
        return domain_detail_request

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
